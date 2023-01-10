# Packages
import wikipedia as wiki
import openai
import os
import datetime
import time

# Key
openai.api_key = ("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")

# Functions
CC = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
now = datetime.datetime.now()

# Main
def main():
  CC()
  user_prompt = input("Prompt: ")
  response = openai.Image.create(
  prompt=user_prompt,
  n=1,
  size="1024x1024")
  image_url = response['data'][0]['url']
  print(image_url)
  time.sleep(4)

  
