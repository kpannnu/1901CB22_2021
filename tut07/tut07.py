
import csv 
from openpyxl import Workbook
import re
import os

path=os.path.join(os.getcwd()+"/course_feedback_remaining.xlsx") # checking if course_feedback_remaining.xlsx already exists in the directory ,if it exists then delete it
if os.path.isfile(path):
	os.remove(path)



def feedback_not_submitted():

	ltp_mapping_feedback_type = {1: 'lecture', 2: 'tutorial', 3:'practical'}
	output_file_name = "course_feedback_remaining.xlsx" 

	dict1={}								#dictionary to map subject no. with LTP from course_master_dont_open_in_excel.csv
	with open(os.path.join(os.getcwd()+"/course_master_dont_open_in_excel.csv")) as file_1:
		reader=csv.reader(file_1)
		for line in reader:
			dict1["{}".format(line[0])]="{}".format(line[2])

	dict2={}								#dictionary to map roll no. with name,email,aemail and contact from studentinfo.csv 
	with open(os.path.join(os.getcwd()+"/studentinfo.csv")) as file_2:
		reader=csv.reader(file_2)
		for line in reader:
			dict2["{}".format(line[1])]=["{}".format(line[0]),"{}".format(line[8]),"{}".format(line[9]),"{}".format(line[10])]# dict prepared to map roll no. with a lists having name,email,aemail and contact 
		
	list_1=[]								#making a list of lists with each list(having only 3 elements) having only the stud_roll, course_code and feedback_type taken from each row of course_feedback_submitted_by_students.csv as other columns in this csv is of our no use
	with open(os.path.join(os.getcwd()+"/course_feedback_submitted_by_students.csv")) as file_3:
		reader=csv.reader(file_3)
		for line in reader:
			list_1.append(["{}".format(line[3]),"{}".format(line[4]),"{}".format(line[5])])
			
			
	def foo(str):                               #function to convert L-T-P to list of required feedback outputs from student for a particular course
		p=re.compile("[\d.]+")
		list=re.findall(p,str)						# covert LTP from L-T-P format to a list in format [L,T,P]  using regex
		for x in range(3):
			if list[x]!='0':
				list[x]="{}".format(x+1)          #if L!=0 then convert the value to 1 ,similarly 2 for non-zero T and 3 for non-zero P in the list,and remain 0 for a zero bit 
		final_list=[y for y in list if y!='0']  # removing elements that are 0(that have zero bit) from the list as that part don't require feedback
		return final_list                      # final list that contains the feedback values required from a student for a particular course and will be checked in course_feedback_submitted_by_students.csv that whether he providd that feedback value

	output_list=[]                              #output_list is list of lists that will be appended to the output xlsx file once it is ready,right now it is declared empty
	with open(os.path.join(os.getcwd()+"/course_registered_by_all_students.csv")) as f:
		reader=csv.reader(f)
		
		for line in reader:
			output_list.append([line[0],line[1],line[2],line[3],dict2["Roll No"][0],dict2["Roll No"][1],dict2["Roll No"][2],dict2["Roll No"][3]])#appending the header row to the output_list
			break
		for line in reader:
			nonzero_bit_list=foo(dict1["{}".format(line[3])])# the list containing  all the feedback values that a student is supposed to give(eg. 1 for non zero L,2 for non zero T,nothing if a zero bit is there)for a particular course returned by calling foo function defined above
			
			for expected_feed_type in nonzero_bit_list:
				if [line[0],line[3],expected_feed_type] not in list_1:# checking if list of  name ,course_code and expected_feedtype matches with any list or element of list_1 that we formed above and see if a particular student have filled the feedback output for particular course ,if it matches then the student have filled feedback for that course and for that feedback type of the course if not then student details with that course code will go to remaing_feedback.csv
					output_list.append([line[0],line[1],line[2],line[3],dict2[line[0]][0],dict2[line[0]][1],dict2[line[0]][2],dict2[line[0]][3]])#appending the row containing student details taken form student info csv  along with the course name of that student who didn't filled the expected feedback for that feedback type of a particular course
					break       #if a student have not filled a particular feedback type of a course that is required to be filled then no need to check for other feedback type for that course as feedback type column  is not asked for that course in final ouptut file so we break the loop as soon as a particular feedback type of a course is not filled

			
	wb=Workbook()
	sheet=wb.active
	for x in output_list:  #appending the Output_list that conatins lists of data of students that didn't filled feedback to the ouput xlsx file  
		sheet.append(x)
	wb.save(os.path.join(os.getcwd()+"/course_feedback_remaining.xlsx"))
 

feedback_not_submitted()

# Note:- following were the Roll no. that were present in course_registered_by_all_students.csv file but were absent in studentinfo.csv file so as
# instructed by sir the following rows were added in studentinfo.csv file my myself  and all other columns corresponding to these roll no. were filled with NA
""" NA,2012PH08,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2021MA18,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2121MA08,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000BI01,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000BI02,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000BI03,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000BI04,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000BI05,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000BI06,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000BI07,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000BI08,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000CB01,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000CB02,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000CB03,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000CB04,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000CB05,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000CB06,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000CB07,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000CE01,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000CE02,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000CH01,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000CS01,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000CS02,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000CS03,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000EE01,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000EE02,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000EE03,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000ME01,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000ME02,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000ME03,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000MM01,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000MM02,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000MM03,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000MM04,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000PH01,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000PH02,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2000PH03,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2001CE30,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2001CE20,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2121ME11,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2111ME10,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2111CE08,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2111EE15,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2111EE17,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2111MC11,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2111MT02,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2111MT04,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2111MT06,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2111MT13,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2121CE17,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2121EE33,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2121M414,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2121MA14,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2121MA15,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2121PH16,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2121PH15,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2121HS17,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2112PH22,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2011ME16,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2011CE14,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2112PH02,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2112CH14,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2011MT15,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2011CE09,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2001MM39,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2121HS22,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2111ME19,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2121CH13,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2001CS85,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2121CS26,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2112PH10,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2112PH09,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2112MA24,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,1721HS03,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2121CB14,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2121CS32,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2111ME17,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2011ME23,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2001CE54,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2011CE06,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,1721HS05,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2112PH11,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2121CS21,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2111CS20,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2112CH03,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2112PH08,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,1701EE05,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2021EE22,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2011ME11,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2011MT05,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2011EE26,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2112MA27,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2001ME49,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2001CB29,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
	NA,2111EE25,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA  """



