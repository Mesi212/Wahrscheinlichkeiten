print("Wie viele Wuerfel wirfst du?")
#numdice = input() --> geht nicht...

number = round(random(1, 6))

def setup():
    size(1000, 1000)
    background(255)
    
def draw():
    xPos = 50
    yPos = 50
    dots = random
    empty_dice(xPos, yPos)
    dice_number(xPos, yPos)
    
def empty_dice(xPos, yPos):
    rectMode(CENTER)
    fill(255)
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
        
