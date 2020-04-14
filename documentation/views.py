from django.http import HttpResponse
from django.shortcuts import render

from documentation import indexing

import markdown

#  Markdown Documentation
# https://python-markdown.github.io

BASE_PATH = " ./documentation/documents"

toc, toc_index = indexing.execute()


# .../documentation/
def index(request):

    context = {

    }
    return render(request, "documentation/index.html", context)


# .../documentation/document/<int:file_id>
def view_document(request, file_id):
    file_path = toc_index[file_id]
    html = markdown.markdown(open(file_path).read(),
                             extensions=['tables', 'fenced_code'])
    # TODO: Add error checking if invalid
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
