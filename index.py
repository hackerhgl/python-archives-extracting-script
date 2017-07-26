import os
import zipfile
import patoolib
import time
import shutil
times = []
removeDirs = False

def timer(note, flag):
    times.append({'note': note, 'time': time.time()})
    if not flag:
        print 'Message: '+note+' Time : '+ str(times[-1]['time'] - times[-2]['time'])

timer("STarted", 1)

indir = "ins/"
outdir = "ous/"
zips = os.listdir(indir)

print "\n ***************** Python Archives Extraction Script ***************** \n"

def mkdir (file):
    extractDir = file.split(".")
    extractDir.pop()
    extractDir = outdir+".".join(extractDir)
    if removeDirs and os.path.isdir(extractDir):
        shutil.rmtree(extractDir)
    if not removeDirs and os.path.isdir(extractDir):
        return extractDir
    os.makedirs(extractDir)
    return extractDir

def extractZip(file):
    extractDir = mkdir(file)
    zipRef = zipfile.ZipFile(indir+file, "r")
    zipRef.extractall(extractDir)
    zipRef.close()

def extractRar(file):
    extractDir = mkdir(file)
    patoolib.extract_archive(indir+file, outdir=extractDir)

print "\n ***************** Script Start ***************** \n"
timer('Before unzip', 0)
for file in zips:
    ext = file.split(".").pop()
    print "\n **** Extracting "+file+" **** \n"
    if ext == "zip":
        extractZip(file)
    elif ext == "rar":
        extractRar(file)
    print "\n **** Extracted "+file+" **** \n"

timer('after unzips', 0)
print "\n ***************** Script End ***************** \n"
