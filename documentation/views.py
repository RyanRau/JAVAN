from django.http import HttpResponse
from django.shortcuts import render
import os
from glob import glob
import markdown


#  Markdown Documentation
# https://python-markdown.github.io


# .../documentation/
def index(request):
    x = getFileTree()

    html = markdown.markdown(open("./documentation/documents/database-structure/user-model.md").read(),
                             extensions=['tables'])
    # html = markdown.markdownFromFile()

    context = {
        'toc': x,
    }
    return render(request, "documentation/index.html", context)


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
