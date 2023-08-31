import random
from MathMines.MathMines import label 
from PyQt5 import QtCore, QtGui, QtWidgets

randomList=[]
answerA=[3, 5, 8]
answerB=[2, 6, 9]
answerC=[1, 10]
answerD=[4, 7]
global placar
placar=0


def rngen():
    for i in range(1):
        # Number = 0
        global Number
        Number = random.randint(1, 7)
        if Number not in randomList:
            randomList.append(Number)
            # Numberg=Number
            print(Number)
            print(f"questions/%s" % Number)
            return f"questions/%s.png" % Number
        elif Number in randomList:
            # Numberg=Number
            return rngen()

# Verificão de resposta


def change_button_color(button):
    button.setStyleSheet("""
        .QPushButton {
            background: green;
            color: white;
            border-color: black;
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            font: bold 14px;
            padding: 25px 10px;
            min-width: 6px;
        }
        
        .QPushButton:hover {
            background: blue;
        }
    """)

def verifyA(placar,button):
    if Number in answerA:
        placar = placar + 10
        print("Questão correta, você ganhou 10 pontos!")
        change_button_color(button.objectName())
    else:
        placar = placar - 5
        print("Questão incorreta, você perdeu 5 pontos!")


def verifyB(placar, button):
    if Number in answerB:
        placar = placar + 10
        print("Questão correta, você ganhou 10 pontos!")
        change_button_color(button.objectName())
    else:
        placar = placar - 5
        print("Questão incorreta, você perdeu 5 pontos!")


def verifyC(placar, button):
    if Number in answerC:
        placar = placar + 10
        print("Questão correta, você ganhou 10 pontos!")
        change_button_color(button.objectName())
    else:
        placar = placar - 5
        print("Questão incorreta, você perdeu 5 pontos!")


def verifyD(placar, button):
    if Number in answerD:
        placar = placar + 10
        print("Questão correta, você ganhou 10 pontos!")
        change_button_color(button.objectName())
    else:
        placar = placar - 5
        print("Questão incorreta, você perdeu 5 pontos!")
