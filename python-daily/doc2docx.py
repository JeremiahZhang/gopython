# -*- coding:utf-8 -*-

# Copy from https://stackoverflow.com/a/48832989
# Using MS word transfer doc to docx.
# But I want to use WPS, I need to change it.

from glob import glob
import re
import os
import win32com.client as win32
from win32com.client import constants

# Create list of paths to .doc.files
paths = glob('E:\\2016-Work\\lab_doc\\working_review\\**\\*.doc', recursive=True)

def save_as_docx(path):
    # Opening MS Word
    word = win32.gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(path)
    doc.Activate()
    
    # Rename path with .docx
    new_file_abs = os.path.abspath(path)
    new_file_abs = re.sub(r'\.\w+$', '.docx', new_file_abs)
    
    # Save and close
    word.ActiveDocument.SaveAs(
        new_file_abs, FileFormat=constants.wdFormatXMLDocument
    )
    
    doc.Close(False)

for path in paths:
    save_as_docx(path)