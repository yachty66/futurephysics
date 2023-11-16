import marvin
from marvin import ai_model
from pydantic import BaseModel, Field
from typing import List
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

marvin.settings.openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    image_urls=get_last_five_images("solar power")
    print(image_urls)
    
    pass

@ai_model(instructions="given a section of a short story. i need to find a good image from wikipedia to represent this section. for this i need only one keyword.")
class Keyword(BaseModel):
    """
    provide the best keyword
    """
    keyword: str

def generate_url(keyword):
    """
    generates a link to the wikipedia commons page with the respective keyword
    """
    keyword = keyword.replace(' ', '+')
    url = f"https://commons.wikimedia.org/w/index.php?search={keyword}&title=Special:MediaSearch&go=Go&type=image&filemime=gif"
    return url

def get_last_five_images(keyword):
    """
    gets the last 5 images from the Wikimedia Commons based on the keyword search
    """
    # Generate the search URL
    url = generate_url(keyword)

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all image elements on the page
    images = soup.find_all('img')

    # Get the last 5 images
    last_five_images = images[0:5]

    # Extract the source URLs of the images
    image_urls = [img['src'] for img in last_five_images]

    return image_urls


def evaluate_images():
    """
    evaluates the 5 images and returns the best one

    i either just take the last 5 images or i do a image mapping 
    """

    pass 

def get_image():
    """
    given a section of a short story:

    A new on-site processing facility uses solar power and advanced filtration systems to refine gold. This reduces the carbon footprint of transporting ores and cuts down on energy consumption, aligning the mining industry with global sustainability goals.

    i need to find a good image from wikipedia to represent this section. for this i need a list of keywords.

    1. get a list of keywords with which i could start a effective search from - 
    2. get for from key word 
    3. let gpt vision make a decision on what image would fit best for the section
    """
    keywoard = Keyword("A new on-site processing facility uses solar power and advanced filtration systems to refine gold. This reduces the carbon footprint of transporting ores and cuts down on energy consumption, aligning the mining industry with global sustainability goals.")




if __name__ == "__main__":
    main()

