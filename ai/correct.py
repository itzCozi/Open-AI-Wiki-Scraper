# Packages
import wikipedia as wiki
import openai
import os
import datetime
import time

# Key
openai.api_key = ("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)

# Functions
CC = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
now = datetime.datetime.now()

# Main
def main():
  CC()
  sen = input("Enter some text: ")
  response = openai.Edit.create(
  model="text-davinci-edit-001",
  input= sen,
  instruction="Fix the spelling mistakes and punctuation and capitalization and the grammar.",
  )
  print(response)
  time.sleep(4)
  quit()