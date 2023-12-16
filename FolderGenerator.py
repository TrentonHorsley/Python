import app

#Inputs
dir_to_create_folders = input('Parent folder to generate in: ')
country = input('Country code: ')
project = input('Client code: ')
sitecode = input('Site Code: ')

infrastructure = []

n = int(input("Enter number of infrastructure for this project: "))\

# Folder Generator Script

for i in range(0, n):
    ele = input("Infrastructure name: ")
    infrastructure.append(ele)

date = input('Date: ')


if __name__ == '__main__':
        app.foldergenerator()