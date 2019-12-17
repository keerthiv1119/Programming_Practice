scores = []
marksheet = []
n = int(input())
for i in range(n):
    name = input()
    score = float(input())
    scores.append(score)
    marksheet.append([name,score])
#For non duplicate values in a list
'''
minimum = int(List[0][1])
s = 0
for i in range(n):
    if int(List[i][1]) < minimum:
        minimum = int(List[i][1])
        s = i
print(List[s][0])
'''
#If the List contain Duplicates we do the following
second_highest_score = sorted(list(set(scores)))[1]
for name,score in sorted(marksheet):#to have the sorted names in the list
    if score == second_highest_score:
        print(name)
