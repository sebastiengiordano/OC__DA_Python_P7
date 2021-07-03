from os.path import dirname, join, exists, isfile
from os import listdir, makedirs


def folder_path(file: str):
    '''Returns the directory component of a pathname.'''
    return dirname(file)


def path_join(*path: str):
    '''Concatenate path'''
    return join(*path)


def files_in_folder(folder_path: str) -> list:
    '''Return the list of all files in folder_path and its subfolder'''
    files_in_folder_path = []
    # Loop on all files or directories inside folder_path
    for file_or_dir in listdir(folder_path):
        file_or_dir_path = join(folder_path, file_or_dir)
        # If file_or_dir is a file
        if isfile(file_or_dir_path):
            # Add it to the files list
            files_in_folder_path.append(file_or_dir)
        else:
            # Loop inside the subfolder to find all files
            files_in_subfolder = files_in_folder(file_or_dir_path)
            # Add relative path from folder_path
            for index, file in enumerate(files_in_subfolder.copy()):
                files_in_subfolder[index] = file_or_dir + "/" + file
            # Add this files to the files list
            files_in_folder_path += files_in_subfolder
    return files_in_folder_path


def file_exists(file):
    '''Return True if the file exists, otherwise return False'''
    return exists(file)


def check_create_folder(file_or_dir):
    '''From an absolute path, create the folder if it doesn't already exist'''
    # keep only the folder path
    dir = dirname(file_or_dir)
    # Check if this/these folders exist
    if not exists(dir):
        # Created the folders
        makedirs(dir)
