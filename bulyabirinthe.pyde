hero_x = 0
hero_y = 0
hero_ligne = 0 #sur quelle ligne il se situe
hero_colonne = 0  #sur quelle colonne il se situe

boite_x = 860
boite_y = 340
boite_ligne = 2
boite_colonne = 28

xstart9 = 600
ystart9 = 360
ligne_start_9 = 3
colonne_start_9 = 12
temps9 = 90

xstart4 = 600
ystart4 = 420
ligne_start_4 = 1
colonne_start_4 = 5
temps4 = 40

temps5 = 60


xstart10 = 580
ystart10 = 380
ligne_start_10 = 4
colonne_start_10 = 14
temps10 = 150

xstart11 = 620
ystart11 = 340
ligne_start_11 = 2
colonne_start_11 = 16
temps11 = 500

xstart7 = 660
ystart7 = 500
ligne_start_7 = 10
colonne_start_7 = 16
temps7 = 120


xstart_tuto = 440
ystart_tuto = 600
ligne_start_tuto = 1
colonne_start_tuto = 1

while_infini = 1 #pour faire des whiles infinis
direction = 'none' #peut valoir droite, gauche, haut, bas, et none, qui signifie qu'il ne se déplace pas
ligne = 300 #la ligne de départ pour creer la map, la valeur sert à rien, c'est juste pour creer la varbiable 
trail_ligne = 300  #la même, mais pour la fonction trail()
stop = 0
secondes = 0
minutes = 0
timer = 0
bloc_wait = 0
ligne_check = 0
stop_check = 0
commence = 0 
map_choisie = 0
last_map = 0
reseted = 0
lost = 0
fanta = 0
last_touche = 0
bloc_move = 0
bloc_move2 = 0
timer_move = 0
ligne_check_move = 0
next_X_R = 0
next_X_L = 0
next_X_U = 0
next_X_D = 0
direction_boite = "none"
boite_disp = 0
bouton_val = 0
choisi = 0
fleche_time = 0

H_S1 = 42069
H_S2 = 42069
H_S4 = 42069
H_S6 = 42069
H_S7 = 42059
H_S8 = 42069


B1X = 150 #positions des boutons
B1Y = 20

B2X = 450
B2Y = 20

B3X = 750
B3Y = 20

B4X = 150
B4Y = 280

B5X = 150
B5Y = 540

B6X = 750
B6Y = 280

B7X = 750
B7Y = 540

B8X = 150
B8Y = 800

B9X = 450
B9Y = 800

B10X = 750
B10Y = 800

B11X = 450
B11Y = 400 #positions des boutons

BAVENTUREX = 50
BAVENTUREY = 300

BARCADEX = 650
BARCADEY = 300


#------------création de fonctions-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def high_score(map_nombre):
    global secondes, H_S1, H_S2, H_S4, H_S6, H_S7, H_S8 
    if map_nombre == map_un_peu_illisible :
        if H_S1 > secondes :
            if secondes != 0 :
                H_S1 = secondes
            fill(255,0,255)
            textSize(50)
            text("High score :",300,800)
            text(H_S1,600,800)
            if H_S1 > 100 :
                text("secondes",710,800)
            if H_S1 < 100 and H_S1 > 9 :
                text("secondes",690,800)
            if H_S1 < 10 :
                text("secondes",660,800)
                
    if map_nombre == map_test :
        if H_S2 > secondes :
            if secondes != 0 :
                H_S2 = secondes
            fill(255,0,255)
            textSize(50)
            text("High score :",300,800)
            text(H_S2,600,800)
            if H_S2 > 100 :
                text("secondes",710,800)
            if H_S2 < 100 and H_S2 > 9 :
                text("secondes",690,800)
            if H_S2 < 10 :
                text("secondes",660,800)

            
    if map_nombre == map_liste_illisible :
        if H_S6 > secondes :
            if secondes != 0 :
                H_S6 = secondes
            fill(255,0,255)
            textSize(50)
            text("High score :",300,800)
            text(H_S6,600,800)
            if H_S6 > 100 :
                text("secondes",710,800)
            if H_S6 < 100 and H_S6 > 9 :
                text("secondes",690,800)
            if H_S6 < 10 :
                text("secondes",660,800)
            
    if map_nombre == map_liste_4 :
        if H_S7 > secondes :
            if secondes != 0 :
                H_S7 = secondes
            fill(255,0,255)
            textSize(50)
            text("High score :",300,800)
            text(H_S7,600,800)
            if H_S7 > 100 :
                text("secondes",710,800)
            if H_S7 < 100 and H_S7 > 9 :
                text("secondes",690,800)
            if H_S7 < 10 :
                text("secondes",660,800)
            
    if map_nombre == map_ultime :
        if H_S8 > secondes :
            if secondes != 0 :
                H_S8 = secondes
            fill(255,0,255)
            textSize(50)
            text("High score :",300,800)
            text(H_S8,600,800)
            if H_S8 > 100 :
                text("secondes",710,800)
            if H_S8 < 100 and H_S8 > 9 :
                text("secondes",690,800)
            if H_S8 < 10 :
                text("secondes",660,800)    
                        
        
    if map_nombre == map_worm :
        if H_S4 > secondes :
            if secondes != 0 :
                H_S4 = secondes
            fill(255,0,255)
            textSize(50)
            text("High score :",300,800)
            text(H_S4,600,800)
            if H_S4 > 100 :
                text("secondes",710,800)
            if H_S4 < 100 and H_S4 > 9 :
                text("secondes",690,800)
            if H_S4 < 10 :
                text("secondes",660,800)

def choix_de_la_map():
    global bouton_1, bouton_2, bouton_3 ,bouton_4, bouton_5, bouton_6, bouton_7, bouton_8, bouton_9, bouton_10, bouton_11, commence
    if commence == 0 :
        image(bouton_1, B1X, B1Y)
        image(bouton_2, B2X, B2Y)
        image(bouton_3, B3X, B3Y)
        image(bouton_4, B4X, B4Y)
        image(bouton_5, B5X, B5Y)
        image(bouton_6, B6X, B6Y)
        image(bouton_7, B7X, B7Y)
        image(bouton_8, B8X, B8Y)
        image(bouton_9, B9X, B9Y)
        image(bouton_10, B10X, B10Y)
        image(bouton_11, B11X, B11Y)
    
    
def tout_tout_tout_sur_les_maps(map_nombre, coords):
    global hero_x, hero_y, xstart1, ystart1, hero_ligne, hero_colonne, while_infini, direction, ligne, trail_ligne, stop, secondes, minutes, timer
    crea_map(map_nombre, coords)
    crea_map2(map_nombre, coords)
    trail_fill(map_nombre, coords)
    trail(map_nombre)
    blocus(map_nombre)
    blocus_draw(map_nombre, coords)
    tik_tok(map_nombre)
    time(map_nombre)
    moving_blocs(map_nombre, coords)
    moving_blocs_2(map_nombre, coords)
    moving_blocs_3(map_nombre, coords)
    moving_blocs_4(map_nombre, coords)
    moving_blocs_draw(map_nombre, coords)
    moving_blocs_draw2(map_nombre, coords)
    moving_blocs_draw_3(map_nombre, coords)
    moving_blocs_draw_4(map_nombre, coords)
    boutons_porte(map_nombre, coords)
    three_freeze(map_nombre, coords)

def crea_map(map_nombre, coords) :          # fonction qui permet de creer la map
    global ligne, coord_liste, stop_check, fanta
    if stop_check == 0 :
        if lost == 0 :
            lane = len(map_nombre)
            colonne = len(map_nombre[0])
            for o in range(lane) :
                for i in range (colonne):
                    if map_nombre [o][i][0] == "1" :
                        if fanta == 0 :
                            rect((coords[i][0]),ligne,20,20)
                        else :
                            image(affronte_les_arabes,(coords[i][0]),ligne) 
                ligne = ligne + 20
            ligne = coords[0][1]
            
def crea_map2(map_nombre, coords) :          # fonction qui permet de creer la map
    global ligne, coord_liste, stop_check, fanta
    if stop_check == 0 :
        if lost == 0 :
            lane = len(map_nombre)
            colonne = len(map_nombre[0])
            for o in range(lane) :
                for i in range (colonne):
                    if map_nombre [o][i][0] == "0" :
                        image(sol,(coords[i][0]),ligne)
                ligne = ligne + 20
            ligne = coords[0][1]
            
            
def moving_blocs_draw(map_nombre, coords) :          # fonction qui permet de creer la map
    global ligne, coord_liste, stop_check, fanta, minecart
    if stop_check == 0 :
        if lost == 0 :
            lane = len(map_nombre)
            colonne = len(map_nombre[0])
            for o in range(lane) :
                for i in range (colonne):
                    if map_nombre [o][i][0] == "L" or map_nombre [o][i][0] == "R" :
                        if fanta == 0 :
                            image(minecart,coords[i][0],ligne)
                        else :
                            image(affronte_les_arabes,(coords[i][0]),ligne) 
                ligne = ligne + 20
            ligne = coords[0][1]
            
def moving_blocs_draw2(map_nombre, coords) :          # fonction qui permet de creer la map
    global ligne, coord_liste, stop_check, fanta
    if stop_check == 0 :
        if lost == 0 :
            lane = len(map_nombre)
            colonne = len(map_nombre[0])
            for o in range(lane) :
                for i in range (colonne):
                    if map_nombre [o][i][0] == "N" :
                        if fanta == 0 :
                            image(case_vide,(coords[i][0]),ligne)
                        else :
                            image(wtc_38,(coords[i][0]),ligne) 
                ligne = ligne + 20
            ligne = coords[0][1]
            
def moving_blocs_draw_3(map_nombre, coords) :          # fonction qui permet de creer la map
    global ligne, coord_liste, stop_check, fanta, minecart
    if stop_check == 0 :
        if lost == 0 :
            lane = len(map_nombre)
            colonne = len(map_nombre[0])
            for o in range(lane) :
                for i in range (colonne):
                    if map_nombre [o][i][0] == "D" or map_nombre [o][i][0] == "U" :
                        if fanta == 0 :
                            image(minecart_2,coords[i][0],ligne)
                        else :
                            image(affronte_les_arabes,(coords[i][0]),ligne) 
                ligne = ligne + 20
            ligne = coords[0][1]
            
def moving_blocs_draw_4(map_nombre, coords) :          # fonction qui permet de creer la map
    global ligne, coord_liste, stop_check, fanta
    if stop_check == 0 :
        if lost == 0 :
            lane = len(map_nombre)
            colonne = len(map_nombre[0])
            for o in range(lane) :
                for i in range (colonne):
                    if map_nombre [o][i][0] == "T" :
                        if fanta == 0 :
                            image(case_vide_2,(coords[i][0]),ligne)
                        else :
                            image(wtc_38,(coords[i][0]),ligne) 
                    if map_nombre [o][i][0] == "X" :
                        if fanta == 0 :
                            image(case_vide_3,(coords[i][0]),ligne)
                        else :
                            image(wtc_38,(coords[i][0]),ligne)
                ligne = ligne + 20
            ligne = coords[0][1]
            
            
def moving_blocs(map_nombre, coords) :
    global ligne, coord_liste, stop_check, fanta, secondes, bloc_move, hero_ligne, hero_colonne, timer_move, next_X_L
    if stop_check == 0 :
        if lost == 0 :
            lane = len(map_nombre)
            colonne = len(map_nombre[0])
            for o in range(lane) :
                for i in range (colonne):
                    if map_nombre [o][i][0] == "L" :
                        if timer_move > 0.49 :
                            if map_nombre[o][i - 1] == "U" or map_nombre[o][i - 1] == "D" :
                                print('')
                            else :
                                map_nombre[o].pop(i)
                                if next_X_L > 0 :
                                    map_nombre[o].insert(i,"X")
                                    next_X_L = 0
                                else:
                                    map_nombre[o].insert(i,"N")
                            
                                if map_nombre[o][i - 1] == "N" :
                                    map_nombre[o].pop(i - 1)
                                    map_nombre[o].insert(i - 1,"L")
                                    
                                if map_nombre[o][i - 1] == "X" :
                                    map_nombre[o].pop(i - 1)
                                    map_nombre[o].insert(i - 1,"L")
                                    next_X_L = 1
                                    
                                if map_nombre[o][i - 1] == "1" :
                                    map_nombre[o].pop(i)
                                    map_nombre[o].insert(i,"R")
                ligne = ligne + 20
            ligne = coords[0][1]            
            

def moving_blocs_2(map_nombre, coords) :
    global ligne, coord_liste, stop_check, fanta, secondes, bloc_move, hero_ligne, hero_colonne, timer_move, next_X_R
    if stop_check == 0 :
        if lost == 0 :
            lane = len(map_nombre)
            colonne = len(map_nombre[0])
            for o in range(lane) :
                for i in range(colonne):
                    if map_nombre[lane - 1][colonne - 1][0] == "R" :
                        if timer_move > 0.49 :
                            if map_nombre[lane - 1][colonne] == "U" or map_nombre[lane - 1][colonne] == "D" :
                                print('')
                            else :
                                map_nombre[lane - 1].pop(colonne - 1)
                                
                                if next_X_R > 0 :
                                    map_nombre[lane - 1].insert(colonne - 1,"X")
                                    next_X_R = 0
                                else :
                                    map_nombre[lane - 1].insert(colonne - 1,"N")
                            
                                if map_nombre[lane - 1][(colonne - 1) + 1] == "N" :
                                    map_nombre[lane - 1].pop((colonne - 1) + 1)
                                    map_nombre[lane - 1].insert((colonne - 1) + 1,"R")
                                    
                                if map_nombre[lane - 1][colonne] == "X" :
                                    map_nombre[lane - 1].pop(colonne)
                                    map_nombre[lane - 1].insert(colonne,"R")
                                    next_X_R = 1
                                    
                                if map_nombre[lane - 1][(colonne - 1) + 1] == "1" :
                                    map_nombre[lane - 1].pop(colonne - 1)
                                    map_nombre[lane - 1].insert(colonne - 1,"L")
                                    map_nombre[lane - 1].pop(colonne - 1)
                                    map_nombre[lane - 1].insert(colonne - 1,"N")
                                    map_nombre[lane - 1].pop(colonne - 2)
                                    map_nombre[lane - 1].insert(colonne - 2,"L")
                    colonne = colonne - 1   
                lane = lane - 1     
                colonne = len(map_nombre[0])
            
def moving_blocs_3(map_nombre, coords) :
    global ligne, coord_liste, stop_check, fanta, secondes, bloc_move, hero_ligne, hero_colonne, timer_move, next_X_D
    if stop_check == 0 :
        if lost == 0 :
            lane = len(map_nombre)
            colonne = len(map_nombre[0])
            for o in range(lane) :
                for i in range (colonne):
                    if map_nombre [o][i][0] == "D" :
                        if timer_move > 0.49 :
                            if map_nombre[o - 1][i] == "L" or map_nombre[o - 1][i] == "R" :
                                print('')
                            else :
                                map_nombre[o].pop(i)
                                
                                if next_X_D > 0 :
                                    map_nombre[o].insert(i,"X")
                                    next_X_D = 0
                                else :
                                    map_nombre[o].insert(i,"T")
                            
                                if map_nombre[o - 1][i] == "X" :
                                    map_nombre[o - 1].pop(i)
                                    map_nombre[o - 1].insert(i,"D")
                                    next_X_D = 1
                                
                                if map_nombre[o - 1][i] == "T" :
                                    map_nombre[o - 1].pop(i)
                                    map_nombre[o - 1].insert(i,"D")
                                    
                                if map_nombre[o - 1][i] == "1" :
                                    map_nombre[o].pop(i)
                                    map_nombre[o].insert(i,"U")
                ligne = ligne + 20
            ligne = coords[0][1]            
            

def moving_blocs_4(map_nombre, coords) :
    global ligne, coord_liste, stop_check, fanta, secondes, bloc_move, hero_ligne, hero_colonne, timer_move, next_X_U
    if stop_check == 0 :
        if lost == 0 :
            lane = len(map_nombre)
            colonne = len(map_nombre[0])
            for o in range(lane) :
                for i in range(colonne):
                    if map_nombre[lane - 1][colonne - 1][0] == "U" :
                        if timer_move > 0.49 :
                            if map_nombre[lane][colonne - 1] == "L" or map_nombre[lane][colonne - 1] == "R" :
                                print('')
                            else :
                                map_nombre[lane - 1].pop(colonne - 1)
                                
                                if next_X_U > 0 :
                                    map_nombre[lane - 1].insert(colonne - 1,"X")
                                    next_X_U = 0
                                else :
                                    map_nombre[lane - 1].insert(colonne - 1,"T")
                            
                                if map_nombre[lane][(colonne - 1)] == "T" :
                                    map_nombre[lane].pop(colonne - 1)
                                    map_nombre[lane].insert(colonne - 1,"U")
                                    
                                if map_nombre[lane][(colonne - 1)] == "X" :
                                    map_nombre[lane].pop(colonne - 1)
                                    map_nombre[lane].insert(colonne - 1,"U")
                                    next_X_U = 1
                                    
                                if map_nombre[lane][colonne - 1] == "1" :
                                    map_nombre[lane - 1].pop(colonne - 1)
                                    map_nombre[lane - 1].insert(colonne - 1,"D")
                                    map_nombre[lane - 1].pop(colonne - 1)
                                    map_nombre[lane - 1].insert(colonne - 1,"T")
                                    map_nombre[lane - 2].pop(colonne - 1)
                                    map_nombre[lane - 2].insert(colonne - 1,"D")
                                
                    colonne = colonne - 1   
                lane = lane - 1     
                colonne = len(map_nombre[0])
                
                
 
def boites_2(map_nombre, coords) :
    global ligne, coord_liste, stop_check, fanta, secondes, bloc_move, hero_ligne, hero_colonne, direction, direction_boite, boite_ligne, boite_colonne, hero_ligne, hero_colonne, boite_x, boite_y, boite_disp
        
    if direction_boite == "bas" :
        if map_nombre [boite_ligne + 1][boite_colonne][0] == "1" or map_nombre [boite_ligne + 1][boite_colonne][0] == "L" or map_nombre [boite_ligne + 1][boite_colonne][0] == "R" or map_nombre [boite_ligne + 1][boite_colonne][0] == "D" or map_nombre [boite_ligne + 1][boite_colonne][0] == "U" or blocus(map_nombre) == 'true' or map_nombre [boite_ligne + 1][boite_colonne][0] == "O" or map_nombre [boite_ligne + 1][boite_colonne][0] == "P":
            direction_boite = 'none'
        else :
            for o in range(20) :
                boite_y = boite_y + 1
            boite_ligne = boite_ligne + 1
            
    if direction_boite == "haut" :
        if map_nombre [boite_ligne - 1][boite_colonne][0] == "1" or map_nombre [boite_ligne - 1][boite_colonne][0] == "L" or map_nombre [boite_ligne - 1][boite_colonne][0] == "R" or map_nombre [boite_ligne - 1][boite_colonne][0] == "D" or map_nombre [boite_ligne - 1][boite_colonne][0] == "U" or blocus(map_nombre) == 'true' or map_nombre [boite_ligne - 1][boite_colonne][0] == "O" or map_nombre [boite_ligne - 1][boite_colonne][0] == "P" :
            direction_boite = 'none'
        else :
            for o in range(20) :
                boite_y = boite_y - 1
            boite_ligne = boite_ligne - 1
            
    if direction_boite == 'droite' :
        if map_nombre [boite_ligne][boite_colonne + 1][0] == "1" or map_nombre [boite_ligne][boite_colonne + 1][0] == "L" or map_nombre [boite_ligne][boite_colonne + 1][0] == "R" or map_nombre [boite_ligne][boite_colonne + 1][0] == "D" or map_nombre [boite_ligne][boite_colonne + 1][0] == "U" or blocus(map_nombre) == 'true' or map_nombre [boite_ligne][boite_colonne + 1][0] == "O" or map_nombre [boite_ligne][boite_colonne + 1][0] == "P" :
            direction_boite = 'none'
        else :
            for i in range(20) :
                boite_x = boite_x + 1
            boite_colonne = boite_colonne + 1 
   
    if direction_boite == 'gauche' :
        if map_nombre [boite_ligne][boite_colonne - 1][0] == "1" or map_nombre [boite_ligne][boite_colonne - 1][0] == "L" or map_nombre [boite_ligne][boite_colonne - 1][0] == "R" or map_nombre [boite_ligne][boite_colonne - 1][0] == "D" or map_nombre [boite_ligne][boite_colonne - 1][0] == "U" or blocus(map_nombre) == 'true' or map_nombre [boite_ligne][boite_colonne - 1][0] == "O" or map_nombre [boite_ligne][boite_colonne - 1][0] == "P" :
            direction_boite = 'none'
        else :
            for i in range(20) :
                boite_x = boite_x - 1
            boite_colonne = boite_colonne - 1 
            
    if boite_disp == 1 :
        boite_x = 860
        boite_y = 340
        boite_ligne = 2
        boite_colonne = 28 
        boite_disp = 0


def boutons_porte(map_nombre, coords):
    if map_nombre == map_ultime :
        global ligne, coord_liste, stop_check, fanta, secondes, bloc_move, hero_ligne, hero_colonne, timer_move, next_X_D, boite_disp, bouton_val, boite_x, boite_y, boite_ligne, boite_colonne, direction_boite
        if stop_check == 0 :
            if lost == 0 :
                lane = len(map_nombre)
                colonne = len(map_nombre[0])
                for o in range(lane) :
                    for i in range (colonne):
                        if map_nombre [o][i][0] == "B" :
                            image(bouton,coords[i][0],ligne)
                            bouton_val = bouton_val + 1
                        if map_nombre [o][i][0] == "Y" :
                            image(bouton_V,coords[i][0],ligne)
                        if map_nombre [o][i][0] == "F" :
                            image(bouton_J,coords[i][0],ligne)
                        if map_nombre [o][i][0] == "P" :
                            image(porte_1,coords[i][0],ligne)
                        if map_nombre[o][i][0] == "K" :
                            image(gold,coords[i][0],ligne)
                        if map_nombre[o][i][0] == "C" :
                            image(cle,coords[i][0],ligne)
                        if map_nombre[o][i][0] == "O" :
                            image(porte_cle,coords[i][0],ligne)
                        if map_nombre[o][i][0] == "G" :
                            image(grinder,coords[i][0],ligne)
                        if map_nombre[o][i][0] == "<" :
                            image(left,coords[i][0],ligne)
                        if map_nombre[o][i][0] == "H" :
                            image(freeze,coords[i][0],ligne)
                    ligne = ligne + 20
                ligne = coords[0][1]
                
                if bouton_val == 0 :
                    if map_nombre == map_ultime :
                        map_nombre[30].pop(2)
                        map_nombre[30].insert(2,"F")
        if map_nombre[boite_ligne][boite_colonne] == "B" :
            map_nombre[boite_ligne][boite_colonne] = "Y"
            boite_disp = 1
            
        if map_nombre[hero_ligne][hero_colonne] == "F" :
            map_nombre[hero_ligne].pop(hero_colonne)
            map_nombre[hero_ligne].insert(hero_colonne,"Y")
            map_nombre[3].pop(6)
            map_nombre[3].insert(6,"0")
            
        if map_nombre[hero_ligne][hero_colonne] == "C" :
            map_nombre[hero_ligne].pop(hero_colonne)
            map_nombre[hero_ligne].insert(hero_colonne,"K")
            map_nombre[15].pop(29)
            map_nombre[15].insert(29,"0")
            
            
        if map_nombre[boite_ligne][boite_colonne] == "G" :
            boite_x = 860
            boite_y = 340
            boite_ligne = 2
            boite_colonne = 28 
            
        if map_nombre[boite_ligne][boite_colonne] == "<" :
            boite_x = boite_x - 20
            boite_colonne = boite_colonne - 1
            direction_boite = "none"
            
        
        bouton_val = 0
        
def three_freeze(map_nombre, coords) :
    global boite_x, boite_y, boite_ligne, boite_colonne
    if map_nombre == map_ultime :
        if map_nombre[boite_ligne][boite_colonne] == "H" :
            map_nombre[boite_ligne - 1].pop(boite_colonne)
            map_nombre[boite_ligne - 1].insert(boite_colonne,"H")
            map_nombre[boite_ligne].pop(boite_colonne)
            map_nombre[boite_ligne].insert(boite_colonne,"1")
            boite_x = 860
            boite_y = 340
            boite_ligne = 2
            boite_colonne = 28
        

def trail_fill(map_nombre, coords) :              # fonctions pour marquer le sol sur lequel on a déja marché 
    global trail_ligne, case, stop_check, fanta
    if stop_check == 0 :
        if lost == 0 :
            lane = len(map_nombre)
            colonne = len(map_nombre[0])
            for o in range(lane) :
                for i in range (colonne):
                    if map_nombre [o][i][0] == "V" :
                        if fanta == 0 :
                            image(case,coords[i][0],trail_ligne)
                        else :
                            image(olfo,coords[i][0],trail_ligne)
                trail_ligne = trail_ligne + 20
            trail_ligne = coords[0][1]
            
        
def trail(map_nombre) :                  # fonction pour reperer le sol sur lequel on a déja marché
    global hero_ligne, hero_colonne
    if map_nombre[hero_ligne][hero_colonne] == "0" :
        map_nombre[hero_ligne].pop(hero_colonne)
        map_nombre[hero_ligne].insert(hero_colonne,"V")
        

def blocus_draw(map_nombre, coords):  
    global trail_ligne, case_blocus, blocus_couleur, case_blocus2, stop_check, fanta
    if stop_check == 0 :
        if lost == 0 :
            lane = len(map_nombre)
            colonne = len(map_nombre[0])
            if bloc_wait < 2 :
                for o in range(lane) :
                    for i in range (colonne):
                        if map_nombre [o][i][0] == "M" :
                            if fanta == 0 :
                                image(case_blocus2, coords[i][0],trail_ligne)
                            else : 
                                image(enfer, coords[i][0],trail_ligne)
                    trail_ligne = trail_ligne + 20
                trail_ligne = coords[0][1]
            else :
                for o in range(lane) :
                    for i in range (colonne):
                        if map_nombre [o][i][0] == "M" :
                            if fanta == 0 :
                                image(case_blocus, coords[i][0],trail_ligne)
                            else : 
                                image(ui, coords[i][0],trail_ligne)
                    trail_ligne = trail_ligne + 20
                trail_ligne = coords[0][1]
        
                
def blocus(map_nombre) :
    global hero_ligne, hero_colonne, stop, direction, bloc_wait, blocus_couleur, case_blocus2, stop_check
    if stop_check == 0 :
        if lost == 0 :
            if map_nombre[hero_ligne][hero_colonne] == "M" :
                if bloc_wait < 2 :
                    return 'true'
                else :
                    return 'false'
 
def tik_tok(map_nombre):
    global timer, secondes, bloc_wait, bloc_move, bloc_move2, timer_move, ligne_check_move, fleche_time
    timer = timer + 0.015
    timer_move = timer_move + 0.015
    if timer > 1.0 :
        secondes = secondes + 1
        bloc_wait = bloc_wait + 1
        timer = 0
        fleche_time = fleche_time + 1
    if timer_move > 0.5 :
        timer_move = 0
    if bloc_wait > 3 :
        bloc_wait = 0
    if fleche_time > 1 :
        fleche_time = 0
        
        
def win(map_nombre) :
    global ligne_check, stop_check, ecran_victoire, secondes
    lane = len(map_nombre)

    if ligne_check == lane :
        ligne_check = 0
        stop_check = 1
        
    if stop_check == 0:
        if map_nombre[ligne_check].count("0") == 0 :
            ligne_check = ligne_check + 1
            
    if stop_check == 1 :
        if commence == 1 :
            if map_nombre == map_ultime :
                image(ecran_fin, 250, 300)
            else :
                image(ecran_victoire, 250, 300)
                high_score(map_nombre)
            secondes = 0
    
def reset(map_nombre, coords):
    global trail_ligne, case, stop_check
    if reseted == 0 :
        lane = len(map_nombre)
        colonne = len(map_nombre[0])
        for o in range(lane) :
            for i in range (colonne):
                if map_nombre [o][i][0] == "V" :
                    map_nombre[o].pop(i)
                    map_nombre[o].insert(i,"0")
            trail_ligne = trail_ligne + 20
        trail_ligne = coords[0][1]
        
    if map_nombre == map_ultime :
        lane = len(map_nombre)
        colonne = len(map_nombre[0])
        for o in range(lane) :
            for i in range (colonne):
                if map_nombre [o][i][0] == "Y" :
                    map_nombre[o].pop(i)
                    map_nombre[o].insert(i,"B")
            trail_ligne = trail_ligne + 20
        trail_ligne = coords[0][1]
        
        map_nombre[4].pop(3)
        map_nombre[4].insert(3,"C")
        
        map_nombre[3].pop(6)
        map_nombre[3].insert(6,"P")
        
        map_nombre[30].pop(2)
        map_nombre[30].insert(2,"0")
        
        map_nombre[15].pop(29)
        map_nombre[15].insert(29,"O")
        
        map_nombre[17].pop(17)
        map_nombre[17].insert(17,"0")
        map_nombre[18].pop(17)
        map_nombre[18].insert(17,"0")
        map_nombre[19].pop(17)
        map_nombre[19].insert(17,"0")
        map_nombre[20].pop(17)
        map_nombre[20].insert(17,"0")
        map_nombre[21].pop(17)
        map_nombre[21].insert(17,"0")
        map_nombre[22].pop(17)
        map_nombre[22].insert(17,"0")
        map_nombre[23].pop(17)
        map_nombre[23].insert(17,"0")
        map_nombre[24].pop(17)
        map_nombre[24].insert(17,"0")
        map_nombre[25].pop(17)
        map_nombre[25].insert(17,"0")
        map_nombre[26].pop(17)
        map_nombre[26].insert(17,"0")
        map_nombre[27].pop(17)
        map_nombre[27].insert(17,"0")
        map_nombre[28].pop(17)
        map_nombre[28].insert(17,"0")
        map_nombre[29].pop(17)
        map_nombre[29].insert(17,"0")
        map_nombre[30].pop(17)
        map_nombre[30].insert(17,"H")
    
        
        direction_boite = "none"
        boite_disp = 0
        bouton_val = 0
        
        boite_x = 860
        boite_y = 340
        boite_ligne = 2
        boite_colonne = 28
        

def start_point(map_nombre):
    global hero_x, hero_y, hero_ligne, hero_colonne
    if map_nombre == map_tuto_1 or map_nombre == map_tuto_2 or map_nombre == map_tuto_3 :
        hero_x = xstart_tuto
        hero_y = ystart_tuto
        hero_ligne = ligne_start_tuto
        hero_colonne = colonne_start_tuto
        
    if map_nombre == map_un_peu_illisible :
        hero_x = xstart4
        hero_y = ystart4
        hero_ligne = ligne_start_4
        hero_colonne = colonne_start_4
        
    if map_nombre == map_test :
        hero_x = xstart4
        hero_y = ystart4
        hero_ligne = ligne_start_4
        hero_colonne = colonne_start_4
        
    if map_nombre == map_liste_illisible :
        hero_x = xstart9
        hero_y = ystart9
        hero_ligne = ligne_start_9
        hero_colonne = colonne_start_9
        
    if map_nombre == map_liste_4 :
        hero_x = xstart10
        hero_y = ystart10
        hero_ligne = ligne_start_10
        hero_colonne = colonne_start_10
        
    if map_nombre == map_ultime :
        hero_x = xstart11
        hero_y = ystart11
        hero_ligne = ligne_start_11
        hero_colonne = colonne_start_11
        
    if map_nombre == map_worm :
        hero_x = xstart7
        hero_y = ystart7
        hero_ligne = ligne_start_7
        hero_colonne = colonne_start_7
        
        
def lose(map_nombre):
    global secondes, lost, ecran_defaite
    
    if map_nombre == map_un_peu_illisible :
        if secondes > temps4 :
            lost = 1
            
    if map_nombre == map_test :
        if secondes > temps5 :
            lost = 1
            
    if map_nombre == map_liste_illisible :
        if secondes > temps9 :
            lost = 1
            
    if map_nombre == map_liste_4 :
        if secondes > temps10 :
            lost = 1
            
    if map_nombre == map_ultime :
        if secondes > temps11 :
            lost = 1
            
    if map_nombre == map_worm :
        if secondes > temps7 :
            lost = 1
    
    if lost == 1 :
        if commence == 1 :
            image(ecran_defaite, 250, 300)
            secondes = 0
            
            
def time(map_nombre):
    
    if map_nombre == map_liste_illisible :
        rect(500,0,200,200)
        if temps9 - secondes > 20 :
            fill(0,0,0)
            textSize(50)
            text(temps9 - secondes,570,120)
        else :
            textSize(100) 
            fill(255,0,0)
            if temps9 - secondes > 9 :
                text(temps9 - secondes,540,130)
            else : 
                text(temps9 - secondes,570,130)
        fill(255,255,255)
        
    if map_nombre == map_un_peu_illisible :
        rect(500,0, 200, 200)
        if temps4 - secondes > 9 :
            fill(0,0,0)
            textSize(50)
            text(temps4 - secondes,570,120)
        else :
            textSize(100) 
            fill(255,0,0)
            text(temps4 - secondes,570,130)
        fill(255,255,255)
        
    if map_nombre == map_test :
        rect(500,0, 200, 200)
        if temps4 - secondes > 9 :
            fill(0,0,0)
            textSize(50)
            text(temps5 - secondes,570,120)
        else :
            textSize(100) 
            fill(255,0,0)
            text(temps5 - secondes,570,130)
        fill(255,255,255)
        
    if map_nombre == map_liste_4 :
        rect(500,0,200,200)
        if temps10 - secondes > 30 :
            fill(0,0,0)
            textSize(50)
            if temps10 - secondes > 99 :
                text(temps10 - secondes, 550, 120)
            else :
                text(temps10 - secondes, 570, 120)
        else :
            textSize(100) 
            fill(255,0,0)
            if temps10 - secondes < 10 :
                text(temps10 - secondes, 570, 130)
            else :
                text(temps10 - secondes, 540, 130)
        fill(255,255,255)
        
        
    if map_nombre == map_ultime :
        rect(500,0,200,200)
        if temps11 - secondes > 30 :
            fill(0,0,0)
            textSize(50)
            if temps11 - secondes > 99 :
                text(temps11 - secondes, 550, 120)
            else :
                text(temps11 - secondes, 570, 120)
        else :
            textSize(100) 
            fill(255,0,0)
            if temps11 - secondes < 10 :
                text(temps11 - secondes, 570, 130)
            else :
                text(temps11 - secondes, 540, 130)
        fill(255,255,255)
        
        
    if map_nombre == map_worm :
        rect(500,0,200,200)
        if temps7 - secondes > 30 :
            fill(0,0,0)
            textSize(50)
            if temps7 - secondes > 99 :
                text(temps7 - secondes, 550, 120)
            else :
                text(temps7 - secondes, 570, 120)
        else :
            textSize(100) 
            fill(255,0,0)
            if temps7 - secondes < 10 :
                text(temps7 - secondes, 570, 130)
            else :
                text(temps7 - secondes, 540, 130)
        fill(255,255,255)
            
#------------création de fonctions-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def setup():
    size(1200, 1200);
    global heroImg, case, case_blocus, blocus_couleur, case_blocus2, ecran_victoire, bouton_1, bouton_2, bouton_3 ,bouton_4, bouton_5, bouton_6, bouton_7, bouton_8, bouton_9, bouton_10, bouton_11, ecran_defaite, fanta_Img, affronte_les_arabes, olfo, enfer, ui, wtc_38, case_vide, minecart, sol, minecart_2, case_vide_2, case_vide_3, boite_img, bouton, bouton_V, bouton_J, porte_1, gold, cle, porte_cle, grinder, left, freeze, ecran_fin, aventure, arcade, fleche
    heroImg = loadImage("bullya.png")
    case = loadImage("sol vert.png")
    case_blocus = loadImage("go.png")
    case_blocus2 = loadImage("stop.png")
    blocus_couleur = loadImage("Jaune.png")
    ecran_victoire = loadImage("win.png")
    ecran_defaite = loadImage("lose.png")
    bouton_1 = loadImage("boutons-1.png.png")
    bouton_2 = loadImage("boutons-2.png.png")
    bouton_3 = loadImage("boutons-3.png.png")
    bouton_4 = loadImage("boutons-4.png.png")
    bouton_5 = loadImage("boutons-5.png.png")
    bouton_6 = loadImage("boutons-6.png.png")
    bouton_7 = loadImage("boutons-7.png.png")
    bouton_8 = loadImage("boutons-8.png.png")
    bouton_9 = loadImage("boutons-9.png.png")
    bouton_10 = loadImage("boutons-10.png.png")
    bouton_11 = loadImage("boutons-11.png.png")
    fanta_Img = loadImage("fanta.png")
    affronte_les_arabes = loadImage("affronte les arabes-1.png.png")
    olfo = loadImage("olfo.png")
    enfer = loadImage("enfer.png")
    ui = loadImage("ui.png")
    case_vide = loadImage("rail.png")
    wtc_38 = loadImage("wtc 38.png")
    minecart = loadImage("minecart.png")
    sol = loadImage("sol.png")
    minecart_2 = loadImage("minecart 2.png") 
    case_vide_2 = loadImage("rail 2.png")
    case_vide_3 = loadImage("rail 3.png")
    boite_img = loadImage("box.png")
    bouton = loadImage("bouton.png")
    bouton_V = loadImage("bouton done.png")
    bouton_J = loadImage("bouton joueur.png")
    porte_1 = loadImage("porte bouton.png")
    gold = loadImage("cle bloc.png")
    cle = loadImage("cle.png")
    porte_cle = loadImage("porte cle.png")
    grinder = loadImage("grinder.png")
    left = loadImage("left.png")
    freeze = loadImage("three freeze.png")
    ecran_fin = loadImage("true end.png")
    arcade = loadImage("ARCADE.png")
    aventure = loadImage("AVENTURE.png")
    fleche = loadImage("fleche.png")

    
def draw():
    global heroImg,hero_x,hero_y, hero_colonne, hero_ligne, backswitch, map_choisie, fanta, fleche_time  #il faut mettre toute les variables qu'on utilise plus bas là dedans ;)
    background(80, 25, 12)
    choix_de_la_map()
    print(map_choisie)
    print(fleche_time)
    
    if map_choisie == 1 :
        if stop_check == 0 :
            if lost == 0 :
                tout_tout_tout_sur_les_maps(map_tuto_1, coord_liste_tuto_1)
                deplacement(map_tuto_1, coord_liste_tuto_1)
                fill(255,255,0)
                textSize(50)
                text("Pour avancer, utilisez les touches Z Q S D",100,300)
                text("comme des touches directionelles.", 170, 400)
                fill(255,255,255)
                if fanta == 0 :
                    image(heroImg, hero_x, hero_y)
                else :
                    image(fanta_Img, hero_x, hero_y)
        win(map_tuto_1)
        lose(map_tuto_1)
            
    if map_choisie == 2 :
        if stop_check == 0 :
            if lost == 0 :
                tout_tout_tout_sur_les_maps(map_tuto_2, coord_liste_tuto_1)
                deplacement(map_tuto_2, coord_liste_tuto_1)
                fill(255,255,0)
                textSize(50)
                text("Bullya a un rendez vous urgent, mais,",15,100)
                text("avant, elle a decide de goumer tout le sol, donc",15,200)
                text("Le but est de passer sur toute les cases possible",15,300)
                text("et de les colorier en vert avant la fin du temps.", 15, 400)
                fill(255,255,255)
                if fanta == 0 :
                    image(heroImg, hero_x, hero_y)
                else :
                    image(fanta_Img, hero_x, hero_y)
        win(map_tuto_2)
        lose(map_tuto_2)
            
    if map_choisie == 3 :
        if stop_check == 0 :
            if lost == 0 :
                tout_tout_tout_sur_les_maps(map_tuto_3, coord_liste_tuto_1)
                deplacement(map_tuto_3, coord_liste_tuto_1)
                fill(255,255,0)
                textSize(50)
                text("Les blocs GO vert sont traversable, ",200,300)
                text("mais vous vous aretez sur les STOP rouges.", 80, 400)
                text("bonne chance !", 400, 500)
                fill(255,255,255)
                if fanta == 0 :
                    image(heroImg, hero_x, hero_y)
                else :
                    image(fanta_Img, hero_x, hero_y)
        win(map_tuto_3)
        lose(map_tuto_3)
            
    if map_choisie == 4 :
        if stop_check == 0 :
            if lost == 0 :
                tout_tout_tout_sur_les_maps(map_un_peu_illisible, coord_liste_2)
                deplacement(map_un_peu_illisible, coord_liste_2)
                if fanta == 0 :
                    image(heroImg, hero_x, hero_y)
                else :
                    image(fanta_Img, hero_x, hero_y)
        win(map_un_peu_illisible)
        lose(map_un_peu_illisible)
        
        
    if map_choisie == 5 :
        if stop_check == 0 :
            if lost == 0 :
                tout_tout_tout_sur_les_maps(map_test, coord_liste_2)
                deplacement(map_test, coord_liste_2)
                if fanta == 0 :
                    image(heroImg, hero_x, hero_y)
                else :
                    image(fanta_Img, hero_x, hero_y)
        win(map_test)
        lose(map_test)
        
        
    if map_choisie == 7 :
        if stop_check == 0 :
            if lost == 0 :
                tout_tout_tout_sur_les_maps(map_worm, coord_liste_7)
                deplacement(map_worm, coord_liste_7)
                if fanta == 0 :
                    image(heroImg, hero_x, hero_y)
                else :
                    image(fanta_Img, hero_x, hero_y)
        win(map_worm)
        lose(map_worm)  
            
    if map_choisie == 9 :
        if stop_check == 0 :
            if lost == 0 :
                tout_tout_tout_sur_les_maps(map_liste_illisible, coord_liste)
                deplacement(map_liste_illisible, coord_liste)
                if fanta == 0 :
                    image(heroImg, hero_x, hero_y)
                else :
                    image(fanta_Img, hero_x, hero_y)
        win(map_liste_illisible)
        lose(map_liste_illisible)    
            
    if map_choisie == 10 :
        if stop_check == 0 :
            if lost == 0 :
                tout_tout_tout_sur_les_maps(map_liste_4, coord_liste_4)
                deplacement(map_liste_4, coord_liste_4)
                if fanta == 0 :
                    image(heroImg, hero_x, hero_y)
                else :
                    image(fanta_Img, hero_x, hero_y)
        win(map_liste_4)
        lose(map_liste_4) 
        
    if map_choisie == 11 :
        if stop_check == 0 :
            if lost == 0 :
                tout_tout_tout_sur_les_maps(map_ultime, coord_liste_11)
                boites_2(map_ultime, coord_liste_11)
                deplacement(map_ultime, coord_liste_11)
                fill(255,255,0)
                textSize(20)
                text("essayez de mettre une boite ici !",200,1020)
                text("et ici !",640,1020)
                fill(255,255,255)
                if fleche_time < 1 :
                    image(fleche, 480, 970)
                    image(fleche, 645, 970)
                else :
                    image(fleche, 480, 950)
                    image(fleche, 645, 950)
                if fanta == 0 :
                    image(heroImg, hero_x, hero_y)
                    image(boite_img, boite_x, boite_y)
                else :
                    image(fanta_Img, hero_x, hero_y)
        win(map_ultime)
        lose(map_ultime) 
        
    print(secondes)
    
#----fonctions de déplacement-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def deplacement(map_nombre, coords):
    global direction, hero_ligne, hero_colonne, hero_x, hero_y, fanta, direction_boite
    if keyPressed : 
        if this.key == 'd' :  
            if direction == 'haut' or direction == 'gauche' or direction == 'bas'   :  
                print("")
            else :
                direction = 'droite'
           
        if this.key == 'q' :
            if direction == 'haut' or direction == 'droite' or direction == 'bas'  :
                print("")
            else :
                direction = 'gauche'
            
        if this.key == 'z' :
            if direction == 'droite' or direction == 'gauche' or direction == 'bas' :  
                print("")
            else :
                direction = 'haut'
            
        if this.key == 's' :
            if direction == 'haut' or direction == 'gauche' or direction == 'droite' :  
                print("")
            else :        
                direction = 'bas'
                
        if this.key == 'p' :
            global trail_ligne, case, stop_check
            if reseted == 0 :
                lane = len(map_nombre)
                colonne = len(map_nombre[0])
                for o in range(lane) :
                    for i in range (colonne):
                        if map_nombre [o][i][0] == "0" :
                            map_nombre[o].pop(i)
                            map_nombre[o].insert(i,"V")
                    trail_ligne = trail_ligne + 20
                trail_ligne = coords[0][1]
                

#        if this.key == 'y' : 
#            if map_nombre == map_liste_illisible :
#               hero_x = xstart1
#               hero_y = ystart1
#               hero_ligne = ligne_start_1
#               hero_colonne = colonne_start_1
#               
#            if map_nombre == map_un_peu_illisible :
#               hero_x = xstart2
#               hero_y = ystart2
#               hero_ligne = ligne_start_2
#               hero_colonne = colonne_start_2
#               
#            if map_nombre == map_liste_3 :
#               hero_x = xstart3
#               hero_y = ystart3
#               hero_ligne = ligne_start_3
#               hero_colonne = colonne_start_3
#        
#            if map_nombre == map_liste_4 :
#                hero_x = xstart4
#                hero_y = ystart4
#                hero_ligne = ligne_start_4
#                hero_colonne = colonne_start_4
#                
#            if map_nombre == map_tuto_1 or map_nombre == map_tuto_2 or map_nombre == map_tuto_3 :
#                hero_x = xstart_tuto_1
#                hero_y = ystart_tuto_1
#                hero_ligne = ligne_start_tuto1
#                hero_colonne = colonne_start_tuto1
                
                
    if direction == 'droite' :
        if map_nombre [hero_ligne][hero_colonne + 1][0] == "1" or blocus(map_nombre) == 'true' or map_nombre [hero_ligne][hero_colonne + 1][0] == "L" or map_nombre [hero_ligne][hero_colonne + 1][0] == "R"  or map_nombre [hero_ligne][hero_colonne + 1][0] == "D" or map_nombre [hero_ligne][hero_colonne + 1][0] == "U" or map_nombre[hero_ligne][hero_colonne + 1][0] == "H" and direction_boite == "stop" or map_nombre[hero_ligne][hero_colonne + 1] == "P" or map_nombre[hero_ligne][hero_colonne + 1] == "O":
            direction = 'none'
        else :
            if hero_ligne == boite_ligne and hero_colonne + 1 == boite_colonne :
                direction_boite = "droite" 
            for i in range(20) :
                hero_x = hero_x + 1
            hero_colonne = hero_colonne + 1  
            
          
    if direction == 'gauche' :
        if map_nombre [hero_ligne][hero_colonne - 1][0] == "1" or blocus(map_nombre) == 'true' or map_nombre [hero_ligne][hero_colonne - 1][0] == "L" or map_nombre [hero_ligne][hero_colonne - 1][0] == "R"  or map_nombre [hero_ligne][hero_colonne - 1][0] == "D" or map_nombre [hero_ligne][hero_colonne - 1][0] == "U" or map_nombre[hero_ligne][hero_colonne - 1][0] == "H" and direction_boite == "stop" or map_nombre[hero_ligne][hero_colonne - 1] == "P" or map_nombre[hero_ligne][hero_colonne - 1] == "O":
            direction = 'none'
        else :
            if hero_ligne == boite_ligne and hero_colonne - 1 == boite_colonne :
                direction_boite = "gauche"
            for i in range(20) :
                hero_x = hero_x - 1
            hero_colonne = hero_colonne - 1

            
    if direction == 'haut' :
        if map_nombre [hero_ligne - 1][hero_colonne][0] == "1" or blocus(map_nombre) == 'true' or map_nombre [hero_ligne - 1][hero_colonne][0] == "L" or map_nombre [hero_ligne - 1][hero_colonne][0] == "R" or map_nombre [hero_ligne - 1][hero_colonne][0] == "D" or map_nombre [hero_ligne - 1][hero_colonne][0] == "U" or map_nombre [hero_ligne - 1][hero_colonne][0] == "H" and direction_boite == "stop" or map_nombre[hero_ligne - 1][hero_colonne] == "P" or map_nombre[hero_ligne - 1][hero_colonne] == "O" :
            direction = 'none'
        else :
            if hero_ligne - 1 == boite_ligne and hero_colonne == boite_colonne :
                direction_boite = "haut"
            for i in range(20) :
                hero_y = hero_y - 1
            hero_ligne = hero_ligne - 1
            
            
    if direction == 'bas' :
        if map_nombre [hero_ligne + 1][hero_colonne][0] == "1" or blocus(map_nombre) == 'true' or map_nombre [hero_ligne + 1][hero_colonne][0] == "L" or map_nombre [hero_ligne + 1][hero_colonne][0] == "R" or map_nombre [hero_ligne + 1][hero_colonne][0] == "D" or map_nombre [hero_ligne + 1][hero_colonne][0] == "U" or map_nombre [hero_ligne + 1][hero_colonne][0] == "H" and direction_boite == "stop_down" or map_nombre[hero_ligne + 1][hero_colonne] == "P" or map_nombre[hero_ligne + 1][hero_colonne] == "O":
            direction = 'none'
        else :
            if hero_ligne + 1 == boite_ligne and hero_colonne == boite_colonne :
                direction_boite = "bas"
            for i in range(20) :
                hero_y = hero_y + 1
            hero_ligne = hero_ligne + 1
                   
        
            
def keyReleased() :
    global fanta, last_touche, boite_x ,boite_y  ,boite_ligne ,boite_colonne
    
    if this.key == 'r' :
        boite_x = 860
        boite_y = 340
        boite_ligne = 2
        boite_colonne = 28
        
    if this.key == 'z' :
        if last_touche == "z" :
            last_touche = "z2"
        else :
            if last_touche == 0 :
                last_touche = "z"
        
        if last_touche == "s" or last_touche == "q" or last_touche == "q2" or last_touche == "s2" or last_touche == "d" or last_touche == "d2" or last_touche == "b" or last_touche == "a" :
            last_touche = 0
            
    if this.key == 's' :
        if last_touche == "z2" :
            last_touche = "s"
        else :
            if last_touche == "s" :
                last_touche = "s2"
                
            if last_touche == "z" or last_touche == "q" or last_touche == "q2" or last_touche == "d" or last_touche == "d2" or last_touche == "b" or last_touche == "a" :
                last_touche = 0
            
            
    if this.key == 'q' :
        if last_touche == "s2" :
            last_touche = "q"
        else :
            if last_touche == "d" :
                last_touche = "q2"
        
        if last_touche == "s" or last_touche == "d2" or last_touche == "b" or last_touche == "a" or last_touche == "z" or last_touche == "z2" :
            last_touche = 0
            
    if this.key == 'd' :
        if last_touche == "q" :
            last_touche = "d"
        else :
            if last_touche == "q2" :
                last_touche = "d2"
                
        if last_touche == "s" or last_touche == "s2" or last_touche == "a" or last_touche == "z" or last_touche == "z2" :
            last_touche = 0

    if this.key == 'b' :
        if last_touche == "d2" :
            last_touche = "b"
            
        if last_touche == "s" or last_touche == "q" or last_touche == "q2" or last_touche == "s2" or last_touche == "d" or last_touche == "a" :
            last_touche = 0
    
    if this.key == 'a' :
        if last_touche == "b" :
            last_touche = 0 
            if fanta == 0 :
                fanta = 1
            else :
                fanta = 0
            
#----fonctions de déplacement-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----fonctions pour appuyer sur les boutons---------------------------------------------------------------------------------------------------------------------------------------------------------------

def mousePressed() :
    global commence, while_infini, stop_check, map_choisie, last_map, lost, choisi
    if commence == 0 :
        if mouseX > B1X and mouseY > B1Y and mouseX < B1X + 250 and mouseY < B1Y + 250 :
            commence = 1
            map_choisie = 1
            last_map = 1
            start_point(map_tuto_1)
        
        if mouseX > B2X and mouseY > B2Y and mouseX < B2X + 250 and mouseY < B2Y + 250 :
            commence = 1
            map_choisie = 2
            last_map = 2
            start_point(map_tuto_2)

        if mouseX > B3X and mouseY > B3Y and mouseX < B3X + 250 and mouseY < B3Y + 250 :
            commence = 1
            map_choisie = 3
            last_map = 3
            start_point(map_tuto_3)

        
        if mouseX > B4X and mouseY > B4Y and mouseX < B4X + 250 and mouseY < B4Y + 250 :
            commence = 1
            map_choisie = 4
            last_map = 4
            start_point(map_un_peu_illisible)
            
            
        if mouseX > B5X and mouseY > B5Y and mouseX < B5X + 250 and mouseY < B5Y + 250 :
            commence = 1
            map_choisie = 5
            last_map = 5
            start_point(map_test)

        if mouseX > B7X and mouseY > B7Y and mouseX < B7X + 250 and mouseY < B7Y + 250 :
            commence = 1
            map_choisie = 7
            last_map = 7
            start_point(map_worm)
        
        if mouseX > B9X and mouseY > B9Y and mouseX < B9X + 250 and mouseY < B9Y + 250 :
            commence = 1
            map_choisie = 9
            last_map = 9
            start_point(map_liste_illisible)

        
        if mouseX > B10X and mouseY > B10Y and mouseX < B10X + 250 and mouseY < B10Y + 250 :
            commence = 1
            map_choisie = 10
            last_map = 10
            start_point(map_liste_4)
            
        if mouseX > B11X and mouseY > B11Y and mouseX < B11X + 250 and mouseY < B11Y + 250 :
            commence = 1
            map_choisie = 11
            last_map = 11
            start_point(map_ultime)

        
    if mouseX > 624 and mouseY > 495 and mouseX < 882 and mouseY < 713 : 
        if stop_check == 1 or lost == 1 :
            commence = 0
            stop_check = 0
            lost = 0
            map_choisie = 0
        
            
    if mouseX > 285 and mouseY > 493 and mouseY < 710 and mouseX < 556 :
        if stop_check == 1 or lost == 1 :
            stop_check = 0
            lost = 0
            if last_map == 1 : 
                reset(map_tuto_1, coord_liste_tuto_1)
                start_point(map_tuto_1)
                
            if last_map == 2 : 
                reset(map_tuto_2, coord_liste_tuto_1)
                start_point(map_tuto_1)

            if last_map == 3 : 
                reset(map_tuto_3, coord_liste_tuto_1)
                start_point(map_tuto_1)

            if last_map == 4 : 
                reset(map_un_peu_illisible, coord_liste_2)
                start_point(map_un_peu_illisible)
                
            if last_map == 5 : 
                reset(map_test, coord_liste_2)
                start_point(map_test)
                
            if last_map == 7 : 
                reset(map_worm, coord_liste_7)
                start_point(map_worm)
                
            if last_map == 9 : 
                reset(map_liste_illisible, coord_liste)
                start_point(map_liste_illisible)
                
            if last_map == 10 : 
                reset(map_liste_4, coord_liste_4)
                start_point(map_liste_4)
                
            if last_map == 11 : 
                reset(map_ultime, coord_liste_11)
                start_point(map_ultime)


#----fonctions pour appuyer sur les boutons---------------------------------------------------------------------------------------------------------------------------------------------------------------

#----Listes pour décrire la map---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
coord_liste = [(360,300) ,(380,300) ,(400,300) ,(420,300) ,(440,300) ,(460,300) ,(480,300) ,(500,300) ,(520,300) ,(540,300) ,(560,300) ,(580,300) ,(600,300) ,(620,300) ,(640,300) ,(660,300) ,(680,300) ,(700,300) ,(720,300) ,(740,300) ,(760,300) ,(780,300) ,(800,300) ,(820,300), (840,300)]
coord_liste_2 = [ (500,400) ,(520,400) ,(540,400) ,(560,400) ,(580,400) ,(600,400) ,(620,400) ,(640,400) ,(660,400) ,(680,300) ,(700,400) ,(720,400) ]
coord_liste_tuto_1 = [ (420,580) ,(440,580) ,(460,580) ,(480,580) ,(500,580) ,(520,580) ,(540,580) ,(560,580) ,(580,580) ,(600,580) ,(620,580) ,(640,580) ,(660,580) ,(680,580) ,(700,580) ,(720,580) ,(740,580) ,(760,580) ,(780,580) ,(800,580) ]
coord_liste_3 = [ (460,500),(480,500),(500,500),(520,500),(540,500),(560,500),(580,500),(600,500), (620,500),(640,500),(660,500),(680,500),(700,500),(720,500),(740,500),(760,500) ]
coord_liste_4 =[ (300,300),(320,300),(340,300),(360,300),(380,300),(400,300),(420,300),(440,300),(460,300),(480,300),(500,300),(520,300),(540,300),(560,300),(580,300),(600,300),(620,300),(640,300),(660,300),(680,300),(700,300),(720,300),(740,300),(760,300),(780,300),(800,300),(820,300),(840,300),(860,300),(880,300),(900,300)]
coord_liste_11 =[ (300,300),(320,300),(340,300),(360,300),(380,300),(400,300),(420,300),(440,300),(460,300),(480,300),(500,300),(520,300),(540,300),(560,300),(580,300),(600,300),(620,300),(640,300),(660,300),(680,300),(700,300),(720,300),(740,300),(760,300),(780,300),(800,300),(820,300),(840,300),(860,300),(880,300),(900,300), (920, 300)]
coord_liste_7 = [ (340,300),(360,300),(380,300),(400,300),(420,300),(440,300),(460,300),(480,300),(500,300),(520,300),(540,300),(560,300),(580,300),(600,300),(620,300),(640,300),(660,300),(680,300),(700,300),(720,300),(740,300),(760,300),(780,300),(800,300),(820,300),(840,300)]

map_liste_illisible = [ ["1", "1", "1", "1", "1","°" ,"°","°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ], 
                        ["1" ,"0" ,"0" ,"0" ,"1" ,"1" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" ,"°" , "°"], 
                        ["1" ,"0" ,"0" ,"0" ,"0" ,"1" ,"°" ,"1" ,"1" ,"1" ,"1" ,"1" ,"1" ,"1","1" ,"1" ,"1" ,"1" ,"°" ,"°" ,"°", "°", "°", "°", "°","°" ], 
                        ["1","0","0","0","0", "1" , "1" , "1", "0", "0", "0", "0", "M", "0", "0", "0", "0", "1", "1", "1", "1", "1", "°", "°", "°","°" ], 
                        ["1","0","0","0","0", "0" , "0" , "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "°", "°","°" ],
                        ["1","0","0","0","0", "0" , "0" , "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "°", "°","°" ],
                        ["1","0","0","0","0", "0" , "0" , "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "°", "°","°" ],
                        ["°","1","0","0","0", "0" , "0" , "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "°", "°", "°","°" ], 
                        ["1","0","0","0","0", "0" , "0" , "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "°", "°", "°", "°","°" ], 
                        ["1","0","0","0","0", "1" , "1" , "1", "0", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "0", "1", "°", "°", "°", "°","°" ], 
                        ["1","0","0","0","0", "0" , "0" , "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "1","°" ], 
                        ["1","0","0","0","0", "0" , "0" , "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "1","°" ], 
                        ["1","1","1","1","0", "1" , "1" , "1", "0", "1", "1", "1", "0", "1", "1", "1", "0", "1", "0", "0", "0", "1", "0", "0", "1","°" ], 
                        ["°","°","°","1","0", "1" , "1" , "1", "0", "1", "1", "1", "0", "1", "1", "1", "0", "1", "0", "0", "0", "1", "0", "0", "1","°" ], 
                        ["°","°","°","1","0", "0" , "0" , "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "0", "1", "0", "1","°" ], 
                        ["°","°","°","1","0", "1" , "1" , "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0", "0", "0", "1", "0", "1","°" ], 
                        ["°","°","°","1","0", "1" , "1" , "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "0", "0", "1", "0", "1","°" ], 
                        ["°","°","°","1","0", "1" , "1" , "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "0", "0", "1", "0", "1","°" ], 
                        ["°","°","°","1","0", "0" , "0" , "0", "M", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1","°" ], 
                        ["°","°","°","1","0", "1" , "1" , "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0", "1", "1", "°","°" ], 
                        ["°","°","°","1","0", "1" , "°" , "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "1", "0", "1", "°", "°", "°","°" ], 
                        ["°","°","°","1","0", "1" , "°" , "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "1", "0","1", "°", "°", "°","°" ], 
                        ["°","°","°","°","1", "°" , "°" , "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "1","°", "°", "°", "°","°" ],
                        ["°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°", "°"] ]

map_un_peu_illisible = [ ["°","1","1","1","1","1","1","1","1","°","°","°"],
                       ["1","0","0","0","0","0","0","0","0","1","°","°"],
                       ["1","0","0","0","0","0","0","0","0","0","1","°"],
                       ["1","0","0","0","0","0","0","0","0","0","1","°"],
                       ["1","1","0","0","0","0","0","0","0","0","1","°"],
                       ["1","0","0","0","0","0","0","0","0","1","1","°"],
                       ["1","0","0","0","0","0","0","0","0","0","1","°"],
                       ["1","0","0","0","0","0","0","0","0","0","1","°"],
                       ["°","1","0","0","0","0","0","0","0","0","1","°"],
                       ["°","°","1","1","1","1","1","1","1","1","°","°"],
                       ["°","°","°","°","°","°","°","°","°","°","°","°"] ]

map_test = [ ["1","1","1","1","1","1","1","1","1","1","1"],
             ["1","0","0","0","0","0","0","0","0","0","1"],
             ["1","0","1","1","1","1","1","1","1","0","1"],
             ["1","0","0","0","0","0","0","0","0","0","1"],
             ["1","N","N","N","N","N","N","N","N","L","1"],
             ["1","0","0","0","0","0","0","0","0","0","1"],
             ["1","0","0","0","0","0","0","0","0","0","1"],
             ["1","R","N","N","N","N","N","N","N","N","1"],
             ["1","0","0","0","0","0","0","0","0","0","1"],
             ["1","0","1","1","1","1","1","1","1","0","1"],
             ["1","0","0","0","0","0","0","0","0","0","1"],
             ["1","1","1","1","1","1","1","1","1","1","1"],
             ["°","°","°","°","°","°","°","°","°","°","°"] ]


map_liste_4 = [ ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                ["1","0","M","0","0","0","0","0","0","0","0","0","M","0","1","0","M","0","0","0","0","0","0","0","0","0","M","0","1"],
                ["1","0","0","0","0","0","M","0","0","0","0","0","0","0","1","0","0","0","0","0","0","0","M","0","0","0","0","0","1"],
                ["1","0","0","1","1","1","0","0","1","1","1","1","0","0","1","0","0","1","1","1","1","0","0","1","1","1","0","0","1"],
                ["1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1"],
                ["1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1"],
                ["1","0","0","1","1","1","0","0","1","0","1","1","1","1","1","1","1","1","1","0","1","0","0","1","1","1","0","0","1"],
                ["1","0","0","0","0","0","0","0","1","0","0","0","0","0","1","0","0","0","0","0","1","0","0","0","0","0","0","0","1"],
                ["1","1","1","1","1","1","0","0","1","1","1","1","1","0","1","0","1","1","1","1","1","0","0","1","1","1","1","1","1"],
                ["°","°","°","°","°","1","0","0","1","0","0","0","0","M","0","M","0","0","0","0","1","0","0","1","°","°","°","°","°"],
                ["1","1","1","1","1","1","0","0","1","0","0","1","1","1","1","1","1","1","0","0","1","0","0","1","1","1","1","1","1"],
                ["1","0","0","0","0","0","0","M","0","0","0","1","°","°","°","°","°","1","0","0","0","0","0","0","0","0","0","0","1"],
                ["1","0","0","0","0","0","0","0","0","0","0","1","°","°","°","°","°","1","0","0","0","M","0","0","0","0","0","0","1"],
                ["1","1","1","1","1","1","0","0","1","0","0","1","1","1","1","1","1","1","0","0","1","0","0","1","1","1","1","1","1"],
                ["°","°","°","°","°","1","0","0","1","0","M","0","0","0","0","0","0","0","0","0","1","0","0","1","°","°","°","°","°"],
                ["°","°","°","°","°","1","0","0","1","0","0","0","0","0","0","0","0","0","M","0","1","0","0","1","°","°","°","°","°"],
                ["1","1","1","1","1","1","0","0","1","0","0","1","1","1","1","1","1","1","0","0","1","0","0","1","1","1","1","1","1"],
                ["1","0","0","0","0","0","0","0","0","0","0","0","0","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0","1"],
                ["1","0","0","0","0","0","0","0","0","0","0","0","0","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0","1"],
                ["1","0","1","1","1","1","0","0","1","1","1","1","1","0","1","0","1","1","1","1","1","0","0","1","1","1","1","0","1"],
                ["1","0","0","0","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","0","0","0","0","1"],
                ["1","0","0","0","0","1","0","0","0","M","0","0","0","0","0","0","0","0","0","M","0","0","0","1","0","0","0","0","1"],
                ["1","1","1","1","0","1","0","0","1","0","1","1","1","1","1","1","1","1","1","0","1","0","0","1","0","1","1","1","1"],
                ["1","0","0","0","0","0","0","0","1","0","0","0","0","0","1","0","0","0","0","0","1","0","0","0","0","0","0","0","1"],
                ["1","0","0","0","0","0","0","0","1","0","0","0","0","0","1","0","0","0","0","0","1","0","0","0","0","0","0","0","1"],
                ["1","0","1","1","1","1","1","1","1","1","1","1","1","0","1","0","1","1","1","1","1","1","1","1","1","1","1","0","1"],
                ["1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1"],
                ["1","0","0","0","0","0","0","0","M","0","0","0","0","0","0","0","0","0","0","0","M","0","0","0","0","0","0","0","1"],
                ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"] ]

map_tuto_1 = [ ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","°"],
               ["1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","°"],
               ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","°"] ]

map_tuto_2 = [ ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","°"],
               ["1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","°"],
               ["1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","°","°","°","°","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","°","°","°","°","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","°","°","°","°","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","°","°","°","°","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","°","°","°","°","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","°","°","°","°","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","°","°","°","°","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","°","°","°","°","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","°","°","°","°","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","°","°","°","°","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","°","°","°","°","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","°","°","°","°","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","°","°","°","°","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","°","°","°","°","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","°"],
               ["1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","°"],
               ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","°"] ]


map_tuto_3 = [ ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","°"],
               ["1","0","0","0","0","0","0","0","0","M","M","0","0","0","0","0","0","0","0","1","°"],
               ["1","0","1","1","1","1","1","1","1","0","0","1","1","1","1","1","1","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","1","0","0","1","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","1","0","0","1","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","1","0","0","1","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","1","0","0","1","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","1","0","0","1","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","1","0","0","1","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","1","0","0","1","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","1","0","0","1","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","1","0","0","1","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","1","0","0","1","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","1","0","0","1","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","1","0","0","1","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","1","0","0","1","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","°","°","°","°","°","1","0","0","1","°","°","°","°","°","1","0","1","°"],
               ["1","0","1","1","1","1","1","1","1","0","0","1","1","1","1","1","1","1","0","1","°"],
               ["1","0","0","0","0","0","0","0","0","M","M","0","0","0","0","0","0","0","0","1","°"],
               ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","°"] ]


map_ultime = [ ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
               ["1","K","K","K","K","K","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","1","0","0","1"],
               ["1","K","K","K","K","K","1","0","0","0","0","0","0","1","1","1","0","1","1","1","0","0","0","0","0","0","1","1","0","0","1"],
               ["1","K","K","K","K","M","P","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","M","1","0","0","0","0","1"],
               ["1","K","K","C","K","K","1","0","0","0","0","0","0","1","1","1","0","1","1","1","0","0","0","0","0","1","0","0","0","0","1"],
               ["1","1","1","1","1","1","1","M","0","M","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","0","1","1","1","1"],
               ["1","0","D","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","T","0","0","1"],
               ["1","0","T","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","T","0","0","1"],
               ["1","0","T","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","T","0","0","1"],
               ["1","0","T","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","T","0","0","1"],
               ["1","N","X","R","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","X","N","N","1"],
               ["1","0","T","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","T","0","0","1"],
               ["1","0","T","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","T","0","0","1"],
               ["1","0","T","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","U","0","0","1"],
               ["1","1","T","0","0","0","0","0","0","0","0","0","0","0","M","0","0","0","0","0","0","0","0","0","0","0","0","T","0","0","1"],
               ["1","1","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","1","1","1","1","1","1","1","1","1","1","1","O","1"],
               ["1","1","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","0","0","0","0","0","0","0","0","0","0","0","0","1"],
               ["1","1","1","0","1","0","1","0","1","0","1","1","1","1","0","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0","1"],
               ["1","1","G","0","0","M","0","M","0","M","0","0","0","0","0","0","1","0","0","0","0","0","0","0","0","0","0","0","0","<","1"],
               ["1","1","0","0","1","0","1","0","1","0","1","1","1","1","1","1","1","0","0","0","0","0","0","0","0","0","0","0","0","1","1"],
               ["1","1","0","0","1","0","1","0","1","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1"],
               ["1","1","0","0","1","0","1","0","1","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1"],
               ["1","1","0","0","1","0","1","0","1","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","M","0","1"],
               ["1","1","0","0","1","0","1","0","1","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","1"],
               ["1","1","0","0","1","0","1","0","1","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1"],
               ["1","1","0","0","1","0","1","0","1","0","1","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1"],
               ["1","1","0","0","1","0","1","0","1","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1"],
               ["1","1","0","0","1","0","1","0","1","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1"],
               ["1","1","0","0","1","0","1","0","1","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","1"],
               ["1","1","0","0","1","0","1","0","1","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1"],
               ["1","1","0","0","0","B","1","B","1","B","1","0","0","0","0","0","0","H","0","0","0","0","0","0","0","0","0","0","0","0","1"],
               ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"] ]


map_worm = [ ["°","°","°","1","1","1","1","°","°","°","°","°","°","°","°","°","°","°","°","°","°","°","°","°","°","°"],
             ["°","°","1","1","0","0","0","1","1","1","°","°","°","°","°","°","°","°","°","°","°","°","°","°","°","°"],
              ["°","1","0","0","0","0","0","0","0","1","1","°","°","°","°","°","°","°","°","°","°","°","°","°","°","°"],
["°","1","0","0","1","1","M","0","0","0","0","1","1","°","°","°","°","°","°","°","°","°","°","°","°","°"],
["1","0","0","0","1","1","0","0","0","0","0","0","0","1","°","°","°","°","°","°","°","°","°","°","°","°"],
["1","0","0","0","0","0","0","0","0","0","0","0","0","0","1","1","°","°","°","°","°","°","°","°","°","°"],
["1","0","0","0","0","0","0","0","M","0","0","0","0","0","0","1","°","°","°","°","°","°","°","°","°","°"],
["1","0","0","0","0","M","0","0","0","0","0","0","0","0","0","0","1","°","°","°","°","°","°","°","°","°"],
["°","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","°","°","°","°","°","°","°","°","°"],
["°","1","1","1","1","0","0","0","0","1","1","1","0","0","0","0","1","1","°","°","°","°","°","°","°","°"],
["°","°","°","1","1","0","0","0","0","1","°","1","0","0","0","0","0","1","°","°","°","°","°","°","°","°"],
["°","°","°","°","1","0","0","0","0","1","°","1","0","0","0","0","0","1","°","°","°","°","°","°","°","°"],
["°","°","°","°","1","0","0","0","0","1","°","1","0","0","0","0","0","1","°","°","°","°","°","°","°","°"],
["°","°","°","°","1","0","0","0","0","1","1","1","0","0","0","0","0","1","°","°","°","°","°","°","°","°"],
["°","°","°","°","1","0","0","0","0","0","0","0","0","0","0","0","0","0","1","°","°","°","°","°","°","°"],
["°","°","°","°","1","0","0","0","0","0","0","0","0","0","M","0","0","0","1","°","°","°","°","°","°","°"],
["°","°","°","°","1","0","0","0","0","0","0","0","0","0","0","0","0","0","1","1","°","°","°","°","°","°"],
["°","°","°","°","°","1","0","0","0","0","0","0","0","0","0","0","0","0","0","1","1","°","°","°","°","°"],
["°","°","°","°","°","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","1","1","1","1","°"],
["°","°","°","°","°","1","1","0","0","0","0","M","0","0","0","0","0","0","0","0","0","0","0","0","0","1"],
["°","°","°","°","°","°","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","M","1"],
["°","°","°","°","°","°","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1"],
["°","°","°","°","°","°","°","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1"],
["°","°","°","°","°","°","°","°","1","1","0","0","0","0","0","0","0","0","0","1","1","0","0","0","0","1"],
["°","°","°","°","°","°","°","°","°","°","1","1","1","0","0","0","0","1","1","°","°","1","1","1","1","°"],
["°","°","°","°","°","°","°","°","°","°","°","°","°","1","1","1","1","°","°","°","°","°","°","1","1","°"] ]

                    
#----Listes pour décrire la map---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
