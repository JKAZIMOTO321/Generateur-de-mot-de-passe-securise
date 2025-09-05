import sys
import random
import string
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from src_design import *


def generate_pasword():
    length=ui.spinBox.value()
    use_majiscule=ui.checkBox_Majuscules.isChecked()
    use_miniscule=ui.checkBox_miniscules.isChecked()
    use_chiffres=ui.checkBox_chiffres.isChecked()
    use_symboles=ui.checkBox_symboles.isChecked()

    # print(f"majiscule : {use_majiscule}")
    # print(f"Miniscule : {use_miniscule}")
    # print(f"Chiffres : {use_chiffres}")
    # print(f"Symboles : {use_symboles}")
    # print("==========================>>>")
    chars=""
    if use_majiscule: chars+=string.ascii_uppercase
    if use_miniscule: chars+=string.ascii_lowercase
    if use_chiffres: chars+=string.digits
    if use_symboles: chars+=string.punctuation
    
    if chars=="":
        ui.line_Edit_generated_password.setText("Selectionner au moins un type")
        ui.line_Edit_generated_password.setStyleSheet("color : red;")
        ui.button_copy.setVisible(False)
    else:
        ui.button_copy.setVisible(True)
        ui.line_Edit_generated_password.setStyleSheet("color: black;")
        password= ''.join(random.choice(chars) for _ in range(length))
        ui.line_Edit_generated_password.setText(password)

    #barre de progression de securite
    puissance_password=0
    if use_majiscule: puissance_password+=1
    if use_miniscule: puissance_password+=1
    if use_chiffres:puissance_password+=1
    if use_symboles:puissance_password+=1
    
    ui.progressBar.setValue(puissance_password)
    #changer la couleur selon la force
    colors=["rgb(255, 0, 0)","rgb(255,0,75)","rgb(100,24,200)","rgb(0,0,255)","rgb(0, 255, 0)"]
    ui.progressBar.setStyleSheet(f"QProgressbar::chunk {{background-color:{colors[puissance_password]};}}")


def copyToClipBoard():
    clipBoard=QApplication.clipboard()
    clipBoard.setText(ui.line_Edit_generated_password.text())


app = QtWidgets.QApplication(sys.argv)
PasswordGenerator = QtWidgets.QWidget()
ui = Ui_PasswordGenerator()
ui.setupUi(PasswordGenerator)


#bouton generer
ui.button_generate.clicked.connect(generate_pasword)
#bouton copier
ui.button_copy.clicked.connect(copyToClipBoard)

PasswordGenerator.show()
sys.exit(app.exec_())
