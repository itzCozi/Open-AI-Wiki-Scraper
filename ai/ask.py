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
  q = input("Question: ")
  response = openai.Completion.create(model="text-davinci-002", prompt=(q), temperature=0, max_tokens=40)
  print(response)
  time.sleep(4)

  