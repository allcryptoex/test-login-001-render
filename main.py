import streamlit as st
from streamlit_option_menu import option_menu
import home, trending, test, your, about
from pathlib import Path

# # # SIDEBAR SETTING

st.set_page_config(
        page_title="UIL SPELLER",
        page_icon='✔'
)

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": function,
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='UIL SPELLER',
                options=['Home','Login','Post','Profile','More'],
                icons=['house-door-fill','box-arrow-in-right','wechat','person-fill','three-dots'],
                menu_icon='app-indicator',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'grey'},
        "icon": {"color": "black", "font-size": "23px"}, 
        "nav-link": {"color":"black","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "grey"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Home":
            trending.app()
        if app == "Login":
            test.app()    
        if app == "Post":
            home.app()        
        if app == 'Profile':
            your.app()
        if app == 'More':
            about.app()    
             
          
             
    run()            

# # # # #

st.write("🔒 Please log in to continue.")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in", type="primary"):
    if username == "uiltest" and password == "curtistest":
        st.session_state.logged_in = True
        st.success("✔️Logged in successfully!")
        sleep(0.5)
        
        # Instead of using st.switch_page(), use st.experimental_rerun() to reload the page.
        st.switch_page("pages/page1.py") # Store the next page in session state
        # st.experimental_rerun()  # Trigger a rerun to go to the new page
    else:
        st.error("❌Incorrect username or password")
         
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
