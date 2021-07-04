
# !/usr/bin/env python
# -*- coding: utf-8 -*-

""" InvertedIndex.py: Clase que implementa los métodos del índice invertido. """

__author__ = "Gonzalo Chacaltana"
__email__ = "gchacaltanab@outlook.com"
__version__ = "1.0.1"

import sys
from glob import glob
from functools import reduce


class InvertedIndex(object):
    def __init__(self, path_directory_documents):
        self.texts = {}
        self.words = set()
        self.dict_inv_idx = {}
        self.encoding = "utf8"
        self.path_directory = path_directory_documents
        self.load_documents()
        self.create_dict_inv_index()

    # Carga el contenido de los ficheros *.txt
    def load_documents(self):
        for file in glob(self.path_directory):
            with open(file, encoding=self.encoding) as f:
                content = f.read().split()
                self.words |= set(content)
                self.texts[file.split('\\')[-1]] = content

    # Crea el índice invertido
    def create_dict_inv_index(self):
        self.dict_inv_idx = {word: set(txt for txt, words in self.texts.items()
                          if word in words) for word in self.words}

    # Búsqueda de palabras en el índice invertido
    def search_words(self, words):
        try:
            return reduce(set.intersection, (self.dict_inv_idx[word] for word in words), set(self.texts.keys()))
        except (Exception, KeyError, IndexError) as err:
            return ""