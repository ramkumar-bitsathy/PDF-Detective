import streamlit as st
import subprocess
import app,home

def login():
    with open(r"C:\Users\RAMKUMAR K\Desktop\WEB retriever\static\style.css", "r") as f:
        css = f.read()

    # Embed the CSS styles using st.markdown
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    button_clicked = False
    if not is_authenticated():
        show_login_page()
    else:
        if not button_clicked:
            st.title("👈Ascess your tabs in left pane")
            #st.header("Navigate where you want👌")
        
        if st.sidebar.button("Home"):
            show_home_page()
            button_clicked = True
        if st.sidebar.button("App"):
            #show_app_content()
            show_app_content()
            button_clicked = True
        if st.sidebar.button("Summarizer"):
            show_summarizer_content()
            button_clicked = True
        if st.sidebar.button("More features to be added"):
            pass
# Read the contents of the CSS file
    
    

def is_authenticated():
    return st.session_state.get("authenticated", False)

def show_login_page():
    st.title("Login to Ease the access of your document")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "ram" and password == "qwerty123":
            st.session_state.authenticated = True
            st.experimental_rerun()
        else:
            st.error("Invalid username or password.")




def show_home_page():
    home.home()
    

def show_app_content():
    subprocess.Popen(["streamlit","run","app.py"])


def show_summarizer_content():
    pass


login()
