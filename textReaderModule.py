#!
from os import listdir
from os.path import isfile, join
def readFile(fileName):
    with open (fileName) as f:
        lines = f.readlines
        return (f)

def readDer(PathStart):
    listFiles = [f for f in listdir(PathStart) if isfile (join(mypath, f))]

def 