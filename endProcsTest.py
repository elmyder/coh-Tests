import re


########## Set variables ##########

filename = r""      #path to log file in quotes
linenum = 0         #first line of test in log file


###################################

pattern0 = re.compile("Performance Shifter")
pattern1 = re.compile("Panacea")
pattern2 = re.compile("endurance")

pshifter = []
panacea = []

with open(filename,"rt") as log:
    for i in range(700):
        log.readline()
    for line in log:
        linenum += 1
        if linenum > 3295:
            break
        if pattern0.search(line) != None:
            pshifter.append([linenum, line.rstrip('\n')])
        if pattern1.search(line) != None and pattern2.search(line) != None:
            panacea.append([linenum, line.rstrip('\n')])

numberInstances0 = len(pshifter)
initialTime0 = int(pshifter[0][1][11]+pshifter[0][1][12])*3600+int(pshifter[0][1][14]+pshifter[0][1][15])*60+int(pshifter[0][1][17]+pshifter[0][1][18])
finalTime0 = int(pshifter[-1][1][11]+pshifter[-1][1][12])*3600+int(pshifter[-1][1][14]+pshifter[-1][1][15])*60+int(pshifter[-1][1][17]+pshifter[-1][1][18])
duration0 = finalTime0 - initialTime0
avgPPM0 = numberInstances0*60/duration0

numberInstances1 = len(panacea)
initialTime1 = int(panacea[0][1][11]+panacea[0][1][12])*3600+int(panacea[0][1][14]+panacea[0][1][15])*60+int(panacea[0][1][17]+panacea[0][1][18])
finalTime1 = int(panacea[-1][1][11]+panacea[-1][1][12])*3600+int(panacea[-1][1][14]+panacea[-1][1][15])*60+int(panacea[-1][1][17]+panacea[-1][1][18])
duration1 = finalTime1 - initialTime1
avgPPM1 = numberInstances1*60/duration1

print("Average Performance Shifter procs per minute: " + str(avgPPM0))
print("Sample size: " + str(numberInstances0))

print("Average Panacea procs per minute: " + str(avgPPM1))
print("Sample size: " + str(numberInstances1))

print("Average endurance per minute: " + str(avgPPM0*11.36+avgPPM1*8.52))

