
from fpdf import FPDF
import os
import datetime
import csv
seal = 1
signature = 1


class PDF(FPDF):  # class made to use fpdf to make pdf
    def lines(self, x1, y1, x2, y2):
        self.set_line_width(0.0)
        self.line(x1, y1, x2, y2)

    def box(self, x, y, w, h):  # function to make a rectangle on pdf
        self.rect(x, y, w, h)

    def imagex(self, x1, y1, w1, h1):  # function to add iitpatna logo image on pdf
        self.image(name=os.getcwd()+r"/IITP_logo.JPG",
                   x=x1, y=y1, w=w1, h=h1)

    def imagex2(self, x1, y1, w1, h1):
        self.image(name=os.getcwd()+r"/Capture.JPG", x=x1, y=y1,
                   w=w1, h=h1)  # function to add  image on pdf

    def seal(self, x1, y1, w1, h1):  # function to add seal on pdf if asked by the user
        self.image(name=os.getcwd()+r"/seal.JPG", x=x1, y=y1, w=w1, h=h1)

    def signature(self, x1, y1, w1, h1):  # function to add signature on pdf if asked by the user
        self.image(name=os.getcwd()+r"/Signature.JPG", x=x1, y=y1, w=w1, h=h1)

    # function to add text in a cell of pdf
    def text(self, x1, y1, w1, h1, font_size, txt, align='C', style='', border=0):
        self.set_xy(x1, y1)
        self.set_font('Arial', style, font_size)
        self.cell(w=w1, h=h1, align=align, txt=txt, border=border)

    # function automated to make tables on the pdf by using coordinates and cell function of fpdf
    def automate(self, t, list1, list2, kp):
        if t <= 4:
            self.text(13+(t-1)*(96+2.5), 51, 10, 5, 8,
                      "Semester {}".format(list2[t-1][0]), 'L', 'UB')
            self.text(15+(t-1)*(96+2.5), 140, 83, 8, 8, "Credits taken:  {}".format(list2[t-1][1])+"   Credits Cleared:  {}".format(
                list2[t-1][1])+"   SPI: {}".format(round(list2[t-1][2], 2))+"   CPI: {}".format(kp[t-1]), 'L', 'B', border=1)
            self.set_xy(14+(t-1)*(96+2.5), 48+8)
        else:
            self.text(13+(t-5)*(96+2.5), 51+90+14+3, 10, 5, 8,
                      "Semester {}".format(list2[t-1][0]), 'L', 'UB')
            self.text(15+(t-5)*(96+2.5), 140+90+14+3-13, 83, 8, 8, "Credits taken:  {}".format(list2[t-1][1])+"   Credits Cleared:  {}".format(
                list2[t-1][1])+"   SPI: {}".format(round(list2[t-1][2], 2))+"   CPI: {}".format(kp[t-1]), 'L', 'B', border=1)
            self.set_xy(14+(t-5)*(96+2.5), 48+8+90+14+3)

        for x in range(len(list1)):
            if x == 0:
                self.set_font('Arial', 'B', 6)
            else:
                self.set_font('Arial', '', 7)
            for y in range(5):
                if(y == 1):
                    self.cell(w=72-5-5, h=6, align='C',
                              txt="{}".format(list1[x][y]), border=1, ln=0)
                else:
                    if(y == 4):
                        self.cell(w=4.5+1+1, h=6, align='C',
                                  txt="{}".format(list1[x][y]), border=1, ln=2)
                    elif(y == 0):
                        self.cell(w=4.5+2.5+2+2, h=6, align='C',
                                  txt="{}".format(list1[x][y]), border=1, ln=0)
                    else:
                        self.cell(w=4.5+1+1, h=6, align='C',
                                  txt="{}".format(list1[x][y]), border=1, ln=0)
            self.cell(w=-85.5-2.5+1+1, h=0, align='C', txt="", border=0, ln=0)


dict = {"AA": 10, "AA*": 10, "AB": 9, "AB*": 9, "BB": 8, "BB*": 8, "BC": 7, "BC*": 7, "CC": 6, "CC*": 6, "CD": 5,
        "CD*": 5, "DD": 4, "DD*": 4, "F": 0, "F*": 0, "I": 0, "I*": 0}  # mapping the grades to grade equivalent
dict_branch = {"CS": "Computer Science and Engineering", "CB": "Chemical Engineering", "CE": 'Civil Engineering',
               "EE": "Electrical and Electronics Engineering", "ME": "Mechanical Engineering"}  # mapping of branches
dict1, dict2, dict3 = {}, {}, {}
i = 2
with open("Input_files/grades.csv", "r") as f1:  # opening grades.csv file and itearting it then
    grade_file_reader = csv.reader(f1)
    next(grade_file_reader)
    for x in grade_file_reader:
        dict1[i] = x  # converting grades.csv file into dictionary
        i = i+1

# opening subjects_master.csv file and itearting it then
with open("Input_files/subjects_master.csv", "r") as f2:
    subject_file_reader = csv.reader(f2)
    for y in subject_file_reader:
        # converting subjects_master.csv file into dictionary
        dict2[y[0]] = [y[1], y[2]]

# opening names-roll.csv file and itearting it then
with open("Input_files/names-roll.csv") as f3:
    name_file_reader = csv.reader(f3)
    for z in name_file_reader:
        dict3[z[0]] = z[1]
        # converting names-roll.csv file into dictionary


def cpi(x, list=list):           # function to calculate CPI till xth semester given as argument with roundoff of 2 decimal digits
    total_credit = 0
    total_temp = 0
    for y in list[:x]:
        total_credit = total_credit+y[1]
        total_temp = total_temp+y[1]*y[2]
    cpi = round(total_temp/total_credit, 2)
    return cpi


def fun(roll):  # function for calculation of all information to form Overall table of each semester of a student using student roll no and then to make pdf of that roll no
    count = credit = temp = 0
    sem_sheet = []
    k = 1  # variable made to check when semester is changing for same roll no. in the iteration
    list = []
    kp = []
    pp = []
    stud = []

    for x in dict1:    # iterating dictionary of grades.csv file
        if(dict1[x][0] == roll):
            if(int(dict1[x][1]) != k):
                # credit=semester wise credit taken, temp=credit*grade equivalent, temp/credit = SPI of a particular sem
                list.append([k, credit, temp/credit])
                stud.append(pp)
                pp = []
                credit = temp = 0

            if "Sem{}".format(dict1[x][1]) not in sem_sheet:
                sem_sheet.append("Sem{}".format(dict1[x][1]))
                pp.append(["Sub. Code", "Subject Name", "L-T-P", "CRD", "GRD"])
            pp.append([dict1[x][2], dict2[dict1[x][2]][0],
                      dict2[dict1[x][2]][1], int(dict1[x][3]), dict1[x][4]])
            credit = credit+int(dict1[x][3])
            temp = temp+int(dict1[x][3])*dict[dict1[x][4].strip()]
            k = int(dict1[x][1])
            count = count+1

        if(dict1[x][0] != roll or x == len(dict1)):
            if(count != 0):
                list.append([k, credit, temp/credit])
                stud.append(pp)

                # calling cpi function to calculate cpi
                kp = [cpi(x[0], list) for x in list]

                # basic layout of the pdf using the pdf object created from PDF class formed above
                pdf = PDF(orientation='P', unit='mm', format=(420, 297))
                pdf.add_page()
                # TITLE PIC FOR INSTITUTE NAME IN HINDI AND ENGLISH
                pdf.imagex2(60, 11, 290, 28)
                # BORDER LINE RECTANGLE OF THE WHOLE PDF
                pdf.box(10.0, 10.0, 400, 277)
                # VERICAL LINE OF TOP LEFTMOST RECTANGLE CONAINING LEFT IITP LOGO
                pdf.lines(45, 10, 45, 36)
                # VERICAL LINE OF TOP RIGHTMOST RECTANGLE CONAINING RIGHT IITP LOGO
                pdf.lines(375, 10, 375, 36)
                pdf.lines(10.0, 36, 410, 36)  # HORIZANTAL LINE
                # IITP LOGO ON LEFT SIDE
                pdf.imagex(17.75-1.9, 12.5, 17.5*1.4, 13.4*1.4)
                # IITP LOGO ON RIGHT SIDE
                pdf.imagex(382.75-1.9, 12.5, 17.5*1.4, 13.4*1.4)
                pdf.box(45+84.5, 38, 161, 10)

                # PRINT INTERIM TRANSCRIPT TEXT BELOW LEFT SIDE IITP LOGO
                pdf.text(18.75, 33.38, 17.5, 3, 6,
                         "INTERIM TRANSCRIPT", 'C', 'U')
                # PRINT INTERIM TRANSCRIPT TEXT BELOW RIGHT SIDE IITP LOGO
                pdf.text(383.75, 33.38, 17.5, 3, 6,
                         "INTERIM TRANSCRIPT", 'C', 'U')
                pdf.text(129.5+2, 38+1, 20, 3, 8, "Roll No:", 'L', 'B')
                pdf.text(129.5+2+19, 38+1, 20, 3.6, 8,
                         "{}".format(roll), 'C', '', border=1)
                pdf.text(129.5+2, 38+5+1, 20, 3, 8, "Programme:", 'L', 'B')
                pdf.text(129.5+2+20, 38+5+1, 28, 3,
                         8, "Bachelor of Technology")
                pdf.text(129.5+2+53.67, 38+1, 20, 3, 8, "Name:", 'L', 'B')
                pdf.text(129.5+2+53.67+12, 38+1, 40, 3.6, 8,
                         "{}".format(dict3[roll]), 'C', '', border=1)
                pdf.text(129.5+2+53.67, 38+5+1, 20, 3, 8, "Course:", 'L', 'B')

                pdf.text(129.5+2+53.67+24-11, 38+5+1, 20, 3, 8,
                         "{}".format(dict_branch[roll[4:6]]), 'L')
                pdf.text(129.5+2+53.67+53.67+5, 38+1, 20, 3,
                         8, "Year of Admission:", 'L', 'B')
                pdf.text(129.5+2+53.67+53.67+20+12, 38+1, 10, 4, 8,
                         "20{}".format(roll[0:2]), 'C', '', border=1)
                pdf.lines(10, 30+99+10+14-2, 410, 30+99+10+14-2)
                pdf.lines(10, 30+93+93+14+15, 410, 30+93+93+14+15)

                if seal == 1:  # checking if seal is required by user
                    pdf.seal(180, 250, 30, 30)

                if signature == 1:  # checking if signature is required by user
                    pdf.signature(360, 251, 37, 26)

                now = datetime.datetime.now()
                pdf.text(13, 30+95+95+25+10+7, 10, 4, 10,
                         "Date of Issue:  _________________", 'L')
                pdf.text(13+10+14, 30+95+95+24+10+7, 30, 4, 10,
                         now.strftime("%d %b %Y, %H:%M"), 'L')
                pdf.text(359, 30+95+95+24+10+7, 10, 4, 10,
                         "_______________________", 'L')
                pdf.text(359, 30+95+95+30+10+7, 10, 4, 10,
                         "Assitant Registrar (Academic)", 'L')

                for t in range(1, len(list)+1):
                    pdf.automate(t, stud[t-1], list, kp)

                # saving the pdf page of a roll no. after adding everything on pdf
                pdf.output('output/{}.pdf'.format(roll), 'F')

                return


def allroll():  # function to make pdf of all the roll no.
    for z in dict3:  # iterating the dictionary of names-roll.csv file to get unique roll no. every time
        fun(z)      # calling the function to calculate the data of a Student by passing his unique roll no. as argument and then to make pdf


def range(s1, s2):
    l = []
    a = int(s1[6])
    a1 = int(s1[7])
    a2 = int(s1[6]+s1[7])
    b2 = int(s2[6]+s2[7])
    for aa in range(b2-a2+1):
        c = str(a)+str(a1)
        l.append(s1[0]+s1[1]+s1[2]+s1[3]+s1[4].upper()+s1[5].upper()+c)
        a2 = a2+1
        a1 = a2 % 10
        a = a2//10

    for aaa in l:
        fun(aaa)


allroll()  # function called for making pdf of all roll no.
range(s1, s2)


print("program complete")
