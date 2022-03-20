import itertools
import operator

from numpy import sort

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

full_string = []
answer_temp = []
answer = []

for i in orders:
    for j in i:
        if j not in full_string:

            full_string.append(j)

#print(full_string)
for num in course:

    npr = list(itertools.permutations(full_string, num))
    npr = [list(npr[x]) for x in range(0,len(npr))]


    permuta_dict = {}
    npr_list = []     
    for i in npr:
        temp = ""
        for j in i:
            temp += j

        npr_list.append(temp)    
    #npr_list = npr_list.sort()
    #print(npr_list)

    for i in npr_list:
        length = len(i)    
        for j in orders:
            cnt = 0
            for k in i:
                if k in j:
                    cnt +=1
            if cnt == length and i not in permuta_dict:
                permuta_dict[i] = 1 
            elif cnt == length and i in permuta_dict:
                permuta_dict[i] += 1
        
    try:
        max_key = max(permuta_dict.items(), key=operator.itemgetter(1))[1]
    except:
        continue
   
    result = []
    if max_key != 1:
        for i,j in permuta_dict.items():
            if j == max_key:
                result.append(i)
        a = list(map(lambda x: sorted(x), result))     
        b = list(map(lambda x:''.join(x), a))
        c = list(set(b))
        for key in c:
            answer_temp.append(key)
#print(answer_temp)

answer = sorted(answer_temp)
print(answer)
    



