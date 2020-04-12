from glob import glob


BASE_PATH = './documentation/documents/'
IMAGE_FOLDER = 'images/'
# index = []


def execute():
    index = create_index(BASE_PATH)
    print(index)


def create_index(directory):
    index = []
    sub_directories = get_directories(directory)
    if len(sub_directories) is 0:
        # return
        return create_directory_list(directory)
    else:
        for sub_directory in sub_directories:
            tmp = []
            directory_name = ((sub_directory.replace(BASE_PATH, '')).replace('/', '')).replace('-', ' ')
            tmp.append(directory_name)

            if has_sub_directories(sub_directory):
                for x in create_index(sub_directory):
                    tmp.append(x)

            tmp.extend(create_directory_list(sub_directory))
            index.append(tmp)

    return index


def create_directory_list(directory):
    tmp = []
    files = glob(directory + '*.md')

    for file in files:
        name = ((file.replace(directory, '')).replace('.md', '')).replace('-', ' ')
        tmp.append(name)

    return tmp


def get_files(directory):
    files = glob(directory + '*.md')
    tmp = []

    counter = 0
    for file in files:
        name = ((file.replace(directory, '')).replace('.md', '')).replace('-', ' ')
        tmp.append(name)
        counter += 1

    return tmp


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


execute()
