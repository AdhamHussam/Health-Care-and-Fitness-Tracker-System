import streamlit as st
import requests
import joblib
from streamlit_lottie import st_lottie
import numpy as np
from PIL import Image
from model import get_row_values
#st.set_page_config(page_title='physical Health', page_icon='::star::')

def Physical():
    
    def load_lottie(url): # test url if you want to use your own lottie file 'valid url' or 'invalid url'
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    def prepare_input_data_for_weight_model(Exercise,CaloriesBurn,ActualWeight,Age,Gender,Duration,HeartRate,BMI,WeatherConditions,ExerciseIntensity):
        
        if Gender=='Female':
            gen=0
        else:
            gen=1
            
        if Exercise=='Exercise 1':
            ex=1
        elif Exercise=='Exercise 2':
            ex=2
        elif Exercise=='Exercise 3':
            ex=3
        elif Exercise=='Exercise 4':
            ex=4
        elif Exercise=='Exercise 5':
            ex=5
        elif Exercise=='Exercise 6':
            ex=6
        elif Exercise=='Exercise 7':
            ex=7
        elif Exercise=='Exercise 8':
            ex=8
        elif Exercise=='Exercise 9':
            ex=9
        elif Exercise=='Exercise 10':
            ex=10
            
        if WeatherConditions=='Cloudy':
            w=0
        elif WeatherConditions=='Rainy':
            w=1
        elif WeatherConditions=='Sunny':
            w=2
            
        A = [ex,CaloriesBurn,ActualWeight,Age,gen,Duration,HeartRate,BMI,w,ExerciseIntensity]
        sample3= np.array(A).reshape(-1,len(A))
        return sample3

    def prepare_input_data_for_Heart_model(id):
        
        A = [get_row_values(id)]
        sample1= np.array(A)#.reshape(-1,len(A))
        return sample1

    def prepare_input_data_for_Calories_model(id):
    
        B = [get_row_values(id)]
        sample2= np.array(B)#.reshape(-1,len(B))
        return sample2

    Heart_model =joblib.load(open("Heart_file", 'rb'))
    Calories_model = joblib.load(open("Calories_file", 'rb'))
    weight=joblib.load(open("Dream_Weight_file",'rb'))

    st.write('# Improve your Physical Health With FitVibe')
    lottie_link= "https://lottie.host/5b8478f2-216f-4e43-b5a1-2e4733a2b8f0/E3FyPRdv14.json"

    st.write('---')

    with st.container():
        
        right_column,left_column = st.columns(2)
        
        with right_column:
            st.subheader('Healthy Body, Healthy Life Style')
            
            id= st.number_input('Smart Watch ID : ')
            
            Age=st.number_input('Age : ',value=5, step=1)
            
            Gender=st.radio('Gender : ', ['Female', 'Male'])
            
            Calories_Burn=st.number_input('The estimated number of calories burned during the exercise session : ',min_value=0.0, max_value=1000.0,value=0.0, step=0.1)
            
            Actual_Weight=st.number_input('Actual Weight : ',min_value=0.0, max_value=1000.0,value=0.0, step=0.1)
            
            Duration=st.number_input('The duration of exercise session in minutes. : ',value=0, step=1)
            
            Heart_Rate=st.number_input('The average heart rate during the exercise session: ',min_value=0.0, max_value=1000.0,value=0.0, step=0.1)        
            
            BMI=st.number_input('The body mass index : ')

            Exercise_Intensity=st.number_input('Exercise_Intensity : ',min_value=0.0, max_value=1000.0,value=0.0, step=0.1)

            Weather_Conditions=st.selectbox('Weather Condition : ', ('Cloudy', 'Rainy', 'Others'))
            
            Exercise=st.selectbox('The type of exercise performed during the session : ', ('Exercise 1', 'Exercise 2', 'Exercise 3','Exercise 4','Exercise 5','Exercise 6','Exercise 7','Exercise 8','Exercise 9','Exercise 10'))

            sample1= prepare_input_data_for_Heart_model(id)
            sample2= prepare_input_data_for_Calories_model(id)
            sample3=prepare_input_data_for_weight_model(Exercise,Calories_Burn,Actual_Weight,Age,Gender,Duration,Heart_Rate,BMI,Weather_Conditions,Exercise_Intensity)
            
            
            if st.button('Heart Rate Level'):
                pred_Y1= Heart_model.predict(sample1)
                if pred_Y1==1:
                    st.write('Your Heart Rate Level is Normal.')
                elif pred_Y1==2:
                    st.write('Your Heart Rate Level is abNormal.')
                
            if st.button('Burnd Calories Level '):
                    pred_Y2= Calories_model.predict(sample2)
                    if pred_Y2== 1:
                        st.write('Your Level is Normal.')
                    elif pred_Y2==2:
                        st.write('Your Level is abNormal. ')
                        
            if st.button('Dream Weight'):
                    pred_Y3= weight.predict(sample3)
                    
                    st.write('Your Weight through this month will be:',pred_Y3)
        with left_column:
            st.write('  ')
            st.write('  ')
            st.write('  ')
            st.write('  ')
            st.write('  ')
            st.write('  ')
            st.write('  ')
            st.write('  ')
            st.write('  ')
            st.write('  ')
            st.write('  ')
            st.write('  ')
            #st_lottie(lottie_link, speed=1, height=400, key="initial")
            st.write('  ')
            st.write('  ')
            st.write('  ')
            st.write('  ')
        
        
        
                
                  