
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






