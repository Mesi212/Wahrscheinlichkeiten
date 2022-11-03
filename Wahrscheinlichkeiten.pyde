# Zufalls-Nummer für Würfel
# random_number = round(random(1, 6))
number = 0 # Punktzahl auf Würfel
button1 = 0 # Wie viele Würfel werden geworfen?
button2 = 0 # Zufallswurf oder erwartetes Ergebnis?

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
    
    if (mouseButton == LEFT) and (30 < mouseX < 70) and (40 < mouseY < 80):
        global button1
        fill(255, 0, 0)
        empty_dice(50, 60)
        button1 = 1
        
    elif (mouseButton == LEFT) and (70 < mouseX < 110) and (40 < mouseY < 80):
        fill(255, 0, 0)
        empty_dice(90, 60)
        button1 = 2

    elif (mouseButton == LEFT) and (110 < mouseX < 150) and (40 < mouseY < 80):
        fill(255, 0, 0)
        empty_dice(130, 60)
        button1 = 3

    elif (mouseButton == LEFT) and (150 < mouseX < 190) and (40 < mouseY < 80):
        fill(255, 0, 0)
        empty_dice(170, 60)
        button1 = 4
    
    elif (mouseButton == LEFT) and (190 < mouseX < 230) and (40 < mouseY < 80):
        fill(255, 0, 0)
        empty_dice(210, 60)
        button1 = 5
        
    elif (mouseButton == LEFT) and (230 < mouseX < 270) and (40 < mouseY < 80):
        fill(255, 0, 0)
        empty_dice(250, 60)
        button1 = 6
        
    else:
        noFill()
    
    print(button1) # zur Kontrolle
    
    textAlign(CENTER, CENTER)
    text("Zufall", 120, 140)
    text("erwartetes Ergebnis", 300, 140)
    
    if (mouseButton == LEFT) and (30 < mouseX < 210) and (120 < mouseY < 160):
        global button2
        fill(255, 0, 0)
        rect(120, 140, 180, 40)
        button2 = 1
        
    elif (mouseButton == LEFT) and (210 < mouseX < 390) and (120 < mouseY < 160):
        fill(255, 0, 0)
        rect(300, 140, 180, 40)
        button2 = 2
        
    else:
        noFill()
    
    print(button2) # zur Kontrolle
    
    if button2 == 2:
        for i in range(0, button1):
            fill(0)
            textAlign(LEFT, CENTER)
            text("Wuerfel " + str(i + 1), 20, 180 + i * 50)
            fill(255)
            for j in range(0, button1):
                empty_dice(130 + i * 50, 190 + j * 50)

        for k in range(0, button1):
            global number
            number = k + 1
            for l in range(0, button1):
                dice_number(130 + (k * 50), 190 + l * 50)
                
    elif button2 == 1:
        for i in range(0, button1):
            fill(0)
            textAlign(LEFT, CENTER)
            text("Zufall", 20, 180)
            fill(255)
            empty_dice(130 + i * 50, 190)
            number = round(random(1, 6))
            dice_number(130 + i * 50, 190)
            noLoop()
            
    else:
        noFill()

def empty_dice(xPos, yPos):
    rectMode(CENTER)
    square(xPos, yPos, 40)
    
def dice_number(xPos, yPos):
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
        
