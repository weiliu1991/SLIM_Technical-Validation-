# -*- coding: utf-8 -*-
"""
Copyright 2016 Wei Liu

This code is released under the terms of the MIT License. This code is not FDA approved for clinical use; it is provided freely for research purposes. 
This code was used in the paper: 

Longitudinal test-retest neuroimaging data from healthy young adults in southwest China  
by  Wei Liu.1, 2, 3, Guorong Wu.1, 2, Dongtao Wei.1, 2, Wenjing Yang,1, 2 Qunlin Chen.1, 2, Jie Meng.1,2, Taiyong Bi. 1, 2, Qinglin Zhang. 1, 2, Xi-Nian Zuo.2,4,5*, Jiang Qiu.1, 2*   

This code can be used to caclculate the Pearson correlation coefficients between the connectivity matrices of the same subject at different time points.

[1] What you need ?
    - Connectivity matrices [.mat] or you should change the way the code load the file 
    - Subject list file [.txt]: 
    - change the nubofsubject varaible in the code according to your subject list

[2] What the code will do ?
    -calculate the Pearson correlation coefficients between two connectivity matrices at the subject level
    -average them and report the final correlation at the group level
    
Things you need to change to make this script run properly

[1] matricesfolder1 and matricesfolder2
    Specify the place you store your [.mat] files
[2] Number of subjects
    The number of subjects you want to include in the analysis.
    The number should match the number of IDs in the [.txt] 
    If the two numbers do not match, the script will stop running and report a error
[3] Name of the variable which contains the functional connectivtiy strength
    when you load the matrices from the [.mat], you need to specify which varaible you would like to load
    
Note:
(1)    [.mat] is a pre-calculated MxM matrix containing individual's connectivity matrix, where M = number of nodes in the chosen brain atlas. The
       functional connectivtiy strength should be stored in a variable called FCstrength. You can use different softwares or even custom script to calculate the MxM matrix. 
       I recommend the beginners use DPABI to calculate the [.mat] file. 
       Yan, C.G., Wang, X.D., Zuo, X.N., Zang, Y.F., 2016. DPABI: Data Processing & Analysis for (Resting-State) Brain Imaging. Neuroinformatics. In press. doi: 10.1007/s12021-016-9299-4
       Matrices at different time points hould be stored separately in  matricesfolder1 and matricesfolder2 using the same name
(2)    [.txt] is a Nx1 vector of the subjects' ID who you want to include in the correlational analysis. the [.txt] should be placed in the same folder as this code.

@author: weiliu
e-mail: liuwei19910511psychology@gmail.com
"""

import os
import scipy.io as sio 
import numpy as np

#---------------------------- load IMPUT---------------------------------------

# where you put the functional connectivtiy matrixs
matricesfolder1="C:\\Users\\weiliu\\Desktop\\Matrix_Test\\Scan1"
matricesfolder2="C:\\Users\\weiliu\\Desktop\\Matrix_Test\\Scan2"

# use a [.txt] file to identify the group of subjects you want to calculate
listfile=open("time12.txt","r+")
#change the number according to the number of names
nubofsubject=170

#---------------------------End INPUT-----------------------------------------

#---------------------------Start to Check Data------------------------------
subjectlist=range(nubofsubject) 
calculatelist=[]
for n in subjectlist:
    calculatelist.append(str(listfile.readline().strip('\n')))
if listfile.closed==False:  #return the situation of certain file(True or False)
      listfile.close() 

listScan1=os.listdir(matricesfolder1)
listScan2=os.listdir(matricesfolder2)

if len(calculatelist)==len(listScan1)==len(listScan2):
    print ("Check Done, Start to caculate !")
else:
    print ("The script stopped since the data did not match the list file")
    print ("Please check")

#-------------------------End Check---------------------------------------------

#------------------------Start load matrices-----------------------------------
# create two new dicts, load the matrices and store them in the dicts
my_matrix1={}
for i in calculatelist:
    matfn=matricesfolder1+"\\%s.mat"%(i)
    data=sio.loadmat(matfn)
    my_matrix1[str(i)]=data['FCstrength']

my_matrix2={}
for i in calculatelist:
    matfn=matricesfolder2+"\\%s.mat"%(i)
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

#------------------Start final report--------------------------------------
print (" ")
print ("The number of subjects is "+str(nubofsubject))
print ("The mean correlation is "+str(averagecor12))
print (" ")
print ("All of the calculations were finished ")



