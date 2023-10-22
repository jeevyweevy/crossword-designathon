import tkinter as tk
import wordsearch
import visuals


left_padding = 20
right_padding = 20
top_padding = 20
bottom_padding = 210

def openEasy():
    def goBack():
        window.destroy()
        visuals.show_menu()

    checked = [False, False, False, False, False, False]

    grid, words, definitions = wordsearch.initialize_screen_easy()

    window = tk.Tk()
    window.title("Easy Level")
    window.geometry("750x750")

    num_rows = 10
    num_columns = 10


    # Calculate the cell size based on the available space and the grid size
    cell_width = (750 - left_padding - right_padding) // num_columns
    cell_height = (750 - top_padding - bottom_padding) // num_rows

    # Create and place labels in the grid
    for row in range(num_rows):
        for col in range(num_columns):
            cell_text = grid[row][col]
            cell_label = tk.Label(window, text=cell_text, width=2, height=1,font=("Arial", 12), bg="white", borderwidth=1, relief="solid")

            # Calculate the position and size of each label
            x = left_padding + col * cell_width
            y = top_padding + row * cell_height
            cell_label.place(x=x, y=y, width=cell_width, height=cell_height)

    words_to_find_label = tk.Label(window, text="WORDS TO FIND: ", font=("Arial", 20))
    words_to_find_label.place(x=left_padding, y=550)

    found = tk.PhotoImage(file="found.png")

    def showDefintion(i):
        checked[i] = True
        checked_label = tk.Label(window, image=found)
        if i in range(0,3):
            checked_label.place(x=left_padding + (200 * i), y=590)
        if i in range(3,6):
            checked_label.place(x=left_padding + (200 * (i-3)), y=630)
        if all(checked):
            win_label = tk.Label(window, text= "CONGRATULATIONS! YOU WON!!!", font=("Arial", 30, "bold"))
            win_label.pack(side = "bottom")
        showDef(definitions[i], words[i])

    for i in range(0,3):

        word_label = tk.Button(window, text=words[i], font=("Arial", 12), command= lambda num=i: showDefintion(num))
        word_label.place(x=left_padding + (200 * i) + 30,y=590)

    for i in range(3,6):
        word_label = tk.Button(window, text=words[i], font=("Arial", 12), command= lambda num=i: showDefintion(num))
        word_label.place(x=left_padding + (200 * (i-3)) +30, y=630)

    back_button = tk.Button(window, text="BACK", font= ("Arial", 20),command=goBack)
    back_button.pack(side= "bottom", anchor= "ne", padx =20, pady=20)


    window.mainloop()

def openMedium():
    checked = [False, False, False, False, False, False]
    def goBack():
        window.destroy()
        visuals.show_menu()
    grid, words, definitions = wordsearch.initialize_screen_medium()

    window = tk.Tk()
    window.title("Medium Level")
    window.geometry("750x750")

    num_rows = 15
    num_columns = 15

    # Calculate the cell size based on the available space and the grid size
    cell_width = (750 - left_padding - right_padding) // num_columns
    cell_height = (750 - top_padding - bottom_padding) // num_rows

    # Create and place labels in the grid
    for row in range(num_rows):
        for col in range(num_columns):
            cell_text = grid[row][col]
            cell_label = tk.Label(window, text=cell_text, width=2, height=1,font=("Arial", 12), bg="white", borderwidth=1, relief="solid")

            # Calculate the position and size of each label
            x = left_padding + col * cell_width
            y = top_padding + row * cell_height
            cell_label.place(x=x, y=y, width=cell_width, height=cell_height)

    words_to_find_label = tk.Label(window, text="WORDS TO FIND: ", font=("Arial", 20))
    words_to_find_label.place(x=left_padding, y=550)
    found = tk.PhotoImage(file="found.png")

    def showDefintion(i):
        checked[i] = True
        checked_label = tk.Label(window, image=found)
        if i in range(0, 3):
            checked_label.place(x=left_padding + (200 * i), y=590)
        if i in range(3, 6):
            checked_label.place(x=left_padding + (200 * (i - 3)), y=630)
        if all(checked):
            win_label = tk.Label(window, text= "CONGRATULATIONS! YOU WON", font=("Arial", 30, "bold"))
            win_label.pack(side = "bottom")

        showDef(definitions[i], words[i])





    for i in range(0,3):
        word_label = tk.Button(window, text=words[i], font=("Arial", 12), command= lambda num=i: showDefintion(num))
        word_label.place(x=left_padding +30+ (200 * i),y=590)
    for i in range(3,6):
        word_label = tk.Button(window, text=words[i], font=("Arial", 12), command= lambda num=i: showDefintion(num))
        word_label.place(x=left_padding +30 + (200 * (i-3)), y=630)

    back_button = tk.Button(window, text="BACK", font= ("Arial", 20),command=goBack)
    back_button.pack(side= "bottom", anchor= "ne", padx =20, pady=20)


    window.mainloop()



def openHard():
    def goBack():
        window.destroy()
        visuals.show_menu()
    grid, words, definitions = wordsearch.initialize_screen_hard()

    window = tk.Tk()
    window.title("Hard Level")
    window.geometry("750x750")

    num_rows = 20
    num_columns = 20



    cell_width = (750 - left_padding - right_padding) // num_columns
    cell_height = (750 - top_padding - bottom_padding) // num_rows

    for row in range(num_rows):
        for col in range(num_columns):
            cell_text = grid[row][col]
            cell_label = tk.Label(window, text=cell_text, width=2, height=1,font=("Arial", 12), bg="white", borderwidth=1, relief="solid")

            # Calculate the position and size of each label
            x = left_padding + col * cell_width
            y = top_padding + row * cell_height
            cell_label.place(x=x, y=y, width=cell_width, height=cell_height)

    words_to_find_label = tk.Label(window, text="WORDS TO FIND: ", font=("Arial", 20))
    words_to_find_label.place(x=left_padding, y=550)

    def showDefintion(i):
        showDef(definitions[i], words[i])


    for i in range(0,4):
        word_label = tk.Button(window, text=words[i], font=("Arial", 12), command= lambda num=i: showDefintion(num))
        word_label.place(x=left_padding + (150 * i),y=590)
    for i in range(4,8):
        word_label = tk.Button(window, text=words[i], font=("Arial", 12), command= lambda num=i: showDefintion(num))
        word_label.place(x=left_padding + (150 * (i-4)), y=630)

    back_button = tk.Button(window, text="BACK", font= ("Arial", 20),command=goBack)
    back_button.pack(side= "bottom", anchor= "ne", padx =20, pady=20)


    window.mainloop()


def showDef(definition, name):
    defWindow = tk.Tk()
    defWindow.geometry("400x200")
    defWindow.title(name)

    header = "DEFINITION OF " + name + ": "
    def_header = tk.Label(defWindow, text=header, font=("Arial", 14, "bold"), wraplength= 250)
    def_header.pack()
    def_label = tk.Label(defWindow, text=definition, font=("Arial", 14), wraplength= 250)
    def_label.pack()



