from array import *
import re
def readfile(filename):
    folder=1
    while(1):
        print("Enter the number of folder you want to read")
        choice=input()
        if(choice==1):
           folder=1
           break
        if(choice==2):
           folder=2
           break
        if(choice==3):
           folder=3
           break
        if(choice==4):
           folder=4
           break
        if(choice==5):
           folder=5
           break
    with open(str(folder)+"/"+filename,'r') as f:
         file=f.readlines()
         stripeddata=list()
         data=list()
         for line in file:
            stripeddata.append(((line.rstrip('\n')).rstrip('\t')).split('\t'))
        
    f.close()
    return stripeddata

def getVariablesNumber(data):
    return(int(data[0][0]))
    
def childParentMatrix(data):
    length=getVariablesNumber(data)
    Matrix = [[0 for i in range(length)] for j in range(length)]# row is child node and column is Parent node 
    probability=[0.0 for i in range(length)]
    
    index,Matrix,probability=getMatrix(data,Matrix,probability)
    final=list()
    for i in range(len(probability)):
        probs=list()
        if probablility[i]>0:
            probs.append(probablility[i])
            final.append(probs)
        else:
            final.append(probs)
     
        
        
            
        
        
    
    print(probability)
    
    
def getMatrix(data,Matrix,probability):
    temp=list()
    index=list()
    for line in data:
        if len(line)>2 and 'T' not in line and 'F' not in line:
            index.append(data.index(line))
            for i in range(len(line)):
                if i>1:
                   
                    Matrix[int(line[1])-1][int(line[i])-1]=1
        if len(line)==2 and 'T' not in line and 'F' not in line:
            probability[int(line[1])-1]=float(data[int(data.index(line))+1][0])
    return index,Matrix,probability
                
filedata=readfile("network.txt")

childParentMatrix(filedata)
