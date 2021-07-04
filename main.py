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
    # definimos directorio donde se encuentran los documentos (comentarios de tweet).
    path_directory_docs = str(pathlib.Path(__file__).parent.resolve()) + "/documents/"
    # definimos el filtro a considerar en la extracción de archivos.
    filter_files = "*.txt"

    # instanciamos la clase InvertedIndex en la variable "ii"
    ii = InvertedIndex(path_directory_docs, filter_files)

    # Realizamos la búsqueda de documentos relacionados a la palabra "solicitud"
    search_words = ["solicitud"]
    print('\nBúsqueda de: ' + repr(search_words))
    pp(sorted(ii.search_words(search_words)))

    # Realizamos la búsqueda de documentos relacionados a la palabra "banco"
    search_words = ["banco"]
    print('\nBúsqueda de: ' + repr(search_words))
    pp(sorted(ii.search_words(search_words)))

    # Realizamos la búsqueda de documentos por intersección de palabras
    print('\nIntersección de palabras ')
    search_words = ["solicitud", "banco"]
    print('Búsqueda de: ' + repr(search_words))
    pp(sorted(ii.search_words(search_words)))