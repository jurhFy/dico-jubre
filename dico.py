import sqlite3

with open('C:/Users/yaMonPrenomIci/Desktop/dico/dico.txt', 'r', encoding='utf-8') as f:
    contenu = f.readlines()

jubre = []
trad = []

for ligne in contenu:
    mots = ligne.split()
    if len(mots) == 2:
        jubre.append(mots[0])
        trad.append(mots[1])

conn = sqlite3.connect('dico.db', detect_types=sqlite3.PARSE_COLNAMES, uri=True)

curseur = conn.cursor()
curseur.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='trans' ''')
if curseur.fetchone()[0] == 0:

    conn.execute('''CREATE TABLE trans (jubre TEXT, trad TEXT)''')

    for i in range(len(jubre)):
        conn.execute("INSERT INTO trans (jubre, trad) VALUES (?, ?)", (jubre[i], trad[i]))

else:
    conn.execute('''DELETE FROM trans''')

    for i in range(len(jubre)):
        conn.execute("INSERT INTO trans (jubre, trad) VALUES (?, ?)", (jubre[i], trad[i]))

curseur.execute("SELECT * FROM trans")

for row in curseur.fetchall():
    print(row)

conn.commit()
conn.close()