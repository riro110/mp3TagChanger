import os

path = input("path = ")
path = path.replace("\\", "/")

        
def rename(path):
    for f in os.listdir(path):
        if os.path.isdir(path+"/"+f):
            rename(path+"/"+f)
        else:
            if "3gp" in f:
                os.rename(path + "/" + f, path + "/" + f.replace("3gp", "m4a"))


rename(path)