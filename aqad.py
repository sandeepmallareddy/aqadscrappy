import requests
import json
import csv
import sys


#set the PHPSESSID
#phpsess = 'r9qlveos8ij6607krd9q2tacq3'

#Set the temp_aqad_userId
#tauID = 'ee1c1e48dc4dafede3a86c02e6b0f250'

#get the class for the item
#grade = 4

#get the date for question
#date = '2016-06-22'

def getAQAD(phpsess,tauID,grade,date,filename='aqad.csv'):
 url = 'http://aqad.in/aqadAjax.php?class={0}'.format(grade)

 headers = {'Cookie': 'PHPSESSID={0};temp_aqad_userId={1}'.format(phpsess,tauID),'Origin': 'http://www.aqad.in','Accept-Encoding': 'gzip, deflate','Accept-Language': 'en-US,en;q=0.8','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Accept':' */*','Referer': '{0}'.format(url),'X-Requested-With': 'XMLHttpRequest','Connection': 'keep-alive'}

 data = {'class':grade,'func':'fetchAQAD','date':date,'user':'sandman.blitz%40gmail.com'}

#run request
 r = requests.get(url,headers=headers,params=data)

#get data and convert it into JSON obj
 jsonobj = json.loads(r.text)

#get the req fields
 if jsonobj.has_key('subject'):
  sub = jsonobj['subject']
  ques = jsonobj['question']
  opA = jsonobj['optiona']
  opB = jsonobj['optionb']
  opC = jsonobj['optionc']
  opD = jsonobj['optiond']
  corr_ans = jsonobj['correct_answer']

#Open CSV file and write

  with open(filename, 'ab') as csvfile:
        rowwriter = csv.writer(csvfile)
        rowwriter.writerow([date,grade,sub,ques.encode('utf-8'),opA.encode('utf-8'),opB.encode('utf-8'),opC.encode('utf-8'),opD.encode('utf-8'),corr_ans.encode('utf-8')])

  print "Gotcha Question {0}".format(jsonobj['qcode']);
 else:
  print "No record"
 



