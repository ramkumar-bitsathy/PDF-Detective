import streamlit as st

def home():
    st.title('Welcome to PDF Detective🕵🏻!')
    st.header('📃📄📃📄📃📃📄📄📃📃📄📄📄📃')
    st.markdown('**What is The Problem?**')
    st.write("""Information explosion" refers to the rapid increase in the amount of information that is
available and easily accessible through various forms of media, such as the internet, social
media. This phenomenon has led to an abundance of information, both useful and unreliable,
which can be overwhelming for individuals and organizations to process and make sense of. As a
result, it has become increasingly important to develop tools and strategies for managing and
filtering this information. Our Virtual librarian project is a self-learning software which can able
to identify the keywords from the documents and enables user to easily retrieve the files using a
search GUI.""")
    """Concept of our Document retriever project is to make software which can
able to identify the entered keywords from the documents by sifting
through all the documents and enables user to easily retrieve the files
using a search GUI.
Documents can be added to the folder manually and can also be
extracted from the given websites and documented as pdf.
"""


    st.header('📃📄📃📄📃📃📄📄📃📃📄📄📄📃')
    st.markdown('**Key Features:**')
    st.write('- Feature 1: Easy accessing of documents')
    st.write('- Feature 2: Sifts throughout the contents of documents and enables user to fetch the document based on the entered Keyword')
    st.write('- Feature 3: Simple web app with easily catching UI')
    

    
    # Read the contents of the CSS file
    with open(r"C:\Users\RAMKUMAR K\Desktop\WEB retriever\static\style.css", "r") as f:
        css = f.read()

    # Embed the CSS styles using st.markdown
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
if __name__ == '__main__':
    home()
