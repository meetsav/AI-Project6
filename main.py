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
    with open(str(folder)+"/"+filename,'r') as f:
         file=f.read()
    f.close()
    print(file)

readfile("network.txt")
