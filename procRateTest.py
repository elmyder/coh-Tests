import re


########## Set variables ##########

filename = r""  #write full path to chat log file in quotes  
start = 0       #fist line of test in log file 
end = 10000     #last line of test in log file

pattern1 = ""   #attack being used
pattern2 = ""   #proc being tested


########## Functions ##########

def instances(filename,pattern1,pattern2,start,end):

    pat1 = re.compile(str(pattern1))
    pat2 = re.compile(str(pattern2))
    instances = []      #will contain a list of all lines containing patterns 1 and 2
    linenum = start     #start line count at start point (line count starts at 0)
    
    with open(filename,"rt") as log:
        for i in range(start):
            log.readline()     #skip all lines up to start point
        for line in log:
            linenum += 1            #add one to line count for each line after start
            if linenum > end:
                break               #stop after end point
            if pat1.search(line) != None and pat2.search(line) != None:
                instances.append([linenum, line.rstrip('\n')])
    
    numberInstances = len(instances)
    
    return numberInstances


########## Print results ##########

Total = instances(filename,"You hit", pattern1, start, end)
Proc1 = instances(filename, pattern2, "", start, end)

print("Sample Size: " + str(Total)) 
print("FF: " + str(Proc1))
print("Proc rate: " +str(100*(Proc1/Total)))

