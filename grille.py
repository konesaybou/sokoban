import os
import pygame
import time
pygame.init()



lig = int()
col = int()
class Grille:

    def __init__(self,lig,col,val=""):
        self.lig=lig
        self.col=col
        self.grille=[[val]*col for _ in range(lig)]
        self.NORD = 0
        self.OUEST = 1
        self.SUD = 2
        self.EST = 3
        self.lig_dir=0
        self.col_dir=0


    def shape(self):
        """ extrait la forme de ``tab``."""
        self.lig = len(self.grille)
        self.col = len(self.grille[0]) if self.lig else 0
        return self.lig, self.col

    def line_str(self, i):
        """affiche proprement la ligne ``i`` de ``tab``."""
        return '|\t' + '\t'.join(val for val in self.grille[i]) + '\t|'

    def to_str(self):
        """affiche proprement ``tab``."""
        res = ''
        for i in range(len(self.grille)):
            res += '\n' + self.line_str(i)
        return res

    def case_to_lc(self,num_case):
        """converti un numéro de case ``num_case`` de ``tab`` vers les coordonnées (ligne, colonne)  correspondants."""
        _, self.col = self.shape()
        return num_case // self.col, num_case % self.col

    def lc_to_case(self, num_lig, num_col):
        """converti les coordonnées (``num_lig``, ``num_col``) de ``tab`` vers le numéro de case correspondant."""
        return num_lig * self.shape()[1] + num_col

    def set_case(self, num_case, val):
        """Positionne la valeur ``val`` en ``num_case`` dans ``tab`` ."""
        self.lig, self.col = self.case_to_lc(num_case)
        self.grille[self.lig][self.col] = val

    def get_case(self, num_case):
        """ extrait la valeur de ``tab`` en ``num_case``."""
        self.lig, self.col = self.case_to_lc(num_case)
        return self.grille[self.lig][self.col]

    def cases(self, val):
        """Fournit la liste des numéros des cases à valeur égale à val dans ``tab``"""
        self.lig, self.col = self.shape()
        return [i for i in range(self.lig * self.col) if self.get_case(i) == val]

    def lig_col_next(self, lig, col, direction, tore=False):
        self.lig_dir=lig
        self.col_dir=col
        """calcule la paire (ligne, colonne) suivant (``lig``, ``col``) dans ``tab`` dans la direction ``direction``
            si ``tore`` est True, le dépassement des limites est géré en considérant la grilles comme un tore
            si ``tore`` est False, le dépassement des limites produit -1
        """
        self.lig, self.col = self.shape()
        self.new_lig, self.new_col = self.lig_dir, self.col_dir
        if direction == self.NORD:
            if not tore and self.lig_dir == 0:
                return -1
            self.new_lig, self.new_col = (self.lig_dir - 1) % self.lig_dir, self.col_dir
        if direction == self.EST:
            if not tore and self.col_dir == self.col - 1:
                return -1
            self.new_lig, self.new_col  = self.lig_dir, (self.col_dir + 1) % self.col
        if direction == self.SUD:
            if not tore and self.lig_dir == self.lig - 1:
                return -1
            self.new_lig, self.new_col  = (lig + 1) % self.lig, self.col_dir
        if direction == self.OUEST:
            if not tore and self.col_dir == 0:
                return -1
            self.new_lig, self.new_col  = lig, (self.col_dir - 1) % self.col
        return self.new_lig, self.new_col

    def num_case_next(self, num_case, direction, tore=False):
        """calcule le numéro de la case d'arrivée suivante dans ``tab`` dans la direction ``direction``
            si ``tore`` est True, le dépassement des limites est géré en considérant la grilles comme un tore
            si ``tore`` est False, le dépassement des limites produit -1
        """
        self.lig, self.col = self.case_to_lc(num_case)
        val = self.lig_col_next(self.lig_dir,self.col_dir,direction, tore)
        if val == -1:
            return val
        return self.lc_to_case(val[0], val[1])


class Level(Grille):
    def __init__(self, numLevel):

        Grille.__init__(self, lig, col,val="")
        self.numLevel = numLevel
        self.levelDirectory = "niveaux"
        self.files = os.listdir(self.levelDirectory)
        self.files.sort()
        self.fileName =self.levelDirectory + "/" + self.files[self.numLevel - 1]
        with open(self.fileName, "r", encoding="utf-8") as self.file:
            self.lire=self.file.readlines()
            self.grilleNonFiltree = [i.strip("\n") for i in self.lire]
            self.grilleFiltree = self.__filtre(self.grilleNonFiltree)
            self.grille = self.__ajusterBordureGrille(self.grilleFiltree)


    def __filtre(self, grilleNonFiltree):
        """ Filtrer la grille contenant le niveau du jeu en renvoyant que des caractères uniquement  """
        grilleFiltre = []
        for line in grilleNonFiltree:
            charactersLine = []
            for character in line:
                if character in ["#", ".", "@", "$", " ", "*"]:
                    charactersLine.append(character)
                elif character != "\n":
                    charactersLine = []
                    break
            if len(charactersLine) > 0:
                grilleFiltre.append(charactersLine)
        self.grilleFiltree = grilleFiltre
        return self.grilleFiltree

    def __ajusterBordureGrille(self, grilleNonAjustee):
        """ L'ajustement des bordures de la grille """
        longueurMaxi = 0
        tab = []
        for longueurTab in grilleNonAjustee:
            if len(longueurTab) >= longueurMaxi:
                longueurMaxi = len(longueurTab)
        for longueurTab in grilleNonAjustee:
            if len(longueurTab) < longueurMaxi:
                vide = longueurMaxi - len(longueurTab)
                for i in range(0, vide):
                    longueurTab+=" "
            tab.append(longueurTab)
        grilleAjustee = tab
        return grilleAjustee


    def estGardien(self):
        self.numCase = self.cases("@")
        return self.case_to_lc(self.numCase[0])

    def estCible(self):
        self.cible = self.cases(".")
        return self.cible

    def estCaisse(self):
        self.caisse = self.cases("$")
        return self.caisse

    def estMur(self):
        self.mur = self.cases("#")
        return self.mur

    def estLibre(self):
        return self.cases(' ')

    def modifie(self,num,val):
        """ Modifie un numero de case fournir en mettant la valeur val dans la case du numero"""
        return self.set_case(num,val)


class Jeu:

    def __init__(self,nivo_runing, fonctionJouer):
        self.nivo_runing=nivo_runing
        self.fonctionJouer = fonctionJouer
        pygame.mixer.music.load('son/test.wav')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)


    def play(self):
        pygame.mixer.music.set_volume(0.5)
        self.level=Level(self.nivo_runing)
        self.cibles = self.level.estCible()
        self.fonctionJouer(self)

    def coords(self,numObjet):
        """ Recupère les coordonnées d'un numéro de case fournir"""
        coods=self.level.case_to_lc(numObjet)
        return coods

    def coordsNext(self,numO,direction):
        """ Recupère les coordonnées suivants d'un numéro de case fournir selon la direction"""
        case=self.coords(numO)
        coodsNext=self.level.lig_col_next(case[0],case[1],direction)
        return coodsNext


    def deplaceGardien(self,dir):
        """ Delpacement du gardien selon les règle du jeu"""
        vide = ' '
        gardien = self.level.estGardien()
        posiNext = self.level.lig_col_next(gardien[0], gardien[1], dir)
        posiGardien = self.level.lc_to_case(gardien[0], gardien[1])
        gdien = self.level.get_case(posiGardien)
        numCaseNext = self.level.lc_to_case(posiNext[0], posiNext[1])  # position de la case suivante du gardie
        ch = self.level.get_case(numCaseNext)  # contenu de la case suivante
        cley = 0
        ciblesCons = self.cibles
        self.mapNum = 1
        sonWin = pygame.mixer.Sound('son/level_complete.wav')

        if numCaseNext in self.level.estMur():
            print("Mur pas de deplacement")

        elif numCaseNext in self.level.estCaisse():
            caisse = self.level.get_case(numCaseNext)  # symbole caisse
            next = self.coordsNext(numCaseNext, dir)
            numCaseN = self.level.lc_to_case(next[0], next[1])  # numero suivant selon direction

            if numCaseN in self.level.estMur():
                print('Mur pas de deplacement')

            elif numCaseN in self.level.estCaisse():
                print('pas de deplacement (deux caisse a la fois)')

            elif numCaseN in self.level.estCible():
                
                self.level.modifie(numCaseN, caisse)
                self.level.modifie(numCaseNext, gdien)
                self.level.modifie(posiGardien, vide)
                for i in self.cibles:
                    symbole = self.level.get_case(i)
                    if (symbole == " "):
                        self.level.modifie(i, ".")

            elif numCaseN in self.level.estLibre():
                pygame.mixer.Sound('son/bruit_de_deplacement.wav').play().set_volume(0.2)
                print("chemin")
                self.level.modifie(posiGardien, ' ')
                self.level.modifie(numCaseNext, gdien)
                self.level.modifie(numCaseN, caisse)
                if posiGardien in self.cibles:
                    self.level.modifie(posiGardien, ".")
                    self.mapNum += 1

        elif numCaseNext in self.level.estCible():
            print("est cible")
            self.tmp = numCaseNext
            self.level.modifie(numCaseNext, gdien)
            self.level.modifie(posiGardien, vide)
            if posiGardien in self.cibles:
                self.level.modifie(posiGardien, ".")

        elif numCaseNext in self.level.estLibre():
            self.level.modifie(posiGardien, ch)
            self.level.modifie(numCaseNext, gdien)
            if posiGardien in self.cibles:
                self.level.modifie(posiGardien, ".")

        for i in self.cibles:
            symbole = self.level.get_case(i)
            print(symbole)
            if (symbole == "$"):
                cley += 1
                print(cley)
                if (cley == len(ciblesCons)):
                    print("Felicitation !!!!")
                    sonWin.play()
                    pygame.mixer.music.set_volume(0.2)
                    self.nivo_runing += 1
                    self.play()
                    time.sleep(4)


# def play():
#     x = Jeu()
#     n=x.affiche()
#     print(x.affiche())
#     run=1
#     while(run):
#         dir=int(input('donner direction (0,1,2,3 respectivement pour NORD,OUEST,SUD,EST ou 5 pour stopper: '))
#         if(dir!=5):
#             e = x.deplaceGardien(dir)
#             print(e)
#         else:
#             run =0
#
# nvo =
# play(nvo)

