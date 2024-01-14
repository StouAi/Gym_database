import sqlite3
import datetime
from datetime import datetime as dt
import database_queries


name_of_file = 'gym_final.db'


# First Drop Menu
def choice():
    print("\nΘα θέλατε να εισάγετε, να διαγράψετε ή να αλλάξετε πληροφορίες; \n")
    print("1: Εισαγωγή πληροφοριών\n2: Διαγραφή πληροφοριών\n3: Τροποποίηση πληροφοριών\n4: Εκτύπωση Πληροφοριών\n5: Έξοδος")
    choice = int(input("Πληκτρολογήστε τον αντίστοιχο αριθμό: "))
    return choice


# Drop Menu για Insert
def starting_menu():
    print("Σε ποιο table θέλετε να εισάγετε πληροφορίες;")
    print("1: ΓΥΜΝΑΣΤΗΡΙΟ \n2: ΓΥΜΝΑΣΤΗΣ \n3: ΟΜΑΔΙΚΟ ΠΡΟΓΡΑΜΜΑ \n4: PERSONAL TRAINING \n5: ΡΑΝΤΕΒΟΥ \n6: ΠΡΟΓΡΑΜΜΑ ΓΥΜΝΑΣΤΗΡΙΟΥ \n7: ΜΕΛΟΣ \n8: ΣΥΝΔΡΟΜΗ \n9: ΕΞΟΠΛΙΣΜΟΣ")

# Επιλογή table για insert
def choose_table(i):
    if (i == 1):
        print("Επιλέξατε το table ΓΥΜΝΑΣΤΗΡΙΟ")
        print("""Πληκτρολογήστε τις κατάλληλες πληροφορίες:
              1) Διεύθυνση
              2) Τηλέφωνο""")
        insert_gymnasthrio()
    if (i == 2):
        print("Επιλέξατε το table ΓΥΜΝΑΣΤΗΣ")   
        print("""Πληκτρολογήστε τις κατάλληλες πληροφορίες: 
            1) ΑΦΜ 
            2) Μισθός (σε αριθμό)
            3) Ονοματεπώνυμο
            4) Κωδικός Γυμναστηρίου
            5) Μέρες Εργασίας (Πχ Monday Thursday Friday)
            6) Ώρα έναρξης εργασίας (HH-MM-SS)
            7) Ώρα λήξης εργασίας (HH-MM-SS)
            8) Τηλέφωνο Γυμναστή""")
        insert_gymnastis()
    elif (i == 3):
        print("Επιλέξατε το table ΟΜΑΔΙΚΟ ΠΡΟΓΡΑΜΜΑ")
        print("""Πληκτρολογήστε τις κατάλληλες πληροφορίες:
            1) Αίθουσα
            2) Όριο ατόμων
            3) Ημερομηνία (Σε μορφή YYYY-MM-DD)
            4) Όνομα του Ομαδικού
            5) Ώρα Έναρξης
            6) Ώρα Λήξης
            7) Κωδικός Γυμναστηρίου που διωργανώνεται""")  
        insert_omadiko()
    elif (i == 4):
        print("Επιλέξατε το table PERSONAL TRAINING \n")
        condition = int(input("Υπάρχει ραντεβού για το αντίστοιχο Personal Training Session? (1 = NAI, 2 = ΟΧΙ) \n"))
        if (condition == 1):
            print("Το Personal Training Session έχει δημιουργηθεί αυτόματα\n")  
        elif (condition == 2):
            print("Παρακαλώ δημιουργείστε πρώτα το αντίστοιχο ραντεβού, και θα δημιουργηθεί αυτόματα το Personal Training \n")
        else:
            print("Δώσσατε λαθος αριθμό")
    elif (i == 5):
        print("Επιλέξατε το table ΡΑΝΤΕΒΟΥ")
        print("""Πληκτρολογήστε τις κατάλληλες πληροφορίες:
              1) ΑΦΜ του γυμναστή που το επιβλέπει
              2) Κωδικός του μέλους που έχει κλείσει το ραντεβού
              3) Ημερομηνία (Σε μορφή YYYY-MM-DD)
              4) Ώρα Έναρξης
              5) Ώρα Λήξης""")
        insert_ranteboy()
    elif (i == 6):
        print("Επιλέξατε το table ΠΡΟΓΡΑΜΜΑ ΓΥΜΝΣΤΗΡΙΟΥ")
        print("""Πληκτρολογήστε τις κατάλληλες πληροφορίες:
              1) Στόχος Προγράμματος
              2) To AFM του γυμναστή που το έγραψε
              3) Τον κωδικό του μέλους που το ακολουθεί""")
        insert_programma_gymnasthrioy()
    elif (i == 7):
        print("Επιλέξατε το table ΜΕΛΟΣ")
        print("""Πληκτρολογήστε τις κατάλληλες πληροφορίες:
              1) Ονοματεπώνυμο
              2) Τηλέφωνο Μέλους""")
        insert_melos()
    elif (i == 8):
        print("Επιλέξατε το table ΣΥΝΔΡΟΜΗ")
        print("""Πληκτρολογήστε τις κατάλληλες πληροφορίες:
              1) Τιμή 
              2) Βαθμίδα
              3) Κωδικός γυμναστηρίου
              4) Ημερομηνία Έναρξης
              5) Ημερομηνία Λήξης
              6) Κωδικός Μέλους""")
        insert_syndromi()
    elif (i == 9):
        print("Επιλέξατε το table ΕΞΟΠΛΙΣΜΟΣ")
        print("""Πληκτρολογήστε τις κατάλληλες πληροφορίες:
              1) Όνομα
              2) Κωδικός Γυμναστηρίου που ανήκει
              3) Μυική Ομάδα που γυμνάζει
              4) Barcode του εξοπλισμού""")
        insert_exoplismos()
# Drop Table για Delete
def starting_menu_del():
    print("Σε ποιο table θέλετε να διαγράψετε πληροφορίες;")
    print("1: ΓΥΜΝΑΣΤΗΡΙΟ \n2: ΓΥΜΝΑΣΤΗΣ \n3: ΟΜΑΔΙΚΟ ΠΡΟΓΡΑΜΜΑ \n4: PERSONAL TRAINING \n5: ΡΑΝΤΕΒΟΥ \n6: ΠΡΟΓΡΑΜΜΑ ΓΥΜΝΑΣΤΗΡΙΟΥ \n7: ΜΕΛΟΣ \n8: ΣΥΝΔΡΟΜΗ \n9: ΕΞΟΠΛΙΣΜΟΣ")

# Επιλογή table για delete
def choose_table_delete(i):
    if (i == 1):
        print("Επιλέξατε το table ΓΥΜΝΑΣΤΗΡΙΟ")
        delete_gymnasthrio()
    if (i == 2):
        print("Επιλέξατε το table ΓΥΜΝΑΣΤΗΣ")   
        print("""Πληκτρολογήστε το ΑΦΜ του γυμναστή που θέλετε να διαγράψετε: """)
        delete_gymnastis()
    elif (i == 3):
        print("Επιλέξατε το table ΟΜΑΔΙΚΟ ΠΡΟΓΡΑΜΜΑ")
        print("""Πληκτρολογήστε τον Κωδικο Ομαδικού που θέλετε να διαγράψετε: """)
        kwd_omad = int(input())
        delete_omadiko(kwd_omad)
    elif (i == 4):
        print("Επιλέξατε το table PERSONAL TRAINING \n")
        print("Πληκτρολογήστε τον κωδικό του Personal Training που θέλετε να διαγράψετε: ")
        kwd_personal = int(input())
        delete_personal(kwd_personal)
    elif (i == 5):
        print("Επιλέξατε το table ΡΑΝΤΕΒΟΥ")
        print("Πληκτρολογήστε τον κωδικό του ραντεβού που θέλετε να διαγράψετε: ")
        kwd_rant = int(input())
        delete_ranteboy(kwd_rant)
    elif (i == 6):
        print("Επιλέξατε το table ΠΡΟΓΡΑΜΜΑ ΓΥΜΝΣΤΗΡΙΟΥ")
        kwd_progr = int(input("Πληκτρολογήστε τον κωδικό προγράμματος που θέλετε να διαγράψετε: "))
        delete_programma_gymnasthrioy(kwd_progr)
    elif (i == 7):
        print("Επιλέξατε το table ΜΕΛΟΣ")
        kwd_melous = int(input("Πληκτρολογήστε τον κωδικό μέλους που θέλετε να διαγράψετε: "))
        delete_melos(kwd_melous)
    elif (i == 8):
        print("Επιλέξατε το table ΣΥΝΔΡΟΜΗ")
        delete_syndromi()
    elif (i == 9):
        print("Επιλέξατε το table ΕΞΟΠΛΙΣΜΟΣ")
        delete_exopismos()

# Drop Menu update
def starting_menu_update():
    print("Σε ποιο table θέλετε να τροποποιήσετε πληροφορίες;")
    print("1: ΓΥΜΝΑΣΤΗΡΙΟ \n2: ΓΥΜΝΑΣΤΗΣ \n3: ΟΜΑΔΙΚΟ ΠΡΟΓΡΑΜΜΑ \n4: PERSONAL TRAINING \n5: ΡΑΝΤΕΒΟΥ \n6: ΠΡΟΓΡΑΜΜΑ ΓΥΜΝΑΣΤΗΡΙΟΥ \n7: ΜΕΛΟΣ \n8: ΣΥΝΔΡΟΜΗ \n9: ΕΞΟΠΛΙΣΜΟΣ")

# Table Choosing Update
def choose_table_update(i):
    if (i == 1):
        print("Επιλέξατε το table ΓΥΜΝΑΣΤΗΡΙΟ")
        update_gymnasthrio()
    if (i == 2):
        print("Επιλέξατε το table ΓΥΜΝΑΣΤΗΣ")
        print("""Πληκτρολογήστε το ΑΦΜ του γυμναστή που θέλετε να τροποποιήσετε: """)
        update_gymnastis()
    elif (i == 3):
        print("Επιλέξατε το table ΟΜΑΔΙΚΟ ΠΡΟΓΡΑΜΜΑ")
        print("Πληκτρολογήστε τον κωδικό ομαδικού προγραμματος που θέλετε να τροποποιήσετε: ")
        update_omadiko()
    elif (i == 4):
        print("Επιλέξατε το table PERSONAL TRAINING \n")
        print("Για να αλλάξετε τις τιμές ενός personal_training_session θα πρέπει να αλλάξουν πρώτα οι τιμές του αντίτοιχου ραντεβού! Παρακαλώ δοκιμάστε ξανά και πατήστε 4")
    elif (i == 5):
        print("Επιλέξατε το table ΡΑΝΤΕΒΟΥ")
        print("Πληκτρολογήστε τον κωδικό του ραντεβού που θέλετε να τροποποιήσετε: ")
        update_ranteboy()
    elif (i == 6):
        print("Επιλέξατε το table ΠΡΟΓΡΑΜΜΑ ΓΥΜΝΣΤΗΡΙΟΥ")
        print("Πληκτρολογήστε τον κωδικό προγράμματος που θέλετε να τροποποιήσετε: ")
        update_programa_gymnasthrioy()
    elif (i == 7):
        print("Επιλέξατε το table ΜΕΛΟΣ")
        print("Πληκτρολογήστε τον κωδικό μέλους που θέλετε να τροποποιήσετε: ")
        update_melos()
    elif (i == 8):
        print("Επιλέξατε το table ΣΥΝΔΡΟΜΗ")
        update_syndromi()
    elif (i == 9):
        print("Επιλέξατε το table ΕΞΟΠΛΙΣΜΟΣ")
        update_exoplismos()

def starting_menu_print():
    print("Ποια πληροφορία θα θέλατε να δείτε;")
    print("""1) Επιλογή εκτύπωσης όλων των τιμών από ένα table \n2) Επιλογή ενός προκαθορισμένου query""")
    
# Συναρτηση επιλογης εκτύπωσης δεδομένων
def choose_table_print_all():
    print("""Πληκτρολόγησε τον αντίστοιχο αριθμό:
          1) ΓΥΜΝΑΣΤΗΡΙΟ
          2) ΣΥΝΔΡΟΜΙ
          3) ΜΕΛΟΣ
          4) ΕΞΟΠΛΙΣΜΟΣ
          5) ΡΑΝΤΕΒΟΥ
          6) ΠΡΟΓΡΑΜΜΑ ΓΥΜΝΑΣΤΗΡΙΟΥ
          7) ΟΜΑΔΙΚΟ ΠΡΟΓΡΑΜΜΑ
          8) ΓΥΜΝΑΣΤΗΣ """)
    choice = int(input("Επέλεγε από ποιο table θές να δεις τις τιμές: "))
    if choice == 1:
        database_queries.print_gym()
    elif choice == 2:
        database_queries.print_syndromi()
    elif choice == 3:
        database_queries.print_melos()
    elif choice == 4:
        database_queries.print_exoplismos()
    elif choice == 5:
        database_queries.print_ranteboy()
    elif choice == 6:
        database_queries.print_programma_gymnasthriou()
    elif choice == 7:
        database_queries.print_omadiko()
    elif choice == 8:
        database_queries.print_gymnastis()
    else:
        print("Λάθος αριθμός")


def choose_query():
    print("""Πληκτρολόγησε τον αντίστοιχο αριθμό:
          1) Εμφάνιση ενεργών μελών και τον κωδικό της συνδρομής τους
          2) Εμφάνιση μελών που συμμετέχουν (τώρα ή παλιά) σε ομαδικά προγράμματα
          3) Εμφάνιση μελλοντικών ραντεβού
          4) Εμφάνιση εξοπλισμού σε κάποια μυική ομάδα""")
    choice = int(input("Επέλεξε το query: "))
    if (choice == 1):
        database_queries.print_active_members()
    if (choice == 2):
        database_queries.print_members_who_take_part_in_team_programms()
    if (choice == 3):
        database_queries.print_future_appointments()
    if (choice == 4):
        print("""Πληκτρολόγησε τον αντίστοιχο αριθμό:
          1) Στήθος
          2) Πλάτη
          3) Χέρια
          4) Πόδια""")
        choice_2 = int(input("Επέλεξε την ομάδα: "))
        if (choice_2 == 1):
            omada = 'Στήθος'
            if (check_for_category(omada)):
                database_queries.print_exoplismos_for_category(omada)
        if (choice_2 == 2):
            omada = 'Πλάτη'
            if (check_for_category(omada)):
                database_queries.print_exoplismos_for_category(omada)
        if (choice_2 == 3):
            omada = 'Χέρια'
            if (check_for_category(omada)):
                database_queries.print_exoplismos_for_category(omada)
        if (choice_2 == 4):
            omada = 'Πόδια'
            if (check_for_category(omada)):
                database_queries.print_exoplismos_for_category(omada)

# Συναρτηση insert στο ΓΥΜΝΑΣΤΗΡΙΟ
def insert_gymnasthrio():
    gym_adress = str(input("Δωστε τιμή για διευθυνση : "))
    gym_phone = str(input("Δωστε τιμή για τηλεφωνο : "))
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    cursor.execute('select max(kwdikos_gym) from GYMNASTIRIO')
    result = cursor.fetchone()
    if (result):
        gym_id = result[0] + 1
    else:
        gym_id = 1
    cursor.execute("INSERT INTO GYMNASTIRIO VALUES(?,?,?,?)",(gym_id,'GETFIT',gym_adress,gym_phone))
    conn.commit()
    conn.close()
    print("το ΓΥΜΝΑΣΤΗΡΙΟ προστεθηκε επιτυχως")

# Συναρτηση delete ΓΥΜΝΑΣΤΗΡΙΟ
def delete_gymnasthrio():
    gym_id = int(input("Βαλε τον κωδικο του ΓΥΜΝΑΣΤΗΡΙΟΥ: "))
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    conf = int(input("Θέλεις να διαγραψεις και ολες τις σχετικες οντοτητες? (1 = NAI 2 = OXI): "))
    if conf == 1:
        # for exomplismos
        cursor.execute("DELETE FROM KATEXEI WHERE kwdikos_gym = ?", (gym_id,))
        conn.commit()
        # FOR MELOI
        cursor.execute("select distinct kwdikos_melous from SYNDROMI where kwdikos_gym = ?", (gym_id,))
        meloi = cursor.fetchall()
        # cursor.execute("DELETE FROM SYNDROMI WHERE kwdikos_gym = ?", (gym_id,))
        conn.commit()
        if meloi != None:
            for melos in meloi:
                cursor.execute("DELETE FROM AKOLOYTHEI WHERE kwdikos_melous =?", (melos[0],))
                conn.commit()
                cursor.execute("DELETE FROM SYMMETEXEI WHERE kwdikos_melous = ?", (melos[0],))
                conn.commit()
                cursor.execute("DELETE FROM MELOS WHERE kwdikos_melous = ?", (melos[0],))
                conn.commit()
                cursor.execute("DELETE FROM SYNDROMI WHERE kwdikos_gym = ?", (gym_id,))
                conn.commit()
        # for gymnastes
        cursor.execute("select AFM from GYMNASTIS where kwdikos_gym = ?", (gym_id,))
        gymnastes = cursor.fetchall()
        if gymnastes != None:
            cursor.execute("DELETE FROM DIORGANONEI WHERE AFM IN (SELECT AFM FROM GYMNASTIS WHERE kwdikos_gym = ?)", (gym_id,))
            conn.commit()
            cursor.execute("DELETE FROM OMADIKO_PROGRAMMA WHERE kwdikos_gym = ?", (gym_id,))
            conn.commit()
            cursor.execute("select kwdikos_ranteboy from RANTEBOY WHERE tr_AFM IN (SELECT AFM FROM GYMNASTIS WHERE kwdikos_gym = ?)", (gym_id,))
            tr_rantevou = cursor.fetchall()

            if tr_rantevou != None:
                for tr_rantevou in tr_rantevou:
                    cursor.execute("DELETE FROM PERSONAL_TRAINING WHERE kwdikos_ranteboy = ?", (tr_rantevou[0],))
                    conn.commit()
                cursor.execute("DELETE FROM RANTEBOY WHERE tr_AFM IN (SELECT AFM FROM GYMNASTIS WHERE kwdikos_gym = ?)", (gym_id,))
                conn.commit()
            cursor.execute("select kwdikos_programmatos from GRAFEI where tr_AFM IN (SELECT AFM FROM GYMNASTIS WHERE kwdikos_gym = ?)", (gym_id,))
            program_codes = cursor.fetchall()
            if program_codes != None:
                for program_code in program_codes:
                    cursor.execute("DELETE FROM GRAFEI WHERE kwdikos_programmatos = ?", (program_codes[0],))
                    conn.commit()
                    cursor.execute("DELETE FROM PROGRAMA_GYMNASTIRIOU WHERE kwdikos_programmatos = ?", (program_codes[0],))
                    conn.commit()
        cursor.execute("DELETE FROM GYMNASTIS where kwdikos_gym= ?", (gym_id,))
        conn.commit()

    cursor.execute("DELETE FROM GYMNASTIRIO WHERE kwdikos_gym = ?", (gym_id,))
    conn.commit()
    conn.close()
    print("Το ΓΥΜΝΑΣΤΗΡΙΟ διαγράφηκε επιτυχώς")

# Συνάρτηση update στο ΓΥΜΝΑΣΤΗΡΙΟ
def update_gymnasthrio():
    gym_id = int(input("Εισαγετε τον κωδικο του ΓΥΜΝΑΣΤΗΡΙΟΥ: "))
    gym_adress=input("Εισαγετε νέα διευθυνση ή πατηστε Enter :")
    gym_phone = input("Εισαγετε νέο τηλεφωνο ή πατηστε Enter :")
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    if gym_adress and gym_phone:
        cursor.execute("UPDATE GYMNASTIRIO SET dieythinsi=?, tilefono=? WHERE kwdikos_gym=?", (gym_adress, gym_phone, gym_id))
    elif gym_adress:
        cursor.execute("UPDATE GYMNASTIRIO SET dieythinsi=? WHERE kwdikos_gym=?", (gym_adress, gym_id))
    elif gym_phone:
        cursor.execute("UPDATE GYMNASTIRIO SET tilefono=? WHERE kwdikos_gym=?", (gym_phone, gym_id))
    else:
        print("Δεν υπάρχει τίποτα για ενημέρωση")
    conn.commit()
    conn.close()
    print("Το ΓΥΜΝΑΣΤΗΡΙΟ ενημερώθηκε επιτυχώς")
    
# Συνάρτηση insert στον ΓΥΜΝΑΣΤΗ
def insert_gymnastis():
    afm = str(input("Δώστε τιμή για το ΑΦΜ: \n"))
    misthos = int(input("Δώστε τιμή για τον μισθό: \n"))
    onoma = str(input("Δώστε τιμή για το Ονοματεπώνυμο: \n"))
    kwd_gym = int(input("Σε ποιο γυμναστήριο δουλεύει (Δωστε τον κωδικο του αντιστοιχου γυμναστηριου) \n"))
    mer_ergasias = str(input("Δώστε τιμή για τις μέρες εργασίας: "))
    wra_enarjis = input("Τι ωρα ξεκινάει να δουλέυει; \n")
    wra_lijis = input("Τι ώρα τελειώνει την δουλειά; \n")
    tilefono = input("Ποιο ειναι το τηλεφωνο του; ")
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute(f"""INSERT INTO GYMNASTIS VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (afm, misthos, onoma, kwd_gym, mer_ergasias, wra_enarjis, wra_lijis, tilefono))
    connection.commit()

    option = int(input("Θα θέλατε να τυπώσετε τους γυμναστές;(1 = ΝΑΙ 2 = ΟΧΙ) "))
    if (option == 1):
        database_queries.print_gymnastis()

# Συνάρτηση DELETE ston GYMNASTI
def delete_gymnastis():
    valid_rant = None  # Initialize valid_rant before the if statement
    current_date = datetime.date.today()
    afm = str(input())
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute("SELECT kwdikos_ranteboy FROM RANTEBOY WHERE tr_afm = ?", (afm, ))
    ranteboy_res = cursor.fetchall()
    cursor.execute("SELECT hmerominia FROM RANTEBOY WHERE tr_afm =?", (afm, ))
    date_rant = cursor.fetchall()
    cursor.execute("""SELECT OMADIKO_PROGRAMMA.kwdikos_omadikou FROM OMADIKO_PROGRAMMA join DIORGANONEI on DIORGANONEI.kwdikos_omadikou = OMADIKO_PROGRAMMA.kwdikos_omadikou
                   WHERE DIORGANONEI.AFM = ?""", (afm, ))
    omadiko_res = cursor.fetchall()
    cursor.execute("""SELECT PROGRAMA_GYMNASTIRIOU.kwdikos_programmatos FROM PROGRAMA_GYMNASTIRIOU join GRAFEI on PROGRAMA_GYMNASTIRIOU.kwdikos_programmatos = GRAFEI.kwdikos_programmatos
                   WHERE GRAFEI.tr_AFM = ?""", (afm, ))
    programma_res = cursor.fetchall()
    cursor.execute("DELETE FROM GYMNASTIS WHERE AFM = ?",(afm,))
    connection.commit()
    # connection.close()
    print(f"Ο γυμναστής με AFM = {afm} διαγράφηκε επιτυχώς!")
    if (ranteboy_res):
        for date in date_rant:
            if (date[0] > str(current_date)):
                cursor.execute("SELECT kwdikos_ranteboy FROM RANTEBOY WHERE tr_afm = ? AND hmerominia = ?", (afm, date[0]))
                valid_rant = cursor.fetchall()
    if (valid_rant):
        print("Ο Γυμναστής αυτός είχε τα ακόλουθα μελλοντικά ραντεβού με κωδικούς: ")
        for rant in valid_rant:
            print(rant)
        choice = int(input("Θα θέλατε να τα διαγράψετε; (1 = ΝΑΙ 2 = ΟΧΙ)"))
        if (choice == 1):
            for rant in valid_rant:
                delete_ranteboy(int(rant[0]))
        if (choice == 2):
            print("Επιλέξατε να μην τα διαγράψετε")
    if (omadiko_res):
        print("Ο Γυμναστής διοργανώνει τα ακόλουθα ομαδικά προγράμματα με κωδικούς: ")
        for omadiko in omadiko_res:
            print(omadiko)
        choice = int(input("Θα θέλατε να τα διαγράψετε; (1 = ΝΑΙ 2 = ΟΧΙ)"))
        if (choice == 1):
            for omadiko in omadiko_res:
                delete_omadiko(int(omadiko[0]))
        if (choice == 2):
            print("Επιλέξατε να μην τα διαγράψετε")
    if (programma_res):
        print("Ο Γυμναστής είναι υπεύθυνος για τα ακόλουθα προγράμματα γυμναστηρίου με κωδικούς: ")
        for programma in programma_res:
            print(programma)
        choice = int(input("Θα θέλατε να τα διαγράψετε; (1 = ΝΑΙ 2 = ΟΧΙ)"))
        if (choice == 1):
            for programma in programma_res:
                delete_programma_gymnasthrioy(int(programma[0]))
        if (choice == 2):
            print("Επιλέξατε να μην τα διαγράψετε")

# Συνάρτηση ενημέρωσης τιμών γυμναστή
def update_gymnastis():
    afm = str(input())
    misthos_input = input("Πληκτρολογήστε τον νέο μισθό ή πατήστε enter αν δεν θέλετε να τον αλλάξετε: ")
    onomateponimo_input = input("Πληκτρολογήστε το νέο ονοματεπώνυμο ή πατήστε enter αν δεν θέλετε να το αλλάξετε: ")
    kwdikos_gym_input = input("Πληκτρολογήστε το νέο κωδικό γυμναστηρίου που δουλεύει ή πατήστε enter αν δεν θέλετε να τον αλλάξετε: ")
    meres_ergasias_input = input("Πληκτρολογήστε τις νέες μέρες εργασίας ή πατήστε enter αν δεν θέλετε να τις αλλάξετε (Αγγλικοί όροι, χωρισμένοι με κενό): ")
    ora_enrajis_input = input("Πληκτρολογήστε την νέα ώρα έναρξης ωραρίου (hh-mm-ss) ή πατήστε enter αν δεν θέλετε να την αλλάξετε: ")
    ora_lijis_input = input("Πληκτρολογήστε την νέα ώρα λήξης ωραρίου (hh-mm-ss) ή πατήστε enter αν δεν θέλετε να την αλλάξετε: ")
    tilefono_input = input("Πληκτρολογήστε το νέο τηλεφωνο του γυμναστή ή πατήστε enter αν δεν θέλετε να το αλλάξετε: ")

    # Convert input to appropriate types or set to None if empty
    misthos = float(misthos_input) if misthos_input else None
    onomateponimo = onomateponimo_input if onomateponimo_input else None
    kwdikos_gym = int(kwdikos_gym_input) if kwdikos_gym_input else None
    meres_ergasias = meres_ergasias_input if meres_ergasias_input else None
    ora_enrajis = ora_enrajis_input if ora_enrajis_input else None
    ora_lijis = ora_lijis_input if ora_lijis_input else None
    tilefono_input = tilefono_input if tilefono_input else None

    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    if misthos:
        cursor.execute("UPDATE GYMNASTIS SET misthos = ? WHERE AFM = ?", (misthos, afm))
    if onomateponimo:
        cursor.execute("UPDATE GYMNASTIS SET onomateponimo = ? WHERE AFM = ?", (onomateponimo, afm))
    if kwdikos_gym:
        cursor.execute("UPDATE GYMNASTIS SET kwdikos_gym = ? WHERE AFM = ?", (kwdikos_gym, afm))
    if meres_ergasias:
        cursor.execute("UPDATE GYMNASTIS SET meres_ergasias = ? WHERE AFM = ?", (meres_ergasias, afm))
    if ora_enrajis:
        cursor.execute("UPDATE GYMNASTIS SET ora_enarxis = ? WHERE AFM = ?", (ora_enrajis, afm))
    if ora_lijis:
        cursor.execute("UPDATE GYMNASTIS SET ora_lixis = ? WHERE AFM = ?", (ora_lijis, afm))
    if tilefono_input:
        cursor.execute("UPDATE GYMNASTIS SET tilefono = ? WHERE AFM = ?", (tilefono_input, afm))
    print("Τα δεδομένα που επιλέξατε ενημερώθηκαν επιτυχώς!")
    conn.commit()
    conn.close()

# Συνάρτηση insert στο OMADIKO_PROGRAMMA
def insert_omadiko():
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute("SELECT kwdikos_omadikou FROM OMADIKO_PROGRAMMA ORDER BY kwdikos_omadikou DESC")
    kwd_omadikou = int(cursor.fetchone()[0])
    aithousa = str(input("Σε ποια αίθουσα διοργανώνεται; \n"))
    orio = int(input("Ποιο είναι το όριο ατόμων; \n"))
    hmeromhnia = input("Πότε διεξάγεται το πρόγραμμα; (Σε μορφή yyyy-mm-dd) \n")
    onoma = str(input("Πως λέγεται το πρόγραμμα; \n"))
    wra_enarjis = input("Τι ωρα ξεκινάει; \n")
    wra_lijis = input("Τι ώρα τελειώνει; \n")
    kwd_gym = int(input("Σε ποιο γυμναστήριο διοργανώνεται; (Δωστε τον κωδικο του αντιστοιχου γυμναστηριου) \n"))

    if (check_for_valid_omadiko(aithousa, hmeromhnia, wra_enarjis, wra_lijis)):
        print("Διεξάγεται άλλο πρόγραμμα στην συγκεκριμένη αίθουσα την ώρα αυτήν")
        return False
    else:
        afm = str(input("Ποιος γυμναστής διοργανώνει αυτό το πρόγραμμα; (Παρακαλώ πληκτρολογήστε το ΑΦΜ του) \n"))
        if (check_for_existing_trainer(afm) and check_for_working_hours(afm, hmeromhnia, wra_enarjis, wra_lijis)):
            cursor.execute(f"""INSERT INTO OMADIKO_PROGRAMMA VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (kwd_omadikou + 1, aithousa, orio, hmeromhnia, onoma, wra_enarjis, wra_lijis, kwd_gym, 1))
            cursor.execute(f"""INSERT INTO DIORGANONEI VALUES (?, ?)""", (afm, kwd_omadikou + 1))
            connection.commit()
        else: 
            print("Ο συγκεκριμένος γυμναστής δεν είναι διαθέσιμος αυτήν την ώρα")
            return False
    option = int(input("Θα θέλατε να τυπώσετε τα ομαδικά;(1 = ΝΑΙ 2 = ΟΧΙ) "))
    if (option == 1):
        database_queries.print_omadiko()

# Έλεγχος για διαθεσιμότητα ημερομηνίας ώρας για το ομαδικό 
def check_for_valid_omadiko(aithousa, hmeromhnia, ora_enarjis, ora_lijis):
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    query = """
    SELECT COUNT(*)
    FROM OMADIKO_PROGRAMMA
    WHERE aithousa = ?
    AND hmerominia = ?
    AND ((ora_enarxis >= ? AND ora_enarxis < ?)
        OR (ora_lixis > ? AND ora_lixis <= ?)
        OR (ora_enarxis <= ? AND ora_lixis >= ?));
    """
    cursor.execute(query, (aithousa, hmeromhnia, ora_enarjis, ora_lijis, ora_enarjis, ora_lijis, ora_enarjis, ora_lijis))
    result = cursor.fetchone()[0]
    return result
# Συναρτηση γι delete ομαδικου
def delete_omadiko(kwd_omad):
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM OMADIKO_PROGRAMMA WHERE kwdikos_omadikou = ?",(kwd_omad,))
    cursor.execute("DELETE FROM DIORGANONEI WHERE kwdikos_omadikou = ?", (kwd_omad, ))
    connection.commit()
    connection.close()
    print("Tα ομαδικά προγράμματα διαγράφηκαν επιτυχώς")

# Συναρτηση για ενημερωση ομαδικου
def update_omadiko():
    kwd_omad = int(input())
    aithousa = input("Πληκτρολογήστε την νέα αίθουσα ή πατήστε enter αν δεν θέλετε να την αλλάξετε: ")
    orio_atomon = input("Πληκτρολογήστε το νέο όριο ατόμων ή πατήστε enter αν δεν θέλετε να το αλλάξετε: ")
    hmerominia = input("Πληκτρολογήστε την νέα ημερομηνία (yyyy-mm-dd) ή πατήστε enter αν δεν θέλετε να την αλλάξετε: ")
    onoma = input("Πληκτρολογήστε το νέο όνομα ή πατήστε enter αν δεν θελετε να το αλλάξετε: ")
    ora_enarxis = input("Πληκτρολογήστε την νέα ώρα έναρξης (hh-mm-ss) ή πατήστε enter αν δεν θέλετε να την αλλάξετε: ")
    ora_lixis = input("Πληκτρολογήστε νέα ώρα λήξης (hh-mm-ss) ή πατήστε enter αν δεν θελετε να την αλλάξετε: ")
    afm = input("Πληκτρολογήστε το νέο ΑΦΜ του γυμναστή που το διοργανώνει ή πατήστε enter αν δεν θέλετε να το αλλάξετε: ")
    result_afm = None

    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    cursor.execute("SELECT ora_enarxis FROM OMADIKO_PROGRAMMA WHERE kwdikos_omadikou = ?", (kwd_omad, ))
    result = cursor.fetchone()
    if (result is not None):
        result_ora_enarxis = result[0]
    cursor.execute("SELECT ora_lixis FROM OMADIKO_PROGRAMMA WHERE kwdikos_omadikou = ?", (kwd_omad, ))
    result = cursor.fetchone()
    if (result is not None):
        result_ora_lixis = result[0]
    cursor.execute("SELECT AFM FROM DIORGANONEI WHERE kwdikos_omadikou = ?", (kwd_omad, ))
    result = cursor.fetchone()
    if (result is not None):
        result_afm = result[0]
    cursor.execute("SELECT hmerominia FROM OMADIKO_PROGRAMMA WHERE kwdikos_omadikou = ?", (kwd_omad, ))
    result = cursor.fetchone()
    if (result is not None):
        result_date = result[0]

    aithousa = aithousa if aithousa else None
    orio_atomon = int(orio_atomon) if orio_atomon else None
    hmerominia = hmerominia if hmerominia else result_date
    onoma = onoma if onoma else None
    ora_enarxis = ora_enarxis if ora_enarxis else result_ora_enarxis
    ora_lixis = ora_lixis if ora_lixis else result_ora_lixis
    if (result_afm):
        afm = afm if afm else result_afm
    else:
        afm = afm if afm else None

    if (afm):
        if (check_for_existing_trainer(afm)):
            if (check_for_working_hours(afm, hmerominia, ora_enarxis, ora_lixis)):
                if (aithousa):
                    cursor.execute("UPDATE OMADIKO_PROGRAMMA SET aithousa = ? WHERE kwdikos_omadikou = ?", (aithousa, kwd_omad))
                if (orio_atomon):
                    cursor.execute("UPDATE OMADIKO_PROGRAMMA SET orio_atomon = ? WHERE kwdikos_omadikou = ?", (orio_atomon, kwd_omad))
                cursor.execute("UPDATE OMADIKO_PROGRAMMA SET hmerominia = ? WHERE kwdikos_omadikou = ?", (hmerominia, kwd_omad))
                if (onoma):
                    cursor.execute("UPDATE OMADIKO_PROGRAMMA SET onoma = ? WHERE kwdikos_omadikou = ?", (onoma, kwd_omad))
                cursor.execute("UPDATE OMADIKO_PROGRAMMA SET ora_enarxis = ? WHERE kwdikos_omadikou = ?", (ora_enarxis, kwd_omad))
                cursor.execute("UPDATE OMADIKO_PROGRAMMA SET ora_lixis = ? WHERE kwdikos_omadikou = ?", (ora_lixis, kwd_omad))
                cursor.execute("UPDATE DIORGANONEI SET AFM = ? WHERE kwdikos_omadikou = ?", (afm, kwd_omad))
                conn.commit()
                conn.close()
                print("Τα δεδομένα ενημερώθηκαν επιτυχώς!")
            else:
                print("O γυμναστής αυτός δεν ειναι διαθέσιμος αυτήν την ώρα ή μέρα.")
                return False
        else:
            print("Ο γυμναστής αυτός δεν υπάρχει.")
            return False
    else:
        if (aithousa):
            cursor.execute("UPDATE OMADIKO_PROGRAMMA SET aithousa = ? WHERE kwdikos_omadikou = ?", (aithousa, kwd_omad))
        if (orio_atomon):
            cursor.execute("UPDATE OMADIKO_PROGRAMMA SET orio_atomon = ? WHERE kwdikos_omadikou = ?", (orio_atomon, kwd_omad))
        cursor.execute("UPDATE OMADIKO_PROGRAMMA SET hmerominia = ? WHERE kwdikos_omadikou = ?", (hmerominia, kwd_omad))
        if (onoma):
            cursor.execute("UPDATE OMADIKO_PROGRAMMA SET onoma = ? WHERE kwdikos_omadikou = ?", (onoma, kwd_omad))
        cursor.execute("UPDATE OMADIKO_PROGRAMMA SET ora_enarxis = ? WHERE kwdikos_omadikou = ?", (ora_enarxis, kwd_omad))
        cursor.execute("UPDATE OMADIKO_PROGRAMMA SET ora_lixis = ? WHERE kwdikos_omadikou = ?", (ora_lixis, kwd_omad))
        conn.commit()
        conn.close()
        print("Τα δεδομένα ενημερώθηκαν επιτυχώς!")

# Συναρτηση για insert σε ραντεβου
def insert_ranteboy():
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute("SELECT kwdikos_ranteboy FROM RANTEBOY ORDER BY kwdikos_ranteboy DESC")
    result = cursor.fetchone()
    if (result is None):
        kwd_ranteboy = 0
    else:
        kwd_ranteboy = int(result[0])
    
    cursor.execute("SELECT kwdikos_personal FROM PERSONAL_TRAINING ORDER BY kwdikos_personal DESC")
    result_2 = cursor.fetchone()
    if (result_2 is None):
        kwd_personal = 0
    else:
        kwd_personal = int(result_2[0])
    
    tr_afm = str(input("Δώστε τιμή για το ΑΦΜ του Γυμναστή: \n"))
    kwd_melous = int(input("Ποιος ειναι ο κωδικός του μέλους που έκλεισε το ραντεβού; \n"))
    hmerominia = input("Ποια ειναι η ημερομηνία του ραντεβού; (yyyy-mm-dd) \n")
    wra_enarxis = input("Ποια είναι η ώρα έναρξης του ραντεβού; (hh-mm-ss) \n")
    wra_lixis = input("Ποια είναι η ώρα λήξης; \n")


    if (check_for_existing_member(kwd_melous) and check_for_existing_trainer(tr_afm)):
        if (check_for_working_hours(tr_afm, hmerominia, wra_enarxis, wra_lixis)):
                bathmida = return_subscription(kwd_melous)
                if (bathmida == 'Χρυσή'):
                    kostos = 0
                else:
                    kostos = 20
                
                cursor.execute(f"""INSERT INTO RANTEBOY VALUES (?, ?, ?, ?, ?, ?, ?)""", (kwd_ranteboy + 1, tr_afm, kwd_melous, kostos, hmerominia, wra_enarxis, wra_lixis))
                cursor.execute(f"""INSERT INTO PERSONAL_TRAINING VALUES (?, ?, ?)""", (kwd_personal + 1, 1, kwd_ranteboy + 1))
                connection.commit()
        else:
            print("Ο γυμναστής δεν ειναι διαθέσιμος αυτήν την ώρα")
            return False
    else:
        print("Το μέλος που εισάγατε ή ο γυμναστής που εισάγατε δεν υπάρχουν")
    
    option = int(input("Θα θέλατε να τυπώσετε τα ραντεβου ;(1 = ΝΑΙ 2 = ΟΧΙ) "))
    if (option == 1):
        database_queries.print_ranteboy()

# Συναρτηση delete ραντεβου
def delete_ranteboy(kwd_rant):
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM RANTEBOY WHERE kwdikos_ranteboy = ?",(kwd_rant,))
    print("Το ραντεβού διαγράφηκε επιτυχώς.")
    choice = int(input("Θέλετε να διαγράψετε και το αντίστοιχο Personal Training session που του αντιστοιχεί; (1 = ΝΑΙ 2 = ΟΧΙ)"))
    if (choice == 1):
        cursor.execute("DELETE FROM PERSONAL_TRAINING WHERE kwdikos_ranteboy = ?", (kwd_rant, ))
        print("Το Personal Training Session διαγράφηκε επιτυχώς.")
    connection.commit()
    connection.close()

# Συναρτηση delete personal
def delete_personal(kwd_personal):
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute("SELECT kwdikos_ranteboy FROM PERSONAL_TRAINING WHERE kwdikos_personal = ?", (kwd_personal, ))
    kwd_rant_res = int(cursor.fetchone()[0])
    cursor.execute("DELETE FROM PERSONAL_TRAINING WHERE kwdikos_personal = ?",(kwd_personal,))
    print("Το Personal Training Session διαγράφηκε επιτυχώς.")
    choice = int(input("Θέλετε να διαγράψετε και το αντίστοιχο ραντεβού που του αντιστοιχεί; (1 = ΝΑΙ 2 = ΟΧΙ)"))
    if (choice == 1):
        cursor.execute("DELETE FROM RANTEBOY WHERE kwdikos_ranteboy = ?",(kwd_rant_res,))
        print("Το ραντεβού διαγράφηκε επιτυχώς.")
    connection.commit()
    connection.close()

# Συναρτηση Ενημερωσης Ραντεβου
def update_ranteboy():
    kwd_rantebou = int(input())
    tr_afm = input("Πληκτρολογήστε τον νέο γυμναστή του ραντεβού ή πατήστε enter αν δεν θελετε να το αλλάξετε: ")
    kwdikos_melous = input("Πληκτρολογήστε το νέο κωδικό μέλους ή πατήστε enter αν δεν θέλετε να το αλλάξετε: ")
    kostos = input("Πληκτρολογηστε το νέο κόστος ή πατήστε enter αν δεν θέλετε να το αλλάξετε: ")
    hmerominia = input("Πληκτρολογήστε την νέα ημερομηνία (yyyy-mm-dd) ή πατήστε enter αν δεν θέλετε να την αλλάξετε: ")
    ora_enarxis = input("Πληκτρολογήστε την νέα ώρα έναρξης (hh-mm-ss) ή πατήστε enter αν δεν θέλετε να την αλλάξετε: ")
    ora_lixis = input("Πληκτρολογήστε την νέα ώρα λήξης (hh-mm-ss) ή πατήστε enter αν δεν θέλετε να την αλλάξετε: ")

    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    cursor.execute("SELECT ora_enarxis FROM RANTEBOY WHERE kwdikos_ranteboy = ?", (kwd_rantebou, ))
    result = cursor.fetchone()
    if (result is not None):
        result_ora_enarxis = result[0]
    cursor.execute("SELECT ora_lixis FROM RANTEBOY WHERE kwdikos_ranteboy = ?", (kwd_rantebou, ))
    result = cursor.fetchone()
    if (result is not None):
        result_ora_lixis = result[0]
    cursor.execute("SELECT tr_AFM FROM RANTEBOY WHERE kwdikos_ranteboy = ?", (kwd_rantebou, ))
    result = cursor.fetchone()
    if (result is not None):
        result_afm = result[0]
    cursor.execute("SELECT hmerominia FROM RANTEBOY WHERE kwdikos_ranteboy = ?", (kwd_rantebou, ))
    result = cursor.fetchone()
    if (result is not None):
        result_date = result[0]
    cursor.execute("SELECT kwdikos_melous FROM RANTEBOY WHERE kwdikos_ranteboy = ?", (kwd_rantebou, ))
    result = cursor.fetchone()
    if (result is not None):
        result_melos = result[0]
    
    kwdikos_melous = kwdikos_melous if kwdikos_melous else result_melos
    kostos = int(kostos) if kostos else None
    hmerominia = hmerominia if hmerominia else result_date
    ora_enarxis = ora_enarxis if ora_enarxis else result_ora_enarxis
    ora_lixis = ora_lixis if ora_lixis else result_ora_lixis
    tr_afm = tr_afm if tr_afm else result_afm
    
    if (check_for_existing_trainer(tr_afm) and check_for_existing_member(kwdikos_melous)):
        if (check_for_working_hours(tr_afm, hmerominia, ora_enarxis, ora_lixis, kwd_rantebou)):
            cursor.execute("UPDATE RANTEBOY SET tr_AFM = ? WHERE kwdikos_ranteboy = ?", (tr_afm, kwd_rantebou))
            cursor.execute("UPDATE RANTEBOY SET kwdikos_melous = ? WHERE kwdikos_ranteboy = ?", (kwdikos_melous, kwd_rantebou))
            if (kostos):
                cursor.execute("UPDATE RANTEBOY SET kostos = ? WHERE kwdikos_ranteboy = ?", (kostos, kwd_rantebou))
            cursor.execute("UPDATE RANTEBOY SET hmerominia = ? WHERE kwdikos_ranteboy = ?", (hmerominia, kwd_rantebou))
            cursor.execute("UPDATE RANTEBOY SET ora_enarxis = ? WHERE kwdikos_ranteboy = ?", (ora_enarxis, kwd_rantebou))
            cursor.execute("UPDATE RANTEBOY SET ora_lixis = ? WHERE kwdikos_ranteboy = ?", (ora_lixis, kwd_rantebou))
            conn.commit()
            conn.close()
            print("Τα δεδομένα ενημερώθηκαν επιτυχώς!")
        else:
            print("Ο συγκεκριμένος γυμναστής δεν είναι διαθέσιμος εκείνη την ώρα ή μέρα.")
            return False
    else:
        print("Το μέλος ή ο γυμναστής που πληκτρολογήσατε δεν υπάρχουν.")
        return False

# Ελεγχος αν υπαρχει το μελος
def check_for_existing_member(kwd_melous):
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute(f"""SELECT count(*) FROM MELOS WHERE kwdikos_melous = ?""", (kwd_melous, ))
    result = cursor.fetchone()[0]
    if result > 0:
        return True
    else:
        return False

# Επιστροφη συνδρομης του μελους
def return_subscription(kwd_melous):
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute(f"""SELECT bathmida FROM SYNDROMI WHERE kwdikos_melous = ?""", (kwd_melous, ))
    result = cursor.fetchone()[0]
    return result

# Ελεγχος αν υπαρχει ο γυμναστης
def check_for_existing_trainer(tr_afm):
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute(f"""SELECT count(*) FROM GYMNASTIS WHERE AFM = ?""", (tr_afm, ))
    result = cursor.fetchone()[0]
    if result > 0:
        return True
    else:
        return False

# Ελεγχος αν ο γυμναστης ειναι διαθεσιμος τις ωρες αυτες και την ημερομηνια αυτή
def check_for_working_hours(tr_afm, date_s, ora_enarjis, ora_lijis, exclude_ranteboy_id = None):
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()

    cursor.execute("SELECT meres_ergasias from GYMNASTIS WHERE AFM = ?", (tr_afm, ))
    working_days_res = cursor.fetchone()
    working_days = working_days_res[0]

    selected_date = dt.strptime(date_s, "%Y-%m-%d").strftime("%A")


    if selected_date not in working_days:
        return False
    
    if exclude_ranteboy_id is not None:
        cursor.execute("""
            SELECT COUNT(*)
            FROM PERSONAL_TRAINING pt
            JOIN RANTEBOY r ON pt.kwdikos_ranteboy = r.kwdikos_ranteboy
            WHERE tr_AFM = ? AND hmerominia = ? AND r.kwdikos_ranteboy NOT IN (?)
        """, (tr_afm, date_s, exclude_ranteboy_id))
    else:
        cursor.execute("""
            SELECT COUNT(*)
            FROM PERSONAL_TRAINING pt
            JOIN RANTEBOY r ON pt.kwdikos_ranteboy = r.kwdikos_ranteboy
            WHERE tr_AFM = ? AND hmerominia = ?
        """, (tr_afm, date_s))


    existing_sessions_count = cursor.fetchone()[0]

    if existing_sessions_count > 0:
        return False
    
    cursor.execute("SELECT ora_enarxis, ora_lixis from GYMNASTIS WHERE AFM = ?", (tr_afm, ))
    first_curs_result = cursor.fetchall()
    if (ora_enarjis < first_curs_result[0][0] or ora_enarjis > first_curs_result[0][1] or ora_lijis < first_curs_result[0][0] or ora_lijis > first_curs_result[0][1]):
        return False

    if exclude_ranteboy_id is not None:
        query = """
        SELECT COUNT(*)
        FROM GYMNASTIS
        WHERE GYMNASTIS.AFM = ?
            AND ? BETWEEN GYMNASTIS.ora_enarxis AND GYMNASTIS.ora_lixis
            AND ? <= GYMNASTIS.ora_lixis
            AND ? >= GYMNASTIS.ora_enarxis
            AND GYMNASTIS.AFM IN (
                SELECT tr_AFM
                FROM RANTEBOY
                WHERE RANTEBOY.hmerominia = ? AND RANTEBOY.kwdikos_ranteboy NOT IN (?)
                AND ((RANTEBOY.ora_enarxis >= ? AND RANTEBOY.ora_enarxis < ?)
                        OR (RANTEBOY.ora_lixis > ? AND RANTEBOY.ora_lixis <= ?)
                        OR (RANTEBOY.ora_enarxis <= ? AND RANTEBOY.ora_lixis >= ?))
        UNION
        SELECT AFM
        FROM DIORGANONEI
        JOIN OMADIKO_PROGRAMMA ON OMADIKO_PROGRAMMA.kwdikos_omadikou = DIORGANONEI.kwdikos_omadikou
        WHERE DIORGANONEI.AFM = ? AND OMADIKO_PROGRAMMA.hmerominia = ?
            AND ((OMADIKO_PROGRAMMA.ora_enarxis >= ? AND OMADIKO_PROGRAMMA.ora_enarxis < ?)
                OR (OMADIKO_PROGRAMMA.ora_lixis > ? AND OMADIKO_PROGRAMMA.ora_lixis <= ?)
                OR (OMADIKO_PROGRAMMA.ora_enarxis <= ? AND OMADIKO_PROGRAMMA.ora_lixis >= ?)));
        """
        cursor.execute(query, (tr_afm, ora_enarjis, ora_lijis, ora_enarjis, date_s, exclude_ranteboy_id, ora_enarjis, ora_lijis, ora_enarjis, ora_lijis, ora_enarjis, ora_lijis, tr_afm, date_s, ora_enarjis, ora_lijis, ora_enarjis, ora_lijis, ora_enarjis, ora_lijis))
    else:
        query = """
        SELECT COUNT(*)
        FROM GYMNASTIS
        WHERE GYMNASTIS.AFM = ?
            AND ? BETWEEN GYMNASTIS.ora_enarxis AND GYMNASTIS.ora_lixis
            AND ? <= GYMNASTIS.ora_lixis
            AND ? >= GYMNASTIS.ora_enarxis
            AND GYMNASTIS.AFM IN (
                SELECT tr_AFM
                FROM RANTEBOY
                WHERE RANTEBOY.hmerominia = ?
                AND ((RANTEBOY.ora_enarxis >= ? AND RANTEBOY.ora_enarxis < ?)
                        OR (RANTEBOY.ora_lixis > ? AND RANTEBOY.ora_lixis <= ?)
                        OR (RANTEBOY.ora_enarxis <= ? AND RANTEBOY.ora_lixis >= ?))
        UNION
        SELECT AFM
        FROM DIORGANONEI
        JOIN OMADIKO_PROGRAMMA ON OMADIKO_PROGRAMMA.kwdikos_omadikou = DIORGANONEI.kwdikos_omadikou
        WHERE DIORGANONEI.AFM = ? AND OMADIKO_PROGRAMMA.hmerominia = ?
            AND ((OMADIKO_PROGRAMMA.ora_enarxis >= ? AND OMADIKO_PROGRAMMA.ora_enarxis < ?)
                OR (OMADIKO_PROGRAMMA.ora_lixis > ? AND OMADIKO_PROGRAMMA.ora_lixis <= ?)
                OR (OMADIKO_PROGRAMMA.ora_enarxis <= ? AND OMADIKO_PROGRAMMA.ora_lixis >= ?)));
        """
        cursor.execute(query, (tr_afm, ora_enarjis, ora_lijis, ora_enarjis, date_s, ora_enarjis, ora_lijis, ora_enarjis, ora_lijis, ora_enarjis, ora_lijis, tr_afm, date_s, ora_enarjis, ora_lijis, ora_enarjis, ora_lijis, ora_enarjis, ora_lijis))

    result = cursor.fetchone()[0]

    if result > 0:
        return False
    else:
        return True
    
# Συναρτηση insert προγραμμα γυμναστηριου
def insert_programma_gymnasthrioy():
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute("SELECT kwdikos_programmatos FROM PROGRAMA_GYMNASTIRIOU ORDER BY kwdikos_programmatos DESC")
    result = cursor.fetchone()
    if (result is None):
        kwd_programmatos = 0
    else:
        kwd_programmatos = int(result[0])
    stoxos = str(input("Πληκτρολογήστε τον στόχο του προγράμματος: "))
    afm = str(input("Πληκτρολογήστε τον γυμναστή που το έγραψε: "))
    kwd_melous = int(input("Πληκτρολογήστε τον κωδικό του μέλους που το ακολουθεί: "))
    hmerominia_enarxis = input("Πληκτρολογήστε την ημερομηνία που θα ξεκινησει το μέλος να ακολουθεί το προγραμμα (YYYY-MM-DD): ")
    hmerominia_lixis = input("Πληκτρολογήστε την ημερομηνία που θα τελειώσει το μέλος να ακολουθεί το προγραμμα (YYYY-MM-DD): ")
    if (check_for_existing_member(kwd_melous) and check_for_existing_trainer(afm)):
        cursor.execute("INSERT INTO PROGRAMA_GYMNASTIRIOU VALUES (?, ?, ?)", (kwd_programmatos + 1, stoxos, 1))
        cursor.execute("INSERT INTO AKOLOYTHEI VALUES (?, ?, ?, ?)", (kwd_melous, kwd_programmatos + 1, hmerominia_enarxis, hmerominia_lixis))
        cursor.execute("INSERT INTO GRAFEI VALUES (?, ?)", (afm, kwd_programmatos))
        connection.commit()
        print("Το προγραμμα προστέθηκε με επιτυχία!")
    else: 
        print("Το μέλος ή ο γυμναστής που εισάγατε δεν υπάρχει!")
        return False
    
# Συναρτηση delete προγραμμα γυμναστηριου
def delete_programma_gymnasthrioy(kwd_programmatos):
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    #kwd_rant = int(input())
    cursor.execute("DELETE FROM PROGRAMA_GYMNASTIRIOU WHERE kwdikos_programmatos = ?",(kwd_programmatos,))
    cursor.execute("DELETE FROM AKOLOYTHEI WHERE kwdikos_programmatos = ?", (kwd_programmatos, ))
    cursor.execute("DELETE FROM GRAFEI WHERE kwdikos_programmatos = ?", (kwd_programmatos, ))
    connection.commit()
    connection.close()
    print("Tα προγράμματα γυμναστηρίου διαγράφηκαν επιτυχώς")
    
# Συναρτηση update προγραμμα γυμναστηριου
def update_programa_gymnasthrioy():
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    kwd_prog = int(input())
    stoxos = str(input("Πληκτρολογήστε τον νέο στόχο του προγράμματος: "))
    cursor.execute("UPDATE PROGRAMA_GYMNASTIRIOU SET stoxos = ? WHERE kwdikos_programmatos = ?", (stoxos, kwd_prog))
    connection.commit()
    connection.close()
    print("Το προγραμμα ενημερώθηκε επιτυχώς!")

# Συνάρτηση insert για μέλος
def insert_melos():
    member_name = input("Πληκτρολογήστε το όνοματεπωνυμο: ")
    member_phone = input("Πληκτρολογήστε το τηλέφωνο: ")
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    cursor.execute("SELECT max(kwdikos_melous) FROM MELOS")
    result = cursor.fetchone()
    if (result):
        member_id = result[0] + 1
    else:
        member_id = 1
    cursor.execute("INSERT INTO MELOS VALUES(?,?,?)",(member_id,member_name,member_phone))
    conn.commit()
    print("Το μέλος προστέθηκε με επιτυχία")
    print(f"Ο κωδικός μέλους είναι: {member_id}")
    choice = int(input("Θέλετε να προσθέσετε συνδρομή για αυτό το μέλος; (1 = NAI 2 = OXI)"))
    if (choice == 1):
        cursor.execute("SELECT max(kwdikos_syndromis) FROM SYNDROMI")
        result = cursor.fetchone()
        if (result):
            sub_id = result[0] + 1
        else:
            sub_id = 1
        sub_gym = input("Enter GYM id: ")
        sub_length = input("Enter subscription length: ")
        sub_start = datetime.date.today()
        sub_end = sub_start + datetime.timedelta(days=int(sub_length))
        sub_tier = input("Enter subscription tier(Απλή,Σπέσιαλ,Χρυσή): ")
        if sub_tier == "Απλή":
            sub_price = 10
        elif sub_tier == "Σπέσιαλ":
            sub_price = 20
        else: 
            sub_price = 30

        cursor.execute("""INSERT INTO SYNDROMI VALUES
                                (?,?,?,?,?,?,?)""",(sub_id,sub_price,sub_tier,sub_gym,sub_start,sub_end,member_id))
        conn.commit()
        print("H συνδρομη προστέθηκε με επιτυχία!")
    else:
        pass
    conn.close()

# Συνάρτηση delete για μέλος
def delete_melos(kwd_melous):
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM MELOS WHERE kwdikos_melous = ?",(kwd_melous,))
    cursor.execute("DELETE FROM AKOLOYTHEI WHERE kwdikos_melous =?", (kwd_melous,))
    cursor.execute("DELETE FROM SYMMETEXEI WHERE kwdikos_melous = ?",(kwd_melous,))
    conn.commit()
    conn.close()

# Συνάρτηση update για μέλος
def update_melos():
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    kwd_melous = int(input())
    if (check_for_existing_member(kwd_melous)):
        onoma = input("Εισάγετε νέα τιμή για το Ονοματεπώνυμο ή πατήστε enter αν δεν θέλετε να το αλλάξετε: ")
        tilefono = input("Εισάγετε νέα τιμή για το τηλέφωνο ή πατήστε enter αν δεν θέλετε να το αλλάξετε: ")
        if (onoma):
            cursor.execute("UPDATE MELOS SET onomateponimo=? WHERE kwdikos_melous=?", (onoma, kwd_melous))
        if (tilefono):
            cursor.execute("UPDATE MELOS SET tilefono=? WHERE kwdikos_melous=?", (tilefono, kwd_melous))
        conn.commit()
        conn.close()
        print("Τα στοιχεία ενημερώθηκαν με επιτυχία!")
    else:
        print("Δεν υπάρχει μέλος με αυτόν τον κωδικό")
        return False

# Συνάρτηση insert για συνδρομή
def insert_syndromi():
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    kwd_melous = int(input("Εισάγετε τον κωδικό μέλους: "))
    if (check_for_existing_member(kwd_melous) == False):
        print("Το μέλος αυτό δεν υπάρχει")
        return False
    elif (check_for_existing_member(kwd_melous)):
        cursor.execute("SELECT max(kwdikos_syndromis) FROM SYNDROMI")
        result = cursor.fetchone()
        if (result):
            kwdikos_syndromis = result[0] + 1
        else:
            kwdikos_syndromis = 1
        kwdikos_gym = int(input("Εισαγάγετε τον κωδικο του γυμναστηρίου: "))
        bathmida = input("Εισάγετε την βαθμίδα (Απλή, Σπέσιαλ, Χρυσή): ")
        imerominia_enraxis = input("Εισάγετε την ημερομηνία έναρξης (YYYY-MM-DD): ")
        imerominia_enraxis = datetime.datetime.strptime(imerominia_enraxis, "%Y-%m-%d").date()
        diarkia = int(input("Εισάγετε την διάρκεια της συνδρομής: "))
        imerominia_lixis = imerominia_enraxis + datetime.timedelta(days=diarkia*30)
        if (bathmida == 'Απλή'):
            kostos = 10
        elif (bathmida == "Σπέσιαλ"):
            kostos = 20
        elif (bathmida == "Χρυσή"):
            kostos = 30
        else:
            print("Λάθος τιμή βαθμίδας")
            kostos = None
            return False
        cursor.execute("""INSERT INTO SYNDROMI VALUES 
                       (?, ?, ?, ?, ?, ?, ?)""", (kwdikos_syndromis, kostos * diarkia, bathmida, kwdikos_gym, imerominia_enraxis, imerominia_lixis, kwd_melous))
        conn.commit()
        conn.close()
        print("Η Συνδρομή προστέθηκε με επιτυχία")

# Συνάρτηση delete για συνδρομή
def delete_syndromi():
    sub_id = int(input("Εισαγάγετε τον κωδικό της συνδρομής που θέλετε να διαγράψετε:"))
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM SYNDROMI WHERE kwdikos_syndromis = ?",(sub_id,))
    conn.commit()
    conn.close()
    print("Η συνδρομή διαγράφηκε επιτυχώς")

# Συνάρτηση update για συνδρομή
def update_syndromi():
    print("Μία συνδρομή δεν μπορεί να τροποποιηθεί, παρακαλώ προσθέστε καινούρια συνδρομή αν επιθυμείτε να κάνετε κάποια αλλαγή! ")
    return False

# Συναρτηση insert εξοπλισμού
def insert_exoplismos():
    onoma = input("Εισάγετε το όνομα του εξοπλισμού: ")
    kwdikos_gym = int(input("Εισάγετε τον κωδικό του γυμναστηρίου που ανήκει: "))
    omada = input("Εισάγετε την μυϊκή ομάδα που γυμνάζει: ")
    barcode = input("Εισάγετε το barcode του εξοπλισμού: ")
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO EXOPLISMOS 
                    VALUES(?,?,?,?)""", (barcode, onoma, omada, 1))
    cursor.execute("""INSERT INTO KATEXEI 
                    VALUES(?,?)""", (kwdikos_gym, barcode))
    conn.commit()
    print("Ο εξοπλισμός προστέθηκε με επιτυχία!")
    if (check_for_category(omada) == False):
        cursor.execute("""INSERT INTO KATHGORIA VALUES (?)""", (omada, ))

# Συναρτηση delete εξοπλισμού
def delete_exopismos():
    barcode = input("Εισάγετε το barcode του εξοπλισμού: ")
    if (check_for_equipment(barcode)):
        conn = sqlite3.connect(name_of_file)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM EXOPLISMOS WHERE barcode = ?",(barcode,))
        conn.commit()
        cursor.execute("DELETE FROM KATEXEI WHERE barcode = ?",(barcode,))
        cursor.execute("""SELECT OMADIKO_PROGRAMMA.kwdikos_omadikou FROM OMADIKO_PROGRAMMA join XRISIMOPOIEI on OMADIKO_PROGRAMMA.kwdikos_omadikou = XRISIMOPOIEI.kwdikos_omadikou
                       WHERE XRISIMOPOIEI.barcode = ?""", (barcode, ))
        result = cursor.fetchone()
        if (result):
            res = result[0]
            print("Τα ομαδικά προγράμματα με τους ακόλουθους κωδικούς χρησιμοποιούσαν τον εξοπλισμό αυτόν: ")
            for kwd in res:
                print(kwd)
        cursor.execute("DELETE FROM XRISIMOPOIEI WHERE barcode = ?",(barcode,))
        conn.commit()
        conn.close()
        print("Ο εξοπλισμός διαγράφηκε με επιτυχία")
    else:
        print("Ο εξοπλισμός αυτός δεν υπάρχει")
        return False

# Συναρτηση update εξοπλισμού
def update_exoplismos():
    exomplismos_id = input("Εισαγάγετε το barcode του εξοπλισμού: ")
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    if check_for_equipment(exomplismos_id):
        exomplismos_name = input("Εισαγάγετε το όνομα ή πατήστε Enter για να παραλείψετε: ")
        exomplismos_group = input("Εισαγάγετε τη μυϊκή ομάδα του εξοπλισμού ή πατήστε Enter για να παραλείψετε: ")
        if exomplismos_name and exomplismos_group:
            cursor.execute("UPDATE EXOPLISMOS SET onoma=?, muikh_omada=? WHERE barcode=?", (exomplismos_name, exomplismos_group, exomplismos_id))
        elif exomplismos_name:
            cursor.execute("UPDATE EXOPLISMOS SET onoma=? WHERE barcode=?", (exomplismos_name, exomplismos_id))
        elif exomplismos_group:
            cursor.execute("UPDATE EXOPLISMOS SET muikh_omada=? WHERE barcode=?", (exomplismos_group, exomplismos_id))
        else:
            print("Δεν υπάρχουν αλλαγές για ενημέρωση")
        conn.commit()
        conn.close()
        print("Ο εξοπλισμός ενημερώθηκε με επιτυχία")
    else:
        print("Δεν υπάρχει εξοπλισμός με αυτό το barcode")
        return False
    
# Ελεγχος αν υπάρχει ο εξοπλισμός
def check_for_equipment(barcode):
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute(f"""SELECT count(*) FROM EXOPLISMOS WHERE barcode = ?""", (barcode, ))
    result = cursor.fetchone()[0]
    if result > 0:
        return True
    else:
        return False

# Ελεγχος αν υπάρχει η κατηγορία
def check_for_category(category):
    connection = sqlite3.connect(name_of_file)
    cursor = connection.cursor()
    cursor.execute(f"""SELECT count(*) FROM KATHGORIA WHERE muikh_omada = ?""", (category, ))
    result = cursor.fetchone()[0]
    if result > 0:
        return True
    else:
        return False


def main():
    run = True
    while (run):
        choice_p = choice()
        if (choice_p == 1):
            starting_menu()
            table = int(input("\nΠληκτρολόγησε τον αντίστοιχο αριθμό: "))
            choose_table(table)
        elif (choice_p == 2):
            starting_menu_del()
            table = int(input("\nΠληκτρολόγησε τον αντίστοιχο αριθμό: "))
            choose_table_delete(table)
        elif (choice_p == 3):
            starting_menu_update()
            table = int(input("\nΠληκτρολόγησε τον αντίστοιχο αριθμό: "))
            choose_table_update(table)
        elif (choice_p == 4):
            starting_menu_print()
            print_choice = int(input("\nΠληκτρολόγησε τον αντίστοιχο αριθμό: "))
            if (print_choice == 1):
                choose_table_print_all()
            elif (print_choice == 2):
                choose_query()
        elif (choice_p == 5):
            run = False


main()
# print_omadiko()
# print_gymnastis()
# conn = sqlite3.connect(name_of_file)
# cursor = conn.cursor()
# cursor.execute("""SELECT * FROM EXOPLISMOS""")
# res = cursor.fetchall()
# for gymnastis in res:
#     print(gymnastis)

