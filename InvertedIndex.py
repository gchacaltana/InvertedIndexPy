
# !/usr/bin/env python
# -*- coding: utf-8 -*-

""" InvertedIndex.py: Clase que implementa los métodos del índice invertido. """

__author__ = "Gonzalo Chacaltana"
__email__ = "gchacaltanab@outlook.com"
__version__ = "1.0.1"

import sys
import ast
from glob import glob
from functools import reduce


class InvertedIndex(object):
    def __init__(self, path_directory_documents):
        self.texts = {}
        self.words = set()
        self.inverted_index = {}
        self.encoding = "utf8"
        self.path_directory = path_directory_documents
        self.name_file_inv_idx = "data_inv_idx.txt"
        self.run()

    def run(self):
        self.load_documents()
        self.create()
        self.save()

    # Carga el contenido de los ficheros *.txt
    def load_documents(self):
        counter_files = 0
        for file in glob(self.path_directory):
            counter_files = counter_files + 1
            with open(file, encoding=self.encoding) as f:
                content = f.read().split()
                self.words |= set(content)
                self.texts[file.split('\\')[-1]] = content
        print("\nSe procesaron {} documentos. Ruta: {}".format(counter_files, self.path_directory))

    # Crea el índice invertido
    def create(self):
        self.inverted_index = {word: set(txt for txt, words in self.texts.items()
                                         if word in words) for word in self.words}
        print("Se creo el indice invertido")

    def save(self):
        f = open(self.name_file_inv_idx, "w")
        f.write(str(self.inverted_index))
        f.close()
        print("Se guardo la informacion del indice invertido en disco")

    def read_data(self):
        if not self.inverted_index:
            f = open (self.name_file_inv_idx,'r')
            content = f.read()
            f.close()
            self.inverted_index = ast.literal_eval(content)

    # Búsqueda de palabras en el índice invertido
    def search_words(self, words):
        self.read_data()
        try:
            return reduce(set.intersection, (self.inverted_index[word] for word in words), set(self.texts.keys()))
        except (Exception, KeyError, IndexError) as err:
            return ""
