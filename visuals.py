import tkinter as tk
import game

window = tk.Tk()

def easy_call():
    print("EASY")
    game.openEasy()

def medium_call():
    print("medium")
    game.openMedium()
def hard_call():
    print("hard")
    game.openHard()
def show_menu():
    def easy_inner():
        menuWindow.destroy()
        game.openEasy()
    def medium_inner():
        menuWindow.destroy()
        game.openMedium()
    def hard_inner():
        menuWindow.destroy()
        game.openHard()
    menuWindow = tk.Tk()
    menuWindow.title("Menu Window")
    menuWindow.geometry("750x750")

    background_image = tk.PhotoImage(file= "menuScreen.png")
    easy = tk.PhotoImage(file= "easy.png")
    medium = tk.PhotoImage(file= "medium.png")
    hard = tk.PhotoImage(file = "hard.png")

    background_label = tk.Label(menuWindow, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    easy_button = tk.Button(menuWindow, image=easy, width=190, height=150, command= easy_inner)
    easy_button.place(x=150, y=250)

    medium_button = tk.Button(menuWindow, image=medium, width=190, height=150, command=medium_inner)
    medium_button.place(x=400, y = 250)

    hard_button = tk.Button(menuWindow, image=hard, width=190, height=150, command= hard_inner)
    hard_button.place(x=250, y= 400)
    menuWindow.mainloop()

def homeScreen():
    def show_menu_1():
        window.destroy()
        show_menu()
    # Create a tkinter window
    window.geometry("750x750")
    window.title("Home Screen")

    background_image = tk.PhotoImage(file="homescreen_background.png")
    continue_image = tk.PhotoImage(file="continue.png")

    background_label = tk.Label(window, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    continue_button = tk.Button(window, image=continue_image, width=270, height=80, command=show_menu_1)
    continue_button.pack(side="bottom", pady=30)

    window.mainloop()
