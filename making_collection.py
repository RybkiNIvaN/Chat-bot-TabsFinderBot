import os
import shutil


def add_to_collection(dir_name, my_file, path_src):
    os.chdir("C:\\Users\\steve\\PycharmProjects\\pythonProject1\\For_Project\\Tabs")
    print(os.getcwd())
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    print(os.getcwd())
    print(os.path.join(os.getcwd(), dir_name))
    os.chdir(os.path.join(os.getcwd(), dir_name))
    if not os.path.isfile(my_file):
        shutil.copy(os.path.join(path_src, my_file), os.getcwd())


def go_to_collection(dir_name):
    os.chdir("C:\\Users\\steve\\PycharmProjects\\pythonProject1\\For_Project\\Tabs")
    os.chdir(os.path.join(os.getcwd(), dir_name))
    return len(os.listdir())


def open_all_collection():
    collection_list = [i for i in os.listdir(os.getcwd())]
    return ', '.join(collection_list)


def file_in_collection(file_name):
    return file_name in os.listdir(os.getcwd())