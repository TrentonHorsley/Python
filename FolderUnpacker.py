import os
import shutil

#Set global Variables
destination_path = input(r'Path where you want files to go: ')
source_directory = input(r'Path containing folders you want to unpack: ')

def folder_unpacker(source_directory, destination_path):
    for folder_name in os.listdir(source_directory):
        folder_path = os.path.join(source_directory, folder_name)
        for files in os.listdir(folder_path):
            filepath = os.path.join(folder_path, files)
            shutil.copy(filepath, destination_path)
            print(filepath + ' '+'copied to'+ ' '+destination_path)

if __name__ == '__main__':
    folder_unpacker(source_directory, destination_path)