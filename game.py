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
    grid, words = wordsearch.initialize_screen_easy()

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

    for i in range(0,3):
        word_label = tk.Button(window, text=words[i], font=("Arial", 12))
        word_label.place(x=left_padding + (200 * i),y=590)
    for i in range(3,6):
        word_label = tk.Button(window, text=words[i], font=("Arial", 12))
        word_label.place(x=left_padding + (200 * (i-3)), y=620)

    back_button = tk.Button(window, text="BACK", font= ("Arial", 20),command=goBack)
    back_button.pack(side= "bottom", anchor= "ne", padx =20, pady=20)


    window.mainloop()

def openMedium():
    def goBack():
        window.destroy()
        visuals.show_menu()

    grid, words = wordsearch.initialize_screen_medium()

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
            cell_label = tk.Label(window, text=cell_text, width=2, height=1, font=("Arial", 12), bg="white",
                                  borderwidth=1,
                                  relief="solid")

            # Calculate the position and size of each label
            x = left_padding + col * cell_width
            y = top_padding + row * cell_height
            cell_label.place(x=x, y=y, width=cell_width, height=cell_height)

    words_to_find_label = tk.Label(window, text="WORDS TO FIND: ", font=("Arial", 20))
    words_to_find_label.place(x=left_padding, y=550)

    for i in range(0, 3):
        word_label = tk.Button(window, text=words[i], font=("Arial", 12))
        word_label.place(x=left_padding + (200 * i), y=590)
    for i in range(3, 6):
        word_label = tk.Button(window, text=words[i], font=("Arial", 12))
        word_label.place(x=left_padding + (200 * (i - 3)), y=620)

    back_button = tk.Button(window, text="BACK", font=("Arial", 20), command=goBack)
    back_button.pack(side="bottom", anchor="ne", padx=20, pady=20)

    window.mainloop()


    def goBack():
        window.destroy()
        visuals.show_menu()
    grid, words = wordsearch.initialize_screen_easy()

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

    for i in range(0,3):
        word_label = tk.Button(window, text=words[i], font=("Arial", 12))
        word_label.place(x=left_padding + (200 * i),y=590)
    for i in range(3,6):
        word_label = tk.Button(window, text=words[i], font=("Arial", 12))
        word_label.place(x=left_padding + (200 * (i-3)), y=620)

    back_button = tk.Button(window, text="BACK", font= ("Arial", 20),command=goBack)
    back_button.pack(side= "bottom", anchor= "ne", padx =20, pady=20)


    window.mainloop()



def openHard():
    def goBack():
        window.destroy()
        visuals.show_menu()
    grid, words = wordsearch.initialize_screen_hard()

    window = tk.Tk()
    window.title("Hard Level")
    window.geometry("750x750")

    num_rows = 20
    num_columns = 20



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

    for i in range(0,4):
        word_label = tk.Button(window, text=words[i], font=("Arial", 12))
        word_label.place(x=left_padding + (150 * i),y=590)
    for i in range(4,8):
        word_label = tk.Button(window, text=words[i], font=("Arial", 12))
        word_label.place(x=left_padding + (150 * (i-4)), y=630)

    back_button = tk.Button(window, text="BACK", font= ("Arial", 20),command=goBack)
    back_button.pack(side= "bottom", anchor= "ne", padx =20, pady=20)


    window.mainloop()