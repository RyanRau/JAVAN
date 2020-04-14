from glob import glob
from .models import Directory, File

BASE_PATH = './documentation/documents/'
IMAGE_FOLDER = 'images/'

index = []


def execute():
    toc = create_toc(BASE_PATH)
    return toc, index


def create_toc(directory):
    toc = []
    sub_directories = get_directories(directory)
    if len(sub_directories) is 0:
        # return
        return create_directory_list(directory)
    else:
        for sub_directory in sub_directories:
            tmp = []

            directory_object = create_directory_object(sub_directory)
            tmp.append(directory_object)

            if has_sub_directories(sub_directory):
                for x in create_toc(sub_directory):
                    tmp.append(x)

            tmp.extend(create_directory_list(sub_directory))

            toc.append(tmp)

    return toc


def create_directory_list(directory):
    tmp = []
    files = glob(directory + '*.md')

    for file in files:
        tmp.append(create_file_object(file, directory))

    return tmp


def create_directory_object(directory):
    directory_object = Directory()
    directory_object.path = directory
    directory_object.name = ((directory.replace(BASE_PATH, '')).replace('/', '')).replace('-', ' ')
    return directory_object


def create_file_object(file, directory):
    file_object = File()

    file_object.uuid = len(index)
    index.append(file)

    file_object.path = file

    name = ((file.replace(directory, '')).replace('.md', '')).replace('-', ' ')
    file_object.name = name
    return file_object


def get_directories(directory):
    directories = glob(directory + '*/')
    # Hides image folder
    try:
        directories.remove(directory + IMAGE_FOLDER)
    except Exception:
        pass
    return directories


def has_sub_directories(directory):
    sub_directories = get_directories(directory)
    if len(sub_directories) is 0:
        return False
    else:
        return True
