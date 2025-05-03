import streamlit as st
import numpy as np
import pandas as pd


# # # MORE

def app():    
    st.header('A :green[STUDY] ON UNIVERSITY INFORMATION OUTLETS')
    st.subheader('**PROJECT SUMMARY**')
    st.markdown('''This project proposes a mobile and online platform to improve information flow within the university. 
            Students and faculty will receive personalized and timely updates, announcements, and event details. 
            Additionally, a user-friendly system that is developed to help students report and track lost belongings on campus, 
            reducing stress and promoting a more organized environment.''')
    st.markdown('**A study conducted in the University of Dar es Salaam on information outlets, the results are as follows** ')
    



 
    st.write(' ### ')
    st.write(' ### ')

    st.subheader('Team')
    bottom1, bottom2, bottom3 = st.columns(3, gap='small')
    bot1, bot2, bot3 = st.columns([3.5,3,3]) 
    with bottom1:  
       container1 = st.container(border=True) 
       container1.image('profile-pic-3.png', width=150)
       container1.markdown('**Martha Kidumbuyo**')

    with bottom2:
        container2 = st.container(border=True)   
        container2.image('profile-pic.png', width=150)
        container2.markdown('  **[John Ndelembi](https://earnest-puppy-53aea3.netlify.app)**')

    with bottom3:
        container3 = st.container(border=True)    
        container3.image('profile-pic-2.png', width=150)
        container3.markdown('**Dadila Seddy**')

    container = st.container(border=True)
    with container:
        cols1, cols2 = st.columns([7,2])
        cols2.image('logo.png', width=150)    
        cols1.subheader(':green[Chat with Us]')
        cols1.markdown('Contact via: [Whatsapp](https://wa.link/p7ke9l)')
        cols1.markdown('Contact via: [E-mail](https://williamjohnie61@gmail.com)')
    
    
    col1, col2, col3, col4 = st.columns([2,6,2,2])
    col1.caption('mwanachuo.app')
    col3.caption(' [Privacy Policy]()')
    col4.caption( ' [Terms of Use]() ')
    

# Function to check user inactivity and automatically log out after 15 minutes
def check_user_inactivity():
    inactivity_limit = 15 * 60  # 15 minutes in seconds
    current_time = time.time()

    # Track last activity time
    if 'last_activity_time' not in st.session_state:
        st.session_state.last_activity_time = current_time

    # Calculate inactivity time
    inactivity_time = current_time - st.session_state.last_activity_time

    # If the user is inactive for too long, log them out
    if inactivity_time > inactivity_limit:
        st.session_state.clear()  # Clear session state to log the user out
        st.write("You have been logged out due to inactivity.")
        st.experimental_rerun()  # Rerun the app to reset the session

    # Update the last activity time
    st.session_state.last_activity_time = current_time   

# Logout function
def logout():
    st.session_state.logged_in = False
    st.info("✔️Logged out successfully!")
    sleep(0.5)
    st.switch_page("streamlit_app.py")
