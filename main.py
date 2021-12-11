import tkinter as tk

import mysql.connector

database = mysql.connector.connect(host="localhost", user="root", passwd="", database="pythoncounter")

cursor = database.cursor()

def getCountOfTable():
    cursor.execute("select counter from counter where id=1")
    result = cursor.fetchall()
    result = str(result).replace("(","")
    result = result.replace(")", "")
    result = result.replace("[", "")
    result = result.replace("]", "")
    result = result.replace(",", "")

    return result


def buildGUI():
    mainWindow = tk.Tk()
    mainWindow.title("Button clicked counter")
    mainWindow.resizable(False, False)
    mainWindow.geometry("400x300")
    mainWindow.eval('tk::PlaceWindow . center')

    label1 = tk.Label(mainWindow, text="Dieser Button wurde "+getCountOfTable()+"-mal angeklickt!")
    label1.pack()

    newUserButton = tk.Button(mainWindow, text="Klick mich!",
                              command=lambda: updateCount(mainWindow))
    newUserButton.pack()

    mainWindow.mainloop()

def updateCount(window):
    window.destroy()
    oldCount = int(getCountOfTable())
    newCount = oldCount+1
    cursor.execute("update counter set counter="+str(newCount)+" where id=1")
    database.commit()
    buildGUI()


buildGUI()