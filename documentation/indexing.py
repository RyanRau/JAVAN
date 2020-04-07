from glob import glob
from .models import Directory, File


BASE_PATH = './documentation/documents/'
index = []


def excute():
    root_directories = getDirectories(BASE_PATH)

    counter = 0
    for directory in root_directories:
        tmp = []

        new_directory = Directory()
        new_directory.path = directory
        new_directory.name = ((directory.replace(BASE_PATH, '')).replace('/', '')).replace('-', ' ')

        tmp.append(new_directory)

        tmp.extend(getFiles(directory, counter))

        index.append(tmp)
        counter += 1

    # deal with files in root dir
    index.append(getFiles(BASE_PATH, counter))


def getFiles(directory, index):
    files = glob(directory + '*.md')
    tmp = []

    counter = 0
    for file in files:
        new_file = File()
        new_file.uuid = str(index) + "-" + str(counter)
        new_file.path = file

        name = ((file.replace(directory, '')).replace('.md', '')).replace('-', ' ')
        new_file.name = name

        tmp.append(new_file)
        counter += 1

    return tmp


def getDirectories(directory):
    return glob(directory + '*/')


excute()

