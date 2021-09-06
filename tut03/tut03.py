def output_by_subject():
    f=open("regtable_old.csv","r")
    a=f.readline().strip().split(",")

    for line in f:
        c=line.strip().split(",")
        try:                                                                
            file_handler=open("./output_by_subject/{}.csv".format(c[3]),"r")
            file_handler.close()
            file_handler=open("./output_by_subject/{}.csv".format(c[3]),"a")
            file_handler.writelines([c[0],",",c[1],",",c[3],",",c[8],"\n"])
            file_handler.close()

        except:
            file_handler=open("./output_by_subject/{}.csv".format(c[3]),"a")
            file_handler.writelines([a[0],",",a[1],",",a[3],",",a[8],"\n"])
            file_handler.writelines([c[0],",",c[1],",",c[3],",",c[8],"\n"])
            file_handler.close()
        
    f.close()
    return             #function returns here

def output_individual_roll():
    f=open("regtable_old.csv","r")
    a=f.readline().strip().split(",")
    
    for line in f:
        c=line.strip().split(",")
        try:
            file_handler=open("./output_individual_roll/{}.csv".format(c[0]),"r")
            file_handler.close()
            file_handler=open("./output_individual_roll/{}.csv".format(c[0]),"a")
            file_handler.writelines([c[0],",",c[1],",",c[3],",",c[8],"\n"])
            file_handler.close()

        except:
            file_handler=open("./output_individual_roll/{}.csv".format(c[0]),"a")
            file_handler.writelines([a[0],",",a[1],",",a[3],",",a[8],"\n"])
            file_handler.writelines([c[0],",",c[1],",",c[3],",",c[8],"\n"])
            file_handler.close()
        
        
    f.close()
    return  #function returns here

output_individual_roll()            #calling function
output_by_subject()                 #calling function
