__author__ = "red Ant"

# importing required libraries 
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from datetime import date
from tkinter.messagebox import askyesno
from tkinter.messagebox import showwarning
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename

backgroundcolor = "pink"
today = date.today()

# Creating app instance
app = ThemedTk(theme="radiance")
#  ======== app properties ========
app.title("Management")  # app title
app.geometry("1280x800")
app.configure(background=backgroundcolor)
# =================================
# ====== Frames =====
top_frame = Frame(app, border=5, background=backgroundcolor, relief=RIDGE)
top_frame.grid(row=0, column=0, sticky="new")
# -----------------
right_frame_receipt = Frame(app, border=5, relief=RIDGE)
right_frame_receipt.place(x=30, y=381)
# ----
right_frame = Frame(app, border=5, relief=RIDGE, background=backgroundcolor, width=720, height=710)
right_frame.grid(row=0, column=1, sticky="nesw")
# ----------
button_frame = Frame(app, border=5, relief=RIDGE, background=backgroundcolor)
button_frame.grid(row=1, column=1, ipady=4, sticky="sw")
# -----------------
# ========= ---------00000000000 -------- =======
# ========= Styles ======
style = ttk.Style()
style.configure("TButton", width=14)
# --------
# ===================
# --------- ========= Definition ======== -------
# ------ General definition------


def Exit():
    iExit = askyesno("Attention", "Tu es dans le chemin de quitter\nEst-ce-que tu vais vraiment quitter.")
    if iExit > 0:
        app.destroy()
    else:
        return
        
# --------------------------------------
# ------Calcule Total variable--------


Total_Gen = 0
# --------------
# ------- Menu button definition -------


def SoftDrinks():
    return


def Alcohol():
    return


def Vins():
    return


def WhiskyVodka():
    return


def Pains():
    global Total_Gen

    right_frame = Frame(app, border=5, relief=RIDGE, width=720, height=710, background=backgroundcolor)
    right_frame.grid(row=0, column=1, sticky="nesw")

    global E_sandwich_vide
    global E_sandwich_vegetarien
    global E_sandwich_jambon_ou_fromage
    global E_sandwich_jambon_et_Fromage
    global E_sandwich_poulet
    global E_sandwich_thon
    global E_sandwich_club
    global E_hamburger
    global E_cheeseburger
    global E_croque_monsieur
    global E_croque_madame
    # ------------
    def addPain():
        global Total_Gen
        global item5
        global item6
        global item7
        global item8
        global item9
        global item10
        global item11
        global item12
        global item13
        global item14
        global item15
        # ====== Pains ==========
        item5 = round(float(E_sandwich_vide.get()))
        item6 = round(float(E_sandwich_vegetarien.get()))
        item7 = round(float(E_sandwich_jambon_ou_fromage.get()))
        item8 = round(float(E_sandwich_jambon_et_Fromage.get()))
        item9 = round(float(E_sandwich_poulet.get()))
        item10 = round(float(E_sandwich_thon.get()))
        item11 = round(float(E_sandwich_club.get()))
        item12 = round(float(E_hamburger.get()))
        item13 = round(float(E_cheeseburger.get()))
        item14 = round(float(E_croque_monsieur.get()))
        item15 = round(float(E_croque_madame.get()))
        # ------ Prices -------
        p5 = int(1500)
        p6 = int(3500)
        p7 = int(3000)
        p8 = int(4000)
        p9 = int(5000)
        p10 = int(5000)
        p11 = int(4500)
        p12 = int(6000)
        p13 = int(7000)
        p14 = int(3500)
        p15 = int(4500)
        # -----------------
        p5_5 = 0
        p6_6 = 0
        p7_7 = 0
        p8_8 = 0
        p9_9 = 0
        p10_10 = 0
        p11_11 = 0
        p12_12 = 0
        p13_13 = 0
        p14_14 = 0
        p15_15 = 0


        # ---------------------
        if item5 > 0:
            forma = ("Sandwich vide:", str(item5), str(p5),)
            fields = "{0:25}{1:25}{2:25}\n".format(forma[0], forma[1], "x"+forma[2])
            txt_receipt.insert(END, fields)
            #txt_receipt.insert(END, f"\nSandwich vide:\t\t\t" + str(item5) + "\t\t\tx" + str(p5) + "Fbu")
            p5_5 = p5*item5
        if item6 > 0:
            forma = ("Sandwich végetarien:", str(item6), str(p6),)
            fields = "{0:25}{1:25}{2:25}\n".format(forma[0], forma[1], "x"+forma[2])
            txt_receipt.insert(END, fields)
            #txt_receipt.insert(END, f"\nSandwich végetarien:\t\t\t" + str(item6) + "\t\t\tx" + str(p6) + "Fbu")
            p6_6 = p6*item6
        if item7 > 0:
            forma = ("Sandwich JambonOuFromage:", str(item7), str(p7),)
            fields = "{0:25}{1:25}{2:25}\n".format(forma[0], forma[1], "x"+forma[2])
            txt_receipt.insert(END, fields)
            #txt_receipt.insert(END, f"\nSandwich\nJambon ou Fromage:\t\t\t" + str(item7) + "\t\t\tx" + str(p7) + "Fbu")
            p7_7 = p7*item7
        if item8 > 0:
            forma = ("Sandwich Jambon+Fromage:", str(item8), str(p8),)
            fields = "{0:25}{1:25}{2:25}\n".format(forma[0], forma[1], "x"+forma[2])
            txt_receipt.insert(END, fields)
            #txt_receipt.insert(END, f"\nSandwich\nJambon+Fromage:\t\t\t" + str(item8) + "\t\t\tx" + str(p8) + "Fbu")
            p8_8 = p8*item8
        if item9 > 0:
            forma = ("Sandwich au Poulet:", str(item9), str(p9),)
            fields = "{0:25}{1:25}{2:25}\n".format(forma[0], forma[1], "x"+forma[2])
            txt_receipt.insert(END, fields)
            #txt_receipt.insert(END, f"\nSandwich au Poulet:\t\t\t" + str(item9) + "\t\t\tx" + str(p9) + "Fbu")
            p9_9 = p9*item9
        if item10 > 0:
            forma = ("Sandwich au Thon:", str(item10), str(p10),)
            fields = "{0:25}{1:25}{2:25}\n".format(forma[0], forma[1], "x"+forma[2])
            txt_receipt.insert(END, fields)
            #txt_receipt.insert(END, f"\nSandwich au Thon:\t\t\t" + str(item10) + "\t\t\tx" + str(p10) + "Fbu")
            p10_10 = p10*item10
        if item11 > 0:
            forma = ("Sandwich Club:", str(item11), str(p11),)
            fields = "{0:25}{1:25}{2:25}\n".format(forma[0], forma[1], "x"+forma[2])
            txt_receipt.insert(END, fields)
            #txt_receipt.insert(END, f"\nSandwich Club:\t\t\t" + str(item11) + "\t\t\tx" + str(p11) + "Fbu")
            p11_11 = p11*item11
        if item12 > 0:
            forma = ("Hamburger:", str(item12), str(p12),)
            fields = "{0:25}{1:25}{2:25}\n".format(forma[0], forma[1], "x"+forma[2])
            txt_receipt.insert(END, fields)
            #txt_receipt.insert(END, f"\nHamburger:\t\t\t" + str(item12) + "\t\t\tx" + str(p12) + "Fbu")
            p12_12 = p12*item12
        if item13 > 0:
            forma = ("Cheeseburger:", str(item13), str(p13),)
            fields = "{0:25}{1:25}{2:25}\n".format(forma[0], forma[1], "x"+forma[2])
            txt_receipt.insert(END, fields)
            #txt_receipt.insert(END, f"\nCheeseburger:\t\t\t" + str(item13) + "\t\t\tx" + str(p13) + "Fbu")
            p13_13 = p13*item13
        if item14 > 0:
            forma = ("Croque Monsieur:", str(item14), str(p14),)
            fields = "{0:25}{1:25}{2:25}\n".format(forma[0], forma[1], "x"+forma[2])
            txt_receipt.insert(END, fields)
            #txt_receipt.insert(END, f"\nCroque Monsieur:\t\t\t" + str(item14) + "\t\t\tx" + str(p14) + "Fbu")
            p14_14 = p14*item14
        if item15 > 0:
            forma = ("Croque Madame:", str(item15), str(p15),)
            fields = "{0:25}{1:25}{2:25}\n".format(forma[0], forma[1], "x"+forma[2])
            txt_receipt.insert(END, fields)
            #txt_receipt.insert(END, f"\nCroque Madame:\t\t\t" + str(item15) + "\t\t\tx" + str(p15) + "Fbu")
            p15_15 = p15*item15

        if item5 == 0 and item6 == 0 and item7 == 0 and item8 == 0 and item9 == 0 and item10 == 0 and item11 == 0 and item12 == 0 and item13 == 0 and item14 == 0 and item15:
            txt_receipt.insert(END, "")
        E_sandwich_vide.set(0)
        E_sandwich_vegetarien.set(0)
        E_sandwich_jambon_ou_fromage.set(0)
        E_sandwich_jambon_et_Fromage.set(0)
        E_sandwich_poulet.set(0)
        E_sandwich_thon.set(0)
        E_sandwich_club.set(0)
        E_hamburger.set(0)
        E_cheeseburger.set(0)
        E_croque_monsieur.set(0)
        E_croque_madame.set(0)
        # ----- Calculer Total ---
        Tot2 = (p5_5) + (p6_6) + (p7_7) + (p8_8) + (p9_9) + (p10_10) + (p11_11) + (p12_12) + (p13_13) + (p14_14) + (p15_15)
        Total_Gen += Tot2
    # ------------
    ajouter_btn = ttk.Button(button_frame, text="AJOUTER", style="TButton", command=addPain)
    ajouter_btn.grid(row=0, column=0, padx=2, pady=7)
    # ------------
    E_sandwich_vide = StringVar()
    E_sandwich_vegetarien = StringVar()
    E_sandwich_jambon_ou_fromage = StringVar()
    E_sandwich_jambon_et_Fromage = StringVar()
    E_sandwich_poulet = StringVar()
    E_sandwich_thon = StringVar()
    E_sandwich_club = StringVar()
    E_hamburger = StringVar()
    E_cheeseburger = StringVar()
    E_croque_monsieur = StringVar()
    E_croque_madame = StringVar()
    # ----------

    E_sandwich_vide.set(0)
    E_sandwich_vegetarien.set(0)
    E_sandwich_jambon_ou_fromage.set(0)
    E_sandwich_jambon_et_Fromage.set(0)
    E_sandwich_poulet.set(0)
    E_sandwich_thon.set(0)
    E_sandwich_club.set(0)
    E_hamburger.set(0)
    E_cheeseburger.set(0)
    E_croque_monsieur.set(0)
    E_croque_madame.set(0)

    lbl_sandwich_vide = Label(right_frame, text="Sandwich Vide", font=("courier", 14, "bold"), background=backgroundcolor)
    lbl_sandwich_vide.grid(row=0, column=0, sticky="w")

    entry_sandwich_vide = Spinbox(right_frame,  background=backgroundcolor, from_=0, to=50, width=6, textvariable=E_sandwich_vide)
    entry_sandwich_vide.grid(row=0, column=1, pady=4)
    # -------------
    lbl_sandwich_vegetarien = Label(right_frame, text="Sandwich Végetarian", font=("courier", 14, "bold"), background=backgroundcolor)
    lbl_sandwich_vegetarien.grid(row=1, column=0, sticky="w")

    entry_sandwich_vegetarien = Spinbox(right_frame,  background=backgroundcolor, from_=0, to=50, width=6, textvariable=E_sandwich_vegetarien)
    entry_sandwich_vegetarien.grid(row=1, column=1, pady=4)
    # -------------
    lbl_sandwich_jambon_ou_fromage = Label(right_frame, text="Sandwich\nJambonOuFromage", font=("courier", 14, "bold"), background=backgroundcolor)
    lbl_sandwich_jambon_ou_fromage.grid(row=2, column=0, sticky="w")

    entry_sandwich_jambon_ou_fromage = Spinbox(right_frame,  background=backgroundcolor, from_=0, to=50, width=6, textvariable=E_sandwich_jambon_ou_fromage)
    entry_sandwich_jambon_ou_fromage.grid(row=2, column=1)
    # -------------
    lbl_sandwich_jambon_et_Fromage = Label(right_frame, text="Sandwich\nJambon+Fromage", font=("courier", 14, "bold"), background=backgroundcolor)
    lbl_sandwich_jambon_et_Fromage.grid(row=3, column=0, sticky="w")

    entry_sandwich_jambon_et_Fromage = Spinbox(right_frame,  background=backgroundcolor, from_=0, to=50, width=6, textvariable=E_sandwich_jambon_et_Fromage)
    entry_sandwich_jambon_et_Fromage.grid(row=3, column=1)
    # -------------
    lbl_sandwich_poulet = Label(right_frame, text="Sandwich au poulet", font=("courier", 14, "bold"), background=backgroundcolor)
    lbl_sandwich_poulet.grid(row=4, column=0, sticky="w")

    entry_sandwich_poulet = Spinbox(right_frame,  background=backgroundcolor, from_=0, to=50, width=6, textvariable=E_sandwich_poulet)
    entry_sandwich_poulet.grid(row=4, column=1, pady=3)
    # -------------
    lbl_sandwich_thon = Label(right_frame, text="Sandwich au thon", font=("courier", 14, "bold"), background=backgroundcolor)
    lbl_sandwich_thon.grid(row=5, column=0, sticky="w")

    entry_sandwich_thon = Spinbox(right_frame,  background=backgroundcolor, from_=0, to=50, width=6, textvariable=E_sandwich_thon)
    entry_sandwich_thon.grid(row=5, column=1, pady=3)
    # -------------
    lbl_sandwich_club = Label(right_frame, text="Sandwich club", font=("courier", 14, "bold"), background=backgroundcolor)
    lbl_sandwich_club.grid(row=6, column=0, sticky="w")

    entry_sandwich_club = Spinbox(right_frame,  background=backgroundcolor, from_=0, to=50, width=6, textvariable=E_sandwich_club)
    entry_sandwich_club.grid(row=6, column=1, pady=3)
    # -------------
    lbl_hamburger = Label(right_frame, text="Hamburger", font=("courier", 14, "bold"), background=backgroundcolor)
    lbl_hamburger.grid(row=7, column=0, sticky="w")

    entry_hamburger = Spinbox(right_frame,  background=backgroundcolor, from_=0, to=50, width=6, textvariable=E_hamburger)
    entry_hamburger.grid(row=7, column=1, pady=3)
    # -------------
    lbl_cheeseburger = Label(right_frame, text="Cheeseburger", font=("courier", 14, "bold"), background=backgroundcolor)
    lbl_cheeseburger.grid(row=8, column=0, sticky="w")

    entry_cheeseburger = Spinbox(right_frame,  background=backgroundcolor, from_=0, to=50, width=6, textvariable=E_cheeseburger)
    entry_cheeseburger.grid(row=8, column=1, pady=3)
    # -------------
    lbl_croque_monsieur = Label(right_frame, text="Croque Monsieur", font=("courier", 14, "bold"), background=backgroundcolor)
    lbl_croque_monsieur.grid(row=9, column=0, sticky="w")

    entry_croque_monsieur = Spinbox(right_frame,  background=backgroundcolor, from_=0, to=50, width=6, textvariable=E_croque_monsieur)
    entry_croque_monsieur.grid(row=9, column=1, pady=3)
    # -------------
    lbl_croque_madame = Label(right_frame, text="Croque Madame", font=("courier", 14, "bold"), background=backgroundcolor)
    lbl_croque_madame.grid(row=10, column=0, sticky="w")

    entry_croque_madame = Spinbox(right_frame,  background=backgroundcolor, from_=0, to=50, width=6, textvariable=E_croque_madame)
    entry_croque_madame.grid(row=10, column=1, pady=3)



def Jus():
    return


def BoissonChauddes():
    return


def Soupes():
    global Total_Gen

    right_frame = Frame(app, border=5, relief=RIDGE, width=720, height=710, background=backgroundcolor)
    right_frame.grid(row=0, column=1, sticky="nesw")

    global E_SoupecremeLegu
    global E_SoupecremePoisson
    global E_SoupecremePoulet
    global E_SoupecremePoireaux

    def addSoupe():
        global Total_Gen
        global item1
        global item2
        global item3
        global item4
        item1 = round(float(E_SoupecremeLegu.get()))
        item2 = round(float(E_SoupecremePoisson.get()))
        item3 = round(float(E_SoupecremePoulet.get()))
        item4 = round(float(E_SoupecremePoireaux.get()))
        # ------- prices ----
        p1 = int(7000)
        p2 = int(7000)
        p3 = int(7000)
        p4 = int(7000)
        # -----------------
        p1_1 = 0
        p2_2 = 0
        p3_3 = 0
        p4_4 = 0
        # ------------------
        if item1 > 0:
            forma = ("Soupe Creme Legume:", str(item1), str(p1),)
            fields = "{0:25}{1:25}{2:25}\n".format(forma[0], forma[1], "x"+forma[2])
            txt_receipt.insert(END, fields)
            #txt_receipt.insert(END, f"\nSoupe Creme Legume:" + str(item1) + "x" + str(p1))
            #print(p1)
            p1_1 += p1*item1
            #print(p1_1)
        if item2 > 0:
            forma = ("Soupe Creme Poisson:", str(item2), str(p2),)
            fields = "{0:25}{1:25}{2:25}\n".format(forma[0], forma[1], "x"+forma[2])
            txt_receipt.insert(END, fields)
            #txt_receipt.insert(END, f"\nSoupe Creme Poisson:" + str(item2) + "x" + str(p2))
            p2_2 += p2*item2
        if item3 > 0:
            forma = ("Soupe Creme Poulet:", str(item3), str(p3),)
            fields = "{0:25}{1:25}{2:25}\n".format(forma[0], forma[1], "x"+forma[2])
            txt_receipt.insert(END, fields)
            #txt_receipt.insert(END, f"\nSoupe Creme Poulet:" + str(item3) + "x" + str(p3))
            p3_3 += p3*item3
        if item4 > 0:
            forma = ("Soupe Creme Poireaux:", str(item4), str(p4),)
            fields = "{0:25}{1:25}{2:25}\n".format(forma[0], forma[1], "x"+forma[2])
            txt_receipt.insert(END, fields)
            #txt_receipt.insert(END, f"\nSoupe Creme Poireaux:" + str(item4) + "x" + str(p4))
            p4_4 += p4*item4
        if item1 == 0 and item2 == 0 and item3 == 0 and item4:
            txt_receipt.insert(END, "")
        E_SoupecremeLegu.set(0)
        E_SoupecremePoisson.set(0)
        E_SoupecremePoulet.set(0)
        E_SoupecremePoireaux.set(0)
        # ----- Calculer Total ---
        Tot1 = (p1_1) + (p2_2) + (p3_3) + (p4_4)
        Total_Gen += Tot1

    ajouter_btn = ttk.Button(button_frame, text="AJOUTER", style="TButton", command=addSoupe)
    ajouter_btn.grid(row=0, column=0, padx=2, pady=7)
    # ------------------------
    # --------------
    E_SoupecremeLegu = IntVar()
    E_SoupecremePoisson = IntVar()
    E_SoupecremePoulet = IntVar()
    E_SoupecremePoireaux = IntVar()
    # ---------------
    E_SoupecremeLegu.set(0)
    E_SoupecremePoisson.set(0)
    E_SoupecremePoulet.set(0)
    E_SoupecremePoireaux.set(0)
    
    # ======= 1 ========
    lbl_SoupecremeLegu = Label(right_frame, text="Soupe Creme\nLegumes", font=("courier", 14, "bold"), background=backgroundcolor)
    lbl_SoupecremeLegu.grid(row=0, column=0)
    # ------
    entry_SoupecremeLegu = Spinbox(right_frame, background=backgroundcolor, from_=0, to=50, width=6, textvariable=E_SoupecremeLegu)
    entry_SoupecremeLegu.grid(row=0, column=1)
    # =========2=========
    lbl_SoupecremePoisson = Label(right_frame, text="Soupe creme\nde poisson", font=("courier", 14, "bold"), background=backgroundcolor)
    lbl_SoupecremePoisson.grid(row=1, column=0)
    # ==================
    entry_SoupecremePoisson = Spinbox(right_frame,  background=backgroundcolor, from_=0, to=50, width=6, textvariable=E_SoupecremePoisson)
    entry_SoupecremePoisson.grid(row=1, column=1)
    # =========3=========
    lbl_SoupecremePoulet = Label(right_frame, text="Soupe creme\nde poulet", font=("courier", 14, "bold"), background=backgroundcolor)
    lbl_SoupecremePoulet.grid(row=2, column=0)
    # ==================
    entry_SoupecremePoulet = Spinbox(right_frame,  background=backgroundcolor, from_=0, to=50, width=6, textvariable=E_SoupecremePoulet)
    entry_SoupecremePoulet.grid(row=2, column=1)
    # =========4=========
    lbl_SoupecremePoireaux = Label(
        right_frame, text="Soupe creme\nde poireaux", font=("courier", 14, "bold"), background=backgroundcolor)
    lbl_SoupecremePoireaux.grid(row=3, column=0)
    # ==================
    entry_SoupecremePoireaux = Spinbox(right_frame,  background=backgroundcolor, from_=0, to=50, width=6, textvariable=E_SoupecremePoireaux)
    entry_SoupecremePoireaux.grid(row=3, column=1)
    # --------------------------------------

def Omollette():
    return


def Glaces():
    return


def Portions():
    return


def Legumes():
    return


def Pates():
    return


def Take_away():
    return


def Pizza():
    return


def ViandesRouges():
    return


def AmusesBouches():
    return


def Poissons():
    return


def Volailles():
    return

def Salades():
    return

# ============================= Buttons ====================================
# ------- row 0------------
lbl_title_boissons = Label(top_frame, text="Boissons", font=("courier", 16, "bold"), background=backgroundcolor)
lbl_title_boissons.grid(row=0, column=0, padx=8)
# ------- row 1------------
softsDrinks_btn = Button(
    top_frame, text="Softs Drinks", width=10, height=5, command=SoftDrinks)
softsDrinks_btn.grid(row=1, column=0)
# ------- row 2------------
alcohol_btn = Button(top_frame, text="Alcohol",
                     width=10, height=5, command=Alcohol)
alcohol_btn.grid(row=2, column=0)
# ------- row 3------------
vins_btn = Button(top_frame, text="Vins", width=10, height=5, command=Vins)
vins_btn.grid(row=3, column=0)
# ------- row 4------------
whisky_vodka_btn = Button(
    top_frame, text="Whisky/Vodka\net Liqueurs", width=10, height=5, command=WhiskyVodka)
whisky_vodka_btn.grid(row=4, column=0)
# ------- row 5------------
jus_btn = Button(top_frame, text="Jus", width=10, height=5, command=Jus)
jus_btn.grid(row=5, column=0)
# ------- column 1 --------
# ------- row 0------------
lbl_title_p_dejeuner = Label(top_frame, text="P-Déjeuner",
                           font=("courier", 16, "bold"), background=backgroundcolor)
lbl_title_p_dejeuner.grid(row=0, column=1, padx=8)
# ------- row 1------------
pains_btn = Button(top_frame, text="Pains", width=10, height=5, command=Pains)
pains_btn.grid(row=1, column=1)
# ------- row 2------------
boisson_chaudes_btn = Button(
    top_frame, text="Boisson\nChaudes", width=10, height=5, command=BoissonChauddes)
boisson_chaudes_btn.grid(row=2, column=1)
# ------- row 3------------
soupes_btn = Button(top_frame, text="Soupes",
                    width=10, height=5, command=Soupes)
soupes_btn.grid(row=3, column=1)
# ------- row 4------------
omolette_btn = Button(top_frame, text="Omolette",
                      width=10, height=5, command=Omollette)
omolette_btn.grid(row=4, column=1)
# ------- row 5------------
glaces_btn = Button(top_frame, text="Glaces", width=10, height=5, command=Glaces)
glaces_btn.grid(row=5, column=1)
# ------ column 2 -------------
# ------- row 0------------
lbl_title_Dejeuner_1 = Label(top_frame, text="Déjeuner-1",
                             font=("courier", 16, "bold"), background=backgroundcolor)
lbl_title_Dejeuner_1.grid(row=0, column=2, padx=8)
# ------- row 1------------
portions_btn = Button(top_frame, text="Portions",
                      width=10, height=5, command=Portions)
portions_btn.grid(row=1, column=2)
# ------- row 2------------
legumes_btn = Button(top_frame, text="Legumes",
                     width=10, height=5, command=Legumes)
legumes_btn.grid(row=2, column=2)
# ------- row 3------------
pates_btn = Button(top_frame, text="Påtes", width=10, height=5, command=Pates)
pates_btn.grid(row=3, column=2)
# ------- row 4------------
take_away_btn = Button(top_frame, text="Take Away",
                       width=10, height=5, command=Take_away)
take_away_btn.grid(row=4, column=2)
# ------- row 5------------
pizza_btn = Button(top_frame, text="Pizza", width=10, height=5, command=Pizza)
pizza_btn.grid(row=5, column=2)
# ----- column 3 --------------
# ------- row 0------------
lbl_title_dejeneur_2 = Label(top_frame, text="Déjeuner-2",
                             font=("courier", 16, "bold"), background=backgroundcolor)
lbl_title_dejeneur_2.grid(row=0, column=3, padx=8)
# ------- row 1------------
viande_rouges_btn = Button(top_frame, text="Viandes\nrouges", width=10, height=5, command=ViandesRouges)
viande_rouges_btn.grid(row=1, column=3)
# ------- row 2------------
amuses_bouches_btn = Button(top_frame, text="Amuses\nBouche", width=10, height=5, command=AmusesBouches)
amuses_bouches_btn.grid(row=2, column=3)
# ------- row 3------------
poissons_btn = Button(top_frame, text="Poissons",
                      width=10, height=5, command=Poissons)
poissons_btn.grid(row=3, column=3)
# ------- row 4------------
volailles_btn = Button(top_frame, text="Volailles", width=10, height=5, command=Volailles)
volailles_btn.grid(row=4, column=3)
# ------- row 5------------
salades_btn = Button(top_frame, text="Salades",
                     width=10, height=5, command=Salades)
salades_btn.grid(row=5, column=3)
# -----------------------
# ==============================================================================
# ------ buttons -------
# ======= buttons Function =====
def Ajouter():
    pass


def Total():
    '''
    Every time when Total is pressed do those stuffs
    '''
    global Total_Gen
    # udusharizo
    txt_receipt.insert(END, "{0:75}\n".format("_"*58))#"\n----------------------------------------------------------")
    total_format = "{0:25}{1:25}{2:25}\n".format("Total:", '.', str(Total_Gen))
    txt_receipt.insert(END, total_format)
    footer = "{0:18} {1:25} {2:25}".format(".","MERCI A BIENTOT", ".")
    txt_receipt.insert(END, footer)
    #txt_receipt.insert(END, f"\nTotal:\t\t\t\t\t\t"+str(Total_Gen) + " Fbu")
    Total_Gen *= 0

# setting the file path where the recu number is
filepath_recu = f'/Users/Desktop/Dossier_Des_recus/recu_no.csv'
# open the recu number
with open(filepath_recu, 'r') as input_file:
    # read first line where there is a number of recu
    readed = input_file.readlines(0)
    # transform the list to string and try catching exception
    try:
        to_Str = ' '.join(map(str, readed)) # from list to string
        to_integer = int(to_Str) # then transform it to int
    except ValueError:
        showwarning("Warning", "Impossible")

# assing recu number to count_recu
count_Recu = to_integer
# get todday date 
date_today = today

def printR():
    '''
    Every time when printR is clicked
    increment (count_Recu) to one by the number who's in count_Recu
    then transform it to str and store it in (to_str)
    then reprace to exsting number with the number incremented
    which is stored in (to_str variable)
    then on line (633) we store the path in filepath which we want to save our recu,
    And his default name (name + no_recu + date_of_out.csv)
    Then finally the file.csv is saved.
    '''
    global count_Recu
    global filepath_recu

    count_Recu += 1
    to_str = str(count_Recu)

    with open(filepath_recu, 'w') as output_file:
        output_file.write(to_str)

    filepath = f'/Users/Desktop/Dossier_Des_recus/Reçu_numero_{count_Recu}_date_{date_today}.csv'
    with open(filepath, 'w') as output_file:
        text = txt_receipt.get("1.0", END)
        output_file.write(text)

    # finally clear the way
    txt_receipt.delete("1.0", END)
    header = "{0} {1} {2}\n".format("*"*25,"Facture", "*"*25)
    txt_receipt.insert(END, header)
    #txt_receipt.insert(END, "********************** WELCOME AGAIN *********************\n")
    txt_receipt.insert(END, "{0}\n".format("Nom du resto"))
    txt_receipt.insert(END, "{0}\n".format("NIF:00000"))
    txt_receipt.insert(END, "{0}\n".format("Commune:"))
    txt_receipt.insert(END, "{0}\n".format("Tel:"))
    txt_receipt.insert(END, "{0}\n".format("Assujeti à la TVA"))
    txt_receipt.insert(END, "{0}\n".format(""))
    txt_receipt.insert(END, "{0:25}{1:25}{2:25}\n".format("Reçu numero: " + f'{count_Recu}', ".", "Table:"))
    txt_receipt.insert(END, "{0:25}{1:25}{2:25}\n".format("Date: " + f'{today}', ".", "Place:"))
    txt_receipt.insert(END, "{0:25}{1:25}{2:25}\n".format("Caissier:", ".", "Heure:"))
    txt_receipt.insert(END, "\n-----------------------------------------------------------\n")
    fields = "{0:25}{1:25}{2:25}\n".format("Produit", "Quantité", "Prix")
    txt_receipt.insert(END, fields)
    # ----------------


def Effacer():
    '''
    Every time when Effacer is pressed clear all the Text filled then set following stuffs.
    '''
    txt_receipt.delete("1.0", END)
    header = "{0} {1} {2}\n".format("*"*25,"Facture", "*"*25)
    txt_receipt.insert(END, header)
    #txt_receipt.insert(END, "********************** WELCOME AGAIN *********************\n")
    txt_receipt.insert(END, "{0}\n".format("Nom du resto"))
    txt_receipt.insert(END, "{0}\n".format("NIF:00000"))
    txt_receipt.insert(END, "{0}\n".format("Commune:"))
    txt_receipt.insert(END, "{0}\n".format("Tel:"))
    txt_receipt.insert(END, "{0}\n".format("Assujeti à la TVA"))
    txt_receipt.insert(END, "{0}\n".format(""))
    txt_receipt.insert(END, "{0:25}{1:25}{2:25}\n".format("Reçu numero: " + f'{count_Recu}', ".", "Table:"))
    txt_receipt.insert(END, "{0:25}{1:25}{2:25}\n".format("Date: " + f'{today}', ".", "Place:"))
    txt_receipt.insert(END, "{0:25}{1:25}{2:25}\n".format("Caissier:", ".", "Heure:"))
    txt_receipt.insert(END, "\n-----------------------------------------------------------\n")
    fields = "{0:25}{1:25}{2:25}\n".format("Produit", "Quantité", "Prix U")
    txt_receipt.insert(END, fields)
    #txt_receipt.insert(END, "\nProduit                   Quantité                   Prix\n")

# ------ text receipt section -----

#txt_receipt = Text(right_frame_receipt, font=('arial', 16, 'bold'), bg="aliceblue", width=59, height=25)
#txt_receipt.grid()

txt_receipt = Text(right_frame_receipt, font=('TkFixedFont'), bg="aliceblue", width=59, height=25)
txt_receipt.grid()

# ---------------------------------
txt_receipt.delete("1.0", END)
header = "{0} {1} {2}\n".format("*"*25,"Facture", "*"*25)
txt_receipt.insert(END, header)
#txt_receipt.insert(END, "********************** WELCOME AGAIN *********************\n")
txt_receipt.insert(END, "{0}\n".format("Nom du resto"))
txt_receipt.insert(END, "{0}\n".format("NIF:00000"))
txt_receipt.insert(END, "{0}\n".format("Commune:"))
txt_receipt.insert(END, "{0}\n".format("Tel:"))
txt_receipt.insert(END, "{0}\n".format("Assujeti à la TVA"))
txt_receipt.insert(END, "{0}\n".format(""))
txt_receipt.insert(END, "{0:25}{1:25}{2:25}\n".format("Reçu numero: " + f'{count_Recu}', ".", "Table:"))
txt_receipt.insert(END, "{0:25}{1:25}{2:25}\n".format("Date: " + f'{today}', ".", "Place:"))
txt_receipt.insert(END, "{0:25}{1:25}{2:25}\n".format("Caissier:", ".", "Heure:"))
txt_receipt.insert(END, "\n-----------------------------------------------------------\n")
fields = "{0:25}{1:25}{2:25}\n".format("Produit", "Quantité", "Prix U")
txt_receipt.insert(END, fields)
#txt_receipt.insert(END, "\nProduit                   Quantité                   Prix\n")
# -----------------------
ajouter_btn = ttk.Button(button_frame, text=".", style="TButton", command=Ajouter)
ajouter_btn.grid(row=0, column=0, padx=2, pady=7)
# ---
recu_btn = ttk.Button(button_frame, text="Print", style="TButton", command=printR)
recu_btn.grid(row=0, column=1, padx=2, pady=7)
# --
print_btn = ttk.Button(button_frame, text="Total", style="TButton", command=Total)
print_btn.grid(row=0, column=2, padx=2, pady=7)
# --
effacer_btn = ttk.Button(button_frame, text="Effacer", style="TButton", command=Effacer)
effacer_btn.grid(row=0, column=3, padx=2, pady=7)
# --
quitter_btn = ttk.Button(button_frame, text="Quiter",
                         style="TButton", command=Exit)
quitter_btn.grid(row=0, column=4, padx=2, pady=7)
# ----------------------

app.mainloop()
