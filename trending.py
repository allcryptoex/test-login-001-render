import streamlit as st
from firebase_admin import auth

def app():
    #st.header(' UIL SPELLER ')
    
    header1, header2 = st.columns([0.75,3])
    with header1:
        container1 = st.container(border=True)   
        container1.image('logo.png', width=100)

    
    st.header(' :green[How to Start Self Practice?]')
    col1, col2 = st.columns([1,2])
 
    col1.markdown(' **The self practice platform for UiL spelling participants.** ')
    col1.markdown('''UIL Spellers makes it easier to practice spelling.''')
    col1.markdown('''Let's get started by signing up or logging in.''')
    
    col2.write('[Learn More](https://wa.link/p7ke9l)')


    with col2:
        col5, col6 = st.columns(2)
        col5.button(' :green[**Sign Up**]', use_container_width=True)
        


    st.write(' ### ')
    st.write(' ### ')
    st.write(' ### ')
    # X mid1, mid2, mid3 = st.columns([4,2,4])
    # X mid2.subheader('.')
    # X mid6, mid7, mid8 = st.columns([0.5,15,0.5])
    # X mid7.write('**.**')

    # X mid4, mid5 = st.columns([3,4])

    # X st.caption("")


    st.write(' ### ')
    container = st.container(border=True)
    with container:
        col1, col2 = st.columns([4,2])
        col1.subheader(':green[**Subscribe to our newsletter**] ')
        col1.write('**Get our real time updates**')
        col2.text_input(label='', placeholder='Your Email')
        col2.button("Subscribe")


    st.write(' ### ')
    # X st.markdown(''' UIL Speller. ''')    
        

    st.write(' ### ')
    st.write(' ### ')
    st.write(' ### ')
    st.write(' ### ')
    col1, col2, col3, col4 = st.columns([2,6,2,2])
    # X col1.caption('mwanachuo.app')
    col3.caption(' [Privacy Policy]()')
    col4.caption( ' [Terms of Use]() ')

    

    
