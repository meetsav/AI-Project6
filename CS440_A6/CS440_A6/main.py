from array import *
import re

query=dict()
q=list()

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
        if(choice==6):
           folder=6
           break
        if(choice==7):
           folder=7
           break
        if(choice==8):
           folder=8
           break
        if(choice==9):
           folder=9
           break
        if(choice==10):
           folder=10
           break
        else:
            print("value shouls be in between 1 to 10")
    with open(str(folder)+"/"+filename,'r') as f:
         file=f.readlines()
         stripeddata=list()
         data=list()
         for line in file:
            stripeddata.append(((line.rstrip('\n')).rstrip('\t')).split('\t'))
    
    f.close()
    with open(str(folder)+"/"+"query.txt",'r') as f:
         file=f.readlines()
         querydata=list()
         for line in file:
            querydata.append(((line.rstrip('\n')).rstrip('\t')).split('\t'))
         temp=list()
         temp=[1 if x=='T' else 0 for x in querydata[0]]
         
         for i in range(len(temp)):
             query[i]=temp[i]
         #print(query)
    return stripeddata,folder

def getVariablesNumber(data):
    return(int(data[0][0]))
    
def childParentMatrix(data):
    length=getVariablesNumber(data)
    Matrix = [[0 for i in range(length)] for j in range(length)]# row is child node and column is Parent node 
    probability=[0.0 for i in range(length)]
    
    index,Matrix,probability=getMatrix(data,Matrix,probability)
    final=list()
    pro=dict()
    for i in range(len(probability)):
        probs=list()
        if probability[i]>0:
            probs.append(probability[i])
            final.append(probs)
        else:
            final.append(probs)
    for i in range(len(final)):
         pro[i]=final[i]
    #print(pro)
    getPossibilities(data,index,pro)
    temp=solve(Matrix,pro)
    return temp
    
def getParent(Matrix, node):
    parent=list()
    for i in range(len(Matrix[node])):
        if Matrix[node][i]==1:
            parent.append(i)
    return parent

def binaryToint(value):
    return(int(value,2))
    
def solve(Matrix,pro):
    probability=1.0
    #print(query)
    for i in range(len(query)):
        tmp=query[i]
        parent=getParent(Matrix,i)
        if len(parent)==0:
            if(tmp==0):
                probability=probability*(1-pro[i][0])
            else:
                probability=probability*(pro[i][0])
        else:
            string=''
            #print(parent)
            for j in range(len(parent)):
                string+=str(query[parent[j]])
            #print(string)
            value=binaryToint(string)
            #print(value)
            temp=pro[i]
            #print(temp)
            actualvalue=len(temp)-value
            #print(temp)
            #print(temp[actualvalue-1])
            if(tmp==0):
                probability=probability*(1-float(temp[actualvalue-1]))
            else:
                 probability=probability*(float(temp[actualvalue-1]))
    return probability
    

            
def getPossibilities(data, index, pro):
    for indx in index:
        line=data[indx]
        numberofParent=line[0]
        targetNode=line[1]
        #print(numberofParent)
        #print(targetNode)
        
        tobeconsideredLine=pow(2,int(numberofParent))
        #print(tobeconsideredLine)
        temp=list()
        for i in range(1,tobeconsideredLine+1):
            sentence=data[indx+i]
            temp.append(float(sentence[int(numberofParent)]))
        pro[int(targetNode)-1]=temp
        
        #print("-----------------------")
         
    return pro
    
    
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
                
filedata,folder=readfile("network.txt")

temp=childParentMatrix(filedata)
with open(str(folder)+"/"+"out.txt",'w') as f:
         f.write("{0:.6f}".format(temp))
         
f.close()

