import re
import matplotlib.pyplot as plt


############## Set variables ##############

filename = r"" #path to log file in quotes 

pattern0 = re.compile("you rolled a")
pattern1 = re.compile("HIT")
pattern2 = re.compile("streakbreaker")

rolls = []
hits = []
rolls2 = []
hits2 = []
percentages = []
percentages2 = []

linenum = 0 #change to first number of test


############## Without streakbreaker ##############

k = 1

with open(filename,"rt") as log:
    for line in log:
        linenum += 1
        if pattern0.search(line) != None:
            rolls.append([k])
            k += 1
        if pattern1.search(line) != None and pattern0.search(line) != None:
            hits.append([linenum])
        numRolls = len(rolls)
        numHits = len(hits)
        if pattern0.search(line) != None:
            percentages.append([100*(round(numHits/numRolls,4))])

noStreakbreaker = plt.figure()
plt.axhline(y=95, color='r', linestyle='-')
plt.plot(rolls,percentages)
noStreakbreaker.savefig('noStreakbreaker.png') 


############## With streakbreaker ##############

k = 1

with open(r"filename","rt") as log:
    for line in log:
        linenum += 1
        if pattern0.search(line) != None or pattern2.search(line) != None:
            rolls2.append([n])
            k += 1
        if pattern1.search(line) != None and pattern0.search(line) != None:
            hits2.append([linenum])
        if pattern1.search(line) != None and pattern2.search(line) != None:
            hits2.append([linenum])
        numRolls = len(rolls2)
        numHits = len(hits2)
        if pattern0.search(line) != None or pattern2.search(line) != None: 
            percentages2.append([100*(round(numHits/numRolls,4))])
            
streakbreaker = plt.figure()
plt.axhline(y=95, color='r', linestyle='-')
plt.plot(rolls2,percentages2)
streakbreaker.savefig('streakbreaker.png') 


############## Print summary  ##############

x = len(rolls)
y = len(hits)
z = y/x

a = len(rolls2)
b = len(hits2)
c = b/a

print("Total hit rolls w/o streakbreaker: " + str(x))
print("Total hits w/o streakbreaker: " + str(y))
print("Percentage of hits w/o streakbreaker: " + str(100*z))
print("")
print("Total hit rolls w/ streakbreaker: " + str(a))
print("Total hits w/ streakbreaker: " + str(b))
print("Percentage of hits w/ streakbreaker: " + str(100*c))

