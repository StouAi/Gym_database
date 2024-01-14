import tkinter as tk
import sqlite3
import datetime
from datetime import datetime as dt

root = tk.Tk()
root.title("GETFIT GYM")
root.geometry("600x600")
name_of_file = 'gym_final.db'
# GYM buttons
def Gym_click(gym_number):
    gymid[0] = gym_number
    selected_gym_label.config(text=f"You selected the gym on {gymlabels[gym_number-1]['text']}")

gymid = [0]
gymlabels = []

# Connect to the SQLite database
conn = sqlite3.connect(name_of_file)
cursor = conn.cursor()

# Execute the query to fetch all gym information
cursor.execute("SELECT dieythinsi FROM GYMNASTIRIO")
rows = cursor.fetchall()

# Create buttons and labels for each gym
for i, row in enumerate(rows):
    gymlabels.append({"text": row[0]})
    button = tk.Button(root, text="GETFIT", padx=10, pady=10, fg="white", bg="black", command=lambda i=i: Gym_click(i+1))
    label = tk.Label(root, text=gymlabels[i]["text"])
    button.grid(row=1, column=i, padx=10, pady=10)
    label.grid(row=0, column=i, padx=10, pady=10)

selected_gym_label = tk.Label(root, text="")
selected_gym_label.grid(row=1, column=len(rows)+1, columnspan=2, padx=10, pady=10)




# Omadiko programa buttons
def Omadiko_click():
    if omadiko_label.cget("text") == "":
        current_date = datetime.date.today()
        conn = sqlite3.connect(name_of_file)
        cursor = conn.cursor()
        cursor.execute("""select  o.onoma,o.hmerominia
        from OMADIKO_PROGRAMMA as o,DIORGANONEI as d
        WHERE o.kwdikos_gym = ? and d.kwdikos_omadikou = o.kwdikos_omadikou and o.hmerominia > ?""",(gymid[0],current_date))
        
        # Get the results from the cursor
        results = cursor.fetchall()
        if not results:
            omadiko_label.config(text="Δεν υπάρχουν ομαδικά προγράμματα")
            conn.close()
        else:
        # Create a string to display the results
            result_str = ""
            for row in results:
                result_str += f"Όνομα: {row[0]}, Ημερομηνία: {row[1]}\n"
            conn.close()
        # Update the label with the results
            omadiko_label.config(text=result_str)
    else:
        omadiko_label.config(text="")

omadiko_btn = tk.Button(root, text="Ομαδικά Προγράμματα", padx=10, pady=10, fg="white", bg="black", command=lambda: Omadiko_click())
omadiko_btn.grid(row=2, column=0,columnspan=2, padx=10, pady=10)

omadiko_label = tk.Label(root, text="")
omadiko_label.grid(row=3, column=0,columnspan=2, padx=5, pady=5)

#gymnastes buttons
def Gymnastes_click():
    if gymnastes_label.cget("text") == "":
        conn = sqlite3.connect(name_of_file)
        cursor = conn.cursor()
        cursor.execute(f"""select onomateponimo
        from GYMNASTIS 
        WHERE kwdikos_gym = {gymid[0]}""")
        
        # Get the results from the cursor
        results = cursor.fetchall()
        conn.close()
        # Create a string to display the results
        result_str = ""
        for row in results:
            result_str += f"{row[0]}\n"
        
        # Update the label with the results
        gymnastes_label.config(text=result_str)
    else:
        gymnastes_label.config(text="")

gymnastes_btn = tk.Button(root, text="Γυμναστές", padx=10, pady=10, fg="white", bg="black", command=lambda: Gymnastes_click())
gymnastes_btn.grid(row=2, column=3,columnspan=2, padx=10, pady=10)
gymnastes_label = tk.Label(root, text="")
gymnastes_label.grid(row=3, column=3,columnspan=2, padx=5, pady=5)

# Eggrafh buttons


def Eggrafi_click():
    eggrafi_window = tk.Toplevel(root)
    eggrafi_window.title("Eggrafi Window")
    eggrafi_window.geometry("1000x800")

    # Create labels and input boxes
    stoixeia = tk.Label(eggrafi_window, text="Συμπληρώστε τα στοιχεία σας")
    stoixeia.grid(row=2, column=0,columnspan=2, padx=10, pady=10)

    onoma_eponimo = tk.Entry(eggrafi_window)
    onoma_eponimo.insert(0, "Όνομα Επώνυμο")  # Insert default text
    onoma_eponimo.bind("<FocusIn>", lambda event: onoma_eponimo.delete(0, "end"))  # Delete default text on focus
    onoma_eponimo.grid(row=3, column=0, padx=10, pady=10)

    telephone = tk.Entry(eggrafi_window)
    telephone.insert(0, "Τηλέφωνο")  # Insert default text
    telephone.bind("<FocusIn>", lambda event: telephone.delete(0, "end"))  # Delete default text on focus
    telephone.grid(row=3, column=1, padx=10, pady=10)

    syndro = tk.Label(eggrafi_window, text="""Τα γυμναστήρια μας παρέχουν συνδρομες τριων βαθμίδων.Απλή,Σπέσιαλ και Χρυσή\nΜε την απλή 
                      εχετε δωρεάν πρόσβαση σε όλο τον εξοπλισμό του γυμναστηρίου καθως και σε προσωπικό προγραμμα εκγύμνασης γραμμενο απο τους γυμναστές μας.
                      Με την "Σπέσιαλ" έχετε επιπλέον δωρεάν πρόσβαση στα ομαδικά μας προγράμματα.Τέλος η "Χρυσή" σας δινει και δωρεαν πρόσβαση
                      σε personal training.Μπορείτε να επιλέξετε συνδρομη διαρκειας 1,3,6 ή 12 μηνών.""")
    syndro.grid(row=4, column=0,columnspan=2, padx=10, pady=10)

    tier = tk.Entry(eggrafi_window)
    tier.insert(0, "βαθμίδα")  # Insert default text
    tier.bind("<FocusIn>", lambda event: tier.delete(0, "end"))  # Delete default text on focus
    tier.grid(row=5, column=0, padx=10, pady=10)

    diarkeia = tk.Entry(eggrafi_window)
    diarkeia.insert(0, "Διάρκεια(σε μήνες)")  # Insert default text
    diarkeia.bind("<FocusIn>", lambda event: diarkeia.delete(0, "end"))  # Delete default text on focus
    diarkeia.grid(row=5, column=1, padx=10, pady=10)
    kostos = tk.Label(eggrafi_window, text="Κόστος:Για 'Απλή' ειναι 10 ευρω/μηνα,για 'Σπέσιαλ' ειναι 20 ευρω/μηνα και για 'Χρυσή' ειναι 30 ευρω/μηνα")
    kostos.grid(row=6, column=0,columnspan=2, padx=10, pady=10)
    submit = tk.Button(eggrafi_window, text="Υποβολή", padx=10, pady=10, fg="white", bg="black",command=lambda: submit_click())
    submit.grid(row=7, column=0,columnspan=2 ,padx=10, pady=10)
    
    conn = sqlite3.connect(name_of_file)
    cursor.execute("SELECT dieythinsi FROM GYMNASTIRIO")
    rows = cursor.fetchall()
    conn.close()
    def Gym_click2(gym_number):
        gymid[0] = gym_number
        selected_gym_label2.config(text=f"You selected the gym on {gymlabels[gym_number-1]['text']}")
# Create buttons and labels for each gym
    for i, row in enumerate(rows):
        gymlabels.append({"text": row[0]})
        button = tk.Button(eggrafi_window, text="GETFIT", padx=10, pady=10, fg="white", bg="black", command=lambda i=i: Gym_click2(i+1))
        label = tk.Label(eggrafi_window, text=gymlabels[i]["text"])
        button.grid(row=1, column=i, padx=10, pady=10)
        label.grid(row=0, column=i, padx=10, pady=10)

    selected_gym_label2 = tk.Label(eggrafi_window, text="")
    selected_gym_label2.grid(row=1, column=len(rows)+1, columnspan=2, padx=10, pady=10)
    def submit_click():
        onoma_eponimo_value = onoma_eponimo.get()
        telephone_value = telephone.get()
        tier_value = tier.get()
        diarkeia_value = int(diarkeia.get())
        if tier_value == "Απλή":
            tier_price = 10
        elif tier_value == "Σπέσιαλ":
            tier_price = 20
        else:
            tier_price = 30
        print(onoma_eponimo_value, telephone_value, tier_value, diarkeia_value)
        conn = sqlite3.connect(name_of_file)
        cursor = conn.cursor()
        cursor.execute("""SELECT MAX(kwdikos_syndromis) 
                        FROM SYNDROMI""")
        last_id = cursor.fetchone()[0]
        cursor.execute("""SELECT MAX(kwdikos_melous) from MELOS """)
        last_id2 = cursor.fetchone()[0]
        conn.close()
        
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=diarkeia_value*30)
        conn = sqlite3.connect(name_of_file)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO MELOS VALUES(?,?,?)",(last_id2+1,onoma_eponimo_value,telephone_value))
        conn.commit()
        cursor.execute("INSERT INTO SYNDROMI VALUES(?,?,?,?,?,?,?)", (last_id+1, tier_price*diarkeia_value, tier_value, gymid[0], today, end_date,last_id2+1))
        conn.commit()
        conn.close()
        onoma_eponimo.delete(0, "end")
        telephone.delete(0, "end")
        tier.delete(0, "end")
        diarkeia.delete(0, "end")
        confirmation = tk.Label(eggrafi_window, text="Επιτυχής Εγγραφή.Μπορειτε να κλεισετε το παραθυρο.Ο κωδικός σας ειναι: "+str(last_id2+1))
        confirmation.grid(row=8, column=0,columnspan=2, padx=10, pady=10)

eggrafi_btn = tk.Button(root, text="ΕΓΓΡΑΦΗ", padx=10, pady=10, fg="white", bg="black", command=Eggrafi_click)
eggrafi_btn.grid(row=5, column=0, padx=10, pady=10)


def get_working_days(coach_n):
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()

    cursor.execute("SELECT meres_ergasias from GYMNASTIS WHERE onomateponimo = ?", (coach_n))
    res = cursor.fetchone()

    conn.close()

    return res[0] if res else ""

def get_working_hours(coach_n):
    hours = []
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()

    cursor.execute("SELECT ora_enarxis, ora_lixis from GYMNASTIS WHERE onomateponimo = ?", (coach_n))
    res = cursor.fetchall()
    for hour in res:
        hours.append(hour)
    return hours

def return_AFM(coach_name):
    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    cursor.execute("SELECT AFM from GYMNASTIS WHERE onomateponimo=?", (coach_name))
    tr_AFM_res = cursor.fetchone()
    return tr_AFM_res[0]
 
def check_for_valid_appointment(cursor, coach_afm, date_s, start_time, end_time):
    query = """
    SELECT COUNT(*) AS count
    FROM GYMNASTIS
    WHERE AFM = ?
        AND ? BETWEEN ora_enarxis AND ora_lixis
        AND ? <= ora_lixis
        AND ? >= ora_enarxis
        AND ? NOT IN (
            SELECT ora_enarxis
            FROM PERSONAL_TRAINING
            WHERE kwdikos_ranteboy IN (
                SELECT kwdikos_ranteboy
                FROM RANTEBOY
                WHERE tr_AFM = ?
                    AND hmerominia = ?
            )
            UNION
            SELECT ora_lixis
            FROM PERSONAL_TRAINING
            WHERE kwdikos_ranteboy IN (
                SELECT kwdikos_ranteboy
                FROM RANTEBOY
                WHERE tr_AFM = ?
                    AND hmerominia = ?
            )
        );
    """
    cursor.execute(query, (coach_afm, start_time, end_time, start_time, end_time, coach_afm, date_s, coach_afm, date_s))
    result = cursor.fetchone()[0]

    return result

def check_for_working_day(date_s, coach_name, time_start, time_end):
    AFM = return_AFM(coach_name)
    
    if AFM is None:
        print("Cannot check availability for this coach")

    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()

    cursor.execute("SELECT meres_ergasias from GYMNASTIS WHERE onomateponimo = ?", (coach_name))
    working_days_res = cursor.fetchone()
    working_days = working_days_res[0]


    selected_date = dt.strptime(date_s, "%Y-%m-%d").strftime("%A")

    
    if check_for_valid_appointment(cursor, AFM, date_s, time_start, time_end):
        print("The appointment is valid")
    else:
        print("The appointment is notvalid")
        return False
    
    if selected_date not in working_days:
        return False

    cursor.execute("""
            SELECT COUNT(*) 
            FROM PERSONAL_TRAINING pt
            JOIN RANTEBOY r ON pt.kwdikos_ranteboy = r.kwdikos_ranteboy
            WHERE tr_AFM = ? AND hmerominia = ?
        """, (AFM, date_s))

    existing_sessions_count = cursor.fetchone()[0]

    if existing_sessions_count > 0:
        return False

    return True


# Personal_Buttons
def personal_click(melos_kwdikos, bathmida):

    if bathmida == 'Απλή':
        cost = 20
    elif bathmida == 'Σπέσιαλ':
        cost = 20
    else:
        cost = 0
    personal_window = tk.Toplevel(root)
    personal_window.title("Personal Window")
    personal_window.geometry("1200x1000")
    access = [0]
    # Tables and Inputs
    stoixeia_personal = tk.Label(personal_window, text = "Επιλέξτε ένα ραντεβού με κάποιον από τους γυμναστές μας")
    stoixeia_personal.grid(row = 2, column = 0, columnspan=2, padx = 10, pady = 10)

    paratirisi = tk.Label(personal_window, text = "Παρακαλώ συμπληρώστε την ημερομηνία που θα επιθυμούσατε, σε μορφή YYYY-MM-DD καθώς και την ώρα έναρξης και λήξης σε μορφή HH-MM-SS")
    paratirisi.grid(row = 3, column = 0, columnspan=2, padx = 10, pady = 10)

    # Date Input
    date_personal = tk.Entry(personal_window)
    date_personal.insert(0, "Ημερομηνία") 
    date_personal.bind("<FocusIn>", lambda event: date_personal.delete(0, "end"))
    date_personal.grid(row = 4, column = 0, padx = 10, pady = 10)

    # Time Input
    time_start = tk.Entry(personal_window)
    time_start.insert(0, "Ώρα έναρξης")
    time_start.bind("<FocusIn>", lambda event: time_start.delete(0, "end"))
    time_start.grid(row = 4, column = 1, padx = 10, pady = 10)

    time_end = tk.Entry(personal_window)
    time_end.insert(0, "Ώρα λήξης")
    time_end.bind("<FocusIn>", lambda event: time_end.delete(0, "end"))
    time_end.grid(row = 4, column = 2, padx = 10, pady = 10)


    submit_b = tk.Button(personal_window, text="Submit Personal", padx=10, pady=10, fg="white", bg="black",command=lambda: submit_personal())    
    submit_b.grid(row = 5, column = 0, padx = 10, pady = 10)

    # List of available coaches
    coach_list = tk.Listbox(personal_window, selectmode= tk.SINGLE)
    coach_list.grid(row=4, column=3, padx=10, pady=10, sticky=tk.NS, columnspan=2)

    scrollbar_coach = tk.Scrollbar(personal_window, command = coach_list.yview)
    scrollbar_coach.grid(row=4, column=5, padx=(0, 10), pady=10, sticky=tk.NS)

    coach_list.config(yscrollcommand=scrollbar_coach.set)

    conn = sqlite3.connect(name_of_file)
    cursor = conn.cursor()
    cursor.execute(f"""SELECT onomateponimo from GYMNASTIS WHERE kwdikos_gym = ?""", (gymid[0], ))
    coaches = cursor.fetchall()
    if (coaches):
        for coach in coaches:
            coach_list.insert(tk.END, coach)
            # print(coach)



    # Button for submission
    def submit_personal():
        date_personal_val = date_personal.get()
        time_start_val = time_start.get()
        time_end_val = time_end.get()
        if(coach_list):
            selected_coach = coach_list.get(coach_list.curselection())
            if check_for_working_day(date_personal_val, selected_coach, time_start_val, time_end_val):
                cursor.execute("""SELECT kwdikos_ranteboy from RANTEBOY ORDER BY kwdikos_ranteboy DESC""")
                kwdikos_rantebou_res = cursor.fetchone()
                if kwdikos_rantebou_res is None:
                    kwdikos_rantebou_res = 0
                else:
                    kwdikos_rantebou_res = int(kwdikos_rantebou_res[0])
                cursor.execute("""SELECT kwdikos_personal FROM PERSONAL_TRAINING ORDER BY kwdikos_personal DESC""")
                kwdikos_personal_res = cursor.fetchone()
                if kwdikos_personal_res is None:
                    kwdikos_personal_res = 0
                else:
                    kwdikos_personal_res = int(cursor.fetchone()[0])
                is_working = tk.Label(personal_window, text = f"""Σας ευχαριστούμε, το ραντεβού σας είναι με τον {selected_coach} εν ώρα {time_start_val} - {time_end_val} και ημερομηνία {date_personal_val}.
                                    Θα σας κοστίσει {cost} ευρώ""")
                is_working.grid(row = 6, column = 0, padx = 10, pady = 10)
                cursor.execute(f"""INSERT INTO RANTEBOY VALUES (?, ?, ?, ?, ?, ?, ?)""", (kwdikos_rantebou_res + 1, return_AFM(selected_coach), melos_kwdikos, cost, date_personal_val, time_start_val, time_end_val))
                cursor.execute(f"""INSERT INTO PERSONAL_TRAINING VALUES (?, ?, ?,?)""", (kwdikos_personal_res + 1, 1, kwdikos_rantebou_res + 1))
                conn.commit()
                cursor.execute("""SELECT * FROM RANTEBOY""")
                res = cursor.fetchall()
                for i in res:
                    print(i)
            else:
                is_working = tk.Label(personal_window, text = "O επιλεγμένος γυμναστής ΔΕΝ είναι διαθέσιμος αυτήν την ημερομηνία")
                is_working.grid(row = 6, column = 0, padx = 10, pady = 10)
            
    # Function to display working_days
    def on_coach_select(event):
        selected_coach = coach_list.get(coach_list.curselection())
        print("Selected coach: ", selected_coach)
        meres = tk.Label(personal_window, text = "Μέρες εργασίας: " + get_working_days(selected_coach))
        meres.grid(row = 5, column = 3,  padx = 20, pady = 10)
        ores_ergasias = tk.Label(personal_window, text = "Ώρες εργασίας: " + str(get_working_hours(selected_coach)[0]))
        ores_ergasias.grid(row = 6, column = 3,  padx = 20, pady = 10)
    coach_list.bind("<<ListboxSelect>>", on_coach_select)

# Syndesi buttons

def Syndesi_click():
    syndesi_window = tk.Toplevel(root)
    syndesi_window.title("Syndesi Window")
    syndesi_window.geometry("800x800")
    access=[0]
    # Create labels and input boxes
    stoixeia = tk.Label(syndesi_window, text="Συμπληρώστε τα στοιχεία σας")
    stoixeia.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    onoma_eponimo = tk.Entry(syndesi_window)
    onoma_eponimo.insert(0, "Όνομα Επώνυμο")  # Insert default text
    onoma_eponimo.bind("<FocusIn>", lambda event: onoma_eponimo.delete(0, "end"))  # Delete default text on focus
    onoma_eponimo.grid(row=3, column=0, padx=10, pady=10)

    melos_code = tk.Entry(syndesi_window)
    melos_code.insert(0, "Κωδικός Μέλους")  # Insert default text
    melos_code.bind("<FocusIn>", lambda event: melos_code.delete(0, "end"))  # Delete default text on focus
    melos_code.grid(row=3, column=1, padx=10, pady=10)
    login_btn = tk.Button(syndesi_window, text="Σύνδεση", padx=10, pady=10, fg="white", bg="black",command=lambda: syndload_click())
    login_btn.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    stoixeia.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    bathmida = tk.Entry(syndesi_window)
    bathmida.insert(0, "Βαθμίδα")  # Insert default text
    bathmida.bind("<FocusIn>", lambda event: bathmida.delete(0, "end"))  # Delete default text on focus
    bathmida.grid(row=8, column=0, padx=10, pady=10)

    diarkeia = tk.Entry(syndesi_window)
    diarkeia.insert(0, "Διάρκεια")  # Insert default text
    diarkeia.bind("<FocusIn>", lambda event: diarkeia.delete(0, "end"))  # Delete default text on focus
    diarkeia.grid(row=8, column=1, padx=10, pady=10)

    gymplace_var = tk.StringVar()
    gymplace_var.set("Μαιζώνος 13")

    gymplace_checkbox1 = tk.Checkbutton(syndesi_window, text="Μαιζώνος 13", variable=gymplace_var, onvalue="Μαιζώνος 13")
    gymplace_checkbox2 = tk.Checkbutton(syndesi_window, text="Κορίνθου 35", variable=gymplace_var, onvalue="Κορίνθου 35")

    gymplace_checkbox1.grid(row=9, column=0, padx=10, pady=10)
    gymplace_checkbox2.grid(row=9, column=1, padx=10, pady=10)
    bathmida.grid_remove()
    diarkeia.grid_remove()
    gymplace_checkbox1.grid_remove()
    gymplace_checkbox2.grid_remove()

    def syndload_click():
        stoixeia.config(text="")
        melos_code_value = melos_code.get()
        onoma_eponimo_value = onoma_eponimo.get()
        conn = sqlite3.connect(name_of_file)
        cursor = conn.cursor()
        cursor.execute(f"""SELECT s.kwdikos_melous
        from SYNDROMI as s,MELOS as m
        WHERE s.kwdikos_melous = {melos_code_value} AND m.onomateponimo = '{onoma_eponimo_value}' """)
        melos = cursor.fetchone()
        conn.close()
        if melos is None:
            statuslabel.config(text="Δεν υπάρχει μέλος με αυτόν τον κωδικό κάντε εγγραφή")
        else:
            current_date = datetime.date.today()
            conn = sqlite3.connect(name_of_file)
            cursor = conn.cursor()
            cursor.execute("""SELECT hmerominia_lixis
            from SYNDROMI 
            WHERE kwdikos_melous = ? and hmerominia_lixis > ? """,(melos_code_value,current_date))
            result = cursor.fetchone()
            conn.close()
            if  result  is None:
                # Create labels and input boxes
                bathmida.grid()
                diarkeia.grid()
                gymplace_checkbox1.grid()
                gymplace_checkbox2.grid()
                statuslabel.config(text="Η ημερομηνία λήξης έχει παρέλθει.Καντε ανανέωση συνδρομής")
                
                ananewsi_btn = tk.Button(syndesi_window, text="Ανανέωση", padx=10, pady=10, fg="white", bg="black",command=lambda: sumbit_ananewsh())
                ananewsi_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10)
                ananewsi_btn.grid()
                def update_gymid():
                    global gymid
                    if gymplace_var.get() == "Μαιζώνος 13":
                        gymid[0] = 1
                    elif gymplace_var.get() == "Κορίνθου 35":
                        gymid[0] = 2

                gymplace_checkbox1.config(command=update_gymid)
                gymplace_checkbox2.config(command=update_gymid)
            
        
            else:
                statuslabel.config(text="Επιτυχής Σύνδεση")
                conn = sqlite3.connect(name_of_file)
                cursor = conn.cursor()
                cursor.execute("""Select kwdikos_syndromis,bathmida,kwdikos_gym,kwdikos_melous,hmerominia_lixis
                               from SYNDROMI 
                                WHERE kwdikos_melous = ? and hmerominia_lixis > ? """,(melos_code_value,current_date))
                result = cursor.fetchone()
                conn.close()
                syndromi_label = tk.Label(syndesi_window, text=f"""
                                          Tα στοιχεία σας ειναι
                                          Κωδικος Μέλους: {result[3]}
                                          Βαθμίδα: {result[1]}
                                          Ημερομηνία λήξης συνδρομής: {result[4]}""")
                syndromi_label.grid(row=10, column=0, columnspan=2, padx=10, pady=10)
                kwd_mel = result[3]
                bathmida_kwd = result[1] 
                conn = sqlite3.connect(name_of_file)
                current_date = datetime.date.today()
                cursor = conn.cursor()
                cursor.execute("""SELECT OP.kwdikos_omadikou,OP.onoma,OP.aithousa,OP.hmerominia,OP.ora_enarxis,Op.ora_lixis
                    FROM OMADIKO_PROGRAMMA OP
                    LEFT JOIN (
                    SELECT kwdikos_omadikou, COUNT(*) as count
                    FROM SYMMETEXEI
                    GROUP BY kwdikos_omadikou
                    ) S ON OP.kwdikos_omadikou = S.kwdikos_omadikou
                    WHERE (S.count IS NULL OR S.count < OP.orio_atomon) and OP.kwdikos_gym=? and OP.hmerominia > ?;""",(result[2],current_date))
            
                omadik_info = cursor.fetchall()
                conn.close()
                omadik_label = tk.Label(syndesi_window, text="Τα διαθέσιμα ομαδικά προγράμματα ειναι:")
                omadik_label.grid(row=11, column=0, columnspan=2, padx=10, pady=10)
                omadik_str = ""
                check_vars = {}
                conn = sqlite3.connect(name_of_file)
                cursor = conn.cursor()
                row_number = 12
                for omadik_row in omadik_info:
                    omadik_str = f"Όνομα: {omadik_row[1]},{omadik_row[2]}, Ημερομηνία: {omadik_row[3]}, Ώρα Έναρξης: {omadik_row[4]}, Ώρα Λήξης: {omadik_row[5]}\n"
                    omadik_label = tk.Label(syndesi_window, text=omadik_str)
                    omadik_label.grid(row=row_number, column=0, padx=10, pady=10)

                    check_var = tk.IntVar()
                    cursor.execute("""SELECT kwdikos_melous from SYMMETEXEI where kwdikos_omadikou = ? and kwdikos_melous = ?""",(omadik_row[0],melos_code_value))
                    applic=cursor.fetchone()
                    if applic is None:
                        omadik_check = tk.Checkbutton(syndesi_window,text='δηλωσε συμμετοχη', variable=check_var)
                        omadik_check.grid(row=row_number, column=1, padx=10, pady=10)
                        check_vars[omadik_row] = check_var
                    else:
                        already_applied = tk.Label(syndesi_window, text="Εχετε ηδη δηλωσει συμμετοχη σε αυτο το ομαδικο προγραμμα")
                        already_applied.grid(row=row_number, column=1, padx=10, pady=10)

                        delete_button = tk.Button(syndesi_window, text="Διαγραφή Συμμετοχής", command=lambda omadik_row=omadik_row: delete_symmetexei(omadik_row))
                        delete_button.grid(row=row_number, column=2, padx=10, pady=10)

                    # Store the Checkbutton variable and the row data in the dictionary

                    row_number += 1

                dhlwsh_btn = tk.Button(syndesi_window, text="Δήλωση Συμμετοχης", padx=10, pady=10, fg="white", bg="black",command=lambda: dhlwsh_click())
                dhlwsh_btn.grid(row=row_number+1, column=0, columnspan=2, padx=10, pady=10)
                personal_label = tk.Label(syndesi_window, text = "Αν θέλετε να κλείσετε Personal Training παρακαλώ πατήστε εδώ: ")
                personal_label.grid(row = row_number+2, column = 0, columnspan = 2, padx = 12, pady = 12)
                personal_button = tk.Button(syndesi_window, text = "Personal Training", padx=12, pady=12, fg="white", bg="black", command = lambda : personal_click(kwd_mel, bathmida_kwd))
                personal_button.grid(row = row_number+3, column = 0, columnspan = 2, padx = 12, pady = 12)

                def dhlwsh_click():
                    if result[1] == "Απλή":
                        kostos =10
                    else:
                        kostos = 0
                    conn = sqlite3.connect(name_of_file)
                    cursor = conn.cursor()

                    # Iterate over the check_vars dictionary
                    for  row ,var in check_vars.items():
                        # If the Checkbutton is selected, insert the row data into the SYMMETEXEI table
                        if var.get() == 1:
                            cursor.execute("""INSERT INTO SYMMETEXEI VALUES(?,?,?)""", (melos_code_value,row[0],kostos))

                    conn.commit()
                    conn.close()
                
                def delete_symmetexei(omadik_row):
                    conn = sqlite3.connect(name_of_file)
                    cursor = conn.cursor()

                    cursor.execute("""DELETE FROM SYMMETEXEI WHERE kwdikos_omadikou = ? AND kwdikos_melous = ?""", (omadik_row[0], melos_code_value))

                    conn.commit()
                    conn.close()
                                    

                
                
        def sumbit_ananewsh():
            bathmida.grid_remove()
            diarkeia.grid_remove()
            gymplace_checkbox1.grid_remove()
            gymplace_checkbox2.grid_remove()
            conn = sqlite3.connect(name_of_file)
            cursor = conn.cursor()
            bathmida_value = bathmida.get()
            diarkeia_value = int(diarkeia.get())
            if bathmida_value == "Απλή":
                bathmida_price = 10
            elif bathmida_value== "Σπέσιαλ":
                bathmida_price = 20
            else:
                bathmida_price = 30
            today = datetime.date.today()
            end_date = today + datetime.timedelta(days=diarkeia_value*30)
            cursor.execute("""SELECT kwdikos_syndromis FROM SYNDROMI ORDER by kwdikos_syndromis DESC""")
            last_id = int(cursor.fetchone()[0])
            cursor.execute(f"""INSERT INTO SYNDROMI VALUES(?,?,?,?,?,?,?)""",(last_id+1,bathmida_price*diarkeia_value,bathmida_value,gymid[0],today,end_date,melos_code_value))
            conn.commit()
            conn.close()
            bathmida.grid_remove()
            diarkeia.grid_remove()
            gymplace_checkbox1.grid_remove()
            gymplace_checkbox2.grid_remove()
            ananewsi_btn.grid_remove()
    statuslabel = tk.Label(syndesi_window, text="")
    statuslabel.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    
    

syndesi_btn = tk.Button(root, text="ΣΥΝΔΕΣΗ", padx=10, pady=10, fg="white", bg="black",command=Syndesi_click)
syndesi_btn.grid(row=5, column=1, padx=10, pady=10)


root.mainloop()