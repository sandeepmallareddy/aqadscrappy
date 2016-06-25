import aqad
import config
import sys
import argparse
import datetime


#Arguments accepted by getAQAD --from --to --grade
parser = argparse.ArgumentParser()
parser.add_argument("grade",type=int,help="Specify the grade 3-9")
parser.add_argument("fromdate",help="Specify the start date")
parser.add_argument("todate",help="Specify the end date")
args = parser.parse_args()

#Assign the variables
grade = args.grade
fromdate = args.fromdate
todate = args.todate

filename = 'aqad-{0}_{1}-Grades_{2}.csv'.format(fromdate,todate,grade)

#convert time from string to a date-time struct
convfromdate = datetime.datetime.strptime(fromdate,"%Y-%m-%d").date()
convtodate =  datetime.datetime.strptime(todate,'%Y-%m-%d').date()

#diff in dates
diffdate = convtodate-convfromdate


if(grade>=3 and diffdate.days > 0):
    for i in range(diffdate.days+1):
        onedate =  convfromdate+datetime.timedelta(days=i)
        aqad.getAQAD(config.phpsess,config.tauID,grade,onedate,filename)
else:
    print "Wrong inputs.From date should be less than to date"





#use aqad.getAQAD function to retrieve the item and write it to aqad.csv 
#aqad.getAQAD(config.phpsess,config.tauID,6,'2016-06-26')
