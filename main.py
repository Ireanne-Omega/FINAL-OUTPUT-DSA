# DATA STRUCTURE AND ALGORITHMS - FINAL PROJECT
print("\nPROGRAMMED BY:")
print("IREANNE N. OMEGA")
print("BSCOE 2-2\n")


import tkinter as tk

root = tk.Tk()
root.geometry("600x450")
root.title("Output Selection")

title_label = tk.Label(root, text="DATA STRUCTURE AND ALGORITHM FINAL PROJECT", font=("Agency FB", 24))
title_label1 = tk.Label(root, text="Inspect One", font=("Arial", 16))
title_label.pack(pady=20)
title_label1.pack(pady=20)

def start_game(game_name):
    root.destroy()
    from output1 import welcome ## changed file name for easier importing of the file
    print(f"Starting {game_name}...")

def start_game2(game_name):
    root.destroy()
    from output2 import checkans ## changed file name for easier importing of the file
    print(f"Starting {game_name}...")
def start_game3(game_name):
    root.destroy()
    from output3 import gameLoop ## changed file name for easier importing of the file
    print(f"Starting {game_name}...")

game1_button = tk.Button(root, text="DICTIONARIES", font=("Arial", 12), command=lambda: start_game("ONLINE MOVIE TICKET"))
game1_button.pack(pady=10)

game2_button = tk.Button(root, text="QUEUES", font=("Arial", 12), command=lambda: start_game2("JUMBLED WORD GAME"))
game2_button.pack(pady=10)

game3_button = tk.Button(root, text="STACK QUEUES", font=("Arial", 12), command=lambda: start_game3("TOWER GAME"))
game3_button.pack(pady=10)

root.mainloop()
