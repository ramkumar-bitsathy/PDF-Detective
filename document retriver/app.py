import os
import streamlit as st
from PyPDF2 import PdfFileReader
import home
import subprocess
import re


# Read the contents of the CSS file
def search_files(folder_paths, keyword):
    search_results = []

    for folder_path in folder_paths:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".pdf"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "rb") as f:
                        pdf = PdfFileReader(f)
                        for page_num in range(pdf.getNumPages()):
                            page = pdf.getPage(page_num)
                            page_text = page.extractText()
                            if re.search(re.escape(keyword), page_text, re.IGNORECASE):
                                # Highlight the keyword with <strong> tags
                                page_text = re.sub(re.escape(keyword), f"<strong>{keyword}</strong>", page_text, flags=re.IGNORECASE)
                                search_results.append((file_path, file, page_num + 1, page_text))

    return search_results
def open_file(file_path):
    os.startfile(file_path)

def app():
    with open(r"C:\Users\RAMKUMAR K\Desktop\WEB retriever\static\style.css", "r") as f:
        css = f.read()

    # Embed the CSS styles using st.markdown
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    st.title("The PDF Detective🕵🏻")
    folder_paths = [
        r"C:\Users\RAMKUMAR K\Desktop\document retriver\local_drive_2",
        r"C:\Users\RAMKUMAR K\Desktop\document retriver\downloads"
        # Add more folder paths as needed
    ]

    keyword = st.text_input("Enter keyword to search")

    if st.button("Search"):
        if keyword:
            st.write(f"Keyword: {keyword}")

            search_results = search_files(folder_paths, keyword)

            st.write(f"Search results: {len(search_results)} matches found")
            if len(search_results) > 0:
                for result in search_results:
                    file_path, file_name, page_num, page_text = result
                    st.subheader(f"File: {file_name}, Page: {page_num}")
                    st.markdown(page_text, unsafe_allow_html=True)
                    
                    # Add a button to open the entire PDF
                    st.write("Click👇 the button to open Full PDF", unsafe_allow_html=True)
                    st.button(
                            label=f"Open File: {file_name}, Page: {page_num}",
                            on_click=open_file,
                            args=(file_path,),
                        )
        else:
            st.warning("Please enter a keyword.")

    st.text("Instructions: Enter a keyword to search. Click the 'Search' button to perform the search.")



app()





