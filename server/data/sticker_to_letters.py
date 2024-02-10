from openai import OpenAI
from dotenv import load_dotenv

# -------------------
# This tries to extract the letters from a sticker.
# Results: if there are actual letters in the image, it works great,
#   but when a symbol looks like a letter for us, it does not recognize it.
#--------------------

# You need a .env file with OPENAI_API_KEY
load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What letters are visible in this image? Your answer is python-compatible: you either answer the letters or your answer None. The letters may be an image that looks like a letter, like a banana that looks like a c."},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/stickers/community02/ctbanana_large.bd0d0ae817c8f86b70c9041b6fb2c9fb5af1118a.png",
            "detail": "high",
          },
        },
      ],
    }
  ],
  max_tokens=200,
)

print(response.choices[0])