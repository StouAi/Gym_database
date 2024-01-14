import sqlite3
import datetime
from datetime import datetime as dt


name_of_file = 'gym_final.db'

def print_omadiko():    
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM OMADIKO_PROGRAMMA""")
    res = cursor.fetchall()
    for programma in res:
        print(programma)

def print_gymnastis():
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM GYMNASTIS""")
    res = cursor.fetchall()
    for gymnastis in res:
        print(gymnastis)

def print_ranteboy():
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM RANTEBOY""")
    res = cursor.fetchall()
    for ranteboy in res:
        print(ranteboy)

def print_programma_gymnasthriou():    
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM PROGRAMA_GYMNASTIRIOU""")
    res = cursor.fetchall()
    for programma in res:
        print(programma)

def print_syndromi():    
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM SYNDROMI""")
    res = cursor.fetchall()
    for syndromi in res:
        print(syndromi)

def print_exoplismos():    
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM EXOPLISMOS""")
    res = cursor.fetchall()
    for exopl in res:
        print(exopl)

def print_melos():    
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM MELOS""")
    res = cursor.fetchall()
    for melos in res:
        print(melos)

def print_gym():
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM GYMNASTIRIO""")
    res = cursor.fetchall()
    for gym in res:
        print(gym)

def print_active_members():
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    cursor.execute("""SELECT MELOS.kwdikos_melous, onomateponimo, kwdikos_syndromis FROM SYNDROMI join MELOS on SYNDROMI.kwdikos_melous = MELOS.kwdikos_melous
                   WHERE SYNDROMI.hmerominia_lixis >= DATE('now')""")
    results = cursor.fetchall()
    if (results):
        for result in results:
            kwdikos_melous, onomateponimo, kwdikos_syndromis = result
            print(f"Κωδικός Μέλους: {kwdikos_melous}, Ονοματεπώνυμο: {onomateponimo}, Κωδικός Συνδρομής: {kwdikos_syndromis}")


def print_members_who_take_part_in_team_programms():
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    cursor.execute("""SELECT MELOS.kwdikos_melous, onomateponimo, OMADIKO_PROGRAMMA.kwdikos_omadikou, SYMMETEXEI.kostos, OMADIKO_PROGRAMMA.hmerominia
                   FROM MELOS join SYMMETEXEI on MELOS.kwdikos_melous = SYMMETEXEI.kwdikos_melous 
                   join OMADIKO_PROGRAMMA on OMADIKO_PROGRAMMA.kwdikos_omadikou = SYMMETEXEI.kwdikos_omadikou
                   """)
    results = cursor.fetchall()
    if (results):
        for result in results:
            kwdikos_melous, onomateponimo, kwdikos_omadikou, kostos, hmerominia = result
            print(f"Κωδικός Μέλους: {kwdikos_melous}, Ονοματεπώνυμο: {onomateponimo}, Κωδικός Ομαδικού: {kwdikos_omadikou}, Κόστος για το Μέλος: {kostos}, Ημερομηνία Προγράμματος: {hmerominia}")


def print_future_appointments():
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    cursor.execute("""SELECT kwdikos_ranteboy, hmerominia, ora_enarxis, tr_afm, kwdikos_melous
                   FROM RANTEBOY
                   WHERE hmerominia >= DATE('now')""")
    results = cursor.fetchall()
    if (results):
        for result in results:
            kwdikos_rant, date, start_time, afm, kwd_melous = result
            print(f"Κωδικός Ραντεβού: {kwdikos_rant}, Ημερομηνία: {date}, 'Ωρα έναρξης: {start_time}, ΑΦΜ Γυμναστή: {afm}, Κωδικός Μέλους που Συμμετέχει: {kwd_melous}")

def print_exoplismos_for_category(category):
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    cursor.execute("""SELECT onoma FROM EXOPLISMOS WHERE muikh_omada = ?""", (category, ))
    results = cursor.fetchall()
    if (results):
        for result in results:
            print(f"Εξοπλισμός: {result[0]}")
