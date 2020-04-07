from django.db import models


# Create your models here.
class Directory:
    name = ''
    path = ''

    def getClass(self):
        return 'Directory'


class File:
    uuid = '0'
    path = ''
    name = ''

    def getClass(self):
        return 'File'
