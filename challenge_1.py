import os

f = open(os.getcwd() + '/input_challenge1.txt', 'r')
listWithVal = f.read().split('\n')
print(listWithVal)

for i in range(len(listWithVal)):
    for j in range(i+1, len(listWithVal)):
        for k in range(j+1, len(listWithVal)):
            if int(listWithVal[i]) + int(listWithVal[j]) + int(listWithVal[k]) == 2020:
                print(int(listWithVal[i])*int(listWithVal[j])*int(listWithVal[k]))