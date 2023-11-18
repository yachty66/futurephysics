# glorious_future_bot

The aim of the bot is to create scenarious of really ambitious projects which are still in the realm of physics similar to what https://hieroglyph.asu.edu/2015/08/hieroglyph-anthology-recognized-by-association-of-professional-futurists/ is doing BUT each story is entirely created by AI, this includes the text and images. Challenges

- find a way to make the AI creative and not only have the AI create similar scenarious
    - a way how this could be done is to have some kind of big database where the AI is retrieving information from to create its scenarious (wikipedia)
- create scenarious which are only possible in the realm of physics!

some examples for twitter threads:

- https://x.com/BenjaminDEKR/status/1723173630966907175?s=20
- https://x.com/codyaims/status/1723206795316121969?s=20
- https://x.com/granawkins/status/1723146302920577145?s=20
- https://x.com/viennahypertext/status/1681077864626630657?s=20
- https://promptbase.com/prompt/futuristic-business-model-intodays-world
- https://promptbase.com/prompt/factory-of-the-future-storyboarding

## brainstorming

how could the connection to wikipedia look like? it could take existing projects and than use them for making up stories. 

i feel like its only a matter of lacking missing data

below each section should be a mix of images, i.e. 50% image gen and 50% taken from wikipedia. need to find realistic looking images given the scenario. 

## prompts:

### first prompt:

I want you to be my cowriter on innovative and ambitious future ideas which are still in the realm of physics so that its not unrealistic that something like this exists. Following and exampl of such and scenario:

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

The example was about an innovative school concept. There are no limits for which areas you can create the concept for. I will provide you with a few categories which should be involved in the concept and you should create the concept from there. please focus on the science aspects and that its in the realm of phyisics.


### Second prompt:

User
the categories are: computer simulations, gold, mining. dont focus on to many different concepts but rather narrow it down a bit and make sure to focus on physics. please go ahead and write the short story based on this categories. the structure of the story should be as following:

---
Title: [title]
Year: [year]

[first section] should contain around 280 characters

[second section] should contain around 280 characters

... (for me to shorten it. you should write out all 10 sections)

[tenth section] should contain around 280 characters
--- 

## image generation 

### image gen

given the following short story. please create images for section 1, [four other randomly selected sections].

--- 
last response
---

### wikipedia

- extract and than search keywords
- make query for gifs at https://commons.wikimedia.org/wiki/Main_Page
    - this is still a good question how i can get here good results for
- could also try to use simulations from https://phet.colorado.edu/en/simulations/browse (but not so many available)
- i can take each wikipedia portal and from each portal the topics as possible space of options for categories in the story creation
    - i can also just use a llm for creating these 
    - need at least one thousand topics 


## todos 

- make gen ai images smaller - 
- improve prompt system so that its more similar to https://x.com/codyaims/status/1723206795316121969?s=20 -
    - should be less a story but more a excursion - 
    - make year vary a bit - 
- improve image selection from wikipedia 
    - [x] make a dataset with around 300 lines of categories in a text file
    - [x] make a optional parameter for if categories should be taken from dataset or if taken from user
    - [x] make a test run
- python package so that people can super easy create their own future stories


- super simple page (framer) where every day a new story is created 
    - on top of the website is a support work link where people can order a colorful printed book 
- setup my account in a way that i tweet every day a link to a story
- share in AGI house slack channel research hackathon 
- share with people from tweets above