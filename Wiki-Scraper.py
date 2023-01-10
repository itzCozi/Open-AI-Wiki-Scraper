# A wiki scraper with bulit in open AI communication for questions

# Packages
import wikipedia as wiki
import openai
import os
import datetime
import time
from colorama import Fore, Style

# Functions
CC = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
now = datetime.datetime.now()

# Key
openai.api_key = ("YOUR_API_KEY")

# Variables
lang = "en"
pg = wiki.page

# Menu
def menu():
  CC()
  print(Fore.GREEN+"______Welcome to the WikiScraper!______")
  print('''
  1. Search for a article
  2. Commands
  3. OpenAI
  4. Change Lang
  5. Exit
  ''')
  men_opt = input("What would you like to do? "+Fore.BLUE)
  if men_opt == "1":
    search()
  if men_opt == "2":
    commands()
  if men_opt == "3":
    openai()
  if men_opt == '4':
    lang_opt = input("What language would you like to use? ")
    if lang_opt == "en":
      lang = "en"
      wiki.set_lang("lang")
      print(Fore.GREEN+"Language changed to English")
      time.sleep(3)
      CC()
      menu()
    if lang_opt == "ru":
      lang = "ru"
      wiki.set_lang("lang")
      print(Fore.GREEN+"Language changed to Russian")
      time.sleep(3)
      CC()
      menu()
    if lang_opt == "es":
      lang = "es"
      wiki.set_lang("lang")
      print(Fore.GREEN+"Language changed to Spanish")
      time.sleep(3)
      CC()
      menu()
    if lang_opt == "de":
      lang = "de"
      wiki.set_lang("lang")
      print(Fore.GREEN+"Language changed to German")
      time.sleep(3)
      CC()
      menu()
    if lang_opt == "it":
      lang = "it"
      wiki.set_lang("lang")
      print(Fore.GREEN+"Language changed to Italian")
      time.sleep(3)
      CC()
      menu()
  if men_opt == "5":
    print(Fore.GREEN+"Goodbye!")
    time.sleep(3)
    quit()
  else:
      print(Fore.RED+"Language not supported")
      time.sleep(3)
      CC()
      menu()

# Search
def search():
  CC()
  print(Fore.GREEN+"______Searching for an article______")
  art_opt = input("What are you looking for? ")
  print(wiki.search(art_opt))
  print("Wiki Suggests")
  print(wiki.suggest(art_opt))
  user_command = input("Enter Command: ")
  if user_command == "sum":
    print(wiki.summary(art_opt))
    input("Press enter to continue...")
    search()
  if user_command == "title":
    print(pg.title)
    input("Press enter to continue...")
    search()
  if user_command == "url":
    print(pg.url)
    input("Press enter to continue...")
    search()
  if user_command == "full":
    print(pg.content)
    input("Press enter to continue...")
    search()
  if user_command == "img":
    print(pg.images)
    input("Press enter to continue...")
    search()
  if user_command == "links":
    print(pg.links)
    input("Press enter to continue...")
    search()
  if user_command == "search":
    print("---------------------")
    new_serch = input(Fore.RED+"What are you looking for? ")
    print(wiki.search(new_serch))
    input("Press enter to continue...")
    search()
  else:
    print(Fore.RED+"Command not found")
    time.sleep(3)
    search()

# Commands
def commands():
  CC()
  print(Fore.GREEN+"______Commands______")
  print('''
    1. sum (Prints the summary))
    2. title (Prints the title of the page))
    3. url (Prints the url of the page)))
    4. full (Prints the full text of the page)))
    5. img (Prints the images of the page)))
    6. links (Prints the links of the page)))
    ''')
  input("Press enter to exit...")
  time.sleep(3)
  menu()

# OpenAI
def openai():
  CC()
  print(Fore.GREEN+"______OpenAI______")
  print('''
  1. Ask a question
  2. Correct text
  3. Image generator
  4. Back
  ''')
  ai_opt = input("Option: ")
  if ai_opt == "1":
    from ai import ask as ask_ai
    ask_ai.main()
  if ai_opt == "2":
    from ai import correct as correct_ai
    correct_ai.main()
  if ai_opt == "3":
    from ai import image_gen as image_gen_ai
    image_gen_ai.main()
  if ai_opt == "4":
    menu()
  else: 
    print(Fore.RED+"Command not found")
    time.sleep(3)
    openai()
  
    
# Start
menu()
  
