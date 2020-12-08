import os

f = open(os.getcwd() + '/input_challenge2.txt', 'r')
listWithVal = f.read().split('\n')
# *********** PART 1 *******************
# wrongPassword = 0
# goodPassword = 0
# for i in range(len(listWithVal)):
#     listTmp = listWithVal[i].split(" ")
#
#     condition = listTmp[1][0]   # letter to check
#     conditionValueLower, conditionValueHigher = listTmp[0].split("-")
#
#     sentence = listTmp[-1]
#     amountOfConditionVal = 0
#     for v in range(len(sentence)):
#         if sentence[v] == condition:
#             amountOfConditionVal+=1
#
#     if amountOfConditionVal >= int(conditionValueLower) and amountOfConditionVal <= int(conditionValueHigher):
#         goodPassword+=1
#     else:
#         wrongPassword+=1
#
# print(goodPassword)
# print(wrongPassword)

wrongPassword = 0
goodPassword = 0
amountOfConditionVal = 0
# ************ PART 2 *********************
for i in range(len(listWithVal)):
    listTmp = listWithVal[i].split(" ")

    condition = listTmp[1][0]   # letter to check
    conditionValueLower, conditionValueHigher = listTmp[0].split("-")
    sentence = listTmp[-1]
    if sentence[int(conditionValueLower)-1] == condition and sentence[int(conditionValueHigher)-1] != condition:
        goodPassword += 1
    elif sentence[int(conditionValueLower)-1] != condition and sentence[int(conditionValueHigher)-1] == condition:
        goodPassword += 1
    else:
        wrongPassword+=1

print(goodPassword)
print(wrongPassword)