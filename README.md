# SLIM_Technical-Validation-

This repository relates to 

[1] the paper under review in Scientific Data
Longitudinal test-retest neuroimaging data from healthy young adults in southwest China  
by  Wei Liu.1, 2, 3, Guorong Wu.1, 2, Dongtao Wei.1, 2, Wenjing Yang,1, 2 Qunlin Chen.1, 2, Jie Meng.1,2, Taiyong Bi. 1, 2, Qinglin Zhang. 1, 2, Xi-Nian Zuo.2,4,5*, Jiang Qiu.1, 2*   

Abstract
Multimodal magnetic resonance imaging (mMRI) has been widely used to map the structure and function of the human brain, as well as its behavioral associations. However, to date, a large sample with a long-term longitudinal design and a narrow age-span has been lacking for the assessment of test-retest reliability and reproducibility of brain-behavior correlations, as well as the development of novel causal insights into these correlational findings. Here we describe the SLIM dataset, which includes brain and behavioral data across a long-term retest-duration within three and a half years, mMRI scans provided a set of structural, diffusion and resting-state functional MRI images, along with rich samples of behavioral assessments addressed - demographic, cognitive and emotional information. Together with the Consortium for Reliability and Reproducibility (CoRR), the SLIM is expected to accelerate the reproducible sciences of the human brain by providing an open resource for brain-behavior discovery sciences with big-data approaches. 


[2] the data released at 1000 Functional Connectomes Project 
Southwest University Longitudinal Imaging Multimodal (SLIM) Brain Data Repository: A Long-term Test-Retest Sample of Young Healthy Adults in Southwest China (http://fcon_1000.projects.nitrc.org/indi/retro/southwestuni_qiu_index.html)

In the paper, we performed the several Technical Validations and you can find the customed codes here. In addition, we provided a script to help users download and organize the functional connectivtiy matrices for further use.

[1] Organize the matrices [SD_organize.py]
    This code can be used to organize the connectivtiy matrices downloaded from this link:
    http://fcon_1000.projects.nitrc.org/indi/retro/southwestuni_qiu_index.html
    (Southwest University Longitudinal Imaging Multimodal (SLIM) Brain Data Repository: A Long-term Test-Retest Sample of Young Healthy   Adults in Southwest China)

    After being re-organized, those matrices were placed in 3 separate folders. You can use the SD_correlation_matrix.py to calculate the correlation between connectivtiy matrices at different time points

    Things you need to change to make this script run properly

    [1] datapath
    where you store the [.tar.gz] file

    [2] file_to_un
    the name of the file you would like to untar


[2] Calculate the correlation between matrices [SD_correlation_matrix.py]
    This code can be used to caclculate the Pearson correlation coefficients between the connectivity matrices of the same subject at different time points.

   (1) What you need ?
    - Connectivity matrices [.mat] or you should change the way the code load the file 
    - Subject list file [.txt]: 
    - change the nubofsubject varaible in the code according to your subject list

   (2) What the code will do ?
    -calculate the Pearson correlation coefficients between two connectivity matrices at the subject level
    -average them and report the final correlation at the group level
    
   Things you need to change to make this script run properly

   (1) matricesfolder1 and matricesfolder2
       Specify the place you store your [.mat] files
   (2) Number of subjects
       The number of subjects you want to include in the analysis.
       The number should match the number of IDs in the [.txt] 
       If the two numbers do not match, the script will stop running and report a error
   (3) Name of the variable which contains the functional connectivtiy strength
       when you load the matrices from the [.mat], you need to specify which varaible you would like to load
    
   Note:
   (1)    [.mat] is a pre-calculated MxM matrix containing individual's connectivity matrix, where M = number of nodes in the chosen     brain atlas. The
          functional connectivtiy strength should be stored in a variable called FCstrength. You can use different softwares or even custom script to calculate the MxM matrix. 
          I recommend the beginners to use DPABI to calculate the [.mat] file. 
          Yan, C.G., Wang, X.D., Zuo, X.N., Zang, Y.F., 2016. DPABI: Data Processing & Analysis for (Resting-State) Brain Imaging. Neuroinformatics. In press. doi: 10.1007/s12021-016-9299-4
          Matrices at different time points hould be stored separately in  matricesfolder1 and matricesfolder2 using the same name
   (2)    [.txt] is a Nx1 vector of the subjects' ID who you want to include in the correlational analysis. the [.txt] should be placed in the same folder as this code.

