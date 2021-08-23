    def get_memory_score(list):
        score=0
        memory=[]
        for x in list:
            if x in memory:
                score=score+1
                continue
            elif len(memory)==5:
                del memory[0]
                memory.append(x)
            else :
                memory.append(x)
    
        
        return score

input_nums = [3, 4, 5, 3, 2, 1]
invalid_list=[]
for x in input_nums:
    if ( type(9)!=type(x)):
        invalid_list.append(x)
if(len(invalid_list)!=0):
    print("\"Please enter a valid input list\". Invalid inputs detected\": {}".format(invalid_list))
    exit()
print("Score: {}".format(get_memory_score(input_nums)))
