
mode = "eingabe dices"
dices = 0 # Wie viele Würfel werden geworfen?
throw_type = 0 # Zufallswurf oder erwartetes Ergebnis?

def setup():
    size(800, 900)
    background(255)
    textSize(20)
    fill(0)
    stroke(0)

    # erste Frage
    textAlign(LEFT, CENTER)
    text("Wie viele Wuerfel wirfst du?", 20, 20)
    
    # Buttons ohne Inhalt
    for i in range(0, 6):
        noFill()
        empty_dice(50 + i * 40, 60)
        
    # zweite Frage
    textAlign(LEFT, CENTER)
    text("Zufaelliges Wuerfeln oder erwartetes Ergebnis?", 20, 100)
    
    # Buttons ohne Inhalt
    rect(120, 140, 180, 40)
    rect(300, 140, 180, 40)
    
    
def draw():
    for i in range(0, 6):
        textAlign(CENTER, CENTER)
        fill(0)
        text(1 + i, 50 + i * 40, 60)
    
    if mode == "eingabe dices":
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
    
    print(dices) # zur Kontrolle
    
    textAlign(CENTER, CENTER)
    text("Zufall", 120, 140)
    text("erwartetes Ergebnis", 300, 140)
    
    if (mouseButton == LEFT) and (30 < mouseX < 210) and (120 < mouseY < 160):
        global throw_type
        fill(255, 0, 0)
        rect(120, 140, 180, 40)
        throw_type = 1
        
    elif (mouseButton == LEFT) and (210 < mouseX < 390) and (120 < mouseY < 160):
        fill(255, 0, 0)
        rect(300, 140, 180, 40)
        throw_type = 2
        
    else:
        noFill()
    
    print(throw_type) # zur Kontrolle
    
    if throw_type == 2:
        for i in range(0, dices):
            fill(0)
            textAlign(LEFT, CENTER)
            text("Wuerfel " + str(i + 1), 20, 180 + i * 50)
            fill(255)
            for j in range(0, 6):
                empty_dice(130 + j * 50, 190 + i * 50)

        for k in range(0, 6):
            for l in range(0, dices):
                dice_number(130 + (k * 50), 190 + l * 50, k + 1)
                
    elif throw_type == 1:
        for i in range(0, dices):
            fill(0)
            textAlign(LEFT, CENTER)
            text("Zufall", 20, 180)
            fill(255)
            empty_dice(130 + i * 50, 190)
            dice_number(130 + i * 50, 190, round(random(1, 6)))
            noLoop()
            
    else:
        noFill()

def empty_dice(xPos, yPos):
    rectMode(CENTER)
    square(xPos, yPos, 40)
    
def dice_number(xPos, yPos, number):
    fill(0)
    if number == 1:
        circle(xPos, yPos, 5)
    if number == 2:
        circle(xPos - 10, yPos - 10, 5)
        circle(xPos + 10, yPos + 10, 5)
    if number == 3:
        circle(xPos, yPos, 5)
        circle(xPos - 10, yPos - 10, 5)
        circle(xPos + 10, yPos + 10, 5)
    if number == 4:
        circle(xPos - 10, yPos - 10, 5)
        circle(xPos + 10, yPos - 10, 5)
        circle(xPos - 10, yPos + 10, 5)
        circle(xPos + 10, yPos + 10, 5)
    if number == 5:
        circle(xPos - 10, yPos - 10, 5)
        circle(xPos + 10, yPos - 10, 5)
        circle(xPos, yPos, 5)
        circle(xPos - 10, yPos + 10, 5)
        circle(xPos + 10, yPos + 10, 5)
    if number == 6:
        circle(xPos - 10, yPos - 10, 5)
        circle(xPos + 10, yPos - 10, 5)
        circle(xPos - 10, yPos, 5)
        circle(xPos + 10, yPos, 5)
        circle(xPos - 10, yPos + 10, 5)
        circle(xPos + 10, yPos + 10, 5)
        
