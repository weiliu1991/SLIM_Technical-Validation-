# -*- coding: utf-8 -*-
"""
Copyright 2016 Wei Liu

This code is released under the terms of the MIT License. This code is not FDA approved for clinical use; it is provided freely for research purposes. 
This code was used in the paper: 

Longitudinal test-retest neuroimaging data from healthy young adults in southwest China  
by  Wei Liu.1, 2, 3, Guorong Wu.1, 2, Dongtao Wei.1, 2, Wenjing Yang,1, 2 Qunlin Chen.1, 2, Jie Meng.1,2, Taiyong Bi. 1, 2, Qinglin Zhang. 1, 2, Xi-Nian Zuo.2,4,5*, Jiang Qiu.1, 2*   

This code can be used to organize the connectivtiy matrices downloaded from this link:
http://fcon_1000.projects.nitrc.org/indi/retro/southwestuni_qiu_index.html
(Southwest University Longitudinal Imaging Multimodal (SLIM) Brain Data Repository: A Long-term Test-Retest Sample of Young Healthy Adults in Southwest China)

After being re-organized, those matrices were placed in 3 separate folders. You can use the SD_correlation_matrix.py to calculate the correlation between connectivtiy matrices at different time points

Things you need to change to make this script run properly

[1] datapath
    where you store the [.tar.gz] file

[2] file_to_un
    the name of the file you would like to untar

@author: weiliu
e-mail: liuwei19910511psychology@gmail.com
"""

import os
import gzip  
import tarfile  
import shutil

#------------------INPUT-------------------------------------------------
datarpath="D:\\Done"
os.chdir(datarpath)
file_to_un="swu_slim_connmats_subs25629-30757"

#-----------------Funtion Define-----------------------------------------
def un_gz(file_name):  
    """ungz zip file"""  
    f_name = file_name.replace(".gz", "")  
    g_file = gzip.GzipFile(file_name)  
    open(f_name, "wb").write(g_file.read())  
    g_file.close()  

    

def un_tar(file_name):  
    """untar zip file"""
    tar = tarfile.open(file_name)  
    names = tar.getnames()  
    if os.path.isdir(file_name + "_files"):  
        pass  
    else:  
        os.mkdir(file_name + "_files")  
    for name in names:  
        tar.extract(name, file_name + "_files/")  
    tar.close()  

#------------Start to untar-----------------------------------------------
file_to_un_gz=file_to_un+".tar.gz"
file_to_un_tar=file_to_un+".tar"

print ("Start to un_gz, please wait...")
print (" ")
un_gz(file_to_un_gz)
print ("Done !")
print ("----------------------------------------------")
print ("Start to un_tar, please wait...")
print (" ")
un_tar(file_to_un_tar)
print ("Done !")

#-------------Start to create new folders--------------------------------------
folderlist=["matricesfolder1","matricesfolder2","matricesfolder3"]
for i in folderlist:
    folderpath=datarpath+"\\"+str(i)
    if os.path.isdir(folderpath):
        pass
    else:
        os.makedirs(folderpath)
#-------------Start to rename and copy file-----------------------------------
subjectfolder=datarpath+"\\"+file_to_un+".tar_files"
subjectlist=os.listdir(subjectfolder)
for n in subjectlist:
   individualfolder=subjectfolder+"\\"+str(n)
   sessionfolder=os.listdir(individualfolder)
   for s in sessionfolder:
       if s=="session_1":
           #print ("There is Scan 1")
           oldname1=individualfolder+"\\"+str(s)+"\\"+"Dosenbach_160\\ROI_FC.mat"
           oldname2=individualfolder+"\\"+str(s)+"\\"+"shen_268\\ROI_FC.mat"
           newname1=individualfolder+"\\"+str(s)+"\\"+"Dosenbach_160\\"+str(n)+"_160"+"ROI_FC.mat"
           newname2=individualfolder+"\\"+str(s)+"\\"+"shen_268\\"+str(n)+"_268"+"ROI_FC.mat"
           if os.path.isfile(oldname1):
               os.rename(oldname1,newname1)
           if os.path.isfile(oldname2):
               os.rename(oldname2,newname2)
           copyto1=datarpath+"\\matricesfolder1"
           if os.path.isfile(newname1):
             shutil.copy(newname1,copyto1)
           if os.path.isfile(newname2):
             shutil.copy(newname2,copyto1)
           print ("Copy Done...")
       elif s=="session_2":
           #print ("There is Scan 2")
           oldname1=individualfolder+"\\"+str(s)+"\\"+"Dosenbach_160\\ROI_FC.mat"
           oldname2=individualfolder+"\\"+str(s)+"\\"+"shen_268\\ROI_FC.mat"
           newname1=individualfolder+"\\"+str(s)+"\\"+"Dosenbach_160\\"+str(n)+"_160"+"ROI_FC.mat"
           newname2=individualfolder+"\\"+str(s)+"\\"+"shen_268\\"+str(n)+"_268"+"ROI_FC.mat"
           if os.path.isfile(oldname1):
               os.rename(oldname1,newname1)
           if os.path.isfile(oldname2):
               os.rename(oldname2,newname2)
           copyto2=datarpath+"\\matricesfolder2"
           if os.path.isfile(newname1):
             shutil.copy(newname1,copyto2)
           if os.path.isfile(newname2):
             shutil.copy(newname2,copyto2)
           print ("Copy Done...")
       elif s=="session_3":
           oldname1=individualfolder+"\\"+str(s)+"\\"+"Dosenbach_160\\ROI_FC.mat"
           oldname2=individualfolder+"\\"+str(s)+"\\"+"shen_268\\ROI_FC.mat"
           newname1=individualfolder+"\\"+str(s)+"\\"+"Dosenbach_160\\"+str(n)+"_160"+"ROI_FC.mat"
           newname2=individualfolder+"\\"+str(s)+"\\"+"shen_268\\"+str(n)+"_268"+"ROI_FC.mat"
           if os.path.isfile(oldname1):
               os.rename(oldname1,newname1)
           if os.path.isfile(oldname2):
               os.rename(oldname2,newname2)
           copyto3=datarpath+"\\matricesfolder3"
           if os.path.isfile(newname1):
             shutil.copy(newname1,copyto3)
           if os.path.isfile(newname2):
             shutil.copy(newname2,copyto3)
           print ("Copy Done...")
           
print ("All the matrices were re-organized...!")         