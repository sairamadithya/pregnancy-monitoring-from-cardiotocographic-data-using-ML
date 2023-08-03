import streamlit as st
import numpy as np
import pandas as pd
import pickle
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.takeshape.io/f1ba446a-c0cf-4882-b0c9-50298f143ec2/dev/d801bb91-bd2e-4af0-a060-7243ef785476/861915");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
html_temp = """ 
  <div style="background-color:orange ;padding:7px">
  <h2 style="color:black;text-align:center;"><b>AUTOMATED FETAL CARDIAC ANALYSIS FROM CARDIOTOCOGRAPHY DATA USING ML<b></h2>
  </div>
  """ 
st.markdown(html_temp,unsafe_allow_html=True)
model1= pickle.load(open(r"stage-1.pkl", 'rb'))
model2= pickle.load(open(r"stage-2.pkl", 'rb'))
x1,buff, buff2 = st.columns(3)
x1=st.number_input('Enter the value of start instant',0,4000)
x2=st.number_input('Enter the value of end instant',0,4000)
x3=st.number_input('Enter the value of baseline value of expert',0,160)
x4=st.number_input('Enter the value of baseline of sisporto',0,160)
x5=st.number_input('Enter the value of acceleration of sisporto',0,26)
x6=st.number_input('Enter the value of foetal movement',0,600)
x7=st.number_input('Enter the value of uterine contraction',0,25)
x8=st.number_input('Enter the value of percentage of time with abnormal short term variability',0,100)
x9=st.number_input('Enter the value of mean value of short term variability',0,10)
x10=st.number_input('Enter the value of percentage of time with abnormal long term variability',0,100)
x11=st.number_input('Enter the value of  mean value of long term variability',0,60)
x12=st.number_input('Enter the value of  light deceleration',0,20)
x13=st.number_input('Enter the value of  severe deceleration',0,1)
x14=st.number_input('Enter the value of  prolonged deceleration',0,4)
x15=st.number_input('Enter the value of  width',0,200)
x16=st.number_input('Enter the value of  min',0,200)
x17=st.number_input('Enter the value of  max',0,250)
x18=st.number_input('Enter the value of  nmax',0,20)
x19=st.number_input('Enter the value of  nzeros',0,10)
x20=st.number_input('Enter the value of  mode',0,200)
x21=st.number_input('Enter the value of  mean',0,200)
x22=st.number_input('Enter the value of  median',0,200)
x23=st.number_input('Enter the value of  variance',0,200)
x24=st.number_input('Enter the value of  tendency',0,300)
inp=pd.DataFrame([[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24]],columns=['b', 'e', 'LBE', 'LB', 'AC', 'FM', 'UC', 'ASTV', 'MSTV', 'ALTV', 'MLTV','DL','DS','DP','Width','Min','Max','Nmax','Nzeros','Mode','Mean','Median','Variance','Tendency'])
inm=inp.copy()
if st.button('Basic diagnosis'):
    op=model1.predict(inp).astype(np.int16)
    if op==0:
        st.markdown(""" 
  <div style="background-color: green;padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">No pathology observed!!</h2>
  </div>
  """ ,unsafe_allow_html=True)
    elif op==1:
        st.markdown(""" 
  <div style="background-color: yellow;padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">Pathology suspected!!</h2>
  </div>
  """ ,unsafe_allow_html=True)
    elif op==2:
        st.markdown(""" 
  <div style="background-color: red;padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">Pathology confirmed!!</h2>
  </div>
  """ ,unsafe_allow_html=True)
st.write()
st.write()
if st.button('Advanced diagnosis'):
        out=model2.predict(inm)
        st.write(out)
        if out==0:
            st.markdown(""" 
  <div style="background-color: green;padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">Calm sleep!!</h2>
  </div>
  """ ,unsafe_allow_html=True)
        elif out==1:
            st.markdown(""" 
  <div style="background-color: green;padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">REM sleep!!</h2>
  </div>
  """ ,unsafe_allow_html=True)
        elif out==2:
            st.markdown(""" 
  <div style="background-color: yellow;padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;"> Calm vigilance!!</h2>
  </div>
  """ ,unsafe_allow_html=True)
        elif out==3:
            st.markdown(""" 
  <div style="background-color: yellow;padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">Active vigilance!!</h2>
  </div>
  """ ,unsafe_allow_html=True)
        elif out==4:
            st.markdown(""" 
  <div style="background-color: red;padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">Shift pattern!!</h2>
  </div>
  """ ,unsafe_allow_html=True)
        elif out==5:
            st.markdown(""" 
  <div style="background-color: red;padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">Stress!!</h2>
  </div>
  """ ,unsafe_allow_html=True)
        elif out==6:
            st.markdown(""" 
  <div style="background-color: red;padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">Vagus reflex!!</h2>
  </div>
  """ ,unsafe_allow_html=True)
        elif out==7:
            st.markdown(""" 
  <div style="background-color: red;padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">Largely decelerative!!</h2>
  </div>
  """ ,unsafe_allow_html=True)
        elif out==8:
            st.markdown(""" 
  <div style="background-color: red;padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">Flat sinusoidal pattern!!</h2>
  </div>
  """ ,unsafe_allow_html=True)
        else:
            st.markdown(""" 
  <div style="background-color: red;padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">Suspect pattern!!</h2>
  </div>
  """ ,unsafe_allow_html=True)
            
st.write('https://www.linkedin.com/in/sairamadithya')
st.write('https://github.com/sairamadithya')
st.write('https://medium.com/@sairamadithya2002')
st.write('https://www.quora.com/profile/Sairam-Adithya')
