import os
import re
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests

load_dotenv()

# Function to remove special characters from a string
def remove_special_characters(text):
    # Define the pattern for special characters
    pattern = r'[^a-zA-Z0-9\s]'
    # Remove special characters using regex substitution
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text

# Scraper function to scrape the content from the URL and store it in the database
def scrape_and_store(user_id, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    # From the page, get the text content and remove new lines, spaces, and special characters
    content = soup.find('body').get_text().replace('\n', '').replace('\r', '').replace('\t', '')
    content = remove_special_characters(content)
    
    client = MongoClient(os.getenv("MONGO_CONNECTION_STRING"))  
    db = client[os.getenv("MONGO_DB_NAME")]
    collection = db[os.getenv("MONGO_COLLECTION_NAME")]
    data = {
        "user_id": user_id,        
        "content": content,
        "url": url
    }
      
    collection.insert_one(data)

