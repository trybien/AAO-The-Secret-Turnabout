# Code is a mildly adapted version of this SO answer. https://stackoverflow.com/a/56381857

import glob
import os

# Make sure file is in the highest directory of your repository
# Assumes there is only 1 Folder called GitHub above it
mypath=os.getcwd()
githubSite = mypath[mypath.find('\\GitHub\\')+8:mypath.find('.io')+4]

# Change r'\**\*.gif' to whatever extension you want to generate links for.
files = glob.glob(mypath + r'\**\*.*', recursive=True)

fileOutput = '<body>'
# print(files) # as list
for f in files:
    splitResult = f.split(".github.io")
    fileOutput += "<a href=https://" + githubSite + splitResult[1].replace('\\','/').replace(' ','%20') + ">https://" + githubSite + splitResult[1].replace('\\','/') + '</a> <br />'
	
fileOutput += '</body>'

f = open('index.html', "w", encoding="utf-8")
f.write(fileOutput)
f.close()