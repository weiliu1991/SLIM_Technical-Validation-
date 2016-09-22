# -*- coding: utf-8 -*-
"""
This code can be used to caclculate the Pearson correlation coefficients between the connectivity matrices of the same subject at different time points.

[1] What you need ?
    - Connectivity matrices [.mat] or you should change the way the code load the file
    - Subject list file [.txt]: 
    - change the nubofsubject varaible in the code according to your subject list

[2] What the code will do
    -calculate the Pearson correlation coefficients between two connectivity matrices at the subject level
    -average them and report the final correlation at the group level

@author: weiliu
e-mail: liuwei19910511psychology@gmail.com
"""

import scipy.io as sio 
import numpy as np

# where you store your connectivity matrices
matricesfolder1="C:\\Users\\weiliu\\Desktop\\Matrix_Test\\Scan1"
matricesfolder2="C:\\Users\\weiliu\\Desktop\\Matrix_Test\\Scan2"

# use a [.txt] file to identify the group of subjects you want to calculate
listfile=open("time12.txt","r+")
nubofsubject=100  #change the number according to the number of names
subjectlist=range(nubofsubject) 
calculatelist=[]
for n in subjectlist:
    calculatelist.append(str(listfile.readline().strip('\n')))
if listfile.closed==False:  #return the situation of certain file(True or False)
      listfile.close() 

# create two new dicts, load the matrices and store them in the dicts
my_matrix1={}
for i in calculatelist:
    matfn=matricesfolder1+"\\%s.mat"%(i)
    data=sio.loadmat(matfn)
    my_matrix1[str(i)]=data['FCstrength']

my_matrix2={}
for i in calculatelist:
    matfn=matricesfolder2+"\\Scan2_%s.mat"%(i)
    data=sio.loadmat(matfn)
    my_matrix2[str(i)]=data['FCstrength']
    
# calculate the correlation betweeen differernt time points one by one 
    
totalcor12=0

for i in calculatelist:
    print (" ")
    print ("start to calculate for subject "+str(i))
    #numberofsubject=numberofsubject+1
    
    a=my_matrix1["%s"%(i)] 

    b=my_matrix2["%s"%(i)]
   
    a_new= a.ravel()

    b_new= b.ravel()
    
    matrixA=[]
    for a in a_new:
     if str(a)=="inf":
       matrixA.append(a)
     else:
       matrixA.append(a)

    matrixB=[]
    for b in b_new:
     if str(b)=="inf":
         matrixB.append(b)
     else:
         matrixB.append(b)

    #start to calculate the r at the individual level
         
    corr12=np.corrcoef(matrixA,matrixB)
    
    totalcor12=totalcor12+corr12[1,0]

#start to calculate the r at the group level (the mean r), and report it
averagecor12=totalcor12/nubofsubject
print (" ")
print ("The number of subjects is "+str(nubofsubject))
print ("The mean correlation is "+str(averagecor12))
print (" ")
print ("All of the calculations were finished ")


