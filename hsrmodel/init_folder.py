def init_folder(parms):
    import os
    import shutil

    PathDataFolder = '../Data/' + parms["Name"]
    PathCore = PathDataFolder
    n = 0
    if os.path.isdir(PathDataFolder):

        prompt = 'Folder ' + PathDataFolder + ' already excists. Overwrite y/n?'
        overwrite = boolinput(prompt)

        if overwrite:
            shutil.rmtree(PathDataFolder)

        while os.path.isdir(PathDataFolder) and overwrite == False:
            PathDataFolder = PathCore + str(n)
            n = n + 1

    os.mkdir(PathDataFolder)
    parms["PathDataFolder"] = PathDataFolder

    return parms

def boolinput(prompt):
    # from https://stackoverflow.com/questions/32616548/how-to-have-user-true-false-input-in-python
    # credit Joran Beasley
    while True:
            try:
               return {"y":True,"n":False}[input(prompt+'\n').lower()]
            except KeyError:
               print("Invalid input please enter y or n!")
