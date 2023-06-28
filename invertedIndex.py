import sys,os,re

import time

define global variables used as counters
tokens = 0

documents = 0

terms = 0

termindex = 0

docindex = 0

initialize list variablenull
alltokens = []

alldocs = []

nullCapture the start time of the routine so that we can determine the total runningtime required to process the corpusnull
t2 = time.localtime()  

set the name of the directory for the corpusnull
dirname = "c:\users\datai\cacm"

For each document in the directory read the document into a stringnull
all = [f for f in os.listdir(dirname)]

for f in all:

  documents+=1

  with open(dirname+'/'+f, 'r') as myfile:

  alldocs.append(f)

  data=myfile.read().replace('\n', '') 

  for token in data.split():

  alltokens.append(token)

  tokens+=1

Open for write a file for the document dictionarynull
documentfile = open(dirname+'/'+'documents.dat', 'w')

alldocs.sort()

for f in alldocs:

  docindex += 1

  documentfile.write(f+','+str(docindex)+os.linesep)

documentfile.close()

nullSort the tokens in the list
alltokens.sort()

nullDefine a list for the unique terms
g=[]

nullIdentify unique terms in the corpus
for i in alltokens:   

  if i not in g:

  g.append(i)

  terms+=1

terms = len(g)

Output Index to disk file. As part of this process we assign an 'index' number to each unique term.null
indexfile = open(dirname+'/'+'index.dat', 'w')

for i in g:

  termindex += 1

  indexfile.write(i+','+str(termindex)+os.linesep)

indexfile.close()

Print metrics on corpusnull
print 'Processing Start Time: %.2d:%.2d' % (t2.tm_hour, t2.tm_min)

print "Documents %i" % documents

print "Tokens %i" % tokens

print "Terms %i" % terms

t2 = time.localtime()  

print 'Processing End Time: %.2d:%.2d' % (t2.tm_hour, t2.tm_min)
