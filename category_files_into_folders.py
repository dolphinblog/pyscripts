#!/usr/bin/python3
# coding:utf-8

'''
Usage:

******************************
python do.py task col database
******************************
task: a text file, list every single task
col: where the folder name locates in a task line that you want to put the file in.
database: the file database where you get the specified file.

'''

import sys
import os
import shutil
import codecs

if len(sys.argv) != 4:
	print('Wrong argument number.')
	sys.exit(0)
if not os.path.isfile('./' + sys.argv[1]):
	print("Task file: " + sys.argv[1] + ' doesn\'t exit.')
	sys.exit(0)
if not sys.argv[2].isdigit():
	print(sys.argv[2] + ' is not a valid int number.')
	sys.exit(0)
if not os.path.isdir('./' + sys.argv[3]):
	print(sys.argv[3] + ' doesn\'t exist.')
	sys.exit(0)

task = sys.argv[1]
nameCol = int(sys.argv[2])
database = sys.argv[3]

dataList = os.listdir('./' + database)

with codecs.open(task, 'r', encoding="utf-8") as f:
	taskLines = f.readlines()

log = codecs.open(task + '.log.txt', 'w', encoding='utf-8')
wc = 0
for taskLine in taskLines:
	oneLineList = taskLine.split('|')
	if not len(oneLineList) < 2:
		barCode = oneLineList[0].strip()
		picName = barCode + '.jpg'
		try:
			folderName = oneLineList[nameCol - 1].strip()
		except:
			warnword = "Warning: Line\"",taskLine,"\"doesn't have", nameCol, "column after split by |."
			print(warnword)
			log.write(warnword + '\r\n')
			continue
	else:
		warnword = 'Not a valid line:' + taskLine
		print(warnword)
		log.write(warnword + '\r\n')
		continue
	desPath = './' + task + '-' + database + '/' + folderName + '/'
	if not os.path.isdir(desPath):
		os.makedirs(desPath)
	if picName in dataList:
		shutil.copy('./'+database+'/'+picName, desPath + picName)
		print('Succuss copy: ' + './' + database + '/' + picName + '-->' + desPath + picName)
		wc += 1
	else:
		warnword = 'Cannot find ' + picName + ' in '+ database
		print(warnword)
		log.write(warnword + '\r\n')


endword = "All " + str(wc) + ' times copy were done.'
print(endword)
log.write(endword+'\r\n')
log.close()
