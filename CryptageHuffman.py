# importation des modules utilisés
from tkinter import *
import fonctions as f
import arbreB as ab

# création de la fenêtre tkinter
root=Tk()
root.title('Cryptage Huffman')

# création d'une frame pour tout ce qui es de l'affichage de l'arbre
frame=Frame(root,width=500,height=500)
frame.pack(side=RIGHT, expand=True, fill=BOTH)
# canvas qui affichera l'arbre
canvas=Canvas(frame,bg='white', width=500, height=500)
# les scrollbar pour pouvoir ce déplacer sur la frame, 
# si l'arbre est plus grand que le canvas
# + placement des scrollbars et du canvas
hbar=Scrollbar(frame,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)
vbar=Scrollbar(frame, orient=VERTICAL)
vbar.pack(side=RIGHT, fill=Y)
vbar.config(command=canvas.yview)
canvas.config(width=500, height=500)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side=LEFT, expand=True, fill=BOTH)

# affiche le text en haut a gauche
label1 = Label(text = "Cryptage Huffman", height=3, font=('Calibri', 23), fg='black')
label1.pack(side=TOP)

# initialisation d'une variable global arbre 
arbre = None

# fonctions qui recupèrent les textes entrés 
# dans les barres de texte après avoir appuyer
# sur le bouton
def recuperer_text_c_a():
    global arbre
    text = entry_crypter_arbre.get()
    arbre = f.fusion_des_arbres(f.dico_arbre(f.frequences(text)))
    arbre.affiche_arbre(canvas)
    arbre.renommer_etiquette()
    entry_decrypter.delete(0, END)
    entry_decrypter.insert(0, f.text_to_code(text, arbre))

def recuperer_text_c():
    global arbre
    text = entry_crypter.get()
    entry_decrypter.delete(0, END)
    if arbre is not None:
        entry_decrypter.insert(0, f.text_to_code(text, arbre))
    else:
        entry_decrypter.insert(0, "Erreur: Arbre non définie")

def recuperer_text_d():
    global arbre
    code = entry_decrypter.get()
    entry_crypter.delete(0, END)
    if arbre is not None:
        entry_crypter.insert(0, arbre.decrypter(code))
    else:
        entry_crypter.insert(0, "Erreur: Arbre non définie")

# fonction pour le bouton qui supprime
# tout le texte dans les barres de texte
def remove():
    entry_crypter_arbre.delete(0, END)
    entry_crypter.delete(0, END)
    entry_decrypter.delete(0, END)

# création et affichage de toute
# les barres de texte, texte d'explication
# et boutons sur la gauche de la fenêtre
label2 = Label(text="Texte à crypter", font=('Calibri', 12), fg='black')
label2.place(x=49, y=78)
entry_crypter_arbre = Entry(root, bg='white', fg='black')
entry_crypter_arbre.place(x=0, y=98)
bouton_crypter_arbre = Button(root, text='Valider', command=recuperer_text_c_a, fg='black')
bouton_crypter_arbre.place(x=56, y=125)

label3 = Label(text="Texte à crypter avec l'arbre", font=('Calibri', 12), fg='black')
label3.place(x=14, y=177)
entry_crypter = Entry(root, bg='white', fg='black')
entry_crypter.place(x=0, y=197)
bouton_crypter = Button(root, text='Valider', command=recuperer_text_c, fg='black')
bouton_crypter.place(x=56, y=224)

label4 = Label(text="Code à décrypter", font=('Calibri', 12), fg='black')
label4.place(x=40, y=276)
entry_decrypter = Entry(root, bg='white', fg='black')
entry_decrypter.place(x=0, y=296)
bouton_decrypter = Button(root, text='Valider', command=recuperer_text_d, fg='black')
bouton_decrypter.place(x=56, y=323)

bouton_remove = Button(root, text="Tout supprimer", command=remove, fg='black')
bouton_remove.place(x=30, y=400)

# boucle qui lance la
# fenêtre
root.mainloop()
