import math

print(str(1233))

print(list(filter(lambda x: x>0, [1,-3,2,0,-5,6])))

print(list(map(lambda a: a*2, [1,2,3,4])))

print(type("hi".upper()))

li = [4,2,1,3]

print(sorted(li))

li.sort()

print(li)

numbers = [0, 31, 24, 10, 1, 9]
answer = sorted(numbers)[len(numbers)-3: len(numbers)-2]

print(answer)

print(13.0*13.0)

print(ord('Z')-ord('Z'))

str="heLLo"
str.upper()
print(str)

my_string="people"

def solution(my_string):
    dic = {}
    
    for i in range(len(my_string)) :
        li = []
        if my_string[i] not in dic :
            for j in range(i+1, len(my_string)) :
                if my_string[i] == my_string[j] :
                    li.append(j)
            dic[my_string[i]] = li
    
    tempLi = []
    for key in list(dic.keys()) :
        for i in dic[key] :
            tempLi.append(i)
    
    tempLi2 = list(my_string)
    tempLi2.sort()
    tempLi2.reverse()
    
    print("dfs", tempLi2)
        
    return my_string
print(solution(my_string))

print(int('-1'))

print([1,2][:4])

print("onetwo".replace("one", '1'))

print("")