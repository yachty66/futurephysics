import marvin
from marvin import ai_model
from pydantic import BaseModel, Field
from typing import List
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import openai

load_dotenv()

marvin.settings.openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    short_story = "A new on-site processing facility uses solar power and advanced filtration systems to refine gold. This reduces the carbon footprint of transporting ores and cuts down on energy consumption, aligning the mining industry with global sustainability goals."
    image_urls=get_last_five_images("solar power")
    print(image_urls)
    most_general_image = evaluate_images(image_urls, short_story)
    print(most_general_image)

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
    # Find all <a> elements that have an <img> child
    image_links = soup.find_all('a', {'class': 'sdms-image-result'})
    # Get the last 5 image links
    last_five_image_links = image_links[:5]
    # Extract the source URLs of the images
    image_src_urls = [link.find('img')['src'] for link in last_five_image_links]
    return image_src_urls

def evaluate_images(image_urls, section):
    """
    evaluates the 5 images and returns the best one
    """
    prompt = f"""
    i am creating a short story with different sections and each section also has a image. i am making a query on wikimedia commons with a keyword which represents my section. its about the following section:

    ---
    {section}
    ---

    of the series of images which one represents the section best? return only the number of the image and nothing else:
    """
    # Prepare the initial message
    messages = [{
        "role": "user",
        "content": [{
            "type": "text",
            "text": prompt,
        }]
    }]

    # Add each image URL to the messages
    for url in image_urls:
        messages.append({
            "role": "user",
            "content": [{
                "type": "image_url",
                "image_url": {
                    "url": url,
                }
            }]
        })

    # Send the API request
    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=messages,
        max_tokens=300,
    )
    return response.choices[0].message.content 

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




