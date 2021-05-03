from downloadFunctions import *
from time import sleep
import pafy

def download(vid, location):
    title = standardizeTitle(vid.title)    #Make title conform to acceptable system parameters,
                                           #e.g. some videos have '\' and '?', which can mess up in certain systems

    existence = find(title, location)    #Check if the video isn't already downloaded in the assigned destination folder to conserve data

    if existence[0] == False:
        vid.getbest().download(filepath=location, quiet=True)    #Downloads video to folder
        print("        Succesfully downloaded %s!"%(vid.title))
    else:
        print("%s already exists in %s\n" % (title, location))
        sleep(1)
