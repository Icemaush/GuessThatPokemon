# Created by Reece Pieri, 16/6/19.
# All art assets from the Pokemon game and anime series.
# Background music: Eastward Bound from Treasures of Aht Urhgan Original Soundtrack, by Naoshi Mizuta. Owned by
# Square-Enix.

from tkinter import *
from PIL import ImageTk
import random
import time
from datetime import datetime
from pygame import mixer
from SlideUp import Slide2Up
import pyglet


class PokeGame(object):
    def __init__(self):
        self.window = Tk()
        self.window.title("Guess That Pokemon!")
        self.window.geometry("1000x750")
        self.window.resizable(False, False)
        self.canvas = Canvas(self.window, width=1000, height=750)
        self.canvas.pack()

        mixer.init()
        mixer.music.set_volume(0.4)
        mixer.music.load("Audio/BGM.mp3")
        mixer.music.play(-1)

        pyglet.font.add_file("Fonts/Pokemon Solid.ttf")
        pokemon_solid = pyglet.font.load("Pokemon Solid")

        self.slideup = Slide2Up()
        self.title_screen()

    def title_screen(self):
        self.canvas.delete("all")
        self.background_img = PhotoImage(file="Backgrounds/Grass.png")
        self.bg_img = self.background_img
        self.canvas.create_image(500, 375, image=self.bg_img)

        title_img = ImageTk.PhotoImage(file="Buttons/Title.png")
        gametitle_img = title_img
        self.canvas.create_image(500, 225, image=gametitle_img)

        start_img = ImageTk.PhotoImage(file="Buttons/StartGame.png")
        startgame_img = start_img
        self.start = self.canvas.create_image(500, 600, image=startgame_img)
        self.canvas.tag_bind(self.start, "<Button-1>", self.easy_mode_start)

        self.canvas.bind("<Motion>", self.check_hand_on_start)  # binding to motion

        mainloop()

    # def select_mode(self):
    #     self.canvas.delete("all")
    #
    #     self.canvas.create_image(500, 375, image=self.bg_img)
    #
    #     diff_img = ImageTk.PhotoImage(file="Buttons/SelectDifficulty.png")
    #     difficulty_img = diff_img
    #     self.canvas.create_image(500, 125, image=difficulty_img)
    #     diffeasy_img = ImageTk.PhotoImage(file="Buttons/Easy.png")
    #     easy_img = diffeasy_img
    #     easy_btn = Button(self.canvas, image=easy_img, borderwidth=0, relief="flat", command=self.easy_mode_start)
    #     self.canvas.create_window(500, 225, window=easy_btn)
    #     diffhard_img = ImageTk.PhotoImage(file="Buttons/Hard.png")
    #     hard_img = diffhard_img
    #     hard_btn = Button(self.canvas, image=hard_img, borderwidth=0, relief="flat")
    #     self.canvas.create_window(500, 325, window=hard_btn)
    #
    #     mainloop()

    # ----- CREATES VARIABLES AND LIST OF POKEMON TO USE IN GAME ----- #
    def easy_mode_start(self, event=None):
        self.start_time = datetime.now()
        self.score = 0
        self.chain = 0
        self.highest_chain = 0
        self.correct_guesses = 0
        self.scoretxt = StringVar()
        self.chaintxt = StringVar()
        self.game_list = []
        self.choice_list = []
        self.pokemon_num = 20
        self.guess = ""
        self.pokemon = ""
        self.resetcursor()

        self.gen1_list = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle",
                          "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna",
                          "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow",
                          "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran♀", "Nidorina",
                          "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix",
                          "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume",
                          "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian",
                          "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag",
                          "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp",
                          "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler",
                          "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton",
                          "Farfetchd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder",
                          "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler",
                          "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee",
                          "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela",
                          "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime",
                          "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados",
                          "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte",
                          "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres",
                          "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]

        self.gen2_list = ["Chikorita", "Bayleef", "Meganium", "Cyndaquil", "Quilava", "Typhlosion", "Totodile",
                          "Croconaw", "Feraligatr", "Sentret", "Furret", "Hoothoot", "Noctowl", "Ledyba", "Ledian",
                          "Spinarak", "Ariados", "Crobat", "Chinchou", "Lanturn", "Pichu", "Cleffa", "Igglybuff",
                          "Togepi", "Togetic", "Natu", "Xatu", "Mareep", "Flaaffy", "Ampharos", "Bellossom", "Marill",
                          "Azumarill", "Sudowoodo", "Politoed", "Hoppip", "Skiploom", "Jumpluff", "Aipom", "Sunkern",
                          "Sunflora", "Yanma", "Wooper", "Quagsire", "Espeon", "Umbreon", "Murkrow", "Slowking",
                          "Misdreavus", "Unown", "Wobbuffet", "Girafarig", "Pineco", "Forretress", "Dunsparce",
                          "Gligar", "Steelix", "Snubbull", "Granbull", "Qwilfish", "Scizor", "Shuckle", "Heracross",
                          "Sneasel", "Teddiursa", "Ursaring", "Slugma", "Magcargo", "Swinub", "Piloswine", "Corsola",
                          "Remoraid", "Octillery", "Delibird", "Mantine", "Skarmory", "Houndour", "Houndoom", "Kingdra",
                          "Phanpy", "Donphan", "Porygon2", "Stantler", "Smeargle", "Tyrogue", "Hitmontop", "Smoochum",
                          "Elekid", "Magby", "Miltank", "Blissey", "Raikou", "Entei", "Suicune", "Larvitar", "Pupitar",
                          "Tyranitar", "Lugia", "Ho-Oh", "Celebi"]
        self.pokemon_list = self.gen1_list + self.gen2_list

        random.shuffle(self.pokemon_list)
        for i in self.pokemon_list[:self.pokemon_num]:
            self.game_list.append(i)
        print(self.game_list)
        self.select_pokemon()

    # ----- PULLS RANDOM POKEMON AND CREATES LIST TO USE IN GAME ----- #
    def select_pokemon(self):
        self.afk_time = str(datetime.now())
        self.afk_tuple = (
            int(self.afk_time.split(":", 2)[1]), int(self.afk_time.split(":", 2)[2].split(".")[0]), self.score)
        if len(self.game_list) == 0:
            self.endgame()
        else:
            self.choice_list = []
            self.pokemon = str(self.game_list.pop())
            self.choice_list.append(self.pokemon)
            other_choices = random.choices(self.pokemon_list, k=3)
            for i in other_choices:
                if i == str(self.pokemon):
                    x = random.choice(self.pokemon_list)
                    self.choice_list.append(x)
                if i in self.choice_list:
                    x = random.choice(self.pokemon_list)
                    self.choice_list.append(x)
                else:
                    self.choice_list.append(i)
            if len(self.choice_list) == 5:
                if self.choice_list[4] == self.pokemon:
                    self.choice_list.remove(self.choice_list[0])
                else:
                    self.choice_list.remove(self.choice_list[4])
            random.shuffle(self.choice_list)
            print(self.pokemon)
            print(self.choice_list)
            self.display_widgets()
            self.display_silhouette(window=self.window)

    # ----- CLEAR CANVAS THEN DISPLAY WIDGETS ----- #
    def display_widgets(self):
        self.canvas.delete("all")
        self.canvas.create_image(500, 375, image=self.bg_img)

        pause_audio_img = ImageTk.PhotoImage(file="Buttons/Pause.png")
        self.pause_img = pause_audio_img
        self.pause = self.canvas.create_image(35, 35, image=self.pause_img, tag="pause")
        self.canvas.tag_bind(self.pause, "<Button-1>", self.pause_bgm)
        self.canvas.bind("<Motion>", self.check_hand_on_pauseaudio)

        scoreboard_img = ImageTk.PhotoImage(file="Buttons/Score.png")
        self.score_img = scoreboard_img
        self.canvas.create_image(910, 35, image=self.score_img)

        self.sc = self.canvas.create_text(910, 70, fill="#ffffff", font=("Pokemon Solid", 32),
                                          text=self.scoretxt.get())  # #ffd530
        self.scoretxt.set(self.score)
        self.scoretxt.trace_variable('w', self.change_score)
        self.scoretxt.set(self.score)

        chainboard_img = ImageTk.PhotoImage(file="Buttons/Chain.png")
        self.chain_img = chainboard_img
        self.canvas.create_image(910, 140, image=self.chain_img)

        self.ch = self.canvas.create_text(910, 175, fill="#ffffff", font=("Pokemon Solid", 32),  # #ffd530
                                          text=self.chaintxt.get())
        self.chaintxt.set(self.chain)
        self.chaintxt.trace_variable('w', self.change_chain)
        self.chaintxt.set(self.chain)

        self.button_list = []
        self.gamebtn1 = Button(self.canvas, bg="#327ffc", fg="#ffd530", font=("Pokemon Solid", 16), state="normal",
                               borderwidth=0, relief="flat", width=20, height=1, command=self.btn1, cursor="hand2")
        self.canvas.create_window(350, 565, window=self.gamebtn1)
        self.gamebtn2 = Button(self.canvas, bg="#327ffc", fg="#ffd530", font=("Pokemon Solid", 16), state="normal",
                               borderwidth=0, relief="flat", width=20, height=1, command=self.btn2, cursor="hand2")
        self.canvas.create_window(650, 565, window=self.gamebtn2)
        self.gamebtn3 = Button(self.canvas, bg="#327ffc", fg="#ffd530", font=("Pokemon Solid", 16), state="normal",
                               borderwidth=0, relief="flat", width=20, height=1, command=self.btn3, cursor="hand2")
        self.canvas.create_window(350, 680, window=self.gamebtn3)
        self.gamebtn4 = Button(self.canvas, bg="#327ffc", fg="#ffd530", font=("Pokemon Solid", 16), state="normal",
                               borderwidth=0, relief="flat", width=20, height=1, command=self.btn4, cursor="hand2")
        self.canvas.create_window(650, 680, window=self.gamebtn4)
        self.button_list.append(self.gamebtn1)
        self.button_list.append(self.gamebtn2)
        self.button_list.append(self.gamebtn3)
        self.button_list.append(self.gamebtn4)

        # ----- VALIDATION FOR POKEMON NAME WITH SPECIAL CHARACTER ----- #
        count = 0
        for i in self.choice_list:
            if i == "Farfetchd":
                i = "Farfetch'd"
                self.button_list[count].configure(text=i.upper())
                count += 1
            else:
                self.button_list[count].configure(text=i.upper())
                count += 1

    # ----- CHECKS FOR AFK AND RETURNS TO TITLE SCREEN ----- #
    def check_for_afk(self):
        if self.canvas.find_withtag("sil") or self.canvas.find_withtag("col"):
            now_time = str(datetime.now())
            now_tuple = (int(now_time.split(":", 2)[1]), int(now_time.split(":", 2)[2].split(".")[0]), self.score)
            if (now_tuple[0], now_tuple[1], now_tuple[2]) == (self.afk_tuple[0] + 1, self.afk_tuple[1],
                                                              self.afk_tuple[2]):
                print("User AFK. Returning to title screen.")
                self.title_screen()
                return
            else:
                self.window.after(60000, self.check_for_afk)

    # ----- DISPLAY SILHOUETTE OR COLOUR POKEMON IMAGES ----- #
    def display_silhouette(self, window):
        self.canvas.delete("col")
        if str(self.pokemon) in self.gen1_list:
            path = "Images/Gen1/"
        if str(self.pokemon) in self.gen2_list:
            path = "Images/Gen2/"
        silhouette_img = ImageTk.PhotoImage(file=str(path + self.pokemon + "-1.png"))
        window.silhouette_img = silhouette_img
        self.canvas.create_image(500, 275, image=silhouette_img, tag="sil")
        self.window.update_idletasks()
        if self.canvas.find_withtag("sil")[0]:
            self.check_for_afk()

    def display_colour(self, window):
        self.canvas.delete("sil")
        if self.pokemon in self.gen1_list:
            path = "Images/Gen1/"
        if self.pokemon in self.gen2_list:
            path = "Images/Gen2/"
        colour_img = ImageTk.PhotoImage(file=path + self.pokemon + ".png")
        window.colour_img = colour_img
        self.canvas.create_image(500, 275, image=colour_img, tag="col")
        self.window.update_idletasks()

    # ----- ASSIGNS TEXT OF BUTTON PRESSED TO BE COMPARED TO ANSWER ----- #
    def btn1(self):
        if self.gamebtn1['text'] == "EEVEE":
            formatted_name = "Eevee"
        else:
            formatted_name = str(self.gamebtn1['text'][0]).upper() + \
                         str(self.gamebtn1['text']).lstrip(self.gamebtn1['text'][0]).lower()
        self.guess = formatted_name
        print(self.guess)
        self.check_answer()

    def btn2(self):
        if self.gamebtn1['text'] == "EEVEE":
            formatted_name = "Eevee"
        else:
            formatted_name = str(self.gamebtn2['text'][0]).upper() + \
                         str(self.gamebtn2['text']).lstrip(self.gamebtn2['text'][0]).lower()
        self.guess = formatted_name
        print(self.guess)
        self.check_answer()

    def btn3(self):
        if self.gamebtn1['text'] == "EEVEE":
            formatted_name = "Eevee"
        else:
            formatted_name = str(self.gamebtn3['text'][0]).upper() + \
                         str(self.gamebtn3['text']).lstrip(self.gamebtn3['text'][0]).lower()
        self.guess = formatted_name
        print(self.guess)
        self.check_answer()

    def btn4(self):
        if self.gamebtn1['text'] == "EEVEE":
            formatted_name = "Eevee"
        else:
            formatted_name = str(self.gamebtn4['text'][0]).upper() + \
                         str(self.gamebtn4['text']).lstrip(self.gamebtn4['text'][0]).lower()
        self.guess = formatted_name
        print(self.guess)
        self.check_answer()

    # ----- FUNCTIONS TO CONTROL BACKGROUND MUSIC ----- #
    def play_bgm(self, event=None):
        self.canvas.delete("play")
        pause_audio_img = ImageTk.PhotoImage(file="Buttons/Pause.png")
        self.pause_img = pause_audio_img
        self.pause = self.canvas.create_image(35, 35, image=self.pause_img, tag="pause")
        self.canvas.tag_bind(self.pause, "<Button-1>", self.pause_bgm)
        mixer.music.unpause()
        self.canvas.bind("<Motion>", self.check_hand_on_pauseaudio)

    def pause_bgm(self, event=None):
        self.canvas.delete("pause")
        play_audio_img = ImageTk.PhotoImage(file="Buttons/Play.png")
        self.play_img = play_audio_img
        self.play = self.canvas.create_image(35, 35, image=self.play_img, tag="play")
        self.canvas.tag_bind(self.play, "<Button-1>", self.play_bgm)
        mixer.music.pause()
        self.canvas.bind("<Motion>", self.check_hand_on_playaudio)

    # ----- UPDATE SCORE AND CHAIN ----- #
    def change_score(self, varname, index, mode):
        self.canvas.itemconfigure(self.sc, text=self.scoretxt.get())

    def change_chain(self, varname, index, mode):
        self.canvas.itemconfigure(self.ch, text=self.chaintxt.get())

    # ----- MOUSE OVER FUNCTIONS FOR BUTTON WIDGETS ----- #
    def check_hand_on_start(self, e):  # runs on mouse motion
        bbox = self.canvas.bbox(self.start)
        if bbox[0] < e.x and bbox[2] > e.x and bbox[1] < e.y and bbox[
            3] > e.y:  # checks whether the mouse is inside the boundaries
            self.canvas.config(cursor="hand2")
        else:
            self.canvas.config(cursor="")

    def check_hand_on_playagain(self, e):  # runs on mouse motion
        bbox = self.canvas.bbox(self.playagain)
        if bbox[0] < e.x and bbox[2] > e.x and bbox[1] < e.y and bbox[
            3] > e.y:  # checks whether the mouse is inside the boundaries
            self.canvas.config(cursor="hand2")
        else:
            self.canvas.config(cursor="")

    def check_hand_on_playaudio(self, e):  # runs on mouse motion
        bbox = self.canvas.bbox(self.play)
        if bbox[0] < e.x and bbox[2] > e.x and bbox[1] < e.y and bbox[
            3] > e.y:  # checks whether the mouse is inside the boundaries
            self.canvas.config(cursor="hand2")
        else:
            self.canvas.config(cursor="")

    def check_hand_on_pauseaudio(self, e):  # runs on mouse motion
        bbox = self.canvas.bbox(self.pause)
        if bbox[0] < e.x and bbox[2] > e.x and bbox[1] < e.y and bbox[
            3] > e.y:  # checks whether the mouse is inside the boundaries
            self.canvas.config(cursor="hand2")
        else:
            self.canvas.config(cursor="")

    def resetcursor(self):  # Stops trying to detect mouse movement.
        self.canvas.unbind("<Motion>")
        self.canvas.config(cursor="")

    def pokemon_cry(self):
        if self.pokemon in self.gen1_list:
            path = "Audio/Cries/Gen1/"
        if self.pokemon in self.gen2_list:
            path = "Audio/Cries/Gen2/"
        if self.pokemon == "Farfetchd":
            x = mixer.Sound(path + "Farfetch'd" + ".wav")
        else:
            x = mixer.Sound(path + self.pokemon + ".wav")
        mixer.Sound.set_volume(x, 0.3)
        mixer.Sound.play(x)

    # ----- PROCESSES AND VALIDATES GUESSES ----- #
    def check_answer(self):
        if self.guess == "Farfetch'd":
            self.guess = "Farfetchd"
        if self.guess != self.pokemon:  # If answer is incorrect.
            self.display_colour(window=self.window)
            self.chain = 0
            self.chaintxt.set(self.chain)
            self.chaintxt.trace_variable('w', self.change_chain)
            self.score += -50
            self.scoretxt.set(self.score)
            self.scoretxt.trace_variable('w', self.change_score)
            print(self.score)
            for button in self.button_list:
                button_text = str(button['text'][0]).upper() + \
                                 str(button['text']).lstrip(button['text'][0]).lower()
                if button_text == self.guess:
                    button.configure(bg="#f97a77")
                if button_text == self.pokemon:
                    button.configure(bg="#52c448")
                if button_text != self.pokemon:
                    button.configure(state="disabled")
            self.window.update_idletasks()
            self.pokemon_cry()
            self.incorrect_notification()
            time.sleep(1.5)
            self.select_pokemon()

        if self.guess == self.pokemon:  # If answer is correct.
            self.display_colour(window=self.window)
            self.correct_guesses += 1
            if self.score != 0:
                self.chain += 1
            if self.chain > self.highest_chain:
                self.highest_chain += 1
            self.score += self.chain * 10
            self.chaintxt.set(self.chain)
            self.chaintxt.trace_variable('w', self.change_chain)
            self.score += 100
            self.scoretxt.set(self.score)
            self.scoretxt.trace_variable('w', self.change_score)
            print(self.score)
            for button in self.button_list:
                button_text = str(button['text'][0]).upper() + \
                                 str(button['text']).lstrip(button['text'][0]).lower()
                if button_text == self.guess:
                    button.configure(bg="#52c448")
                else:
                    button.configure(state="disabled")
            self.window.update_idletasks()
            self.pokemon_cry()
            self.correct_notification()
            time.sleep(1.5)
            self.select_pokemon()

    # ----- DISPLAY NOTIFACTIONS ON CORRECT AND INCORRECT GUESSES ----- #
    # Uses my very own SlideUp module! :D
    def correct_notification(self):
        correct_txt = "CORRECT!"
        score_txt = " +" + str(100 + self.chain * 10)
        self.canvas.create_text(175, 250, fill="#ffffff", font=("Pokemon Solid", 30), text=correct_txt, tag="correct")
        self.canvas.create_text(300, 250, fill="#2d9133", font=("Pokemon Solid", 30), text=score_txt, tag="correct")
        self.slideup.get_pos(window=self.window, canvas=self.canvas, tag="correct")

    def incorrect_notification(self):
        correct_txt = "Incorrect!"
        score_txt = " -50"
        self.canvas.create_text(175, 250, fill="#ffffff", font=("Pokemon Solid", 30), text=correct_txt, tag="incorrect")
        self.canvas.create_text(305, 250, fill="#e54242", font=("Pokemon Solid", 30), text=score_txt, tag="incorrect")
        self.slideup.get_pos(window=self.window, canvas=self.canvas, tag="incorrect")

    # ----- DISPLAY END GAME SCREEN STATS ----- #
    def endgame(self):
        end_time = datetime.now()
        self.canvas.delete("all")
        self.canvas.create_image(500, 375, image=self.bg_img)

        finished_img = ImageTk.PhotoImage(file="Buttons/Finished.png")
        fin_img = finished_img
        self.canvas.create_image(500, 100, image=fin_img)

        correct_guesses_txt = "You got " + str(self.correct_guesses) + " out of " + str(self.pokemon_num) + "!"
        self.canvas.create_text(500, 225, fill="#ffd530", font=("Pokemon Solid", 28, "bold"), text=correct_guesses_txt)

        your_score = "Your score: " + self.scoretxt.get()
        self.canvas.create_text(500, 305, fill="#ffd530", font=("Pokemon Solid", 28, "bold"), text=your_score)

        high_chain = "Highest chain: " + str(self.highest_chain)
        self.canvas.create_text(500, 385, fill="#ffd530", font=("Pokemon Solid", 28, "bold"), text=high_chain)

        comp = str(end_time - self.start_time)
        completion_time_txt = comp.split(":", 1)[1].split(".")[0]
        self.canvas.create_text(500, 465, fill="#ffd530", font=("Pokemon Solid", 28, "bold"), text="Completion time: " +
                                                                                                   completion_time_txt)

        playagain_img = ImageTk.PhotoImage(file="Buttons/PlayAgain.png")
        play_img = playagain_img
        self.playagain = self.canvas.create_image(500, 600, image=play_img)
        self.canvas.tag_bind(self.playagain, "<Button-1>", self.easy_mode_start)
        self.canvas.bind("<Motion>", self.check_hand_on_playagain)

        mainloop()


PokeGame()
