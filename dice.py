# leerer Wuerfel
def empty_dice(xPos, yPos):
    rectMode(CENTER)
    square(xPos, yPos, 40)
  
# Wuerfelpunkte fuer jede Zahl von 1 bis 6
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
