import os,glob
import shutil
import re
def regex_renamer():

	# Taking input from the user

	print("1. Breaking Bad")
	print("2. Game of Thrones")
	print("3. Lucifer")

	webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
	season_padding = int(input("Enter the Season Number Padding: "))
	episode_padding = int(input("Enter the Episode Number Padding: "))

	def padding(no,padding):    #defining function to convert a number according to it's padding given by user
		num=str(no)
		while(len(num)<padding):
			num='0'+num
		return num

	dict={1:"Breaking Bad",2:"Game of Thrones",3:"Lucifer"}

	if not os.path.isdir(r'./corrected_srt'):# check if corrected_srt folder already exists 
		os.mkdir(r'./corrected_srt')
	
	if not os.path.isdir(r'./corrected_srt/'+str(dict[webseries_num])):  #check if the selected web series directory already exists
		shutil.copytree(r'./wrong_srt/'+str(dict[webseries_num]),r'./corrected_srt/'+str(dict[webseries_num]))
	else:
		shutil.rmtree(r'./corrected_srt/'+str(dict[webseries_num]))
		shutil.copytree(r'./wrong_srt/'+str(dict[webseries_num]),r'./corrected_srt/'+str(dict[webseries_num]))
	mp4_files=glob.glob(r'./corrected_srt/'+str(dict[webseries_num])+'/'+'*.mp4')       #all mp4 extension files in webseries folder
	srt_files=glob.glob(r'./corrected_srt/'+str(dict[webseries_num])+'/'+'*.srt')       #all srt extension files in webseries folder
	all_files=mp4_files+srt_files    #all files in the webseries folder
	
	for path in all_files:
		dirname,fname=os.path.split(path)
		
		p1=re.compile(r'mp4$')
		if re.search(p1,fname):    #check if extension of file is mp4
			ext=r'.mp4'
		p2=re.compile(r'srt$')     
		if re.search(p2,fname):    #check if extension of file is srt
			ext=r'.srt'
			
		pattern=re.compile(r'[\d]+')
		list_1=re.findall(pattern,fname)  # list whose 1st two elements will give season no. and episode number using regular expression
		season=padding(int(list_1[0]),season_padding)     #calling padding function,list_1[0]=season no. without padding
		episode=padding(int(list_1[1]),episode_padding)   #calling padding function,list_1[1]=episode no. without padding

		if(dict[webseries_num]=="Breaking Bad"):     # check if webseries is Breaking Bad as it's format is diffrent from other webseries
			list_2=re.findall(r'[a-rt-zA-Z ]+',fname)  #list whose first element will give series name using regular expression
			Series_name=list_2[0]
			new_path=dirname+r"/"+"{}".format(Series_name)+"- Season {} ".format(season)+"Episode {}".format(episode)+"{}".format(ext) # file name of the renamed file
			
		else:
			list_2=re.findall(r'[a-zA-Z ]+',fname)     #list whose 1st two elements will give series name and episode name 
			
			Series_name=list_2[0]                 #series name
			episode_name=list_2[4]                #epiode naame
			new_path=dirname+"/"+"{}".format(Series_name)+"- Season {} ".format(season)+"Episode {} -".format(episode)+"{}".format(episode_name)+"{}".format(ext)  # file name of the renamed file
			
		os.rename(path,new_path)     #finally  renaming the file 

regex_renamer()  #calling the function to rename files