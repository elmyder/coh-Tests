import re


########## Set variables ##########

filename = r""  #write full path to chat log file in quotes  
start = 1       #line number of the log file where the test began
end = 10000     #line number of the log file where the test ended


########## Functions ##########

def instances(filename,pattern1,pattern2,start,end):

    pat1 = re.compile(str(pattern1))
    pat2 = re.compile(str(pattern2))
    instances = []           #will contain a list of all lines containing patterns 1 and 2
    linenum = start          #start line count at start point (line count starts at 0)
    
    with open(filename,"rt") as log:
        for i in range(start):
            log.readline()  #skip all lines up to start point
        for line in log:
            linenum += 1    #add one to line count for each line after start
            if linenum > end:
                break       #stop after end point
            if pat1.search(line) != None and pat2.search(line) != None:
                instances.append([linenum, line.rstrip('\n')])
    
    numberInstances = len(instances)
    
    return numberInstances


########## Print results ########## 

Total = instances(filename,"HIT", "you rolled a", start, end)   #total = total number of hits
Crits = instances(filename, "[CRITICAL]", "", start, end)       #crits = total number of crits

print("Sample Size: " + str(Total)) 
print("Crits: " + str(Crits))
print("Crit rate: " +str(100*(Crits/Total)))
















