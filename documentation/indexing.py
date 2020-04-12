import os
from glob import glob
from .models import Directory, File


BASE_PATH = './documentation/documents/'
IMAGE_FOLDER = 'images/'
index = []
x = os.walk(BASE_PATH)

def excute():
    root_directories = getDirectories(BASE_PATH)
    # buildIndex(root_directories, '')

    x = os.walk(BASE_PATH)

    # deal with files in root dir
    # index.append(getFiles(BASE_PATH, counter))



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
    directories = glob(directory + '*/')
    # Hides image folder
    try:
        directories.remove(directory + IMAGE_FOLDER)
    except Exception:
        pass
    return directories


# def buildIndex(current_directory, index):
    # counter = 0
    # for directory in current_directory:
    #     sub_directories = getDirectories(directory)
    #
    #     if len(sub_directories) is 0:
    #         buildIndex(sub_directories, index + '-' + str(counter))
    #
    #     tmp = []
    #
    #     new_directory = Directory()
    #     new_directory.path = directory
    #     new_directory.name = ((directory.replace(BASE_PATH, '')).replace('/', '')).replace('-', ' ')
    #
    #     tmp.append(new_directory)
    #
    #     tmp.extend(getFiles(directory, index + '-' + str(counter)))
    #
    #     index.append(tmp)
    #     counter += 1

excute()

