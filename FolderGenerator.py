import os

def folder_generator():

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

    #Lists containing folders to be created in batches
    last3 = ['dgn', 'Rasters', 'Models']
    photogram3 = ['Data', 'Output', "Processing"]
    processingfolders = ['Exports']
    processing = ['3Dprocessing','2Dprocessing']
    rasterfolders = ['1stExport','2ndRotated','3rdGeoPostprocessed','4thTransparentForCloud','acoustic']
    AcousticCorrectionFolders = ['CSRS_Corrections', 'Raw_Logs', 'Base_Logs','RINEX','Solution']
    cloudsync = ['preprocessing', 'deliveries']

    # Create primary directory

    contractHolder = str(dir_to_create_folders) + '/' + str(country) + '/' + str(project) + '/' + str(sitecode)

    try:
        os.makedirs(contractHolder)
        os.chdir(contractHolder)
    except FileExistsError:
        print("Directory ", contractHolder, " already exists")
        os.chdir(contractHolder)


    #loop through remaining directories for each site

    for j in range(0, len(infrastructure)):

            infraDirs = str(infrastructure[j])

            try:
                os.makedirs(infraDirs)
                print("Directory ", infraDirs, " Created ")
            except FileExistsError:
                print("Directory ", infraDirs, " already exists")

            # Create target Directory if don't exist

            if not os.path.exists(infraDirs):
                os.makedirs(infraDirs)
                print("Directory ", infraDirs, " Created ")
            else:
                print("Directory ", infraDirs, " already exists")

    for k in range(0,len(infrastructure)):

            dirName = str(infrastructure[k]) + '/' + str(date)

            try:
                # Create target Directory
                os.makedirs(dirName)
            except FileExistsError:
                print("Directory ", dirName, " already exists")

                # Create target Directory if don't exist
            if not os.path.exists(dirName):
                os.makedirs(dirName)
                print("Directory ", dirName, " Created ")
            else:
                print("Directory ", dirName, " already exists")

                for t in range(0,len(processing)):

                        dirName2 = str(infrastructure[k]) + '/' + str(date) + '/' + str(processing[t])

                        try:
                            # Create target Directory
                            os.makedirs(dirName2)
                        except FileExistsError:
                                print("Directory ", dirName2, " already exists")

                            # Create target Directory if don't exist
                        if not os.path.exists(dirName2):
                            os.makedirs(dirName2)
                            print("Directory ", dirName2, " Created ")
                        else:
                            print("Directory ", dirName2, " already exists")

                            for u in range(0,len(last3)):

                                dirname3 = str(infrastructure[k]) + '/' + str(date) + '/' + '2DProcessing' + '/' + str(last3[u])
                                dirnotes = str(infrastructure[k]) + '/' + str(date) + '/' + '2DProcessing' + '/' + str(ras)
                                try:
                                         # Create target Directory
                                    os.makedirs(dirname3)
                                except FileExistsError:
                                        print("Directory ", dirname3, " already exists")

                                     # Create target Directory if don't exist
                                if not os.path.exists(dirname3):
                                        os.makedirs(dirname3)
                                        print("Directory ", dirname3, " Created ")
                                else:
                                        print("Directory ", dirname3, " already exists")

                        for o in range(0, len(last3)):

                            dirname4 = str(infrastructure[k]) + '/' + str(date) + '/' + '3DProcessing' + '/' + str(photogram3[o])

                            try:
                                # Create target Directory
                                os.makedirs(dirname4)
                            except FileExistsError:
                                print("Directory ", dirname4, " already exists")

                            # Create target Directory if don't exist
                            if not os.path.exists(dirname4):
                                os.makedirs(dirname4)
                                print("Directory ", dirname4, " Created ")
                            else:
                                print("Directory ", dirname4, " already exists")

                            for b in range(0, len(processingfolders)):

                                dirname5 = str(infrastructure[k]) + '/' + str(date) + '/' + '3DProcessing' + '/' + 'Processing' + '/' + str(processingfolders[b])


                                try:
                                    # Create target Directory
                                    os.makedirs(dirname5)
                                except FileExistsError:
                                    print("Directory ", dirname5, " already exists")

                                # Create target Directory if don't exist
                                if not os.path.exists(dirname5):
                                    os.makedirs(dirname5)
                                    print("Directory ", dirname5, " Created ")
                                else:
                                    print("Directory ", dirname5, " already exists")


                            for e in range(0, len(rasterfolders)):

                                dirname6 = str(infrastructure[k]) + '/' + str(date) + '/' + '2DProcessing' + '/' + 'Rasters' + '/' + str(rasterfolders[e])

                                try:
                                # Create target Directory
                                 os.makedirs(dirname6)
                                except FileExistsError:
                                    print("Directory ", dirname6, " already exists")

                                # Create target Directory if don't exist
                                if not os.path.exists(dirname6):
                                    os.makedirs(dirname6)
                                    print("Directory ", dirname6, " Created ")
                                else:
                                    print("Directory ", dirname6, " already exists")

                            for v in range(0, len(AcousticCorrectionFolders)):

                                dirname6 = str(infrastructure[k]) + '/' + str(date) + '/' + '3DProcessing' + '/' + 'Data' + '/' + 'acoustic' + '/' + str(AcousticCorrectionFolders[v])

                                try:
                                # Create target Directory
                                 os.makedirs(dirname6)
                                except FileExistsError:
                                    print("Directory ", dirname6, " already exists")

                                # Create target Directory if don't exist
                                if not os.path.exists(dirname6):
                                    os.makedirs(dirname6)
                                    print("Directory ", dirname6, " Created ")
                                else:
                                    print("Directory ", dirname6, " already exists")

                            for m in range(0, len(cloudsync)):

                                dirname6 = str(infrastructure[k]) + '/' + str(date) + '/' + '3DProcessing' + '/' + 'Output' + '/' + 'aws' + '/' + str(cloudsync[m])

                                try:
                                # Create target Directory
                                 os.makedirs(dirname6)
                                except FileExistsError:
                                    print("Directory ", dirname6, " already exists")

                                # Create target Directory if don't exist
                                if not os.path.exists(dirname6):
                                    os.makedirs(dirname6)
                                    print("Directory ", dirname6, " Created ")
                                else:
                                    print("Directory ", dirname6, " already exists")









if __name__ == '__main__':
        folder_generator()