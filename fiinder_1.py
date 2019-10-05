import os
import re
import sys
import glob
from os import walk
import mmap
from threading import  Thread
from datetime import datetime

#jake

extension_List = [".txt", ".ppt", ".doc",".xls", ".csv"]
#xtension_List = [".txt", ".doc"]
#filesList = [] # this is the domain of the search function.
searchList = []

t1 = datetime.now()
# def searchFile(fileName, keyword):
# 	openfile = open(fileName, encoding ='utf-8')
# 	line = openfile.readlines()
# 	for line in openfile:
#
# 				if keyword in part:
# 					print(fileName)
# 				line = openFile.readline()

def get_drives():
	response = os.popen("wmic logicaldisk get caption")
	list1 = []
	total_file = []

	for line in response.readlines():
		line = line.strip("\n")
		line = line.strip("\r")
		line = line.strip(" ")
		if (line == "Caption" or line == ""):
			continue
		list1.append(line)
	return list1

drivesList = get_drives()
print(drivesList)


#for drive in drivesList:

#	listOfFiles = os.listdir() # each Drive will have the main folders in it is directory.
	#for x in listOfFiles:
	#	print(drive)
	#	print(x)
os.chdir('/')
def spider(drivesList):

	counter = 0
	for drive in drivesList:
		for (dirname,dirs,files) in os.walk(drive):
			for filename in files:
				for extension in extension_List:
					if filename.lower().endswith(extension):
						cwd = os.getcwd()
						fullPath  = os.path.join(dirname,filename)
						if os.path.isfile(fullPath):
							print(fullPath)
							searchList.append(fullPath)

#### ver_01 : storing cwd and filename separately ####
cwdList = []
fileNameList = []

# def spider(drivesList):
#
# 	counter = 0
# 	for drive in drivesList:
# 		for (dirname,dirs,files) in os.walk(drive):
# 			for filename in files:
# 				for extension in extension_List:
# 					if filename.lower().endswith(extension):
# 						#if os.path.isfile(filename):
# 							#cwd = os.getcwd()
# 							#cwdList.append(cwd)
# 							#fileNameList.append(filename)
# 							print(cwd)


#spider(drivesList)
keyword ="trademarks"

file1 = 'C:Program Files\MATLAB\R2019a\trademarks.txt'


def searchFile1(sourceFile, keyword):

	a = sourceFile.replace('\t', '\\t').replace('\a', '\\a')
	#print(a)
	f = open(a, 'r')
	contents = f.read()
	if (contents.find(keyword) >0):
		print(sourceFile)

	# cwdSize = len(cwdList)
	# fileNameListSize = len(fileNameList)
	# if cwdSize != fileNameList:
	# 	print("ERROR: cwdSize and fileNameSize are not the same")
	# 	exit(1)
	# else :
	# 	index = 0;
	# 	while (index < cwdSize):
	# 		cwd = os.chdir(cwdList[indx])
	# 		sourceFile = fileNameList[index]
	# 		inFile = open(sourceFile,'r')
	# 		line = inFile.readlines()
	# 		for line in inFile:
	# 			if keyword in line:
	# 				print(inFile)
	# 			line = inFile.readlines()
searchFile1(file1, keyword)
t2 = datetime.now()

totalTime = t2-t1
print(totalTime)


					#print((str1+'/'+dirpath+'/'+dirname+'/'+name))




