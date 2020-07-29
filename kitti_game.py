from tkinter import *
from tkinter import ttk

win = Tk()
win.title("KITTI GAME")
win.geometry("400x400")
win.configure(bg = "light blue")

welcome_frame = Frame(win)
welcome_frame.pack(padx = 20, pady = 10)

welcome_text = Label(welcome_frame, text = "KITTI GAME", fg = "green", font = ("times", 30, "bold"))
welcome_text.pack()

box_frame = Frame(win)
box_frame.configure(bg = "light blue")
box_frame.pack(pady = 50)

no_of_player = Label(box_frame, text = "Select Number Of Players", font = ("arial", 13, "bold"))
no_of_player.pack()

box = ttk.Combobox(box_frame, width = 20)
box['values'] = [1, 2, 3, 4, 5, 6, 7]
box.set(1)
box.pack()

button_frame = Frame(win)
button_frame.pack(pady = 50)

def second_window():
    player_no = box.get()
    win.destroy()
    win_two = Tk()
    win_two.title("KITTI PLAY")
    win_two.configure(bg = "light blue")

    frame_one = Frame(win_two)
    frame_one.pack(padx = 20, pady = 10)


    names_of_players_text = Label(frame_one,fg = "green", bg = "light blue",text = "Names Of The Players ", font = ("arial", 25, "bold"))
    names_of_players_text.pack()

    frame_two = Frame(win_two)
    frame_two.pack()

    frame_two.configure(bg = "light blue")
    names_player = []

    for a in range(int(player_no)):
        player_number = Label(frame_two, text = "Player " + str(a + 1), bg = "light blue")
        player_number.pack()
        entry_box = Entry(frame_two, width = 20)
        entry_box.pack(pady = 10)
        names_player.append(entry_box)

    frame_three = Frame(win_two)
    frame_three.pack(pady = 20)

    def main_window():
        player_names = []
        score = []
        for names in names_player:
            player_names.append(names.get())
        win_two.destroy()

        win_three = Tk()
        win_three.title("KITTI  PLAY")
        win_three.configure(bg = "light blue")

        welcome_frame = Frame(win_three, borderwidth = 5)
        welcome_frame.pack()

        Label(welcome_frame, text = "Displaying Scores", fg = "green", font = ("times", 30, "bold")).pack(pady = 20, padx = 20)

        frame_one = Frame(win_three)
        frame_one.pack(pady = 10)
        frame_one.configure(bg = "light blue")

        for a in player_names:
            Label(frame_one, text = str(a), fg = "white", bg = "light blue", font = ("arial", 15, "bold")).pack(side = LEFT, padx = 15)

        frame_two = Frame(win_three, bg = "light blue")
        frame_two.pack()

        frame_three = Frame(win_three, bg = "light blue")
        frame_three.pack()

        frame_four = Frame(win_three, bg = "light blue")
        frame_four.pack()
        
        score_label = []

        for i in range(len(player_names)):
            score.append(100)
            score_label.append(0)
            score_label[i] = Label(frame_two, text = "Score : " + str(score[i]), fg = "white", bg = "light blue", font = ("arial", 10, "bold"))
            score_label[i].pack(side = LEFT, padx = 5)

        def won(n):
            score[n] += 10
            score_label[n].configure(text = "Score : " + str(score[n]))

        def lost(n):
            score[n] -= 10
            score_label[n].configure(text = "Score : " + str(score[n]))

        for i in range(len(player_names)):
            Button(frame_three, text = "Won", width = 5, command = lambda i = i : won(i)).pack(side = LEFT, padx = 15, pady = 5)
            Button(frame_four, text = "Lost", width = 5, command = lambda i = i : lost(i)).pack(side = LEFT, padx = 15, pady = 5)

        win_three.mainloop()

    def start_calculating():
        main_window()
        
    calculate_button = Button(frame_three, width = 15,bg = "green", fg = "white", text = "Start Calculating", font = ("arial", 15, "bold"), command = start_calculating)
    calculate_button.pack()

    win_two.mainloop()

def start_game():
    second_window()

start_button = Button(button_frame, width = 15, text = "Start Game", font = ("arial", 15, "bold"), fg = "green", command = start_game)
start_button.pack()

win.mainloop()
