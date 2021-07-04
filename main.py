# !/usr/bin/env python
# -*- coding: utf-8 -*-

""" main.py: aplicación que utiliza la clase InvertedIndex como búsqueda de índice invertido. """

import sys
import pathlib
from InvertedIndex import InvertedIndex
from pprint import pprint as pp

__author__ = "Gonzalo Chacaltana"
__email__ = "gchacaltanab@outlook.com"

if __name__ == "__main__":
    path_directory_docs = str(pathlib.Path(
        __file__).parent.resolve()) + "/documents/*.txt"
    ii = InvertedIndex(path_directory_docs)
    
    # Búsqueda de palabras
    search_words = ["solicitud"]
    print('\nBúsqueda de: ' + repr(search_words))
    pp(sorted(ii.search_words(search_words)))

    search_words = ["banco"]
    print('\nBúsqueda de: ' + repr(search_words))
    pp(sorted(ii.search_words(search_words)))

    print('\nIntersección de palabras ')
    search_words = ["solicitud", "banco"]
    print('Búsqueda de: ' + repr(search_words))
    pp(sorted(ii.search_words(search_words)))