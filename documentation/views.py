import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import os
from glob import glob
import markdown

from documentation import indexing
from documentation import demo

#  Markdown Documentation
# https://python-markdown.github.io

BASE_PATH = " ./documentation/documents"

# .../documentation/
def index(request):
    x = getFileTree()

    html = markdown.markdown(open("./documentation/documents/database-structure/user-model.md").read(),
                             extensions=['tables'])
    # html = markdown.markdownFromFile()

    context = {
        'toc': indexing.index,
    }
    return render(request, "documentation/index.html", context)



def getDocument(request,  doc_id):
    # Create file path
    d = doc_id.split('-')
    return render(request, "documentation/index.html")


def getFileTree():
    p = []
    p.append(glob("./documentation/documents/*.md"))

    folder = './documentation/documents'
    filepaths = [os.path.join(folder, f) for f in os.listdir(folder)]

    fol = glob("./documentation/documents/*/")
    for f in fol:
        e = f.replace('./documentation/documents/', '')
        tmp = [e]
        tmp.extend(glob(f + "*.md"))
        p.append(tmp)

    return p
