# -*- coding: utf-8 -*-
import os

class FileInfo():

    def __init__(self, path):
        self.original_path = path
        self.filename = os.path.basename(path)

    def get_info(self):
        return (
                self.filename,
                self.original_path,
                os.path.abspath(self.filename),
                os.path.getsize(self.filename)
                )
