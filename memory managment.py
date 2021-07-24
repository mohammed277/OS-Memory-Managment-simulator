# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 13:38:30 2019

@author: mohammed
"""

def bestfit(blockSize,No_of_blocks,processSize,No_of_processes):
    allocation =[-1] * No_of_processes
    for i in range (No_of_processes):
        ID=-1
        for j in range (No_of_blocks):
            if processSize[i] <= blockSize[j]:
                if ID==-1 :
                    ID = j
                elif blockSize[ID]>blockSize[j]:
                    ID = j
        if ID!=-1:
           allocation[i]=ID
           blockSize[ID]-=processSize[i]                      
    print("process NO.  process size  Block No.")
    for i in range(No_of_processes):
        print(i + 1, "              ", processSize[i],end ="          " )
        if allocation[i]!=-1:
             print(allocation[i]+1)
        else:
            print("Not allocated")
            
def worstfit(blockSize,No_of_blocks,processSize,No_of_processes):
    allocation =[-1] * n
    for i in range (No_of_processes):
        ID=-1
        for j in range (No_of_blocks):
            if processSize[i] <= blockSize[j]:
                if ID==-1 :
                    ID = j
                elif blockSize[ID]<blockSize[j]:
                    ID = j
        if ID!=-1:
           allocation[i]=ID
           blockSize[ID]-=processSize[i]                      
    print("process NO.  process size  Block No.")
    for i in range(No_of_processes):
        print(i + 1, "              ", processSize[i],end ="          " )
        if allocation[i]!=-1:
             print(allocation[i]+1)
        else:
            print("Not allocated")
            
def firstfit(blockSize,No_of_blocks,processSize,No_of_processes):
    allocation =[-1] * No_of_processes
    for i in range (No_of_processes):
        for j in range (No_of_blocks):
            if processSize[i] <= blockSize[j]:
                 allocation[i] = j
                 blockSize[j] -= processSize[i]
                 break
    print("process NO.  process size  Block No.")
    for i in range(No_of_processes):
        print(i + 1, "              ", processSize[i],end ="          " )
        if allocation[i]!=-1:
             print(allocation[i]+1)
        else:
            print("Not allocated") 

def nextfit(blockSize,No_of_blocks,processSize,No_of_processes):
    pointer=0
    allocation =[-1] * No_of_processes
    for i in range (No_of_processes):
        for j in range (No_of_blocks):
            if processSize[i] <= blockSize[j]:
                 allocation[i] = j
                 blockSize[j] -= processSize[i]
                 pointer=j
                 break
            for f in range (pointer-1):
                 if blockSize[f] >= processSize[i]:
                      allocation[i] = f
                      blockSize[f] -= processSize[i]
                      pointer = f
                      break
    print("process NO.  process size  Block No.")
    for i in range(No_of_processes):
        print(i + 1, "              ", processSize[i],end ="          " )
        if allocation[i]!=-1:
             print(allocation[i]+1)
        else:
            print("Not allocated")            

while True :
    print("1.Best_Fit");
    print("2.First_Fit");
    print("3.Worst_Fit");
    print("4.Next_Fit");
    print("5.Exit");
    val = input()

    if val ==str(1):
        blockSize = [ 100, 500, 200, 300, 600 ]
        processSize = [ 212, 417, 112, 426 ]
        m = len(blockSize)
        n = len(processSize)
        bestfit(blockSize, m, processSize, n)
    

    elif val == str(2): 
        blockSize1 = [ 100, 500, 200, 300, 600 ]
        processSize1 = [ 212, 417, 112, 426 ]
        m1 = len(blockSize1)
        n1 = len(processSize1)
        firstfit(blockSize1, m1, processSize1, n1)
        
    elif val == str(3): 
        blockSize2 = [ 100, 500, 200, 300, 600 ]
        processSize2 = [ 212, 417, 112, 426 ]
        m2 = len(blockSize2)
        n2 = len(processSize2)
        worstfit(blockSize2, m2, processSize2, n2)
        
    elif val == str(4): 
        blockSize3 = [ 100, 500, 200, 300, 600 ]
        processSize3 = [ 212, 417, 112, 426, 100,290 ]
        m3 = len(blockSize3)
        n3 = len(processSize3)
        nextfit(blockSize3, m3, processSize3, n3)
        
    elif val==str(5):
        break;
        
    else:
        print("wrong input")
  

    
    
    

    
#y=[]
#for i in range (int(input("enter the size"))):
        #y.append(input("enter the elements "))