# pregnancy-monitoring-from-cardiotocographic-data-using-ML
This project is about the development of a machine learning model and website for the analysis of the cardiac health of the fetus using cardiotocographic data.

**Features:**
FileName: of CTG examination
Date: of the examination
b: start instant
e: end instant
LBE: baseline value (medical expert)
LB: baseline value (SisPorto)
AC: accelerations (SisPorto)
FM: foetal movement (SisPorto)
UC: uterine contractions (SisPorto)
ASTV: percentage of time with abnormal short term variability (SisPorto)
mSTV: mean value of short term variability (SisPorto)
ALTV: percentage of time with abnormal long term variability (SisPorto)
mLTV: mean value of long term variability (SisPorto)
DL: light decelerations
DS: severe decelerations
DP: prolongued decelerations
DR: repetitive decelerations
Width: histogram width
Min: low freq. of the histogram
Max: high freq. of the histogram
Nmax: number of histogram peaks
Nzeros: number of histogram zeros
Mode: histogram mode
Mean: histogram mean
Median: histogram median
Variance: histogram variance
Tendency: histogram tendency: -1=left assymetric; 0=symmetric; 1=right assymetric

**Classes**
A: calm sleep
B: REM sleep
C: calm vigilance
D: active vigilance
SH: shift pattern (A or Susp with shifts)
AD: accelerative/decelerative pattern (stress situation)
DE: decelerative pattern (vagal stimulation)
LD: largely decelerative pattern
FS: flat-sinusoidal pattern (pathological state)
SUSP: suspect pattern
CLASS: Class code (1 to 10) for classes A to SUSP
NSP:- Normal=1; Suspect=2; Pathologic=3

dataset link- https://www.kaggle.com/datasets/akshat0007/fetalhr
