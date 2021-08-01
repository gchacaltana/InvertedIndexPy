# !/usr/bin/env python
# -*- coding: utf-8 -*-

""" InvertedIndex: Clase que implementa los métodos del índice invertido. """

__author__ = "Gonzalo Chacaltana"
__email__ = "gchacaltanab@outlook.com"
__version__ = "1.0.1"

import sys
import ast
import pathlib

from functools import reduce


class DocumentSearchEngine(object):
    def __init__(self):
        self.documents = []
        self.texts = {}
        self.words = set()
        self.documents_search_engine = {}
        self.keys_search_engine = {}
        self.encoding = "utf8"
        self.name_db_search_engine = "data_documents_search_engine.txt"
        self.name_key_search_engine = "key_documents_search_engine.txt"
        self.path_directory = "c:/documents/prueba/"
        self.strange_characters = '._()[]"$“”%-:@#!|?¿{}'

    def insert_documents(self, documents):
        self.documents = documents
        self.load_documents()
        self.create()
        self.save()
        
    # Carga el contenido de los ficheros *.txt
    def load_documents(self):
        counter = 0
        for doc in self.documents:
            counter = counter + 1
            print("Procesando documento [{}]: {}".format(counter,doc[0]))
            tokens = [x.lower().translate({ord(c):None for c in self.strange_characters}) for x in str(doc[1]).split()]
            self.words |= set(tokens)
            self.texts[doc[0].split('\\')[-1]] = tokens

    # Crea el índice invertido
    def create(self):
        self.documents_search_engine = {word: set(txt for txt, words in self.texts.items()
                                         if word in words) for word in self.words}
        print("Se inserto el indice invertido en la base de datos")

    # Almacena el contenido de la estructura indice invertido en disco (FS)
    def save(self):
        f = open(self.name_db_search_engine, "w")
        f.write(str(self.documents_search_engine))
        f.close()
        f = open(self.name_key_search_engine, "w")
        f.write(str(self.texts))
        f.close()
        print("Se guardo la informacion en la base de datos en disco")

    # Búsqueda de terminos (palabras) en el motor de búsqueda de documentos
    def query(self, words):
        self.read_data()
        try:
            #return (self.documents_search_engine[word] for word in words)
            return reduce(set.intersection, (self.documents_search_engine[word] for word in words), set(self.keys_search_engine.keys()))
        except (Exception, KeyError, IndexError) as err:
            return ''

    # Recupera el contenido de la estructura índice invertido del disco (FS)
    def read_data(self):
        if not self.documents_search_engine:
            f = open(self.name_db_search_engine,'r')
            content = f.read()
            f.close()
            self.documents_search_engine = ast.literal_eval(content)
            k = open(self.name_key_search_engine,"r")
            content = k.read()
            k.close()
            self.keys_search_engine = ast.literal_eval(content)
    
    def get_content_file(self,file):
        f = open(str(self.path_directory+file),encoding='utf8')
        content = f.read()
        f.close()
        return content