# futurephysics

futurephysics is a Python package that generates stories about future concepts that are not to far fetched, i.e. concepts should be possible to be implemented. It uses OpenAI's GPT-4, DALL-E models and Wikipedia to generate the story and corresponding images.

## Background

It's great to have all these creative tools. One efficient way to use them is to create glorious visions of humanity's future, which will probably be powered by technology. I am a big fan of the [Project Hieroglyph](https://en.wikipedia.org/wiki/Project_Hieroglyph), an initiative of the University of Arizona. This initiative can be best explained by quoting from Wikipedia: "an initiative to create science fiction in order to spur innovation in science and technology." The goal of this repository and the easy-to-use Python package is to replicate this project but with generative AI and Wikipedia. I've also seen a few tweets where people tried to create visionary concepts with AI in Twitter threads:

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
```

The `html` variable contains the story formatted as HTML. 

You can also provide your own list of three categories with which the story gets drafted:

```python
from futurephysics import story

#Replace 'your-openai-api-key' with your actual OpenAI API key
openai_api_key = 'your-openai-api-key'

#Generate a story
html = story(openai_api_key, categories=["Computational archaeology", "Cosmogony", "Plants"])
```
 
The story is generated based on these categories.

Since the Dalle3 API is used, the returned image URLs expire after a while. You can provide details to your Google bucket for hosting images (the bucket needs to be public for this):

```python
from futurephysics import story

#Replace 'your-openai-api-key' with your actual OpenAI API key
openai_api_key = 'your-openai-api-key'

#Generate a story
html = story(openai_api_key, google_id="your-google-id", google_bucket="your-google-id")
```

## Contributing

If you run into any issues, the most helpful thing you can do is open an issue on [GitHub](https://github.com/yachty66/futurephysics). Thank you so much!

## Roadmap

- [ ] Improve image selection from Wikipedia 
- [ ] Improve image generation via DALL-E
- [ ] Improve prompting

## License

This project is licensed under the [MIT License](LICENSE).