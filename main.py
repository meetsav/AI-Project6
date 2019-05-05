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
    with open("/home/meet/PycharmProjects/CS440_A6/"+str(folder)+"/"+filename,'r') as f:
         file=f.readlines()
         stripeddata=list()
         data=list()
         for line in file:
            stripeddata.append(((line.rstrip('\n')).rstrip('\t')).split('\t'))
    
    f.close()
    with open("/home/meet/PycharmProjects/CS440_A6/"+str(folder)+"/"+"query.txt",'r') as f:
         file=f.readlines()
         querydata=list()
         for line in file:
            querydata.append(((line.rstrip('\n')).rstrip('\t')).split('\t'))
         temp=list()
         temp=[1 if x=='T' else 0 for x in querydata[0]]
         
         for i in range(len(temp)):
             query[i]=temp[i]
         #print(query)
    return stripeddata

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
    solve(Matrix,pro)
    
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
    print(query)
    for i in range(len(query)):
        tmp=query[i]
        parent=getParent(Matrix,i)
        if len(parent)==0:
            probability=probability*pro[i][0]
            
        else:
            string=''
            print(parent)
            for j in range(len(parent)):
                string+=str(query[parent[j]])
            print(string)
            value=binaryToint(string)
            print(value)
            temp=pro[i]
            #print(temp)
            actualvalue=len(temp)-value
            print(temp)
            print(temp[actualvalue-1])
            probability=probability*float(temp[actualvalue-1])
    print('{0:.10f}'.format(probability))
    
    
        
    
    
            
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
                
filedata=readfile("network.txt")

childParentMatrix(filedata)
