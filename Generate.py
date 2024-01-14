import random
import datetime
from datetime import datetime, timedelta,time
import sqlite3

name_of_file = "gym_final.db"
# Function to generate a Greek full name
generated_phone_numbers = set()
afm = set()
def generate_full_name():
    first_names = ["Γιώργος", "Αναστασία", "Δημήτρης", "Ελένη", "Μαρία", "Νίκος", "Σοφία", "Αλέξανδρος","Λάζαρος",
                   "Νεκταρία","Γιάννης","Αντώνης","Ανδρέας","Αναστάσης","Ελευθερία","Γεωργία","Δανάη","Παναγιώτης","Χριστίνα",]
    last_names = ["Παπαχρήστου", "Καραγιάννη", "Μακρής", "Κορωναίου", 
                  "Πετρίδου", "Παναγόπουλος", "Καραγιάννη", "Αντωνίου","Ζευγουλά","Παπουτσάς","Ροδόπουλος","Μιχάλης",
                  "Σιδέρη","Βοβός","Σκλαβενίτης","Ζέρβας","Καραμπάτσος","Παπαδόπουλος","Ρεμπούτσικας","Ζουγανέλη","Τσάμπρα"]
    
    full_name = random.choice(first_names) + " " + random.choice(last_names)
    return full_name

# Function to generate a phone number starting with '69'
generated_phone_numbers = set()
afm = set()
def generate_phone_number():
    while True:
        phone_number = "69" + str(random.randint(10000000, 99999999))
        if phone_number not in generated_phone_numbers:
            generated_phone_numbers.add(phone_number)
            return phone_number
def generate_days():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    chosen_days = random.sample(days, 3)
    return ' '.join(chosen_days)

def generate_times():
        start_hour = random.randint(9, 15)  # Ensure there's at least 8 hours left in the day

        start_time = time(start_hour, 0, 0)  # Minutes and seconds are set to zero

        end_hour = start_hour + 8

        end_time = time(end_hour, 0, 0)  # Minutes and seconds are set to zero
        start_time_str = start_time.strftime('%H:%M:%S')
        end_time_str = end_time.strftime('%H:%M:%S')
        return start_time_str, end_time_str

def generate_bathmida():
    
    types = ["Απλή", "Σπέσιαλ", "Χρυσή"]
    choice = random.choice(types)
    if choice == "Απλή":
        kostos = 10
    elif choice == "Σπέσιαλ":
        kostos = 20
    else:
        kostos = 30
    return choice,kostos

#generate dates for syndromi that has ended
def generate_old_date(diarkeia):
    start_year = random.randint(2020, 2022)
    start_month = random.randint(1, 12)
    start_day = random.randint(1, 28)  # To avoid issues with months that have less than 31 days

    start_date = datetime(start_year, start_month, start_day)

    end_date = start_date + timedelta(days=int(diarkeia)*30)

    return start_date.date(), end_date.date()

def generate_new_date(diarkeia):
        start_year = 2023
        start_month = random.randint(11,12)
        start_day = random.randint(1, 28)  # To avoid issues with months that have less than 31 days
        
        start_date = datetime(start_year, start_month, start_day)
        
        end_date = start_date + timedelta(days=int(diarkeia)*30)
        
        return start_date.date(), end_date.date()
      
def generate_omadiko_hours_day():
        start_hour = random.randint(9, 21)  # Ensure that the omadiko starts and finished during working hours
        start_time = time(start_hour, 0, 0)  # Minutes and seconds are set to zero
        diarkeia = random.choice([1, 2])
        end_hour = start_hour + diarkeia
        
        end_time = time(end_hour, 0, 0)  # Minutes and seconds are set to zero
        start_time_str = start_time.strftime('%H:%M:%S')
        end_time_str = end_time.strftime('%H:%M:%S')

        program_year = random.randint(2020, 2022)
        program_month = random.randint(1, 12)
        program_day = random.randint(1, 28)  # To avoid issues with months that have less than 31 days

        program_date = datetime(program_year, program_month, program_day)
        if program_date.weekday() == 6:
                program_date = program_date + timedelta(days=1)
        date_string = program_date.date().strftime('%Y-%m-%d')
       
        return start_time_str, end_time_str, date_string

def generate_symmetoxes():
        cursor.execute("""select  s.kwdikos_melous,s.bathmida,o.kwdikos_omadikou,o.orio_atomon
                        from SYNDROMI as s,OMADIKO_PROGRAMMA as o
                        where o.hmerominia BETWEEN s.hmerominia_enarxis and s.hmerominia_lixis""")
        results = cursor.fetchall()
        for result in results:
                kwdikos_melous = result[0]
                bathmida = result[1]
                kwdikos_omadikou = result[2]
                orio = result[3]
                cursor.execute("""select count(*) from SYMMETEXEI where kwdikos_omadikou = ?""",(kwdikos_omadikou,))
                atoma_now = cursor.fetchone()
                if atoma_now[0] <orio:
                        if bathmida == "Απλή":
                                kostos = 10
                        else:
                                kostos = 0
                        cursor.execute("""INSERT INTO SYMMETEXEI VALUES(?,?,?)""",(kwdikos_melous,kwdikos_omadikou,kostos))
                        conn.commit()

       



def check_and_gen_equipement_availability(kwdikos_omad,orio, date_s,ora_lijis):
       muscle_groups = ["Στήθος", "Κοιλιακοί", "Πλάτη", "Πόδια", "Χέρια", "Καρδιοαναπνευστικό Σύστημα","Ελεύθερα Βάρη","Ώμους","Ραχαίοι","Αξεσουάρ"]
       quary ="""
               SELECT e.barcode
                FROM XRISIMOPOIEI AS x, OMADIKO_PROGRAMMA AS o, EXOPLISMOS AS e
                WHERE x.barcode = e.barcode 
                AND x.kwdikos_omadikou = o.kwdikos_omadikou 
                AND o.hmerominia = ? 
                AND (? BETWEEN o.ora_enarxis AND o.ora_lixis)
                AND (e.muikh_omada = ? OR e.muikh_omada = ?)"""
       cursor.execute(quary,(date_s,ora_lijis,muscle_groups[6],muscle_groups[9]))
       barcodes_unav = [item[0] for item in cursor.fetchall()]
       cursor.execute("""SELECT barcode FROM EXOPLISMOS WHERE muikh_omada = ? OR muikh_omada = ?""",(muscle_groups[6],muscle_groups[9]))
       barcodes_all = [item[0] for item in cursor.fetchall()]

       inserted_barcodes = 0
       for barcode in barcodes_all:
                if inserted_barcodes >= orio:
                        break
                if barcode not in barcodes_unav:
                        insert_query = """
                                INSERT INTO XRISIMOPOIEI 
                                            VALUES (?,?)"""
                                                        
                        cursor.execute(insert_query, (kwdikos_omad,barcode))
                        conn.commit()
                        inserted_barcodes += 1



       
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
    if (result):
           return False
    else:
           return True

def check_for_working_hours(tr_afm, date_s, ora_enarjis, ora_lijis, exclude_ranteboy_id = None):
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()

    cursor.execute("SELECT meres_ergasias from GYMNASTIS WHERE AFM = ?", (tr_afm, ))
    working_days_res = cursor.fetchone()
    working_days = working_days_res[0]

    selected_date = datetime.strptime(date_s, "%Y-%m-%d").strftime("%A")


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
afm_set = set()

def generate_afm():
    while True:
        afm = str(random.randint(10000, 99999))
        if afm not in afm_set:
            afm_set.add(afm)
            return afm

    


barcode_set = set()
def generate_barcode():
        while True:
                barcode = str(random.randint(10000, 99999))
                if barcode not in barcode_set:
                        barcode_set.add(barcode)
                        return barcode

def diarkeia_generate():
        diarkeia = random.choice([1, 3, 6, 12])
        return diarkeia

def generate_program():
        stoxos = random.choice(["Αδυνάτισμα", "Ενδυνάμωση", "Υπερτροφία","Αποκατάσταση"])
        start_year = random.randint(2020, 2023)
        start_month = random.randint(1, 12)
        start_day = random.randint(1, 28)  # To avoid issues with months that have less than 31 days
        start_date = datetime(start_year, start_month, start_day)
        end_date = start_date + timedelta(days=90)
        return stoxos, start_date.date(), end_date.date()


def generate_gyms():
        cursor.execute("INSERT INTO GYMNASTIRIO VALUES(?,?,?,?)",(1,"GETFIT","Μαιζώνος 18","2610886747"))
        conn.commit()
        cursor.execute("INSERT INTO GYMNASTIRIO VALUES(?,?,?,?)",(2,"GETFIT","Αρόη 2","2610886748"))
        conn.commit()
        cursor.execute("INSERT INTO PAROHES VALUES(?)",(1,))
          
def generate_melh():
       for i in range(1, 201):
                kwdikos_melous = i
                phone_number = generate_phone_number()
                onomateponimo = generate_full_name()
                bathmida,kostos = generate_bathmida()
                diarkeia = diarkeia_generate()
                start_date, end_date = generate_old_date(diarkeia)
                cursor.execute("INSERT INTO MELOS VALUES (?, ?, ?);", (kwdikos_melous, onomateponimo, phone_number))
                conn.commit()
                if i < 101:
                        cursor.execute("INSERT INTO SYNDROMI VALUES (?, ?, ?, ?, ?, ?, ?)",
                                                   (kwdikos_melous, diarkeia * kostos, bathmida, 1, start_date, end_date, kwdikos_melous))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO SYNDROMI VALUES (?, ?, ?, ?, ?, ?, ?)",
                                                   (kwdikos_melous, diarkeia * kostos, bathmida, 2, start_date, end_date, kwdikos_melous))
                        conn.commit()

def generate_new_syndromes():
        active_member = set()
        for i in range(201, 301):
                bathmida,kostos = generate_bathmida()
                diarkeia = diarkeia_generate()
                start_date, end_date = generate_new_date(diarkeia)
                kwdikos_melous = random.randint(1, 200)
                while kwdikos_melous in active_member:
                        kwdikos_melous = random.randint(1, 200)
                active_member.add(kwdikos_melous)
                if i<250:
                        cursor.execute("""INSERT INTO SYNDROMI VALUES(?, ?, ?, ?, ?, ?, ?)""", 
                                        (i,diarkeia*kostos,bathmida,1,start_date,end_date,kwdikos_melous))
                        conn.commit()
                else:
                        cursor.execute("""INSERT INTO SYNDROMI VALUES 
                                                        (?, ?, ?, ?, ?, ?, ?)""",
                                                        (i, diarkeia*kostos, bathmida, 2, start_date, end_date, kwdikos_melous))
                        conn.commit()
             
def generate_gymnastes():
        for k in range(1, 20):
                afm = generate_afm()
                phone_number = generate_phone_number()
                onomateponimo = generate_full_name()
                misthos = random.randint(800, 1500)
                working_days = generate_days()  # Assign the result of generate_days() to working_days
                start_time, end_time = generate_times()
                if k < 10:
                        kwdikos_gym = 1
                else:
                        kwdikos_gym = 2
                cursor.execute("""INSERT INTO GYMNASTIS VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                                                (afm, misthos, onomateponimo, kwdikos_gym, working_days, start_time, end_time, phone_number))
                conn.commit()
        
def generate_equiment():
        muscle_groups = ["Στήθος", "Κοιλιακοί", "Πλάτη", "Πόδια", "Χέρια", "Καρδιοαναπνευστικό Σύστημα","Ελεύθερα Βάρη","Ώμους","Ραχαίοι","Αξεσουάρ"]
        for muscle_group in muscle_groups:
                cursor.execute("INSERT INTO KATHGORIA VALUES (?)", (muscle_group,))
                conn.commit()

        barakia_names1 = ["Βαράκι 1kg","Βαράκι 2kg","Βαράκι 5kg","Βαράκι 7.5kg"]
        barakia_names2=["Βαράκι 7.5kg",
                                        "Βαράκι 10kg","Βαράκι 12kg","Βαράκι 15kg","Βαράκι 20kg","Βαράκι 25kg"]
        for barakia in barakia_names1:
                for i in range(80):
                        barcode_val = generate_barcode()
                        cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                        (barcode_val, barakia, muscle_groups[6], 1))
                        conn.commit()   
                        if i < 40:
                                cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                                conn.commit()
                        else:
                                cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (2, barcode_val))
                                conn.commit()

        for barakia in barakia_names2:
                for i in range(20):
                        barcode_val = generate_barcode()
                        cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                        (barcode_val, barakia, muscle_groups[6], 1))
                        conn.commit()
                        if i < 10:
                                cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                                conn.commit()
                        else:
                                cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (2, barcode_val))
                                conn.commit()

        diskoi_names = ["Δίσκος 2.5kg","Δίσκος 5kg","Δίσκος 7.5kg","Δίσκος 10kg","Δίσκος 12.5kg","Δίσκος 15kg","Δίσκος 20kg","Δίσκος 25kg"]
        for diskoi in diskoi_names:
                for i in range(16):
                        barcode_val = generate_barcode()
                        cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                        (barcode_val, diskoi, muscle_groups[6], 1))
                        conn.commit()
                        if i < 8:
                                cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                                conn.commit()
                        else:
                                cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (2, barcode_val))
                                conn.commit()

        bares_names = ["Μπάρα 10kg","Μπάρα 15kg","Μπάρα 20kg","Μπάρα 25kg"]
        for bara in bares_names:
                for i in range(6):
                        barcode_val = generate_barcode()
                        cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                        (barcode_val, bara, muscle_groups[6], 1))
                        conn.commit()
                        if i < 3:
                                cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                                conn.commit()
                        else:
                                cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (2, barcode_val))
                                conn.commit()

        for i in range(30):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Μπάρα 5kg', muscle_groups[6], 1))
                conn.commit()
                if i < 15:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (2, barcode_val))
                        conn.commit()

        for i in range(4):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Πιέσεις ώμων', muscle_groups[7], 1))
                conn.commit()
                if i < 2:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (2, barcode_val))
                        conn.commit()

        for i in range(4):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Πρέσα ώμων', muscle_groups[7], 1))
                conn.commit()
                if i < 2:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (2, barcode_val))
                        conn.commit()

        for i in range(4):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Πλευρικες ανυψώσεις ώμων', muscle_groups[7], 1))
                conn.commit()
                if i < 2:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (2, barcode_val))
                        conn.commit()

        for i in range(12):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Διάδρομος', muscle_groups[5], 1))
                conn.commit()
                if i < 6:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (2, barcode_val))
                        conn.commit()

        for i in range(12):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Ποδήλατο', muscle_groups[5], 1))
                conn.commit()
                if i < 6:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?);", (2, barcode_val))
                        conn.commit()

        for i in range(10):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Πάγκος Στήθους', muscle_groups[0], 1))
                conn.commit()
                if i < 10:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (2, barcode_val))
                        conn.commit()

        for i in range(8):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Πιέσεις στήθους', muscle_groups[0], 1))
                conn.commit()
                if i < 4:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (2, barcode_val))
                        conn.commit()

        for i in range(8):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Pec deck', muscle_groups[0], 1))
                conn.commit()
                if i < 4:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (2, barcode_val))
                        conn.commit()

        for i in range(8):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Chest fly', muscle_groups[0], 1))
                conn.commit()
                if i < 4:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (2, barcode_val))
                        conn.commit()

        for i in range(8):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Τροχαλία πλάτης', muscle_groups[2], 1))
                conn.commit()
                if i < 4:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (2, barcode_val))
                        conn.commit()

        for i in range(8):
                barcode_val= generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Κωπηλατική πλάτης', muscle_groups[2], 1))
                conn.commit()
                if i < 4:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (2, barcode_val))
                        conn.commit()

        for i in range(8):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Μονόζυγο', muscle_groups[2], 1))
                conn.commit()
                if i < 4:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (2, barcode_val))
                        conn.commit()

        for i in range(8):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Εμπροστιαίο pull over', muscle_groups[2], 1))
                conn.commit()
                if i < 4:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (2, barcode_val))
                        conn.commit()

        for i in range(60):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Αερόβια σκαλοπάτια', muscle_groups[9], 1))
                conn.commit()
                if i < 30:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?);", (2, barcode_val))
                        conn.commit()
        
        for i in range(60):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Στρώματα γυμναστικής', muscle_groups[9], 1))
                conn.commit()
                if i < 30:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?);", (2, barcode_val))
                        conn.commit()

        for i in range(60):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Μπάλες γυμναστικής', muscle_groups[9], 1))
                conn.commit()
                if i < 30:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?);", (2, barcode_val))
                        conn.commit()
        
        for i in range(60):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Λάστιχα αντίστασης', muscle_groups[9], 1))
                conn.commit()
                if i < 30:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?);", (2, barcode_val))
                        conn.commit()

        for i in range(8):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Έκταση τρικεφάλων', muscle_groups[4], 1))
                conn.commit()
                if i < 4:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?);", (2, barcode_val))
                        conn.commit()
        
        for i in range(8):
                barcode_val = generate_barcode()
                cursor.execute("""INSERT INTO EXOPLISMOS VALUES (?, ?, ?, ?)""",
                                                (barcode_val, 'Κάμψεις δικεφάλων', muscle_groups[4], 1))
                conn.commit()
                if i < 4:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?)", (1, barcode_val))
                        conn.commit()
                else:
                        cursor.execute("INSERT INTO KATEXEI VALUES (?, ?);", (2, barcode_val))
                        conn.commit()

def generate_programa_gym():
        cursor.execute("""SELECT AFM FROM GYMNASTIS WHERE kwdikos_gym=?""",(1,))
        afm_data1 = cursor.fetchall()
        
        cursor.execute("""SELECT AFM FROM GYMNASTIS WHERE kwdikos_gym=?""",(2,))
        afm_data2 = cursor.fetchall()
        for i in range(1,150):
                stoxos, start_date, end_date = generate_program()
                if i<75:
                        afm1 = random.choice(afm_data1)[0]
                        cursor.execute("""INSERT INTO PROGRAMA_GYMNASTIRIOU VALUES(?,?,?)""",(i,stoxos,1))
                        conn.commit()
                        cursor.execute("""INSERT INTO AKOLOYTHEI VALUES(?,?,?,?)""",(i,i,start_date,end_date))
                        conn.commit()
                        cursor.execute("""INSERT INTO GRAFEI VALUES(?,?)""",(afm1,i))
                        conn.commit()
                else:
                        afm2 = random.choice(afm_data2)[0]
                        cursor.execute("""INSERT INTO PROGRAMA_GYMNASTIRIOU VALUES(?,?,?)""",(i,stoxos,1))
                        conn.commit()
                        cursor.execute("""INSERT INTO AKOLOYTHEI VALUES(?,?,?,?)""",(i,i,start_date,end_date))
                        conn.commit()
                        cursor.execute("""INSERT INTO GRAFEI VALUES(?,?)""",(afm2,i))
                        conn.commit()

def generate_omadika():
        cursor.execute("""SELECT AFM FROM GYMNASTIS WHERE kwdikos_gym=?""",(1,))
        afm_data1 = cursor.fetchall()
        
        cursor.execute("""SELECT AFM FROM GYMNASTIS WHERE kwdikos_gym=?""",(2,))
        afm_data2 = cursor.fetchall()
        onoma = ["Yoga","Yoga advanced","Pilates","Ζούμπα","Pilates advanced","Αερόβια","Αερόβια advanced"]
        orio_atomwn =[10,15,20]
        aithouses = ["Αίθουσα 1","Αίθουσα 2","Αίθουσα 3","Αίθουσα 4","Αίθουσα 5"]
        for i in range(1,100):
                onoma_omadikou = random.choice(onoma)
                orio = random.choice(orio_atomwn)
                aithousa = random.choice(aithouses)
                start_time, end_time, program_date = generate_omadiko_hours_day()
                if i<50:
                        afm1 = random.choice(afm_data1)[0]
                        if (check_for_valid_omadiko(aithousa, program_date, start_time, end_time) and check_for_working_hours(afm1, program_date, start_time, end_time)):
                                cursor.execute("""INSERT INTO OMADIKO_PROGRAMMA VALUES(?,?,?,?,?,?,?,?,?)""",(i,aithousa,orio,program_date,onoma_omadikou,start_time,end_time,1,1))
                                conn.commit()
                                cursor.execute("""INSERT INTO DIORGANONEI VALUES(?,?)""",(afm1,i))
                                conn.commit()
                                check_and_gen_equipement_availability(i,orio,program_date,end_time)
                                conn.commit()
                else:
                        afm2 = random.choice(afm_data2)[0]
                        if (check_for_valid_omadiko(aithousa, program_date, start_time, end_time) and check_for_working_hours(afm1, program_date, start_time, end_time)):
                                cursor.execute("""INSERT INTO OMADIKO_PROGRAMMA VALUES(?,?,?,?,?,?,?,?,?)""",(i,aithousa,orio,program_date,onoma_omadikou,start_time,end_time,2,1))
                                conn.commit()
                                cursor.execute("""INSERT INTO DIORGANONEI VALUES(?,?)""",(afm2,i))
                                conn.commit()
                                check_and_gen_equipement_availability(i,orio,program_date,end_time)
                                conn.commit()
       

if __name__ == "__main__":
        conn = sqlite3.connect(name_of_file)
        cursor = conn.cursor()
        generate_gyms()
        generate_melh()
        generate_new_syndromes()
        generate_gymnastes()
        generate_equiment()
        generate_programa_gym()
        generate_omadika()
        generate_symmetoxes()
        
        
                
               

        
               

                       

        print("Η βαση δεδομενων δημιουργηθηκε επιτυχως")
        conn.close()
