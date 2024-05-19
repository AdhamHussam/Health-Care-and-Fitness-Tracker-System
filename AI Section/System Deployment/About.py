import streamlit as st
import requests
import joblib
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import numpy as np
from Mental_health import Mental
from Physical_health import Physical

st.set_page_config(
    page_title="Fitness Tracker System",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
def load_lottie(url): # test url if you want to use your own lottie file 'valid url' or 'invalid url'
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_link= "https://lottie.host/7aa4362e-7255-4a45-8bca-e45597f011e4/YImVoaNfhv.json"

# Define function for About page
def about_page():
    st.title("About")
    with st.container():
    #
        right_column,left_column= st.columns(2) 
    
        with right_column:
            st.write('  ')
            st.write('  ')
            st.markdown("""
        Welcome to our Healthcare and Fitness Tracker System!

        Our system integrates AI and Electrical technologies to monitor and optimize users' health and fitness activities. It includes features such as:
        - Stress level prediction
        - Sleep pattern recommendation
        - Heart rate prediction
        - Burnt calories prediction

        We aim to provide personalized recommendations and insights to help users achieve their health and fitness goals.

        **Developed by [Adham Hussam/Bansee AbdelNasser/Habiba Yousry].**
        """)
    # Add a separator
            st.markdown("---")
        with left_column:
            st_lottie(lottie_link, speed=1, height=400, key="initial")
            
            
    # Add a user testimonial
    st.markdown(
        """
        **User Testimonial:**

        "Since I started using the Healthcare and Fitness Tracker System, I've seen incredible improvements in my overall well-being. 
        The personalized recommendations and insights have helped me achieve my fitness goals faster than I ever thought possible!"

        \- Sarah D., Happy User
        """
    )

    # Add a separator
    st.markdown("---")

    # Add a card layout for features
    st.subheader("Key Features")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("🌟 Stress Level Prediction")
    with col2:
        st.markdown("🌙 Sleep Pattern Recommendation")
    with col3:
        st.markdown("❤️ Heart Rate Prediction")

    

# Main function to run the app
def main():
    # Create sidebar navigation
    with st.sidebar:
        choice = option_menu(None, ["About", "Physical Health", "Mental Health"],
                         icons=["house", "heart", 'brain'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": '#E0E0EF', "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"}
        })
 
    
    # Display selected page
    if choice == "About":
        about_page()
    elif choice == "Physical Health":
        Physical()
    elif choice == "Mental Health":
        Mental()

if __name__ == "__main__":
    main()
