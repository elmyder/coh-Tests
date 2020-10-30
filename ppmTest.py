import re

#Use r before file directory/name
#start = line in file to start search
#end = line in file to end search


########## Set variables ##########

filename = r""      #path to log file in quotes
start = 0           #first line of test in log file
end = 10000         #last line of test in log file

procName = ""       #proc to test
pattern = ""        #phrase uniquely picking out log lines where the proc fires


########## Functions ##########

def procRate(filename,procName,pattern,start,end):

    pat1 = re.compile(str(procName))
    pat2 = re.compile(str(pattern))
    instances = []      #will contain a list of all lines containing patterns 1 and 2
    linenum = start     #start line count at start point (line count starts at 0)
    
    with open(filename,"rt") as log:
        for i in range(start):
            log.readline()      #skip all lines up to start point
        for line in log:
            linenum += 1        #add one to line count for each line after start
            if linenum > end:
                break           #stop after end point
            if pat1.search(line) != None and pat2.search(line) != None:
                instances.append([linenum, line.rstrip('\n')])
    
    numberInstances = len(instances)
    initialTime = int(instances[0][1][11]+instances[0][1][12])*3600+int(instances[0][1][14]+instances[0][1][15])*60+int(instances[0][1][17]+instances[0][1][18])
    finalTime = int(instances[-1][1][11]+instances[-1][1][12])*3600+int(instances[-1][1][14]+instances[-1][1][15])*60+int(instances[-1][1][17]+instances[-1][1][18])
    duration = finalTime - initialTime
    avgPPM = numberInstances*60/duration
    
    #coh log files contain timestamps in the same format for each line
    
    return numberInstances, duration, avgPPM


########## Print results ##########

L = procRate(filename, procName, pattern, start, end)

print(procName + ":")
print("Sample size: " + str(L[0])) 
print("Duration: " + str(L[1]))
print("Average PPM: " + str(L[2]))

