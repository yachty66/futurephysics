"""
file in which i generate the story
"""
import openai 
import json
import os
import random
from dotenv import load_dotenv
import wikipedia 
import sys

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def story():
    categories = load_categories()
    categories_str = make_categories_str(categories)
    story = generate_story(categories_str)
    try:
        title, year, sections = parse_story(story)
    except ValueError as e:
        print(f"Error parsing following story: {categories_str}")
        sys.exit(1)
    image_urls = image_generator(sections)
    html = html_converter(title, sections, image_urls, categories_str)

def parse_story(story_str):
    """
    Parse the story string into a list of sections, title, and year
    """
    # Convert the string into a dictionary
    story_dict = json.loads(story_str)
    # Extract the title, year, and sections
    title = story_dict.get('title')
    year = story_dict.get('year')
    sections = [value for key, value in story_dict.items() if key not in ['title', 'year']]
    return title, year, sections

def make_categories_str(categories):
    """
    takes dict of categories and makes it into a string for the prompt
    """
    # Filter out empty values
    non_empty_categories = filter(None, categories.values())
    categories_str = ', '.join(non_empty_categories)
    return categories_str

def load_categories():
    """
    Load the categories from settings.json
    """
    with open('settings.json', 'r') as f:
        data = json.load(f)
    return data

def gpt(temperature, messages, model):
    """
    helper function to call openai api
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    content = response.choices[0].message.content 
    return content

def dalle(prompt, model="dall-e-3", size="1024x1024", quality="hd", n=1):
    """
    dalle api call helper function
    """
    response = openai.Image.create(
        model=model,
        prompt=prompt,
        size=size,
        quality=quality,
        n=n,
    )
    image_url = response.data[0].url
    return image_url

def generate_story(categories):
    """
    generates a story based on the keyword
    """
    random_year = random.randint(2025, 2035)
    first_prompt = f"""\
    I want you to be my cowriter on innovative and ambitious future ideas which are still in the realm of physics so that its not unrealistic that something like this exists. Following and example of such and scenario:

    ---

    Introducing "Skill Factory" 
    Beginning 2026

    College has failed America. Shop classes are in decline. We are indebted to institutions that no longer serve us. 

    Millions of opportunities grow stale as America's future decays

    It's Time To Rebuild 

    ...

    Welcome to Skill Factory #001

    Designed with your local Employer/Sponsor rather than state-funded

    The simplest way to train for & pursue today's careers

    There are no entry exams, schedules, or pre-requisites.

    No Professors. No Tuition. 

    Download the app and let’s explore

    ...

    Screens across the walls list local 'Opportunities', from the Sponsors

    - Lockheed Layup Tech - $23/hour
    - Northrop CMM Tech - $38/hour
    - Tesla Robotics - $52/hour

    Tesla Robotics? Great choice. Only 15 miles away. 

    Let's scan the code to check it out

    ...

    During setup of your app, the algorithm baselines your "Skill Profile" from your background

    Let's watch it compare your Skill Profile and this Tesla Robotics position

    68% Ready, Great. Only 14 skills missing. This should only take a few weeks.

    Let's head over to Training

    ...

    As we walk over, you'll notice each area is dedicated to a set of selected technologies and skills

    You can reserve space where you'd like to explore. Some rooms may require a safety prep for activation

    These are here 24/7/365 so you can choose times that work for you

    ...

    Training:

    A Skill Path has been generated for you, guiding you through the remaining 14 skills

    You'll build projects specifically approved by Tesla's hiring & engineering team

    Use the AI, AR, & Training modules to aid you

    Upload your project and earn the Tesla Certification

    ...

    Overwhelmed?

    Watch for days where professionals from Sponsors will be spending time here

    They may be exploring new technologies or training new skills for their own skill profile

    They are here to support you. The highest reviewed Mentors are highlighted in the Hall of Fame

    ...

    As you progress you'll see more opportunities in your app light up. 

    You qualify to interview for these instantly

    In your "Careers" tab, you'll find Hiring Managers that have offers or are requesting for you to apply

    Congratulations and good luck on your new journey 🇺🇸❤️

    ...

    Why are we building these?

    Companies waste billions every year to search for people that don't exist

    Meanwhile individuals face slow & expensive options with little guidance

    With capacity to help 100,000+ annually per Skill Factory

    We see a way to unlock a Century of Progress

    ...

    If your company would benefit from an endless pipeline of precisely trained candidates

    Or if you wish to have your hardware / software available in America's greatest "Industry Showroom"

    Drop a note below and follow along as we bring this to the world

    It's Time We Rebuild

    --- 

    The example was about an innovative school concept. There are no limits for which areas you can create the concept for. I will provide you with a few categories which should be involved in the concept and you should create the concept from there. please focus on the science aspects and that its in the realm of phyisics. it also shouldnt be just the story about it but rather a excursion for the reader like if he would be there. The story should play in the year {random_year}, i.e. build the scenario realistically and not to far fetched - we are currently in the year 2023.
    """

    second_prompt = f"""\
    Absolutely, I'd be delighted to collaborate with you on creating innovative and ambitious future concepts grounded in the realm of physics. To begin, you can provide me with a few categories or areas of focus, and I will craft a concept around them, ensuring that the ideas are scientifically plausible, innovative and that its like the view of an person who is there.

    For instance, if you're interested in areas like renewable energy, space exploration, advanced robotics, healthcare technology, or smart cities, just let me know. I will then develop a concept that integrates these categories, keeping in mind the principles of physics and the feasibility of such technologies in the near future.

    Feel free to share the categories or specific areas you're interested in, and we can start brainstorming and shaping these futuristic concepts together!
    """

    third_prompt = f"""\
    the categories are: {categories}. dont focus on to many different concepts but rather narrow it down a bit and make sure to focus on physics. please go ahead and write the short story based on this categories. the story should be returned in JSON (and nothing else) as following:

    ---
    {{
        "title": "title"
        "year": "year"
        "first_section": "first section"
        "second_section": "second section"
        "third_section": "third section"
        "fourth_section": "fourth section"
        "fifth_section": "fifth section"
        "sixth_section": "sixth section"
        "seventh_section": "seventh section"
        "eighth_section": "eighth section"
        "ninth_section": "ninth section"
        "tenth_section": "tenth section"
    }}
    --- 
    """
    messages=[
        {"role": "user", "content": first_prompt},
        {"role": "assistant", "content": second_prompt},
        {"role": "user", "content": third_prompt},
    ]
    #gpt-3.5-turbo-1106
    story=gpt(0.5, messages, model="gpt-3.5-turbo-1106")
    return story

def generate_first_image(first_section):
    """
    generates the first image which is also the title image
    """
    prompt=f"""\
    i generated a short story with ten short sections. my goal is it now to create an appropriate image for each section. the section i am going to provide to you is also the section which is responsible for the title image (the image which serves as thumbnail for the story). please generate an image for the following section:

    ---
    {first_section}
    ---

    please keep in mind that the image you generate shouldnt be to far fetched into the future and realistic in the realm of physics.
    """
    image_url = dalle(prompt)
    return image_url

def generate_image(section):
    """
    generates the first image which is also the title image
    """
    prompt=f"""\
    i generated a short story with ten short sections. my goal is it now to create an appropriate image for each section. please generate an image for the following section:

    ---
    {section}
    ---

    please keep in mind that the image you generate shouldnt be to far fetched into the future and realistic in the realm of physics.
    """
    image_url = dalle(prompt)
    return image_url
    

def image_generator(story):
    """
    adds image to each section 

    1. image for first section is always going to be dalle generated 
    2. randomly pick five sections from the remaining 2-10
    3. iterate over each section and check if its selected section if yes check if its possible to take image from wikipedia, if no make image gen
    4. otherwise make image gen
    """
    image_urls=[]
    random_sections = random.sample(story[1:], 5)
    for line in story:
        #if first line than call generate_first_image function
        if line == story[0]:
            image_url = generate_first_image(line)
            image_urls.append(image_url)
        #if line is in random_sections, call wikipedia.find_image_for_story_section
        elif line in random_sections:
            #returns image url or None 
            image_url = wikipedia.find_image_for_story_section(line)
            if image_url == "no images found":
                image_url = generate_image(line)
            image_urls.append(image_url)
        #otherwise call generate_image function
        else:
            image_url = generate_image(line)
            image_urls.append(image_url)
    return image_urls

def html_converter(title, sections, image_urls, categories):
    """
    Converts the story into fully functional html ready to be rendered in the browser containing images and everything
    """
    with open('story.html', 'w') as f:
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<style>\n')
        f.write('.section, .categories { font-size: 15px; font-weight: normal; }\n')
        f.write('</style>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write(f"<h1><strong>{title}</strong></h1>\n")
        f.write(f'<h3 class="categories"><em>Categories: {categories}</em></h3>\n')
        for section, image_url in zip(sections, image_urls):
            f.write(f'<div class="section">\n')
            f.write(f"<p>{section}</p>\n")
            f.write(f'<img src="{image_url}" alt="Image for {section}" width="256" height="256">\n')
            f.write('</div>\n')
        f.write('</body>\n')
        f.write('</html>\n')

if __name__ == "__main__":
    story()

    