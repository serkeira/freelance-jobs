import sys
import csv

#argument = 'ABCDEF'

#argument = sys.argv[1]

argument = input('Please type the parameters (Format: ABCDEF) \n ')

fileName = 'problem-'
whoopsCount = 0

    
with open('problem.txt') as problem:
    lines = open('problem.txt', 'r').readlines()


if ("A" in argument):
    i = -1
    aExists = 0
    for line in lines:
        i = i + 1
        if ('c --- 5504' in line):
            aExists = 1
            
            lineToBeUpdated = lines[i+3]
            lineToBeUpdated = list(lineToBeUpdated.split());
            lineToBeUpdated[1] = "102"
            lineToBeUpdated[2] = "-1.00"
            lineToBeUpdated.append("\n")
            lines[i+3] = " ".join(lineToBeUpdated)
            #print (line)
            #print (lines[i+3])
        
            
            lineToBeUpdatedB = lines[i+4]
            lineToBeUpdatedB = list(lineToBeUpdatedB.split());
            lineToBeUpdatedB[1] = "102"
            lineToBeUpdatedB[2] = "-1.00"
            lineToBeUpdatedB.append("\n")
            lines[i+4] = " ".join(lineToBeUpdatedB)
            #print (lines[i+4])
       
    if (aExists == 0):
        print("whoops")  
        whoopsCount += 1
    else:       
        fileName = fileName + "A"
    
        
   
if ("B" in argument):
    i = -1
    bExists = 0
    for line in lines:
        i = i + 1
        if ('c --- 5505' in line):
            bExists = 1
            
            lineToBeUpdated = lines[i+3]
            lineToBeUpdated = list(lineToBeUpdated.split());
            lineToBeUpdated[1] = "102"
            lineToBeUpdated[2] = "-1.00"
            lineToBeUpdated.append("\n")
            lines[i+3] = " ".join(lineToBeUpdated)
        
        
            
            lineToBeUpdatedB = lines[i+4]
            lineToBeUpdatedB = list(lineToBeUpdatedB.split());
            lineToBeUpdatedB[1] = "102"
            lineToBeUpdatedB[2] = "-1.00"
            lineToBeUpdatedB.append("\n")
            lines[i+4] = " ".join(lineToBeUpdatedB)
           
    
    if (bExists == 0):
        print("whoops") 
        whoopsCount += 1
    else:       
        fileName = fileName + "B"

        
if ("C" in argument):
    i = -1
    cExists = 0
    for line in lines:
        i = i + 1
        if ('c --- 5506' in line):
            cExists = 1
            
            lineToBeUpdated = lines[i+3]
            lineToBeUpdated = list(lineToBeUpdated.split());
            lineToBeUpdated[1] = "102"
            lineToBeUpdated[2] = "-1.00"
            lineToBeUpdated.append("\n")
            lines[i+3] = " ".join(lineToBeUpdated)
                   
            
            lineToBeUpdatedB = lines[i+4]
            lineToBeUpdatedB = list(lineToBeUpdatedB.split());
            lineToBeUpdatedB[1] = "102"
            lineToBeUpdatedB[2] = "-1.00"
            lineToBeUpdatedB.append("\n")
            lines[i+4] = " ".join(lineToBeUpdatedB)
          
    
    if (cExists == 0):
        print("whoops")   
        whoopsCount += 1
    else:       
        fileName = fileName + "C"

if ("D" in argument):
    i = -1
    dExists = 0
    
    for line in lines:
        i = i + 1
        if ('c --- 5507' in line):
            dExists = 1
            
            lineToBeUpdated = lines[i+3]
            lineToBeUpdated = list(lineToBeUpdated.split());
            lineToBeUpdated[1] = "102"
            lineToBeUpdated[2] = "-1.00"
            lineToBeUpdated.append("\n")
            lines[i+3] = " ".join(lineToBeUpdated)
           
        
            
            lineToBeUpdatedB = lines[i+4]
            lineToBeUpdatedB = list(lineToBeUpdatedB.split());
            lineToBeUpdatedB[1] = "102"
            lineToBeUpdatedB[2] = "-1.00"
            lineToBeUpdatedB.append("\n")
            lines[i+4] = " ".join(lineToBeUpdatedB)
          
            
    if (dExists == 0):
        print("whoops")    
        whoopsCount += 1
    else:       
        fileName = fileName + "D"
    
   
    

if ("E" in argument):
    i = -1
    eExists = 0
    for line in lines:
        i = i + 1
        if ('c --- 5508' in line):
            eExists = 1
            
            lineToBeUpdated = lines[i+3]
            lineToBeUpdated = list(lineToBeUpdated.split());
            lineToBeUpdated[1] = "102"
            lineToBeUpdated[2] = "-1.00"
            lineToBeUpdated.append("\n")
            lines[i+3] = " ".join(lineToBeUpdated)
           
        
            
            lineToBeUpdatedB = lines[i+4]
            lineToBeUpdatedB = list(lineToBeUpdatedB.split());
            lineToBeUpdatedB[1] = "102"
            lineToBeUpdatedB[2] = "-1.00"
            lineToBeUpdatedB.append("\n")
            lines[i+4] = " ".join(lineToBeUpdatedB)
           
            
    if (eExists == 0):
        print("whoops")   
        whoopsCount += 1
    else:       
        fileName = fileName + "E"

if ("F" in argument):
    i = -1
    fExists = 0
    for line in lines:
        i = i + 1
        if ('c --- 5509' in line):
            fExists = 1
            
            lineToBeUpdated = lines[i+3]
            lineToBeUpdated = list(lineToBeUpdated.split());
            lineToBeUpdated[1] = "102"
            lineToBeUpdated[2] = "-1.00"
            lineToBeUpdated.append("\n")
            lines[i+3] = " ".join(lineToBeUpdated)
            
        
            
            lineToBeUpdatedB = lines[i+4]
            lineToBeUpdatedB = list(lineToBeUpdatedB.split());
            lineToBeUpdatedB[1] = "102"
            lineToBeUpdatedB[2] = "-1.00"
            lineToBeUpdatedB.append("\n")
            lines[i+4] = " ".join(lineToBeUpdatedB)
           
            
    if (fExists == 0):
        print("whoops")  
        whoopsCount += 1
    else:       
        fileName = fileName + "F"

filename = fileName + ".txt"

if (whoopsCount > 0):
    print ("Could not generate the file because of " + str(whoopsCount) + " whoops")
else:
    f = open(fileName+".txt", "w")
    f.writelines(lines)
    f.close()

    

    
  