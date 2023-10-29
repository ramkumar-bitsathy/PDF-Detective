import requests
import os
import glob
from googlesearch import search

class main:
    def __init__(self,keyword):
        

        def collect_top_pdfs(keyword, num_results):
            search_results = search(keyword, num_results=num_results)

            pdf_urls = []
            count = 0
            for result in search_results:
                try:
                    if is_pdf_url(result):
                        pdf_urls.append(result)
                        count += 1
                        if count >= num_results:
                            break
                except requests.exceptions.RequestException:
                    print(f"Error accessing URL: {result}")
                    continue

            return pdf_urls

        def is_pdf_url(url):
            try:
                response = requests.head(url)
                content_type = response.headers.get('content-type')

                if content_type and 'application/pdf' in content_type:
                    return True
                else:
                    return False
            except requests.exceptions.RequestException:
                return False

        def delete_existing_pdfs(folder_path):
            pdf_files = glob.glob(os.path.join(folder_path, '*.pdf'))
            for file_path in pdf_files:
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except OSError as e:
                    print(f"Error deleting: {file_path} - {e}")

        def download_pdfs(pdf_urls, folder_path):
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            for url in pdf_urls:
                try:
                    response = requests.get(url)
                    filename = os.path.join(folder_path, os.path.basename(url))
                    with open(filename, 'wb') as file:
                        file.write(response.content)
                    print(f"Downloaded: {filename}")
                except requests.exceptions.RequestException:
                    print(f"Error downloading: {url}")

        
        # Delete existing PDFs
        delete_existing_pdfs(folder_path)

        # Collect new PDF URLs
        pdf_urls = collect_top_pdfs(keyword, num_results)

        # Download new PDFs
        download_pdfs(pdf_urls, folder_path)


# Example usage
keyword = ""
num_results = 10
folder_path = r"C:\Users\RAMKUMAR K\Desktop\qtdoctriever\downloads"  # Specify the folder path where PDFs will be saved




    
