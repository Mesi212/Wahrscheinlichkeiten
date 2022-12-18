from dice import empty_dice
from dice import dice_number
from choose_dice import choose_dice

# Modus "mode" ermöglicht einen geführten Durchgang durch das Programm, indem die Buttons nur im richtigen Modus angeklickt werden können
mode = "eingabe dices"

# Wie viele Würfel werden geworfen? Solange kein kein Button angewählt wird, werden 0 Würfel geworfen.
dices = 0
# Möchte man ein zufälliges Würfelergebnis oder selbst auswählen?
throw_type = 0
# Ist die Reihenfolge der gewürfelten Würfel entscheidend?
order_type = 0
# Liste für die gewürfelten Zahlen
zahlen = []


def setup():
    size(800, 700)
    background(255)
    textSize(20)
    fill(0)
    stroke(0)

    # erste Frage
    textAlign(LEFT, CENTER)
    text(u"Wie viele Würfel wirfst du?", 20, 20) # u vor dem String, damit ä, ö, ü angezeigt werden
    
    # Buttons ohne Inhalt
    for i in range(0, 6):
        noFill()
        empty_dice(50 + i * 40, 60)
        
    # zweite Frage
    textAlign(LEFT, CENTER)
    text(u"Möchtest du zufällig würfeln oder die Würfelzahlen selbst auswählen?", 20, 100)
    
    # Buttons ohne Inhalt
    rect(120, 140, 180, 40)
    rect(300, 140, 180, 40)
    rect(120, 500, 180, 40)
    rect(300, 500, 180, 40)
    
    
def draw():

    # Zahlen für Buttons 1 bis 6
    for i in range(0, 6):
        textAlign(CENTER, CENTER)
        fill(0)
        text(1 + i, 50 + i * 40, 60)
        
# Erste Eingabe: Wähle die Würfel aus? ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    global mode
    if mode == "eingabe dices": # nur in diesem Modus kann die Anzahl Würfel gewählt werden
        if (mouseButton == LEFT) and (30 < mouseX < 70) and (40 < mouseY < 80):
            global dices
            fill(255, 0, 0)
            empty_dice(50, 60)
            dices = 1
            mode = "eingabe throw_type"
            
        elif (mouseButton == LEFT) and (70 < mouseX < 110) and (40 < mouseY < 80):
            fill(255, 0, 0)
            empty_dice(90, 60)
            dices = 2
            mode = "eingabe throw_type"
            
        elif (mouseButton == LEFT) and (110 < mouseX < 150) and (40 < mouseY < 80):
            fill(255, 0, 0)
            empty_dice(130, 60)
            dices = 3
            mode = "eingabe throw_type"
            
        elif (mouseButton == LEFT) and (150 < mouseX < 190) and (40 < mouseY < 80):
            fill(255, 0, 0)
            empty_dice(170, 60)
            dices = 4
            mode = "eingabe throw_type"
            
        elif (mouseButton == LEFT) and (190 < mouseX < 230) and (40 < mouseY < 80):
            fill(255, 0, 0)
            empty_dice(210, 60)
            dices = 5
            mode = "eingabe throw_type"
            
        elif (mouseButton == LEFT) and (230 < mouseX < 270) and (40 < mouseY < 80):
            fill(255, 0, 0)
            empty_dice(250, 60)
            dices = 6
            mode = "eingabe throw_type"

# Zweite Eingabe: Möchtest du die Würfelzahlen selbst auswählen?------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
    textAlign(CENTER, CENTER)
    text("Zufall", 120, 140)
    text(u"selbst auswählen", 300, 140)
    
    if mode == "eingabe throw_type": # nur in diesem Modus kann der "throw type" gewählt werden
        if (mouseButton == LEFT) and (30 < mouseX < 210) and (120 < mouseY < 160):
            global throw_type
            fill(255, 0, 0)
            rect(120, 140, 180, 40)
            throw_type = 1
            mode = "eingabe order"
            
        elif (mouseButton == LEFT) and (210 < mouseX < 390) and (120 < mouseY < 160):
            fill(255, 0, 0)
            rect(300, 140, 180, 40)
            throw_type = 2
            mode = "eingabe choose dice 1"
            
        else:
            noFill()
        
        if throw_type == 2:
            for i in range(0, dices):
                fill(0)
                textAlign(LEFT, CENTER)
                text(u"Würfel " + str(i + 1), 20, 180 + i * 50)
                fill(255)
                for j in range(0, 6):
                    empty_dice(130 + j * 50, 190 + i * 50)
    
            for k in range(0, 6):
                for l in range(0, dices):
                    dice_number(130 + (k * 50), 190 + l * 50, k + 1)
                    
        elif throw_type == 1:
            for i in range(0, dices):
                random_dice = round(random(1, 6))
                zahlen.append(int(random_dice)) #int vor (random_dice), damit die Zahlen als ganze Zahlen ohne Nachkommastelle angezeigt werden
                fill(0)
                textAlign(LEFT, CENTER)
                text("Zufall", 20, 180)
                fill(255)
                empty_dice(130 + i * 50, 190)
                dice_number(130 + i * 50, 190, random_dice)
                
        else:
            noFill()
    
# Dritte Eingabe: Würfelzahlen auswählen------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    choose_dice_x = 130 # Mitte des Würfels x-Achse
    choose_dice_y = 190 # Mitte des Würfels y-Achse
    shift_dice = 50 # Einzug in x- und y-Richtung
    # nur in diesem Modus und mit "selbst auswählen" können selbst Würfel gewählt werden
    if mode == "eingabe choose dice 1" and throw_type == 2: 
        if (mouseButton == LEFT) and ((choose_dice_x - 20) < mouseX < (choose_dice_x + 20)) and ((choose_dice_y - 20) < mouseY < (choose_dice_y + 20)):
            global dices
            fill(255, 0, 0)
            empty_dice(choose_dice_x, choose_dice_y)
            fill(0)
            dice_number(choose_dice_x, choose_dice_y, 1)
            zahlen.append(1)
            mode = "eingabe choose dice 2"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 1) < mouseX < (choose_dice_x + 20 + shift_dice * 1)) and ((choose_dice_y - 20) < mouseY < (choose_dice_y + 20)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 1), choose_dice_y)
            fill(0)
            dice_number((choose_dice_x + shift_dice * 1), choose_dice_y, 2)
            zahlen.append(2)
            mode = "eingabe choose dice 2"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 2) < mouseX < (choose_dice_x + 20 + shift_dice * 2)) and ((choose_dice_y - 20) < mouseY < (choose_dice_y + 20)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 2), choose_dice_y)
            fill(0)
            dice_number((choose_dice_x + shift_dice * 2), choose_dice_y, 3)
            zahlen.append(3)
            mode = "eingabe choose dice 2"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 3) < mouseX < (choose_dice_x + 20 + shift_dice * 3)) and ((choose_dice_y - 20) < mouseY < (choose_dice_y + 20)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 3), choose_dice_y)
            fill(0)
            dice_number((choose_dice_x + shift_dice * 3), choose_dice_y, 4)
            zahlen.append(4)
            mode = "eingabe choose dice 2"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 4) < mouseX < (choose_dice_x + 20 + shift_dice * 4)) and ((choose_dice_y - 20) < mouseY < (choose_dice_y + 20)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 4), choose_dice_y)
            fill(0)
            dice_number((choose_dice_x + shift_dice * 4), choose_dice_y, 5)
            zahlen.append(5)
            mode = "eingabe choose dice 2"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 5) < mouseX < (choose_dice_x + 20 + shift_dice * 5)) and ((choose_dice_y - 20) < mouseY < (choose_dice_y + 20)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 5), choose_dice_y)
            fill(0)
            dice_number((choose_dice_x + shift_dice * 5), choose_dice_y, 6)
            zahlen.append(6)
            mode = "eingabe choose dice 2"
            
    # nur in diesem Modus, mit "selbst auswählen" und mind. 2 geworfenen Würfeln können diese Buttons gewählt werden
    if mode == "eingabe choose dice 2" and dices >= 2:
        if (mouseButton == LEFT) and ((choose_dice_x - 20) < mouseX < (choose_dice_x + 20)) and ((choose_dice_y - 20 + shift_dice * 1) < mouseY < (choose_dice_y + 20 + shift_dice * 1)):
            global dices
            fill(255, 0, 0)
            empty_dice(choose_dice_x, 240)
            fill(0)
            dice_number(choose_dice_x, 240, 1)
            zahlen.append(1)
            mode = "eingabe choose dice 3"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 1) < mouseX < (choose_dice_x + 20 + shift_dice * 1)) and ((choose_dice_y - 20 + shift_dice * 1) < mouseY < (choose_dice_y + 20 + shift_dice * 1)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 1), (choose_dice_y + shift_dice * 1))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 1), (choose_dice_y + shift_dice * 1), 2)
            zahlen.append(2)
            mode = "eingabe choose dice 3"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 2) < mouseX < (choose_dice_x + 20 + shift_dice * 2)) and ((choose_dice_y - 20 + shift_dice * 1) < mouseY < (choose_dice_y + 20 + shift_dice * 1)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 2), (choose_dice_y + shift_dice * 1))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 2), (choose_dice_y + shift_dice * 1), 3)
            zahlen.append(3)
            mode = "eingabe choose dice 3"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 3) < mouseX < (choose_dice_x + 20 + shift_dice * 3)) and ((choose_dice_y - 20 + shift_dice * 1) < mouseY < (choose_dice_y + 20 + shift_dice * 1)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 3), (choose_dice_y + shift_dice * 1))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 3), (choose_dice_y + shift_dice * 1), 4)
            zahlen.append(4)
            mode = "eingabe choose dice 3"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 4) < mouseX < (choose_dice_x + 20 + shift_dice * 4)) and ((choose_dice_y - 20 + shift_dice * 1) < mouseY < (choose_dice_y + 20 + shift_dice * 1)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 4), (choose_dice_y + shift_dice * 1))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 4), (choose_dice_y + shift_dice * 1), 5)
            zahlen.append(5)
            mode = "eingabe choose dice 3"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 5) < mouseX < (choose_dice_x + 20 + shift_dice * 5)) and ((choose_dice_y - 20 + shift_dice * 1) < mouseY < (choose_dice_y + 20 + shift_dice * 1)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 5), (choose_dice_y + shift_dice * 1))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 5), (choose_dice_y + shift_dice * 1), 6)
            zahlen.append(6)
            mode = "eingabe choose dice 3"

    # nur in diesem Modus, mit "selbst auswählen" und mind. 3 geworfenen Würfeln können diese Buttons gewählt werden
    if mode == "eingabe choose dice 3" and dices >= 3: 
        if (mouseButton == LEFT) and ((choose_dice_x - 20) < mouseX < (choose_dice_x + 20)) and ((choose_dice_y - 20 + shift_dice * 2) < mouseY < (choose_dice_y + 20 + shift_dice * 2)):
            global dices
            fill(255, 0, 0)
            empty_dice(choose_dice_x, (choose_dice_y + shift_dice * 2))
            fill(0)
            dice_number(choose_dice_x, (choose_dice_y + shift_dice * 2), 1)
            zahlen.append(1)
            mode = "eingabe choose dice 4"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 1) < mouseX < (choose_dice_x + 20 + shift_dice * 1)) and ((choose_dice_y - 20 + shift_dice * 2) < mouseY < (choose_dice_y + 20 + shift_dice * 2)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 1), (choose_dice_y + shift_dice * 2))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 1), (choose_dice_y + shift_dice * 2), 2)
            zahlen.append(2)
            mode = "eingabe choose dice 4"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 2) < mouseX < (choose_dice_x + 20 + shift_dice * 2)) and ((choose_dice_y - 20 + shift_dice * 2) < mouseY < (choose_dice_y + 20 + shift_dice * 2)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 2), (choose_dice_y + shift_dice * 2))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 2), (choose_dice_y + shift_dice * 2), 3)
            zahlen.append(3)
            mode = "eingabe choose dice 4"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 3) < mouseX < (choose_dice_x + 20 + shift_dice * 3)) and ((choose_dice_y - 20 + shift_dice * 2) < mouseY < (choose_dice_y + 20 + shift_dice * 2)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 3), (choose_dice_y + shift_dice * 2))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 3), (choose_dice_y + shift_dice * 2), 4)
            zahlen.append(4)
            mode = "eingabe choose dice 4"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 4) < mouseX < (choose_dice_x + 20 + shift_dice * 4)) and ((choose_dice_y - 20 + shift_dice * 2) < mouseY < (choose_dice_y + 20 + shift_dice * 2)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 4), (choose_dice_y + shift_dice * 2))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 4), (choose_dice_y + shift_dice * 2), 5)
            zahlen.append(5)
            mode = "eingabe choose dice 4"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 5) < mouseX < (choose_dice_x + 20 + shift_dice * 5)) and ((choose_dice_y - 20 + shift_dice * 2) < mouseY < (choose_dice_y + 20 + shift_dice * 2)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 5), (choose_dice_y + shift_dice * 2))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 5), (choose_dice_y + shift_dice * 2), 6)
            zahlen.append(6)
            mode = "eingabe choose dice 4"

    # nur in diesem Modus, mit "selbst auswählen" und mind. 4 geworfenen Würfeln können diese Buttons gewählt werden
    if mode == "eingabe choose dice 4" and dices >= 4:
        if (mouseButton == LEFT) and ((choose_dice_x - 20) < mouseX < (choose_dice_x + 20)) and ((choose_dice_y - 20 + shift_dice * 3) < mouseY < (choose_dice_y + 20 + shift_dice * 3)):
            global dices
            fill(255, 0, 0)
            empty_dice(choose_dice_x, (choose_dice_y + shift_dice * 3))
            fill(0)
            dice_number(choose_dice_x, (choose_dice_y + shift_dice * 3), 1)
            zahlen.append(1)
            mode = "eingabe choose dice 5"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 1) < mouseX < (choose_dice_x + 20 + shift_dice * 1)) and ((choose_dice_y - 20 + shift_dice * 3) < mouseY < (choose_dice_y + 20 + shift_dice * 3)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 1), (choose_dice_y + shift_dice * 3))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 1), (choose_dice_y + shift_dice * 3), 2)
            zahlen.append(2)
            mode = "eingabe choose dice 5"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 2) < mouseX < (choose_dice_x + 20 + shift_dice * 2)) and ((choose_dice_y - 20 + shift_dice * 3) < mouseY < (choose_dice_y + 20 + shift_dice * 3)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 2), (choose_dice_y + shift_dice * 3))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 2), (choose_dice_y + shift_dice * 3), 3)
            zahlen.append(3)
            mode = "eingabe choose dice 5"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 3) < mouseX < (choose_dice_x + 20 + shift_dice * 3)) and ((choose_dice_y - 20 + shift_dice * 3) < mouseY < (choose_dice_y + 20 + shift_dice * 3)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 3), (choose_dice_y + shift_dice * 3))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 3), (choose_dice_y + shift_dice * 3), 4)
            zahlen.append(4)
            mode = "eingabe choose dice 5"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 4) < mouseX < (choose_dice_x + 20 + shift_dice * 4)) and ((choose_dice_y - 20 + shift_dice * 3) < mouseY < (choose_dice_y + 20 + shift_dice * 3)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 4), (choose_dice_y + shift_dice * 3))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 4), (choose_dice_y + shift_dice * 3), 5)
            zahlen.append(5)
            mode = "eingabe choose dice 5"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 5) < mouseX < (choose_dice_x + 20 + shift_dice * 5)) and ((choose_dice_y - 20 + shift_dice * 3) < mouseY < (choose_dice_y + 20 + shift_dice * 3)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 5), (choose_dice_y + shift_dice * 3))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 5), (choose_dice_y + shift_dice * 3), 6)
            zahlen.append(6)
            mode = "eingabe choose dice 5"
            
    # nur in diesem Modus, mit "selbst auswählen" und mind. 5 geworfenen Würfeln können diese Buttons gewählt werden
    if mode == "eingabe choose dice 5" and dices >= 5:
        if (mouseButton == LEFT) and ((choose_dice_x - 20) < mouseX < (choose_dice_x + 20)) and ((choose_dice_y - 20 + shift_dice * 4) < mouseY < (choose_dice_y + 20 + shift_dice * 4)):
            global dices
            fill(255, 0, 0)
            empty_dice(choose_dice_x, (choose_dice_y + shift_dice * 4))
            fill(0)
            dice_number(choose_dice_x, (choose_dice_y + shift_dice * 4), 1)
            zahlen.append(1)
            mode = "eingabe choose dice 6"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 1) < mouseX < (choose_dice_x + 20 + shift_dice * 1)) and ((choose_dice_y - 20 + shift_dice * 4) < mouseY < (choose_dice_y + 20 + shift_dice * 4)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 1), (choose_dice_y + shift_dice * 4))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 1), (choose_dice_y + shift_dice * 4), 2)
            zahlen.append(2)
            mode = "eingabe choose dice 6"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 2) < mouseX < (choose_dice_x + 20 + shift_dice * 2)) and ((choose_dice_y - 20 + shift_dice * 4) < mouseY < (choose_dice_y + 20 + shift_dice * 4)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 2), (choose_dice_y + shift_dice * 4))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 2), (choose_dice_y + shift_dice * 4), 3)
            zahlen.append(3)
            mode = "eingabe choose dice 6"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 3) < mouseX < (choose_dice_x + 20 + shift_dice * 3)) and ((choose_dice_y - 20 + shift_dice * 4) < mouseY < (choose_dice_y + 20 + shift_dice * 4)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 3), (choose_dice_y + shift_dice * 4))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 3), (choose_dice_y + shift_dice * 4), 4)
            zahlen.append(4)
            mode = "eingabe choose dice 6"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 4) < mouseX < (choose_dice_x + 20 + shift_dice * 4)) and ((choose_dice_y - 20 + shift_dice * 4) < mouseY < (choose_dice_y + 20 + shift_dice * 4)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 4), (choose_dice_y + shift_dice * 4))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 4), (choose_dice_y + shift_dice * 4), 5)
            zahlen.append(5)
            mode = "eingabe choose dice 6"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 5) < mouseX < (choose_dice_x + 20 + shift_dice * 5)) and ((choose_dice_y - 20 + shift_dice * 4) < mouseY < (choose_dice_y + 20 + shift_dice * 4)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 5), (choose_dice_y + shift_dice * 4))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 5), (choose_dice_y + shift_dice * 4), 6)
            zahlen.append(6)
            mode = "eingabe choose dice 6"
                
    # nur in diesem Modus, mit "selbst auswählen" und 6 geworfenen Würfeln können diese Buttons gewählt werden
    if mode == "eingabe choose dice 6" and dices == 6:
        if (mouseButton == LEFT) and ((choose_dice_x - 20) < mouseX < (choose_dice_x + 20)) and ((choose_dice_y - 20 + shift_dice * 5) < mouseY < (choose_dice_y + 20 + shift_dice * 5)):
            global dices
            fill(255, 0, 0)
            empty_dice(choose_dice_x, (choose_dice_y + shift_dice * 5))
            fill(0)
            dice_number(choose_dice_x, (choose_dice_y + shift_dice * 5), 1)
            zahlen.append(1)
            mode = "eingabe order"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 1) < mouseX < (choose_dice_x + 20 + shift_dice * 1)) and ((choose_dice_y - 20 + shift_dice * 5) < mouseY < (choose_dice_y + 20 + shift_dice * 5)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 1), (choose_dice_y + shift_dice * 5))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 1), (choose_dice_y + shift_dice * 5), 2)
            zahlen.append(2)
            mode = "eingabe order"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 2) < mouseX < (choose_dice_x + 20 + shift_dice * 2)) and ((choose_dice_y - 20 + shift_dice * 5) < mouseY < (choose_dice_y + 20 + shift_dice * 5)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 2), (choose_dice_y + shift_dice * 5))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 2), (choose_dice_y + shift_dice * 5), 3)
            zahlen.append(3)
            mode = "eingabe order"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 3) < mouseX < (choose_dice_x + 20 + shift_dice * 3)) and ((choose_dice_y - 20 + shift_dice * 5) < mouseY < (choose_dice_y + 20 + shift_dice * 5)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 3), (choose_dice_y + shift_dice * 5))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 3), (choose_dice_y + shift_dice * 5), 4)
            zahlen.append(4)
            mode = "eingabe order"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 4) < mouseX < (choose_dice_x + 20 + shift_dice * 4)) and ((choose_dice_y - 20 + shift_dice * 5) < mouseY < (choose_dice_y + 20 + shift_dice * 5)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 4), (choose_dice_y + shift_dice * 5))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 4), (choose_dice_y + shift_dice * 5), 5)
            zahlen.append(5)
            mode = "eingabe order"
            
        elif (mouseButton == LEFT) and ((choose_dice_x - 20 + shift_dice * 5) < mouseX < (choose_dice_x + 20 + shift_dice * 5)) and ((choose_dice_y - 20 + shift_dice * 5) < mouseY < (choose_dice_y + 20 + shift_dice * 5)):
            fill(255, 0, 0)
            empty_dice((choose_dice_x + shift_dice * 5), (choose_dice_y + shift_dice * 5))
            fill(0)
            dice_number((choose_dice_x + shift_dice * 5), (choose_dice_y + shift_dice * 5), 6)
            zahlen.append(6)
            mode = "eingabe order"
    
    # Falls die Anzahl Würfel < 6 ist, so müssen die Modi noch auf den richtigen Modus gestellt werden.       
    if mode == "eingabe choose dice 2" and dices == 1:
        mode = "eingabe order"
        
    if mode == "eingabe choose dice 3" and dices == 2:
        mode = "eingabe order"
        
    if mode == "eingabe choose dice 4" and dices == 3:
        mode = "eingabe order"
        
    if mode == "eingabe choose dice 5" and dices == 4:
        mode = "eingabe order"
        
    if mode == "eingabe choose dice 6" and dices == 5:
        mode = "eingabe order"
    
# Vierte Eingabe Mit oder ohne Reihenfolge------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    textAlign(CENTER, CENTER)
    text("mit Reihenfolge", 120, 500)
    text("ohne Reihenfolge", 300, 500)
    
    if mode == "eingabe order": # nur in diesem Modus kann Reihenfolge gewählt werden
        if (mouseButton == LEFT) and (30 < mouseX < 210) and (480 < mouseY < 520):
            global throw_type
            fill(255, 0, 0)
            rect(120, 500, 180, 40)
            fill(0, 0, 0)
            text("mit Reihenfolge", 120, 500) #damit nach dem drücken des Buttons immernoch "mit Reihenfolge" steht
            order_type = 1
            mode = "show result"
            
        elif (mouseButton == LEFT) and (210 < mouseX < 390) and (480 < mouseY < 520):
            fill(255, 0, 0)
            rect(300, 500, 180, 40)
            fill(0, 0, 0)
            text("ohne Reihenfolge", 300, 500)
            order_type = 2
            mode = "show result"
            
# Ausgabe Ergebnisse mit Reihenfolge------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    
    if mode == "show result" and order_type == 1:
        for i in range(0, dices):
            fill(0)
            textAlign(LEFT, CENTER)
            text("1/6", 20 + i * 45, 555)
            if i > 0:
                circle(12 + i * 45, 560, 5)
        text("Die Wahrscheinlichkeit ist...\n= 1/" + str(6 ** dices), 20, 610)


# Ausgabe Ergebnisse ohne Reihenfolge------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                
    #sortieren der gewürfelten Zahlen in der Liste, damit man sie mit den Möglichkeiten abgleichen kann  
    zahlen.sort()
    
    #print(zahlen) #test
    
    
    #alle Kombinationsmöglichkeiten (G = Gleich, V = Verschieden)
    einG = [[1], [2], [3], [4], [5], [6]]

    zweiG = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]
    zweiV = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 3], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6], [4, 5], [4, 6], [5, 6]]
    
    dreiG = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6]]
    zweiGeinV = [[1, 1, 2], [1, 1, 3], [1, 1, 4], [1, 1, 5], [1, 1, 6], [1, 2, 2], [2, 2, 3], [2, 2, 4], [2, 2, 5], [2, 2, 6], [1, 3, 3], [2, 3, 3], [3, 3, 4], [3, 3, 5], [3, 3, 6], [1, 4, 4], [2, 4, 4], [3, 4, 4], [4, 4, 5], [4, 4, 6], [1, 5, 5], [2, 5, 5], [3, 5, 5], [4, 5, 5], [5, 5, 6], [1, 6, 6], [2, 6, 6], [3, 6, 6], [4, 6, 6], [5, 6, 6]]
    dreiV = [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6], [1, 3, 4], [1, 3, 5], [1, 3, 6], [1, 4, 5], [1, 4, 6], [1, 5, 6], [2, 3, 4], [2, 3, 5], [2, 3, 6], [2, 4, 5], [2, 4, 6], [2, 5, 6], [3, 4, 5], [3, 4, 6], [3, 5, 6], [4, 5, 6]]

    vierG = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6]]
    dreiGeinV = [[1, 1, 1, 2], [1, 1, 1, 3], [1, 1, 1, 4], [1, 1, 1, 5], [1, 1, 1, 6], [1, 2, 2, 2], [2, 2, 2, 3], [2, 2, 2, 4], [2, 2, 2, 5], [2, 2, 2, 6], [1, 3, 3, 3], [2, 3, 3, 3], [3, 3, 3, 4], [3, 3, 3, 5], [3, 3, 3, 6], [1, 4, 4, 4], [2, 4, 4, 4], [3, 4, 4, 4], [4, 4, 4, 5], [4, 4, 4, 6], [1, 5, 5, 5], [2, 5, 5, 5], [3, 5, 5, 5], [4, 5, 5, 5], [5, 5, 5, 6], [1, 6, 6, 6], [2, 6, 6, 6], [3, 6, 6, 6], [4, 6, 6, 6], [5, 6, 6, 6]]
    zweiGzweiG = [[1, 1, 2, 2], [1, 1, 3, 3], [ 1, 1, 4, 4], [1, 1, 5, 5], [1, 1, 6, 6], [2, 2, 3, 3], [2, 2, 4, 4], [2, 2, 5, 5], [2, 2, 6, 6], [3, 3, 4, 4], [3, 3, 5, 5], [3, 3, 6, 6], [4, 4, 5, 5], [4, 4, 6, 6], [5, 5, 6, 6]]
    zweiGzweiV = [[1, 1, 2, 3], [1, 1, 2, 4], [1, 1, 2, 5], [1, 1, 2, 6], [1, 1, 3, 4], [1, 1, 3, 5], [1, 1, 3, 6], [1, 1, 4, 5], [1, 1, 4, 6], [1, 1, 5, 6], [1, 2, 2, 3], [1, 2, 2, 4], [1, 2, 2, 5], [1, 2, 2, 6], [2, 2, 3, 4], [2, 2, 3, 5], [2, 2, 3, 6], [2, 2, 4, 5], [2, 2, 4, 6], [2, 2, 5, 6], [1, 2, 3, 3], [1, 3, 3, 4], [1, 3, 3, 5], [1, 3, 3, 6], [2, 3, 3, 4], [2, 3, 3, 5], [2, 3, 3, 6], [3, 3, 4, 5], [3, 3, 4, 6], [3, 3, 5, 6], [1, 2, 4, 4], [1, 3, 4, 4], [1, 4, 4, 5], [1, 4, 4, 6], [2, 3, 4, 4], [2, 4, 4, 5], [2, 4, 4, 6], [3, 4, 4, 5], [3, 4, 4, 6], [4, 4, 5, 6], [1, 2, 5, 5], [1, 3, 5, 5], [1, 4, 5, 5], [1, 5, 5, 6], [2, 3, 5, 5], [2, 4, 5, 5], [2, 5, 5, 6], [3, 4, 5, 5], [3, 5, 5, 6], [4, 5, 5, 6], [1, 2, 6, 6], [1, 3, 6, 6], [1, 4, 6, 6], [1, 5, 6, 6], [2, 3, 6, 6], [2, 4, 6, 6], [2, 5, 6, 6], [3, 4, 6, 6], [3, 5, 6, 6]]
    vierV = [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6], [1, 2, 4, 5], [1, 2, 4, 6], [1, 2, 5, 6], [1, 3, 4, 5], [1, 3, 4, 6], [1, 3, 5, 6], [1, 4, 5, 6], [2, 3, 4, 5], [2, 3, 4, 6], [2, 3, 5, 6], [2, 4, 5, 6], [3, 4, 5, 6]]

    fuenfG = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5], [6, 6, 6, 6, 6]]
    vierGeinV = [[1, 1, 1, 1, 2], [1, 1, 1, 1, 3], [1, 1, 1, 1, 4], [1, 1, 1, 1, 5], [1, 1, 1, 1, 6], [1, 2, 2, 2, 2], [2, 2, 2, 2, 3], [2, 2, 2, 2, 4], [2, 2, 2, 2, 5], [2, 2, 2, 2, 6], [1, 3, 3, 3, 3], [2, 3, 3, 3, 3], [3, 3, 3, 3, 4], [3, 3, 3, 3, 5], [3, 3, 3, 3, 6], [1, 4, 4, 4, 4], [2, 4, 4, 4, 4], [3, 4, 4, 4, 4], [4, 4, 4, 4, 5], [4, 4, 4, 4, 6], [1, 5, 5, 5, 5], [2, 5, 5, 5, 5], [3, 5, 5, 5, 5], [4, 5, 5, 5, 5], [5, 5, 5, 5, 6], [1, 6, 6, 6, 6], [2, 6, 6, 6, 6], [3, 6, 6, 6, 6], [4, 6, 6, 6, 6], [5, 6, 6, 6, 6]]
    dreiGzweiG = [[1, 1, 1, 2, 2], [1, 1, 1, 3, 3], [1, 1, 1, 4, 4], [1, 1, 1, 5, 5], [1, 1, 1, 6, 6], [1, 1, 2, 2, 2], [2, 2, 2, 3, 3], [2, 2, 2, 4, 4], [2, 2, 2, 5, 5], [2, 2, 2, 6, 6], [1, 1, 3, 3, 3], [2, 2, 3, 3, 3], [3, 3, 3, 4, 4], [3, 3, 3, 5, 5], [3, 3, 3, 6, 6], [1, 1, 4, 4, 4], [2, 2, 4, 4, 4], [3, 3, 4, 4, 4], [4, 4, 4, 5, 5], [4, 4, 4, 6, 6], [1, 1, 5, 5, 5], [2, 2, 5, 5, 5], [3, 3, 5, 5, 5], [4, 4, 5, 5, 5], [5, 5, 5, 6, 6], [1, 1, 6, 6, 6], [2, 2, 6, 6, 6], [3, 3, 6, 6, 6], [4, 4, 6, 6, 6], [5, 5, 6, 6, 6]]
    dreiGzweiv = [[1, 1, 1, 2, 3], [1, 1, 1, 2, 4], [1, 1, 1, 2, 5], [1, 1, 1, 2, 6], [1, 1, 1, 3, 4], [1, 1, 1, 3, 5], [1, 1, 1, 3, 6], [1, 1, 1, 4, 5], [1, 1, 1, 4, 6], [1, 1, 1, 5, 6], [1, 2, 2, 2, 3], [1, 2, 2, 2, 4], [1, 2, 2, 2, 5], [1, 2, 2, 2, 6], [2, 2, 2, 3, 4], [2, 2, 2, 3, 5], [2, 2, 2, 3, 6], [2, 2, 2, 4, 5], [2, 2, 2, 4, 6], [2, 2, 2, 5, 6], [1, 2, 3, 3, 3], [1, 3, 3, 3, 4], [1, 3, 3, 3, 5], [1, 3, 3, 3, 6], [2, 3, 3, 3, 4], [2, 3, 3, 3, 5], [2, 3, 3, 3, 6], [3, 3, 3, 4, 5], [3, 3, 3, 4, 6], [3, 3, 3, 5, 6], [1, 2, 4, 4, 4], [1, 3, 4, 4, 4], [1, 4, 4, 4, 5], [1, 4, 4, 4, 6], [2, 3, 4, 4, 4], [2, 4, 4, 4, 5], [2, 4, 4, 4, 6], [3, 4, 4, 4, 5], [3, 4, 4, 4, 6], [4, 4, 4, 5, 6], [1, 2, 5, 5, 5], [1, 3, 5, 5, 5], [1, 4, 5, 5, 5], [1, 5, 5, 5, 6], [2, 3, 5, 5, 5], [2, 4, 5, 5, 5], [2, 5, 5, 5, 6], [3, 4, 5, 5, 5], [3, 5, 5, 5, 6], [4, 5, 5, 5, 6], [1, 2, 6, 6, 6], [1, 3, 6, 6, 6], [1, 4, 6, 6, 6], [1, 5, 6, 6, 6], [2, 3, 6, 6, 6], [2, 4, 6, 6, 6], [2, 5, 6, 6, 6], [3, 4, 6, 6, 6], [3, 5, 6, 6, 6], [4, 5, 6, 6, 6]]
    zweiGzweiGeinV = [[1, 1, 2, 2, 3], [1, 1, 2, 2, 4], [1, 1, 2, 2, 5], [1, 1, 2, 2, 6], [1, 1, 2, 3, 3], [1, 1, 3, 3, 4], [1, 1, 3, 3, 5], [1, 1, 3, 3, 6], [1, 1, 2, 4, 4], [1, 1, 3, 4, 4], [1, 1, 4, 4, 5], [1, 1, 4, 4, 6], [1, 1, 2, 5, 5], [1, 1, 3, 5, 5], [1, 1, 4, 5, 5], [1, 1, 5, 5, 6], [1, 1, 2, 6, 6], [1, 1, 3, 6, 6], [1, 1, 4, 6, 6], [1, 1, 5, 6, 6], [1, 2, 2, 3, 3], [2, 2, 3, 3, 4], [2, 2, 3, 3, 5], [2, 2, 3, 3, 6], [1, 2, 2, 4, 4], [2, 2, 3, 4, 4], [2, 2, 4, 4, 5], [2, 2, 4, 4, 6], [1, 2, 2, 5, 5], [2, 2, 3, 5, 5], [2, 2, 4, 5, 5], [2, 2, 5, 5, 6], [1, 2, 2, 6, 6], [2, 2, 3, 6, 6], [2, 2, 4, 6, 6], [2, 2, 5, 6, 6], [1, 3, 3, 4, 4], [2, 3, 3, 4, 4], [3, 3, 4, 4, 5], [3, 3, 4, 4, 6], [1, 3, 3, 5, 5], [2, 3, 3, 5, 5], [3, 3, 4, 5, 5], [3, 3, 5, 5, 6], [1, 3, 3, 6, 6], [2, 3, 3, 6, 6], [3, 3, 4, 6, 6], [3, 3, 5, 6, 6], [1, 4, 4, 5, 5], [2, 4, 4, 5, 5], [3, 4, 4, 5, 5], [4, 4, 5, 5, 6], [1, 4, 4, 6, 6], [2, 4, 4, 6, 6], [3, 4, 4, 6, 6], [4, 4, 5, 6, 6], [1, 5, 5, 6, 6], [2, 5, 5, 6, 6], [3, 5, 5, 6, 6], [4, 5, 5, 6, 6]]
    zweiGdreiV = [[1, 1, 2, 3, 4], [1, 1, 2, 3, 5], [1, 1, 2, 3, 6], [1, 1, 2, 4, 5], [1, 1, 2, 4, 6], [1, 1, 2, 5, 6], [1, 1, 3, 4, 5], [1, 1, 3, 4, 6], [1, 1, 3, 5, 6], [1, 1, 4, 5, 6], [1, 2, 2, 3, 4], [1, 2, 2, 3, 5], [1, 2, 2, 3, 6], [1, 2, 2, 4, 5], [1, 2, 2, 4, 6], [1, 2, 2, 5, 6], [2, 2, 3, 4, 5], [2, 2, 3, 4, 6], [2, 2, 3, 5, 6], [2, 2, 4, 5, 6], [1, 2, 3, 3, 4], [1, 2, 3, 3, 5], [1, 2, 3, 3, 6], [1, 3, 3, 4, 5], [1, 3, 3, 4, 6], [1, 3, 3, 5, 6], [2, 3, 3, 4, 5], [2, 3, 3, 4, 6], [2, 3, 3, 5, 6], [3, 3, 4, 5, 6], [1, 2, 3, 4, 4], [1, 2, 4, 4, 5], [1, 2, 4, 4, 6], [1, 3, 4, 4, 5], [1, 3, 4, 4, 6], [1, 4, 4, 5, 6], [2, 3, 4, 4, 5], [2, 3, 4, 4, 6], [2, 4, 4, 5, 6], [3, 4, 4, 5, 6], [1, 2, 3, 5, 5], [1, 2, 4, 5, 5], [1, 2, 5, 5, 6], [1, 3, 4, 5, 5], [1, 3, 5, 5, 6], [1, 4, 5, 5, 6], [2, 3, 4, 5, 5], [2, 3, 5, 5, 6], [2, 4, 5, 5, 6], [3, 4, 5, 5, 6], [1, 2, 3, 6, 6], [1, 2, 4, 6, 6], [1, 2, 5, 6, 6], [1, 3, 4, 6, 6], [1, 3, 5, 6, 6], [1, 4, 5, 6, 6], [2, 3, 4, 6, 6], [2, 3, 5, 6, 6], [2, 4, 5, 6, 6], [3, 4, 5, 6, 6]]
    fuenfV = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 6], [1, 2, 3, 5, 6], [1, 2, 4, 5, 6], [1, 3, 4, 5, 6], [2, 3, 4, 5, 6]]
    
    sechsG = [[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4], [5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6]]
    fuenfGeinV = [[1, 1, 1, 1, 1, 2], [1, 1, 1, 1, 1, 3], [1, 1, 1, 1, 1, 4], [1, 1, 1, 1, 1, 5], [1, 1, 1, 1, 1, 6], [1, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 3], [2, 2, 2, 2, 2, 4], [2, 2, 2, 2, 2, 5], [2, 2, 2, 2, 2, 6], [1, 3, 3, 3, 3, 3], [2, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 4], [3, 3, 3, 3, 3, 5], [3, 3, 3, 3, 3, 6], [1, 4, 4, 4, 4, 4], [2, 4, 4, 4, 4, 4], [3, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 5], [4, 4, 4, 4, 4, 6], [1, 5, 5, 5, 5, 5], [2, 5, 5, 5, 5, 5], [3, 5, 5, 5, 5, 5], [4, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 6], [1, 6, 6, 6, 6, 6], [2, 6, 6, 6, 6, 6], [3, 6, 6, 6, 6, 6], [4, 6, 6, 6, 6, 6], [5, 6, 6, 6, 6, 6]]
    vierGzweiV = [[1, 1, 1, 1, 2, 3], [1, 1, 1, 1, 2, 4], [1, 1, 1, 1, 2, 5], [1, 1, 1, 1, 2, 6], [1, 1, 1, 1, 3, 4], [1, 1, 1, 1, 3, 5], [1, 1, 1, 1, 3, 6], [1, 1, 1, 1, 4, 5], [1, 1, 1, 1, 4, 6], [1, 1, 1, 1, 5, 6], [1, 2, 2, 2, 2, 3], [1, 2, 2, 2, 2, 4], [1, 2, 2, 2, 2, 5], [1, 2, 2, 2, 2, 6], [2, 2, 2, 2, 3, 4], [2, 2, 2, 2, 3, 5], [2, 2, 2, 2, 3, 6], [2, 2, 2, 2, 4, 5], [2, 2, 2, 2, 4, 6], [2, 2, 2, 2, 5, 6], [1, 2, 3, 3, 3, 3], [1, 3, 3, 3, 3, 4], [1, 3, 3, 3, 3, 5], [1, 3, 3, 3, 3, 6], [2, 3, 3, 3, 3, 4], [2, 3, 3, 3, 3, 5], [2, 3, 3, 3, 3, 6], [3, 3, 3, 3, 4, 5], [3, 3, 3, 3, 4, 6], [3, 3, 3, 3, 5, 6], [1, 2, 4, 4, 4, 4], [1, 3, 4, 4, 4, 4], [1, 4, 4, 4, 4, 5], [1, 4, 4, 4, 4, 6], [2, 3, 4, 4, 4, 4], [2, 4, 4, 4, 4, 5], [2, 4, 4, 4, 4, 6], [3, 4, 4, 4, 4, 5], [3, 4, 4, 4, 4, 6], [4, 4, 4, 4, 5, 6], [1, 2, 5, 5, 5, 5], [1, 3, 5, 5, 5, 5], [1, 4, 5, 5, 5, 5], [1, 5, 5, 5, 5, 6], [2, 3, 5, 5, 5, 5], [2, 4, 5, 5, 5, 5], [2, 5, 5, 5, 5, 6], [3, 4, 5, 5, 5, 5], [3, 5, 5, 5, 5, 6], [4, 5, 5, 5, 5, 6], [1, 2, 6, 6, 6, 6], [1, 3, 6, 6, 6, 6], [1, 4, 6, 6, 6, 6], [1, 5, 6, 6, 6, 6], [2, 3, 6, 6, 6, 6], [2, 4, 6, 6, 6, 6], [2, 5, 6, 6, 6, 6], [3, 4, 6, 6, 6, 6], [3, 5, 6, 6, 6, 6], [4, 5, 6, 6, 6, 6]]
    vierGzweiG = [[1, 1, 1, 1, 2, 2], [1, 1, 1, 1, 3, 3], [1, 1, 1, 1, 4, 4], [1, 1, 1, 1, 5, 5], [1, 1, 1, 1, 6, 6], [1, 1, 2, 2, 2, 2], [2, 2, 2, 2, 3, 3], [2, 2, 2, 2, 4, 4], [2, 2, 2, 2, 5, 5], [2, 2, 2, 2, 6, 6], [1, 1, 3, 3, 3, 3], [2, 2, 3, 3, 3, 3], [3, 3, 3, 3, 4, 4], [3, 3, 3, 3, 5, 5], [3, 3, 3, 3, 6, 6], [1, 1, 4, 4, 4, 4], [2, 2, 4, 4, 4, 4], [3, 3, 4, 4, 4, 4], [4, 4, 4, 4, 5, 5], [4, 4, 4, 4, 6, 6], [1, 1, 5, 5, 5, 5], [2, 2, 5, 5, 5, 5], [3, 3, 5, 5, 5, 5], [4, 4, 5, 5, 5, 5], [5, 5, 5, 5, 6, 6], [1, 1, 6, 6, 6, 6], [2, 2, 6, 6, 6, 6], [3, 3, 6, 6, 6, 6], [4, 4, 6, 6, 6, 6], [5, 5, 6, 6, 6, 6]]
    dreiGdreiV = [[1, 1, 1, 2, 3, 4], [1, 1, 1, 2, 3, 5], [1, 1, 1, 2, 3, 6], [1, 1, 1, 2, 4, 5], [1, 1, 1, 2, 4, 6], [1, 1, 1, 2, 5, 6], [1, 1, 1, 3, 4, 5], [1, 1, 1, 3, 4, 6], [1, 1, 1, 3, 5, 6], [1, 1, 1, 4, 5, 6], [1, 2, 2, 2, 3, 4], [1, 2, 2, 2, 3, 5], [1, 2, 2, 2, 3, 6], [1, 2, 2, 2, 4, 5], [1, 2, 2, 2, 4, 6], [1, 2, 2, 2, 5, 6], [2, 2, 2, 3, 4, 5], [2, 2, 2, 3, 4, 6], [2, 2, 2, 3, 5, 6], [2, 2, 2, 4, 5, 6], [1, 2, 3, 3, 3, 4], [1, 2, 3, 3, 3, 5], [1, 2, 3, 3, 3, 6], [1, 3, 3, 3, 4, 5], [1, 3, 3, 3, 4, 6], [1, 3, 3, 3, 5, 6], [2, 3, 3, 3, 4, 5], [2, 3, 3, 3, 4, 6], [2, 3, 3, 3, 5, 6], [3, 3, 3, 4, 5, 6], [1, 2, 3, 4, 4, 4], [1, 2, 4, 4, 4, 5], [1, 2, 4, 4, 4, 6], [1, 3, 4, 4, 4, 5], [1, 3, 4, 4, 4, 6], [1, 4, 4, 4, 5, 6], [2, 3, 4, 4, 4, 5], [2, 3, 4, 4, 4, 6], [2, 4, 4, 4, 5, 6], [3, 4, 4, 4, 5, 6], [1, 2, 3, 5, 5, 5], [1, 2, 4, 5, 5, 5], [1, 2, 5, 5, 5, 6], [1, 3, 4, 5, 5, 5], [1, 3, 5, 5, 5, 6], [1, 4, 5, 5, 5, 6], [2, 3, 4, 5, 5, 5], [2, 3, 5, 5, 5, 6], [2, 4, 5, 5, 5, 6], [3, 4, 5, 5, 5, 6], [1, 2, 3, 6, 6, 6], [1, 2, 4, 6, 6, 6], [1, 2, 5, 6, 6, 6], [1, 3, 4, 6, 6, 6], [1, 3, 5, 6, 6, 6], [1, 4, 5, 6, 6, 6], [2, 3, 4, 6, 6, 6], [2, 3, 5, 6, 6, 6], [2, 4, 5, 6, 6, 6], [3, 4, 5, 6, 6, 6]]
    dreiGdreiG = [[1, 1, 1, 2, 2, 2], [1, 1, 1, 3, 3, 3], [1, 1, 1, 4, 4, 4], [1, 1, 1, 5, 5, 5], [1, 1, 1, 6, 6, 6], [2, 2, 2, 3, 3, 3], [2, 2, 2, 4, 4, 4], [2, 2, 2, 5, 5, 5], [2, 2, 2, 6, 6, 6], [3, 3, 3, 4, 4, 4], [3, 3, 3, 5, 5, 5], [3, 3, 3, 6, 6, 6], [4, 4, 4, 5, 5, 5], [4, 4, 4, 6, 6, 6], [5, 5, 5, 6, 6, 6]]
    zweiGvierV = [[1, 1, 2, 3, 4, 5], [1, 1, 2, 3, 4, 6], [1, 1, 2, 3, 5, 6], [1, 1, 2, 4, 5, 6], [1, 1, 3, 4, 5, 6], [1, 2, 2, 3, 4, 5], [1, 2, 2, 3, 4, 6], [1, 2, 2, 3, 5, 6], [1, 2, 2, 4, 5, 6], [2, 2, 3, 4, 5, 6], [1, 2, 3, 3, 4, 5], [1, 2, 3, 3, 4, 6], [1, 2, 3, 3, 5, 6], [1, 3, 3, 4, 5, 6], [2, 3, 3, 4, 5, 6], [1, 2, 3, 4, 4, 5], [1, 2, 3, 4, 4, 6], [1, 2, 4, 4, 5, 6], [1, 3, 4, 4, 5, 6], [2, 3, 4, 4, 5, 6], [1, 2, 3, 4, 5, 5], [1, 2, 3, 5, 5, 6], [1, 2, 4, 5, 5, 6], [1, 3, 4, 5, 5, 6], [2, 3, 4, 5, 5, 6], [1, 2, 3, 4, 6, 6], [1, 2, 3, 5, 6, 6], [1, 2, 4, 5, 6, 6], [1, 3, 4, 5, 6, 6], [2, 3, 4, 5, 6, 6]]
    zweiGzweiGzweiV = [[1, 1, 2, 2, 3, 4], [1, 1, 2, 2, 3, 5], [1, 1, 2, 2, 3, 6], [1, 1, 2, 2, 4, 5], [1, 1, 2, 2, 4, 6], [1, 1, 2, 2, 5, 6], [1, 1, 2, 3, 3, 4], [1, 1, 2, 3, 3, 5], [1, 1, 2, 3, 3, 6], [1, 1, 3, 3, 4, 5], [1, 1, 3, 3, 4, 6], [1, 1, 3, 3, 5, 6], [1, 1, 2, 3, 4, 4], [1, 1, 2, 4, 4, 5], [1, 1, 2, 4, 4, 6], [1, 1, 3, 4, 4, 5], [1, 1, 3, 4, 4, 6], [1, 1, 4, 4, 5, 6], [1, 1, 2, 3, 5, 5], [1, 1, 2, 4, 5, 5], [1, 1, 2, 5, 5, 6], [1, 1, 3, 4, 5, 5], [1, 1, 3, 5, 5, 6], [1, 1, 4, 5, 5, 6], [1, 1, 2, 3, 6, 6], [1, 1, 2, 4, 6, 6], [1, 1, 2, 5, 6, 6], [1, 1, 3, 4, 6, 6], [1, 1, 3, 5, 6, 6], [1, 1, 4, 5, 6, 6], [1, 2, 2, 3, 3, 4], [1, 2, 2, 3, 3, 5], [1, 2, 2, 3, 3, 6], [2, 2, 3, 3, 4, 5], [2, 2, 3, 3, 4, 6], [2, 2, 3, 3, 5, 6], [1, 2, 2, 3, 4, 4], [1, 2, 2, 4, 4, 5], [1, 2, 2, 4, 4, 6], [2, 2, 3, 4, 4, 5], [2, 2, 3, 4, 4, 6], [2, 2, 4, 4, 5, 6], [1, 2, 2, 3, 5, 5], [1, 2, 2, 4, 5, 5], [1, 2, 2, 5, 5, 6], [2, 2, 3, 4, 5, 5], [2, 2, 3, 5, 5, 6], [2, 2, 4, 5, 5, 6], [1, 2, 2, 3, 6, 6], [1, 2, 2, 4, 6, 6], [1, 2, 2, 5, 6, 6], [2, 2, 3, 4, 6, 6], [2, 2, 3, 5, 6, 6], [2, 2, 4, 5, 6, 6], [1, 2, 3, 3, 4, 4], [1, 3, 3, 4, 4, 5], [1, 3, 3, 4, 4, 6], [2, 3, 3, 4, 4, 5], [2, 3, 3, 4, 4, 6], [3, 3, 4, 4, 5, 6], [1, 2, 3, 3, 5, 5], [1, 3, 3, 4, 5, 5], [1, 3, 3, 5, 5, 6], [2, 3, 3, 4, 5, 5], [2, 3, 3, 5, 5, 6], [3, 3, 4, 5, 5, 6], [1, 2, 3, 3, 6, 6], [1, 3, 3, 4, 6, 6], [1, 3, 3, 5, 6, 6], [2, 3, 3, 4, 6, 6], [2, 3, 3, 5, 6, 6], [3, 3, 4, 5, 6, 6], [1, 2, 4, 4, 5, 5], [1, 3, 4, 4, 5, 5], [1, 4, 4, 5, 5, 6], [2, 3, 4, 4, 5, 5], [2, 4, 4, 5, 5, 6], [3, 4, 4, 5, 5, 6], [1, 2, 4, 4, 6, 6], [1, 3, 4, 4, 6, 6], [1, 4, 4, 5, 6, 6], [2, 3, 4, 4, 6, 6], [2, 4, 4, 5, 6, 6], [3, 4, 4, 5, 6, 6], [1, 2, 5, 5, 6, 6], [1, 3, 5, 5, 6, 6], [1, 4, 5, 5, 6, 6], [2, 3, 5, 5, 6, 6], [2, 4, 5, 5, 6, 6], [3, 4, 5, 5, 6, 6]]
    zweiGzweiGzweiG = [[1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 4, 4], [1, 1, 2, 2, 5, 5], [1, 1, 2, 2, 6, 6], [1, 1, 3, 3, 4, 4], [1, 1, 3, 3, 5, 5], [1, 1, 3, 3, 6, 6], [1, 1, 4, 4, 5, 5], [1, 1, 4, 4, 6, 6], [1, 1, 5, 5, 6, 6], [2, 2, 3, 3, 4, 4], [2, 2, 3, 3, 5, 5], [2, 2, 3, 3, 6, 6], [2, 2, 4, 4, 5, 5], [2, 2, 4, 4, 6, 6], [2, 2, 5, 5, 6, 6], [3, 3, 4, 4, 5, 5], [3, 3, 4, 4, 6, 6], [3, 3, 5, 5, 6, 6], [4, 4, 5, 5, 6, 6]]
    sechsV = [[1, 2, 3, 4, 5, 6]]




    if zahlen in einG:
        q = 1
         
    elif zahlen in zweiG:
        q = 1
    elif zahlen in zweiV:
        q = 2
         
    elif zahlen in dreiG:
        q = 1
    elif zahlen in zweiGeinV:
        q = 3
    elif zahlen in dreiV:
        q = 6
            
    elif zahlen in vierG:
        q = 1
    elif zahlen in dreiGeinV:
        q = 4
    elif zahlen in zweiGzweiG:
        q = 6
    elif zahlen in zweiGzweiV:
        q = 12
    elif zahlen in vierV:
        q = 24
        
    elif zahlen in fuenfG:
        q = 1
    elif zahlen in vierGeinV:
        q = 5
    elif zahlen in dreiGzweiG:
        q = 10
    elif zahlen in dreiGzweiv:
        q = 20
    elif zahlen in zweiGzweiGeinV:
        q = 30
    elif zahlen in zweiGdreiV:
        q = 60
    elif zahlen in fuenfV:
        q = 120
        
    elif zahlen in sechsG:
        q = 1
    elif zahlen in fuenfGeinV:
        q = 6
    elif zahlen in vierGzweiV:
        q = 30
    elif zahlen in vierGzweiG:
        q = 15
    elif zahlen in dreiGdreiV:
        q = 120
    elif zahlen in dreiGdreiG:
        q = 20
    elif zahlen in zweiGvierV:
        q = 360
    elif zahlen in zweiGzweiGzweiV:
        q = 180
    elif zahlen in zweiGzweiGzweiG:
        q = 90
    elif zahlen in sechsV:
        q = 720
    else:
        q = 60
    
    
    if mode == "show result" and order_type == 2:
        for i in range(0, dices):
            fill(0)
            textAlign(LEFT, CENTER)
            text(u"Anzahl Anordnungsmöglichkeiten = " + str(q), 20, 545)
            text("1/6", 20 + i * 45, 575)
            if i > 0:
                circle(12 + i * 45, 580, 5)
            circle(12 + dices * 45, 580, 5)
            text(q, 20 + dices * 45, 575)    
            text("Die Wahrscheinlichkeit ist...\n= " + str(q) + "/" + str(6 ** dices) + " = 1/" + str(6 ** dices / q), 20, 625)
