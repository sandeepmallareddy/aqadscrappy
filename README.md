#AQAD Scrapper
# 26-06-2016

aqad.py - Core scraper engine
config.py - To store the session ID and temp_aqad_userID values
            - These values can be obtained by looking at the header of a post request through firebug or              chrome inspector
getaqad.py - Command Line Interface for running batch scripts.

<SYNTAX>
python getaqad.py <grade> <fromdate> <todate>
<grade>- Int- values from 3 to 9; any other value will result in No Record found
<fromdate>-String - From date in 'YYYY-MM-DD' format, anyother format will result in error
<todate> - String - To date in 'YYYY-MM-DD' format. Should be greater than From Date. Record will include the toDate

@Returns
aqad_fromdate-toDate_Grade_grade.csv

containing
Date, Class,Subject, Question, OptionA,OptionB,OptionC,OptionD,Correct_answer. Header might be missing

E.g
python getaqad.py 6 "2016-06-01" "2016-06-26"

Output
Gothca Q12345
No Record
Gotcha Q233
....


