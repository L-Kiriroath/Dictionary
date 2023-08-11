import psycopg2
con=psycopg2.connect(database='postgres',user='postgres',password='6978',host='localhost',port='5432')
cur=con.cursor()
def get_input():
    inp=input('''Welcome to your personal dictionary
You can view the dictionary by typing "view"
You can add word to the dictionary by typing "add"
You can quot the dictionary by typing "quit"
: ''')
    return inp

def view_dictionary():
    cur.execute("  SELECT * FROM DICTIONARY ORDER BY WORD ASC;")
    print('\n')
    row=cur.fetchall()
    j=1
    for i in row:
        print(f"{j}. {i[1]} ({i[2]}) {i[3]}")
        j+=1
    print('\n')

def pospe(pos=""):
    global posp
    pos=input("Tyep N for Noun, ADJ for Adjective, AV for Adverb, \nV for Verb, PREP for Preposition, Pro for Pronouns, \nCON for Conjunction, IN for Injection \n\nPart of speach: ")
    if pos.upper()== "N":
        posp="Noun"
    elif pos.upper()== "ADJ":
        posp="Adjective"
    elif pos.upper()== "AV":
        posp="Adverb"
    elif pos.upper()== "V":
        posp="Verb"
    elif pos.upper()== "Pro":
        posp="APronouns"
    elif pos.upper()== "CON":
        posp="Conjunction"
    elif pos.upper()== "IN":
        posp="Injection"
    else:
        print('Wrong input')
        pospe()
    return posp

def add_word(word="",pos="",definition=""):
    word = input('word: ').capitalize()
    pos=pospe()
    definition=input("Definition: ").lower()
    cur.execute(f'''INSERT INTO DICTIONARY(ID, WORD, PART_OF_SPEACH, DEFINITION) VALUES(NEXTVAL('DICTIONARY_ID_SEQUENCE'), '{word}', '{pos}', '{definition}');''')
    con.commit()
    print("Insert successfully")
    print(word,f'({pos})',definition,'\n')

while True:
    inp = get_input()
    if inp.lower()=="view":
        view_dictionary()
    elif inp.lower()=="add":
        add_word()
    elif inp.lower()=="quit":
        con.close()
        break
    else:
        print('wrong input')

