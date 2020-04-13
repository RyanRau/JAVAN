import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import os
from glob import glob
import markdown
from django.forms.models import model_to_dict

from documentation import indexing

#  Markdown Documentation
# https://python-markdown.github.io

BASE_PATH = " ./documentation/documents"

toc, toc_index = indexing.execute()


# .../documentation/
def index(request):
    # html = markdown.markdownFromFile()

    context = {

    }
    # html = "<ul>" \
    #        "<li>hello</li>" \
    #        "<li>by</li>" \
    #        "</ul>"
    html = build_toc(toc, "<ul>")
    # return HttpResponse(html)
    return render(request, "documentation/index.html", context)


def view_document(request, file_id):
    file_path = toc_index[file_id]
    html = markdown.markdown(open(file_path).read(),
                             extensions=['tables'])
    return HttpResponse(html)


############################################################################
# Auto creates HTML for TOC
############################################################################
# .../documentation/extras/toc
def view_toc(request):
    return HttpResponse(build_toc(toc, "<ul>"))


def build_toc(objects, html):
    for obj in objects:
        if type(obj) is list:
            html = build_toc(obj, html)
        else:
            if obj.getClass() is "Directory":
                html += "<li><b>" + str(obj.name) + "</b></li><ul>"
            else:
                html += "<li><a onclick='getDocument(" + str(obj.uuid) + ")'>" + str(obj.name) + "</a></li>"
    html += "</ul>"
    return html
