# Personal_dictionary
This project aims to create a dictionary platform personalized to you. 

## 1. Project Description
The project takes user input theough the terminal. Currently, you are able to add words, part of speach, and definition, and you can view those words which is arranged alphabetically.
- This project uses postgres as a datbase to store your words 
- It uses a while loop which means that it will run until the user tell it to stop

## 2. How to Install and Run the Project
1. install postgres and psycopg2 in your machine before running this program
link to installation guide: [How to Run PostgreSQL in Visual Studio Code](https://youtu.be/QLsDKboLxjU)
2. run the Dict_DB code once to innitialize the database 
3. run the Dictionary code to use the app

## 3. How to Use the Dictionary
### 1. the user will be greeted with a menu 
'''
Welcome to your personal dictionary
You can view the dictionary by typing "view"
You can add word to the dictionary by typing "add"
You can quot the dictionary by typing "quit"
: *your input here*
'''
### 2. the option view will show your whole dictionary
'''
 *view*


1. Able (Adjective) having the power, skill, means, or opportunity to do something
2. Apple (Noun) a tree fruit with a red skin and sweet taste
3. Car (Noun) wheeled four wheel passenger vehicle that carries its own motor
4. Drink (Verb) the action of consuming water
'''


### 3. the add option will let you add words and it's definition and part of speach
'''
 *add*
word:
Tyep N for Noun, ADJ for Adjective, AV for Adverb, V for Verb, PREP for Preposition, Pro for Pronouns, CON for Conjunction, IN for Injection

Part of speach: v
Definition: the action of consuming water
Insert successfully
Drink (Verb) the action of consuming water
'''

### 4. The quit option will break the loop and stop the program
'''
 *quit*
PS D:\python>
'''
