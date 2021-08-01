# !/usr/bin/env python
# -*- coding: utf-8 -*-

""" main.py: aplicación que utiliza la clase InvertedIndex como búsqueda de índice invertido. """

__author__ = "Gonzalo Chacaltana"
__email__ = "gchacaltanab@outlook.com"

import sys
import os
from glob import glob

import array
from TextExtractor import TextExtractor
from DocumentSearchEngine import DocumentSearchEngine
from pprint import pprint as pp

class MainApp(object):

    def __init__(self):
        self.allowed_extensions = ["*","txt","pdf"]
        self.method_action = "query"
        self.path_directory = "c:/documents/reglamento"
    
    def run(self):
        """
        Método principal de la clase MainApp
        """
        self.dispatcher()
    
    def dispatcher(self):
        """
        Valida la acción enviada como argumento de la aplicación consola.
        """
        self.method_action = str(sys.argv[1])
        if (self.method_action=="read_documents"):
            self.read_documents()    
        elif (self.method_action=="query"):
            self.query_terms()
        else:
            raise Exception("Argumento de la aplicacion no reconocido")

    def read_documents(self):
        """
        Método que implementa el registro de nuevos documentos a la base de datos (índice invertido)
        """
        self.input_documents_type()
        self.insert_document_search_engine()
        
    def input_documents_type(self):
        """
        Método que permite al usuario ingresar la extensión de los archivos a realizar la carga inicial
        """
        self.documents_extension = str(input("Ingrese extension del tipo de documento a filtrar [txt,pdf,jpg,*]: "))
        if not self.documents_extension in self.allowed_extensions:
            raise Exception("La extension de documento no esta permitida")
    
    def insert_document_search_engine(self):
        """
        Método que registra nuevos indices invertidos en la bd.
        """
        # Instanciamos la clase TextExtractor
        extractor = TextExtractor(self.path_directory,self.documents_extension)
        # Obtenemos lista de documentos
        documents = extractor.get_documents()
        # Instanciamos la clase DocumentSearchEngine
        search_engine = DocumentSearchEngine()
        search_engine.insert_documents(documents)

    def query_terms(self):
        """
        Método que implementa la consulta de términos
        """
        n_terms = int(input("Ingrese cantidad de terminos a buscar: "))
        counter = 1
        self.search_words = []
        while counter<=n_terms:
            self.search_words.append(str(input("Termino [{}]: ".format(counter))))
            counter = counter + 1

        self.query_results()

    def query_results(self):
        search_engine = DocumentSearchEngine()
        files = sorted(search_engine.query(self.search_words))
        print("\nResultados: {} documentos encontrados".format(len(files)))
        print("---------------------------------------")
        c = 0
        for file in files:
            c = c + 1
            print("Documento [{}]: {}".format(c,file))
            print("Contenido [{}]: {}\n".format(c,str(search_engine.get_content_file(file))))


if __name__ == "__main__":

    try :
        app = MainApp()
        app.run()
    except Exception as ex: 
        print(ex)
    except KeyError as ex:
        print(ex)