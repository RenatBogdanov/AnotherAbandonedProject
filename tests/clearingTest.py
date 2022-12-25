import os

def clearDir(dir): 
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

clearDir('userProfileAvatars/')
