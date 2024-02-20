#question 1
#print triangle using for look

for i in range (10):
    if i <=5:
        print("* " * i)
    else:
        print("* " * (10 - i))

#question 2
#use look to output odd indexes of list
my_list = [10,20,30,40,50,60,70,80,90,100]
for i in range (len(my_list)):
    if(i%2 == 0):
        print(my_list[i])
#question 3
#write code that appends the type of elements from a given list
x = [23, 'Python', 23.98]
outX = []
for i in range(len(x)):
    outX.append(type(x[i]))

print(outX)

#question 4
#write a function that takes a list and returns a new list
#with the unique items of the first list
def uniqueList(sampleList):
    uniqueList = []
    for i in sampleList:
        if(i not in uniqueList):
            uniqueList.append(i)
    return uniqueList

sampleList = [1, 2, 3, 3, 3, 3, 4, 5]
uniqueOut = uniqueList(sampleList)
print(uniqueOut)

#question 5
#write a function that accepts a string and calculate
#the number of uppercase letters and lowercase letters

def upperLowerCase(inString):
    upper = 0
    lower = 0
    for i in inString:
        if i.isalpha():
            if i.islower():
                lower+=1
            else:
                upper+=1

    print("No. of Upper-case characters: " + str(upper))
    print("No. of Lower-case characters: " + str(lower))

inString = input("Input string: ")

upperLowerCase(inString)
