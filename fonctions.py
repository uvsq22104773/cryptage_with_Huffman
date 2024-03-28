# importation des modules utilisés
import arbreB as abrB

# fonction qui prend un dictionnaire en
# entrée avec tout les caractères
# du texte et leur occurence et
# renvoie le caractère qui apparait
# le moins dans le texte et le supprime
# du dictionnaire
def plus_petite_occurence(d):
    occ = d.values()
    occ = sorted(occ)
    keys = [k for k, v in d.items() if v == occ[0]]
    if keys:
        d.pop(keys[0])
        return keys[0]
    return None

# fonction qui créer un dictionnaire avec
# les caractères présent dans le texte
# en clé et le nombre de fois qu'ils 
# apparaissent dans le texte en valeur
def frequences(text):
    return {caract:text.count(caract) for caract in set(text)}

# fonction qui transforme tout les éléments du
# dictionnaire en arbre binaire avec
# un caractère en valeur et leur nombre
# d'occurence en etiquette et recréer un
# dictionnaire qui à un objet arbre en 
# clé et son occurence en valeur
def dico_arbre(dico):
    dico_arbb = {}
    for (caract, occur) in dico.items():
        tmp_arbb = abrB.ArbreB()
        tmp_arbb.insert(occur, caract)
        dico_arbb[tmp_arbb] = occur
    return dico_arbb

# fonction qui prend les 2 arbres avec 
# les caractères qui sont le moins apparus
# dans le texte et recréer un arbre avec
# comme fils gauche et droite les
# 2 arbres avec le moins d'occurence et
# comme etiquette la somme des 2 etiquettes
# qui sont leurs occurences et le rajoute dans
# le dictionnaire des arbres et continues
# jusqu'à ce que tout les arbres du dictionanire
# sont retirés et avoir un arbre qui contient tout
# les caractères du texte
def fusion_des_arbres(dico):
    if len(dico) > 1:
        while len(dico) > 1:
            arbre1 = plus_petite_occurence(dico)
            arbre2 = plus_petite_occurence(dico)
            arbre3 = arbre1.fusion_arbre(arbre2)
            dico[arbre3] = arbre3.getRacine().getEtiquette()
    else:
        s = plus_petite_occurence(dico)
        arbre3 = abrB.ArbreB(abrB.Sommet(s.getRacine().getEtiquette(), gauche=s.getRacine()))
    return arbre3

# transforme le texte reçu en code
# en cherchant les caractères un par un dans 
# l'arbre et renvoyant l'etiquette du caractère
# qui est devenu le code crypté du caractère
def text_to_code(text, arbre):
    code = ""
    for cara in text:
        c = arbre.chercher_valeur(cara)
        if c is None:
            return "Erreur: Cryptage impossible"
        else:
            code += arbre.chercher_valeur(cara)
    return code
