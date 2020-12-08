import os

f = open(os.getcwd() + '/input3.txt', 'r')
listWithVal = f.read().split('\n')

# 3 in the right, 1 in the bottom
startIndex = 0
treesInTheSlope = 0
sentencesMultiplication = 1
for i in range(2, len(listWithVal), 2):
    sentence = listWithVal[i]*1200
    startIndex +=1
    # print(startIndex)
    # print(sentence[startIndex])
    if sentence[startIndex] == "#":
        treesInTheSlope+=1


print(treesInTheSlope)

# 191  dla 3 w prawo i 1 w dół
# 60 dla 1 w prawo i 1 w dół
# 63 dla 7 w prawo i 1 w dół
# 64 dla 5 w prawo i 1 w dół
# 32 dla 1 w prawo i 2 w dół