import psycopg2
con = psycopg2.connect(database="postgres", user = "postgres", password = "6978", host = "localhost", port = "5432")
cur=con.cursor()
# create a table
cur.execute('''CREATE TABLE DICTIONARY(
        ID SERIAL PRIMARY KEY,
        WORD  VARCHAR(30) NOT NULL,
        PART_OF_SPEACH TEXT NOT NULL,
        DEFINITION VARCHAR(200) NOT NULL);''')
# create a sequence for the primary key
cur.execute('CREATE SEQUENCE DICTIONARY_ID_SEQUENCE start 1 increment 1;')

con.commit()
con.close()
