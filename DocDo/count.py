import os

def GetDoc(Pwd):
    oDir = os.listdir(Pwd)
    for oDoc in oDir:
        oSubDir = os.path.join(Pwd,oDoc)
        if os.path.isdir(oSubDir):
            print os.path.basename(oSubDir)
        else:
            print os.path.basename(oSubDir)

if __name__ == "__main__":
    Pwd = os.getcwd()
    print Pwd
    GetDoc(Pwd)
    
