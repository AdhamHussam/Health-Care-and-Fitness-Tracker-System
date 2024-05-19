import streamlit as st
import requests
import joblib
from streamlit_lottie import st_lottie
import numpy as np
from PIL import Image
from Mental_Health_Model import get_row_values
#st.set_page_config(page_title='Mental Health', page_icon='::star::')

def Mental():
    def load_lottie(url): # test url if you want to use your own lottie file 'valid url' or 'invalid url'
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    def prepare_input_data_for_Stress_model(id):
        
        A = [get_row_values(id)]
        sample1= np.array(A)
        return sample1

    def prepare_input_data_for_Sleep_model(id):
    
        B = [get_row_values(id)]
        sample2= np.array(B)
        return sample2

##256CBF #8E8AF9
    Sleep_model =joblib.load(open("Sleep Model", 'rb'))
    Stress_model = joblib.load(open("Stress Model", 'rb'))

    st.write('# Improve your Mental Health With FitVibe')
    lottie_link= "https://lottie.host/40a99cba-a80b-4c67-af96-166c86d3e3ea/5f7FgTQyUn.json"

    st.write('---')


    with st.container():
        
        right_column,left_column= st.columns(2) 
        
        with right_column:
            st.subheader('“Taking care of your mental health is an act of self-love.”')
            id= st.number_input('Smart Watch ID : ', value=0, step=1)
            
            sample1= prepare_input_data_for_Stress_model(id)
            sample2= prepare_input_data_for_Sleep_model(id)
            
            if st.button('Sleep Disorder prediction'):
                pred_Y1= Sleep_model.predict(sample1)
                if pred_Y1==0:
                    st.write('**You does not exhibit any specific sleep disorder.**')
                elif pred_Y1==1:
                    st.write('**Your Sleep Disorder  is Sleep Apnea,So you suffer from pauses in breathing during sleep, resulting in disrupted sleep patterns and potential health risks.**')
                else:
                    st.write('**Your Sleep Disorder  is Insomnia,So experience difficulty falling asleep or staying asleep, leading to inadequate or poor-quality sleep.he individual experiences difficulty falling asleep or staying asleep, leading to inadequate or poor-quality sleep.**')
            
            if st.button('Stress Level prediction'):
                    pred_Y2= Stress_model.predict(sample2)
                    st.write('Stress refers to the body response to pressure or demands, often resulting in physical, emotional, or mental strain. It can be caused by various factors such as work, relationships, or significant life events, and managing stress is important for overall well-being.**')
                    if pred_Y2== 0:
                        st.write('**Your Stress Level is Normal.**')
                    if pred_Y2== 1:
                        st.write('**Your Stress Level is Normal.**')
                    elif pred_Y2==2:
                        st.write('**Your Stress Level is Normal.**')
                    elif pred_Y2==3:
                        st.write('**Your Stress Level is Normal.**')
                    elif pred_Y2==4:
                        st.write('**Your Stress Level is abNormal.**')
                    elif pred_Y2==5:
                        st.write('**Your Stress Level is abNormal.**')
                    elif pred_Y2==6:
                        st.write('**Your Stress Level is abNormal.**')
                    elif pred_Y2==7:
                        st.write('**Your Stress Level is abNormal.**')
        with left_column:
        
            st_lottie(lottie_link, speed=1, height=400, key="initial")
        
                
                
    
