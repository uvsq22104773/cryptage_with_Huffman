# création de la classe sommet 
# qui sont des objets qui représente 
# les sommets d'un arbres binaire étiqueté
class Sommet(object):
    # le constructeur prend comme argument une etiquette,
    # une valeur, son fils gauche et son fils droit
    def __init__(self, etiquette=None, valeur=None, gauche=None, droit=None):
        self.valeur = valeur
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit

    # définition des getter et setter
    def getEtiquette(self):
        return self.etiquette

    def setEtiquette(self, etiquette):
        self.etiquette = etiquette

    def getValeur(self):
        return self.valeur

    def setValeur(self, valeur):
        self.valeur = valeur

    def getDroit(self):
        return self.droit

    def setDroit(self, droit):
        self.droit = droit

    def getGauche(self):
        return self.gauche

    def setGauche(self, gauche):
        self.gauche = gauche


# class arbres binaire étiqueté
# qui a comme racine un sommet
# et a partir de ce sommet, 
# ce "premène" dans l'arbre en 
# passant de fils gauche et fils droit
# des sommets qui le compose
class ArbreB(object):
    # le constructeur prend en argument
    # un sommet et le met en racine
    def __init__(self, racine=None):
        self.racine = racine

    # définition des getter et setter
    def getRacine(self):
        return self.racine

    def setRacine(self, racine):
        self.racine = racine

    # methode insertion de sommet dans l'arbre,
    # elle appelle la methode _insert en lui donnant
    # un sommet de départ, c'est à dire la racine
    def insert(self, etiquette, valeur):
        if self.getRacine() is None:
            self.setRacine(Sommet(etiquette, valeur))
        else:
            self._insert(etiquette, valeur, self.racine)

    # cette methode est la suite de la précédente,
    # elle est en 2 partis car elle fonctionne par
    # recursivité
    # elle range le sommet en fonction de son étiquette
    # les etiquettes plus petite vont à gauche et les plus
    # grande vers la droite
    def _insert(self, etiquette, valeur, sommet):
        if etiquette < sommet.getEtiquette():
            if sommet.getGauche() is None:
                sommet.setGauche(Sommet(etiquette, valeur))
            else:
                self._insert(etiquette, valeur, sommet.getGauche())
        elif etiquette > sommet.getEtiquette():
            if sommet.getDroit() is None:
                sommet.setDroit(Sommet(etiquette, valeur))
            else:
                self._insert(etiquette, valeur, sommet.getDroit())

    # methode supprime sommet qui verifie si
    # la recine est definie puis appelle
    # une autre methode qui permet de faire de 
    # la recusivité, supprimé en fonction de l'étiquette
    def supprime_sommet(self, etiquette):
        if self.getRacine() is None:
            return None
        else:
            self.setRacine(self._supprime_sommet(etiquette, self.getRacine()))

    # cherche l'étiquette dans l'arbre grace
    # au rangement des étiquettes (petit a gauche,
    # grand a droite) puis supprime le sommet puis
    # rearange les sommets pour garder une coherence
    # dans le rangement des etiquettes
    def _supprime_sommet(self, etiquette, sommet):
        if sommet is None:
            return sommet
        elif etiquette < sommet.getEtiquette():
            sommet.setGauche(self._supprime_sommet(etiquette, sommet.getGauche()))
        elif etiquette > sommet.getEtiquette():
            sommet.setDroit(self._supprime_sommet(etiquette, sommet.getDroit()))
        else:
            if sommet.getGauche() is None:
                temp = sommet.getDroit()
                sommet = None
                return temp
            elif sommet.getDroit() is None:
                temp = sommet.getGauche()
                sommet = None
                return temp
            temp = self._sommet_min(sommet.getDroit())
            sommet.setEtiquette(temp.getEtiquette())
            sommet.setValeur(temp.getValeur())
            sommet.setDroit(self._supprime_sommet(temp.getEtiquette, sommet.getDroit()))
        return sommet

    # cherche le plus petit sommet,
    # elle sert à la methode supprime
    def _sommet_min(self, sommet):
        current = sommet
        while current.getDroit() is not None:
            current = current.getGauche()
        return current

    # calcule la hauteur de l'arbre
    def hauteur(self):
        if self.getRacine() is None:
            return 0
        else:
            return self._hauteur(self.getRacine())

    # récursivité donc séparé
    def _hauteur(self, sommet):
        if sommet is None:
            return 0
        else:
            hauteur_gauche = self._hauteur(sommet.getGauche())
            hauteur_droit = self._hauteur(sommet.getDroit())
            return max(hauteur_gauche, hauteur_droit) + 1

    # prend un canvas comme argument
    # definie sa taille en fonction de l'arbre
    # puis appelle la methode récursive 
    # _affiche_arbre
    def affiche_arbre(self, canvas):
        if self.getRacine() is not None:
            canvas.delete('all')
            hauteur=self.hauteur()**4
            canvas.config(scrollregion=(-hauteur//2+250, 0, hauteur//2+250, hauteur//11))
            self._affiche_arbre(canvas, self.getRacine(), 250, 50, hauteur)

    # methode qui dessine des traits et affiche les sommets
    # dans le canvas de la fenêtre
    def _affiche_arbre(self, canvas, sommet, x, y, hauteur, c=4):
        if sommet is not None:
            canvas.create_text((x, y+8), text=sommet.getValeur(), fill='black')
            if sommet.getGauche() is not None:
                if x-hauteur//c < x:
                    canvas.create_line((x, y), (x-hauteur//c, y+65), fill='black')
                else:
                    canvas.create_line((x, y), (x, y+65), fill='black')
            if sommet.getDroit() is not None:
                if x+3950//c > x:
                    canvas.create_line((x, y), (x+hauteur//c, y+65), fill='black')
                else:
                    canvas.create_line((x, y), (x, y+65), fill='black')
            self._affiche_arbre(canvas, sommet.getGauche(), x-hauteur//c, y+65, hauteur, c*2)
            self._affiche_arbre(canvas, sommet.getDroit(), x+hauteur//c, y+65, hauteur, c*2)
    
    # renvoie un arbre fusionner à partir
    # de 2 autres arbres
    def fusion_arbre(self, arbre2):
        return ArbreB(Sommet(self.getRacine().getEtiquette()+arbre2.getRacine().getEtiquette(), gauche=self.getRacine(), droit=arbre2.getRacine()))

    # surcharge de la methode fusion_arbre
    def __add__(self, arbre2):
        return self.fusion_arbre(arbre2)
    
    def __iadd__(self, arbre2):
        racine = self.fusion_arbre(arbre2)
        self.setRacine(racine.getRacine())
        return self

    # cherche une valeur dans l'arbre
    # et renvoie son étiquette
    def chercher_valeur(self, val):
        if self.getRacine() is not None:
            return self._chercher_valeur(self.getRacine(), val)

    # partie récursive
    def _chercher_valeur(self, sommet, val):
        if sommet is not None:
            if sommet.getValeur() == val:
                return sommet.getEtiquette()
            else:
                valeur_gauche = self._chercher_valeur(sommet.getGauche(), val)
                valeur_droit = self._chercher_valeur(sommet.getDroit(), val)
                return valeur_gauche if valeur_gauche is not None else valeur_droit

    # cherche une étiquette dans l'arbre
    # et renvoie sa valeur
    def chercher_etiquette(self, etiq):
        if self.getRacine() is not None:
            return self._chercher_etiquette(self.getRacine(), etiq)

    # partie récursive
    def _chercher_etiquette(self, sommet, etiq):
        if sommet is not None:
            if sommet.getEtiquette() == etiq:
                return sommet.getValeur()
            else:
                etiquette_gauche = self._chercher_etiquette(sommet.getGauche(), etiq)
                etiquette_droit = self._chercher_etiquette(sommet.getDroit(), etiq)
                return etiquette_gauche if etiquette_gauche is not None else etiquette_droit
    
    # methode qui décrypte le code
    # donner à partir d'un arbre
    # quand c'est 0 on va vers le fils gauche
    # et quand c'est 1 vers le fils droit
    # seule les feuilles on une valeur,
    # les autres sont à None donc quand une valeur
    # est détecter, elle est ajouter au texte
    # et on recommence du haut de l'arbre
    # cela jusqu'à ce que le code ce termine
    def decrypter(self, code):
        text = ""
        sommet = self.getRacine()
        while len(code) > 0:
            if sommet.getValeur() is not None:
                text += sommet.getValeur()
                sommet = self.getRacine()
            else:
                if code[0] == "0":
                    sommet = sommet.getGauche()
                elif code[0] == "1":
                    sommet = sommet.getDroit()
                else:
                    return "Erreur: '0' ou '1' attendus"
                code = code[1:]
        caract = sommet.getValeur()
        if caract is not None:    
            text += sommet.getValeur()
        return text
    
    # renomme toute les etiquettes à 
    # 0 pour la gauche et 1 pour la droite
    # + l'étiquette de son père
    def renommer_etiquette(self):
        if self.getRacine() is not None:
            sommet = self.getRacine()
            sommet.setEtiquette("")
            return self._renommer_etiquette(sommet)
    
    # partie récursive
    def _renommer_etiquette(self, sommet):
        if sommet is not None:
            if sommet.getGauche() is not None:
                sommet.getGauche().setEtiquette(sommet.getEtiquette()+"0")
            if sommet.getDroit() is not None:
                sommet.getDroit().setEtiquette(sommet.getEtiquette()+"1")
            self._renommer_etiquette(sommet.getGauche())
            self._renommer_etiquette(sommet.getDroit())
