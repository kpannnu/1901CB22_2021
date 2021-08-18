def meraki_helper(n):
    """This will detect meraki numner"""
    a=str(n)
    flag=1
    if(len(a)==1):
        print("Yes - {} is a Meraki number".format(int(a)))
    else:
        for x in range(len(a)-1):
            if(abs(int(a[x])-int(a[x+1]))!=1):
                flag=0
                break
        if(flag==1):
             print("Yes - {} is a Meraki number".format(int(a)))
        else:
             print("No - {} is a not a Meraki number".format(int(a)))
    return flag


input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]
count=0
for x in input:
   count=count+ meraki_helper(x)
print("the input list contains {} meraki and {} non meraki numbers".format(count,len(input)-count))
