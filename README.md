# futurephysics

futurephysics is a Python package that generates stories about future concepts that are not to far fetched, i.e. concepts should be possible to be implemented. It uses OpenAI's GPT-4, DALL-E models and Wikipedia to generate the story and corresponding images.

## background

its great to have now all this creative tools, one way to use them efficient is to create glorious futures of humanity which will be probably powered by technology. the author is a big fan of the [project hieroglyph](https://en.wikipedia.org/wiki/Project_Hieroglyph) which is a initiative of the university arizona which can be best explained by qouting from wikipedia "initiative to create science fiction in order to spur innovation in science and technology founded". this repository and the easy usable python packages goal is it to replicate this project but with generative AI Wikipedia. I also saw a few tweets where people tried to create visionary concepts with AI in twitter threads:


- [Skill Factory](https://x.com/codyaims/status/1723206795316121969?s=20)
- [3d printing trees should be easier than meat?](https://x.com/granawkins/status/1723146302920577145?s=20)
- [Vienna expands into Antarctic GPU farms](https://x.com/viennahypertext/status/1681077864626630657?s=20)
- [InventBot](https://x.com/BenjaminDEKR/status/1723173630966907175?s=20)

## Installation

You can install futurephysics from PyPI:

```bash
pip install futurephysics
```

## Usage

Here's a basic example of how to use futurephysics:

```python
from futurephysics import story

#Replace 'your-openai-api-key' with your actual OpenAI API key
openai_api_key = 'your-openai-api-key'

#Generate a story
html = story(openai_api_key)

#The 'html' variable now contains the HTML string of your generated story
```

You can also provide your own list of categories with which the story gets drafted:

```python
from futurephysics import story

#Replace 'your-openai-api-key' with your actual OpenAI API key
openai_api_key = 'your-openai-api-key'

#Generate a story
html = story(openai_api_key, )

#The 'html' variable now contains the HTML string of your generated story
```

## Contributing

If you run into any issue the most helpful you can do is opening a issue in [GitHub](https://github.com/yachty66/futurephysics). Thank you so much!

## Roadmap

- [ ] improve image selection from wikipedia 
- [ ] improve image gen via dalle
- [ ] improve prompting

## License

This project is licensed under the [MIT License](LICENSE).




## todos

- [ ] upload images into google bucket
- [ ] adjust readme
- [ ] generate 50 stories
- [ ] put them on to framer website
- [ ] make framer pretty 
- [ ] launch 