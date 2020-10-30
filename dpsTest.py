import re
import itertools


########## Set variables ##########

filename = r""  #path to log file in quotes
source = ""     #source can be "Me", "Any", or name of source
target = ""     #target can be "Me", "Any", or name of target
power = ""      #power can be "Any" or name of power
# Note that if you specify a power it will NOT count procs!

start = 0       #first line of test in log file
end = 10000     #last line of test in log file 

## By default, dps will be printed. To print full log or total damage, scroll to bottom and uncomment print line according to desired output 


########## Functions ##########

def dps(filename,source,target,power,start,end):

    if source == "Me":
        P1 = "You hit"
        
    elif source == "Any":
        P1 = ""
        
    else: 
        P1 = source
    
    if target == "Me":
        P2 = "hits you"
        
    elif target == "Any":
        P2 = ""
        
    else: 
        P2 = target
        
    if power == "Any":
        P3 = ""
    
    else:
        P3 = power
    
    pat1 = re.compile(str(P1))
    pat2 = re.compile(str(P2))
    pat3 = re.compile(str(P3))
    pat4 = re.compile("damage")
    log = []            #log will contain a list of all lines containing patterns 1 and 2
    time = []           #time will contain a list of all times (in seconds from midnight) when the line occurred
    dmg1 = []           #raw data file to build dmg
    dmg = []            #dmg will contain a list of the damage that occurred at each corresponding line in log
    linenum = start     #start line count at start point (line count starts at 0)
    
    with open(filename,"rt",errors="ignore") as filename:
        for line in itertools.islice(filename,start,None):
            linenum += 1    #add one to line count for each line after start
            if linenum > end:
                break       #stop after end point
            if pat1.search(line) != None and pat2.search(line) != None and pat3.search(line) != None and pat4.search(line) != None:
                log.append(line.rstrip('\n'))
                
    if len(log) == 0:
        return ["None","None","None"]
        
    if len(log) > 0:
    
        for i in range(len(log)):
            time.append(int(log[i][11]+log[i][12])*3600+int(log[i][14]+log[i][15])*60+int(log[i][17]+log[i][18]))
            
        for i in range(len(log)):
            dmg1.append([int(s) for s in re.findall(r'\b\d+\b', log[i])])
            
        for i in range(len(dmg1)):
            if len(dmg1[i]) == 7:
                dmg.append(dmg1[i][6]*0.01)
            if len(dmg1[i]) == 8:
                dmg.append(dmg1[i][6]+dmg1[i][7]*0.01)
    
        damage = sum(dmg)
        duration = time[-1]-time[0]
        dps = damage/duration if duration != 0 else 0
        
        #coh log files contain timestamps in the same format for each line
        
        return dps, log, dmg


########## Print results ##########

## uncomment print line desired

# For just dps
print(dps(filename,source,target,power,start,end)[0])

# for full log
#print(dps(filename,source,target,power,start,end)[1])

# for full damage
#print(dps(filename,source,target,power,start,end)[2])


