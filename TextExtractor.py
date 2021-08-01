# !/usr/bin/env python
# -*- coding: utf-8 -*-

""" TextExtractor: Clase que extrtae texto de los documentos de un directorio. """

__author__ = "Gonzalo Chacaltana"
__email__ = "gchacaltanab@outlook.com"
__version__ = "1.0.1"

from glob import glob
import sys
import os
import PyPDF2
import pathlib


class TextExtractor(object):

    def __init__(self, path_directory, extension_files):
        self.extension_files = extension_files
        self.path_directory = path_directory
        self.encoding = "utf8"
        self.mode_oppening_pdf = "rb" # rb = read on binary
        self.documents = []
        self.filter = "*"
        self.full_path = str(pathlib.Path(self.path_directory +"/"))
        self.extract()

    def extract(self):
        self.setPathExtensionFilter()
        if (self.extension_files == "txt"):
            self.read_documents_txt()
        elif (self.extension_files == "pdf"):
            self.read_documents_pdf()
        elif (self.extension_files == "*"):
            self.read_all_documents()

    def setPathExtensionFilter(self):
        """
        Define el filtro de tipos de archivos y el full path del directorio.
        """
        if self.extension_files != "*":
            self.filter = "*." + self.extension_files
            self.full_path = str(pathlib.Path(self.path_directory + "/" + self.filter))

    def read_documents_txt(self):
        """
        Recorre ficheros txt de un directorio
        """
        self.counter = 0
        for file in glob(self.full_path):
            self.counter = self.counter + 1
            self.extract_document_txt(file)

    def read_documents_pdf(self):
        self.counter = 0
        for file in glob(self.full_path):
            self.counter = self.counter + 1
            self.extract_documents_pdf(file)

    def read_all_documents(self):
        self.counter = 0
        dir_files = os.listdir(self.full_path)
        for file in dir_files:
            self.counter = self.counter + 1
            extension = os.path.splitext(os.path.basename(file))[1]
            if (extension=="txt"):
                self.extract_document_txt(self.full_path + "/"+ file)
            elif (extension=="pdf"):
                self.extract_document_txt(self.full_path + "/"+ file)

    def extract_document_txt(self, file):
        """
        Extrae el texto de ficheros txt
        Args:
            file (string): nombre del fichero 
        """
        filename = os.path.basename(file)
        with open(file, encoding=self.encoding) as f:
            content = f.read()
            self.documents.append((filename, content, self.path_directory))

    def get_file_name(self,file):
        """
        Devuelve nombre de archivo
        Args:
            file (string): Nombre y extensión de fichero.

        Returns:
            string: Nombe sin extension del fichero 
        """
        return os.path.splitext(os.path.basename(file))[0]

    def extract_documents_pdf(self, file):
        filename = os.path.splitext(os.path.basename(file))[0]
        pdf_file = open(file, self.mode_oppening_pdf)
        # Objeto PDF File Reader
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.numPages
        for page in range(num_pages):
            # Creando objeto por cada página del documento PDF.
            pageObj = pdf_reader.getPage(page)
            # Extrayendo texto de la página
            content = pageObj.extractText()
            self.documents.append((filename+"_pag_"+str(page + 1), content))
            # Cerrando el objeto PDF File Reader
        pdf_file.close()

    def get_documents(self):
        return self.documents
