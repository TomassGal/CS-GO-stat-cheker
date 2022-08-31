
from tkinter import *
from data_converter import get_saved_users
import steam_api
from tkinter import ttk

small_bakcround_image = None
big_backround_image = None
#----------------------------------SET UP-------------------------------------------#
def set_up(small_image, big_image):
    global small_bakcround_image
    global big_backround_image
    small_bakcround_image = small_image
    big_backround_image = big_image

#----------------------------------PLAYER UI----------------------------------------#

def player_ui(data, player_name, window):
    player_window = Toplevel(window)

    player_window.iconbitmap(".\\resources\\csgo_93786.ico")
    player_window.geometry("500x600")
    player_window.title(f"{player_name}'s CS:GO stats")
    player_window.minsize(width=500, height=600)
    player_window.maxsize(width=500, height=600)

    player_image_canvas = Canvas(player_window, width=500, height=600, borderwidth=0, highlightthickness=0)
    player_image_canvas.create_image(250, 300, image=small_bakcround_image)
    player_image_canvas.place(x=0,y=0)
    

    if data == None:
        error_text = Label(player_window, text=f"{player_name} has set their game stats to private.", font=("Arial", 12))
        error_text.place(x=120, y=50)
        return

    user_title = Label(player_window, text=f"{player_name}'s stats:", font=("Arial", 18, "bold"))
    user_title.place(x=160, y=50)
    user_title.config(bg="#6d2c00", fg="#31ded5")
    
    kd_text = Label(player_window, text=f"KD: {data['kd']}", font=("Arial", 12))
    kd_text.place(x=120, y=100)
    kd_text.config(bg="#6d2c00", fg="#31ded5")

    winrate_text = Label(player_window, text=f"Winrate: {data['winrate']}%", font=("Arial", 12))
    winrate_text.place(x=120, y=150)
    winrate_text.config(bg="#6d2c00", fg="#31ded5")

    accuracy_text = Label(player_window, text=f"Accuracy: {data['accuracy']}%", font=("Arial", 12))
    accuracy_text.place(x=120, y=200)
    accuracy_text.config(bg="#6d2c00", fg="#31ded5")

    headshots_text = Label(player_window, text=f"Headshot rate: {data['headshots']}%", font=("Arial", 12))
    headshots_text.place(x=120, y=250)
    headshots_text.config(bg="#6d2c00", fg="#31ded5")

    mvps_text = Label(player_window, text=f"Mvp rate: {data['mvps']}%", font=("Arial", 12))
    mvps_text.place(x=120, y=300)
    mvps_text.config(bg="#6d2c00", fg="#31ded5")

    total_matches_text = Label(player_window, text=f"Total matches played: {data['total_matches_played']}", font=("Arial", 12))
    total_matches_text.place(x=120,y=350)
    total_matches_text.config(bg="#6d2c00", fg="#31ded5")

    play_time_text = Label(player_window, text=f"Total time played: {data['total_time_played']}h", font=("Arial", 12))
    play_time_text.place(x=120, y=400)
    play_time_text.config(bg="#6d2c00", fg="#31ded5")

    last_game_button_border = Frame(player_window, highlightbackground="black", highlightthickness=2, bd=0)

    last_game_button = Button(last_game_button_border, text="Last games performance", font=("Arial", 10), command=lambda m={"data": data, "name": player_name, "window": player_window}: last_game_window(m) , padx=6, pady=2)
    last_game_button_border.place(x=165, y=450)
    last_game_button.config(bg="#C27300", borderwidth=0)
    last_game_button.pack()




#----------------------------------------COMPARE UI-----------------------------------------#

def compare_ui(user_data, user_name, player_data, player_name, window):
    compare_window = Toplevel(window)

    compare_window.iconbitmap(".\\resources\\csgo_93786.ico")
    compare_window.geometry("1000x600")
    compare_window.title(f"Your and {player_name}'s CS:GO stats")
    compare_window.minsize(width=1000, height=600)
    compare_window.maxsize(width=1000, height=600)

    player_image_canvas = Canvas(compare_window, width=1000, height=600, borderwidth=0, highlightthickness=0)
    player_image_canvas.create_image(500, 300, image=big_backround_image)
    player_image_canvas.place(x=0,y=0)

    if user_data == None:
        error_text = Label(compare_window, text=f"{player_name} has set their game stats to private, cant compare stats.", font=("Arial", 12))
        error_text.place(x=50, y=50)
        return
    if player_data == None:
        error_text = Label(compare_window, text="You have set your game stats to private, cant compare stats.", font=("Arial", 12))
        error_text.place(x=50, y=50)
        return
    
    #-------------------------------------USERS UI------------------------------------#

    user_title = Label(compare_window, text="Your stats:", font=("Arial", 18, "bold"), bg="#6d2c00", fg="#31ded5")
    user_title.place(x=160, y=45)

    user_kd_text = Label(compare_window, text=f"KD: {user_data['kd']}", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    user_kd_text.place(x=120, y=120)

    user_winrate_text = Label(compare_window, text=f"Winrate: {user_data['winrate']}%", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    user_winrate_text.place(x=120, y=170)

    user_accuracy_text = Label(compare_window, text=f"Accuracy: {user_data['accuracy']}%", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    user_accuracy_text.place(x=120, y=220)

    user_headshots_text = Label(compare_window, text=f"Headshot rate: {user_data['headshots']}%", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    user_headshots_text.place(x=120, y=270)

    user_mvps_text = Label(compare_window, text=f"Mvp rate: {user_data['mvps']}%", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    user_mvps_text.place(x=120, y=320)

    user_total_matches_text = Label(compare_window, text=f"Total matches played: {user_data['total_matches_played']}", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    user_total_matches_text.place(x=120,y=370)

    user_play_time_text = Label(compare_window, text=f"Total time played: {user_data['total_time_played']}h", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    user_play_time_text.place(x=120, y=420)

    user_last_game_button_border = Frame(compare_window, highlightbackground="black", highlightthickness=2, bd=0)

    user_last_game_button = Button(user_last_game_button_border, text="Last games performance", font=("Arial", 10), command=lambda m={"data": user_data, "name": user_name, "window": compare_window}: last_game_window(m) , padx=6, pady=2)
    user_last_game_button_border.place(x=165, y=470)
    user_last_game_button.config(bg="#C27300", borderwidth=0)
    user_last_game_button.pack()

    #-----------------------------------PLAYERS UI-------------------------------------#

    player_title = Label(compare_window, text=f"{player_name}'s stats:", font=("Arial", 18, "bold"), bg="#6d2c00", fg="#31ded5")
    player_title.place(x=660, y=45)

    players_kd_text = Label(compare_window, text=f"KD: {player_data['kd']}", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    players_kd_text.place(x=620, y=120)

    player_winrate_text = Label(compare_window, text=f"Winrate: {player_data['winrate']}%", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    player_winrate_text.place(x=620, y=170)

    player_accuracy_text = Label(compare_window, text=f"Accuracy: {player_data['accuracy']}%", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    player_accuracy_text.place(x=620, y=220)

    player_headshots_text = Label(compare_window, text=f"Headshot rate: {player_data['headshots']}%", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    player_headshots_text.place(x=620, y=270)

    player_mvps_text = Label(compare_window, text=f"Mvp rate: {player_data['mvps']}%", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    player_mvps_text.place(x=620, y=320)

    player_total_matches_text = Label(compare_window, text=f"Total matches played: {player_data['total_matches_played']}", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    player_total_matches_text.place(x=620,y=370)

    player_play_time_text = Label(compare_window, text=f"Time played: {player_data['total_time_played']}h", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    player_play_time_text.place(x=620, y=420)

    player_last_game_button_border = Frame(compare_window, highlightbackground="black", highlightthickness=2, bd=0)

    player_last_game_button = Button(player_last_game_button_border, text="Last games performance", font=("Arial", 10), command=lambda m={"data": player_data, "name": player_name, "window": compare_window}: last_game_window(m) , padx=6, pady=2)
    player_last_game_button_border.place(x=665, y=470)
    player_last_game_button.config(bg="#C27300", borderwidth=0)
    player_last_game_button.pack()

    #--------------------------------------------------COLORS--------------------------------------#

    if(user_data['kd'] > player_data['kd']):
        user_kd_text.config(font=("Arial", 14, "bold"), fg="#31ede1")
    elif(user_data['kd'] < player_data['kd']):
        players_kd_text.config(font=("Arial", 14, "bold"), fg="#31ede1")

    if(user_data['winrate'] > player_data['winrate']):
        user_winrate_text.config(font=("Arial", 14, "bold"), fg="#31ede1")
    elif(user_data['winrate'] < player_data['winrate']):
        player_winrate_text.config(font=("Arial", 14, "bold"), fg="#31ede1")

    if(user_data['accuracy'] > player_data['accuracy']):
        user_accuracy_text.config(font=("Arial", 14, "bold"), fg="#31ede1")
    elif(user_data['accuracy'] < player_data['accuracy']):
        player_accuracy_text.config(font=("Arial", 14, "bold"), fg="#31ede1")

    if(user_data['headshots'] > player_data['headshots']):
        user_headshots_text.config(font=("Arial", 14, "bold"))
    elif(user_data['headshots'] < player_data['headshots']):
        player_headshots_text.config(font=("Arial", 14, "bold"))

    if(user_data['mvps'] > player_data['mvps']):
        user_mvps_text.config(font=("Arial", 14, "bold"))
    elif(user_data['mvps'] < player_data['mvps']):
        player_mvps_text.config(font=("Arial", 14, "bold"))

#-------------------------LAST GAME UI------------------------------------#
def last_game_window(info):
    window = info["window"]
    name = info["name"]
    data = info["data"]

    last_game_window = Toplevel(window)

    last_game_window.iconbitmap(".\\resources\\csgo_93786.ico")
    last_game_window.geometry("500x600")
    last_game_window.title(f"{name}'s last game performance")
    last_game_window.minsize(width=500, height=600)
    last_game_window.maxsize(width=500, height=600)

    last_game_image_canvas = Canvas(last_game_window, width=500, height=600, borderwidth=0, highlightthickness=0)
    last_game_image_canvas.create_image(250, 300, image=small_bakcround_image)
    last_game_image_canvas.place(x=0,y=0)

    player_title = Label(last_game_window, text=f"Last game stats:", font=("Arial", 18, "bold"), bg="#6d2c00", fg="#31ded5")
    player_title.place(x=160, y=65)
    
    score_title = Label(last_game_window, font=("Arial", 12))
    if data["last_match_wins"] > data["last_match_loses"]:
        score_title.config(text=f"WIN ({data['last_match_wins']}:{data['last_match_loses']})", fg="green", bg="#6d2c00")
    elif data["last_match_wins"] < data["last_match_loses"]:
        score_title.config(text=f"LOSS ({data['last_match_wins']}:{data['last_match_loses']})", fg="red", bg="#6d2c00")
    else:
        score_title.config(text=f"TIE ({data['last_match_wins']}:{data['last_match_loses']})",bg="#6d2c00", fg="#31ded5")
    score_title.place(x=120, y=140)

    kills_title = Label(last_game_window, text=f"Kills: {data['last_match_kills']}", font=("Arial",12), bg="#6d2c00", fg="#31ded5")
    kills_title.place(x=120,y=190)

    kd_title = Label(last_game_window, text=f"KD: {data['last_match_kd']}",font=("Arial",12), bg="#6d2c00", fg="#31ded5")
    kd_title.place(x=120, y=240)

    player_score_title = Label(last_game_window, text=f"Score: {data['last_match_score']}", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    player_score_title.place(x=120,y=290)

    adr_title = Label(last_game_window, text=f"ADR: {data['last_match_adr']}", font=("Arial",12), bg="#6d2c00", fg="#31ded5")
    adr_title.place(x=120, y=340)

    fav_wapon_title = Label(last_game_window, text=f"Favorite weapon: {data['last_match_fav_weapon']}",font=("Arial",12), bg="#6d2c00", fg="#31ded5")
    fav_wapon_title.place(x=120,y=390)

#----------------------------------------SAVED USERS UI-----------------------------------#

def saved_users_window(window, function):
    saved_window = Toplevel(window)
    saved_window.config(background="#1e2121")

    users = get_saved_users()
    window_height = (round(len(users)/4) + 1) * 130

    saved_window.iconbitmap(".\\resources\\csgo_93786.ico")
    saved_window.geometry(f"550x{window_height}")
    saved_window.title("Saved users")
    saved_window.minsize(width=550, height=window_height)
    saved_window.maxsize(width=550, height=window_height)


    x_cord = 30
    y_cord = 30
    count = 0

    for user in users:
        with open(f".\\data\\saved_users\\{user}") as file:
            link = file.readline().replace("\n", "")
            name = file.readline()
        name = steam_api.get_player_name(steam_api.get_steamid(link))

        user_save_button_border = Frame(saved_window, highlightbackground="black", highlightthickness=2, bd=0)

        user_save_button = Button(user_save_button_border, text=name, font=("Arial", 10), command=lambda m={"link":link,"window":saved_window}:function(m) , padx=12, pady=2)
        user_save_button.config(bg="#C27300", borderwidth=0)
        user_save_button_border.place(x=x_cord, y=y_cord)
        user_save_button.pack()
        x_cord +=100
        count+=1
        if count == 4:
            y_cord += 100
            x_cord=30
            count = 0

#----------------------------------------SPECILIZED PLAYER UI-----------------------------------------------#
def spec_player_ui(data, player_name, window,  file_name, tracking_function, compare_function):
    player_window = Toplevel(window)

    player_window.iconbitmap(".\\resources\\csgo_93786.ico")
    player_window.geometry("500x600")
    player_window.title(f"{player_name}'s CS:GO stats")
    player_window.minsize(width=500, height=600)
    player_window.maxsize(width=500, height=600)

    player_image_canvas = Canvas(player_window, width=500, height=600, borderwidth=0, highlightthickness=0)
    player_image_canvas.create_image(250, 300, image=small_bakcround_image)
    player_image_canvas.place(x=0,y=0)
    

    if data == None:
        error_text = Label(player_window, text=f"{player_name} has set their game stats to private.", font=("Arial", 12))
        error_text.place(x=120, y=50)
        return

    user_title = Label(player_window, text=f"{player_name}'s stats:", font=("Arial", 18, "bold"))
    user_title.place(x=160, y=50)
    user_title.config(bg="#6d2c00", fg="#31ded5")
    
    kd_text = Label(player_window, text=f"KD: {data['kd']}", font=("Arial", 12))
    kd_text.place(x=120, y=100)
    kd_text.config(bg="#6d2c00", fg="#31ded5")

    winrate_text = Label(player_window, text=f"Winrate: {data['winrate']}%", font=("Arial", 12))
    winrate_text.place(x=120, y=150)
    winrate_text.config(bg="#6d2c00", fg="#31ded5")

    accuracy_text = Label(player_window, text=f"Accuracy: {data['accuracy']}%", font=("Arial", 12))
    accuracy_text.place(x=120, y=200)
    accuracy_text.config(bg="#6d2c00", fg="#31ded5")

    headshots_text = Label(player_window, text=f"Headshot rate: {data['headshots']}%", font=("Arial", 12))
    headshots_text.place(x=120, y=250)
    headshots_text.config(bg="#6d2c00", fg="#31ded5")

    mvps_text = Label(player_window, text=f"Mvp rate: {data['mvps']}%", font=("Arial", 12))
    mvps_text.place(x=120, y=300)
    mvps_text.config(bg="#6d2c00", fg="#31ded5")

    total_matches_text = Label(player_window, text=f"Total matches played: {data['total_matches_played']}", font=("Arial", 12))
    total_matches_text.place(x=120,y=350)
    total_matches_text.config(bg="#6d2c00", fg="#31ded5")

    play_time_text = Label(player_window, text=f"Total time played: {data['total_time_played']}h", font=("Arial", 12))
    play_time_text.place(x=120, y=400)
    play_time_text.config(bg="#6d2c00", fg="#31ded5")

    last_game_button_border = Frame(player_window, highlightbackground="black", highlightthickness=2, bd=0)

    last_game_button = Button(last_game_button_border, text="Last games performance", font=("Arial", 10), command=lambda m={"data": data, "name": player_name, "window": player_window}: last_game_window(m) , padx=6, pady=2)
    last_game_button_border.place(x=165, y=450)
    last_game_button.config(bg="#C27300", borderwidth=0)
    last_game_button.pack()

    start_tracking_button_border = Frame(player_window, highlightbackground="black", highlightthickness=2, bd=0)

    start_tracking_button = Button(start_tracking_button_border, text="Start tracking", font=("Arial", 8), command=lambda m=file_name: tracking_function(m) , padx=6, pady=2)
    start_tracking_button_border.place(x=125, y=485)
    start_tracking_button.config(bg="#C27300", borderwidth=0)
    start_tracking_button.pack()

    compare_button_border = Frame(player_window, highlightbackground="black", highlightthickness=2, bd=0)

    compare_button = Button(compare_button_border, text="Compare past", font=("Arial", 8), command=lambda m=file_name: compare_function(m) , padx=6, pady=2)
    compare_button_border.place(x=275, y=485)
    compare_button.config(bg="#C27300", borderwidth=0)
    compare_button.pack()

#--------------------------------------------COMPARE HISTORY--------------------------------------#
def compare_history_ui(user_data, user_past_data, date, window):
    compare_window = Toplevel(window)

    compare_window.iconbitmap(".\\resources\\csgo_93786.ico")
    compare_window.geometry("1000x600")
    compare_window.title(f"Your {date} CS:GO stats")
    compare_window.minsize(width=1000, height=600)
    compare_window.maxsize(width=1000, height=600)

    player_image_canvas = Canvas(compare_window, width=1000, height=600, borderwidth=0, highlightthickness=0)
    player_image_canvas.create_image(500, 300, image=big_backround_image)
    player_image_canvas.place(x=0,y=0)

    
    #-------------------------------------USERS UI------------------------------------#

    user_title = Label(compare_window, text="Your stats:", font=("Arial", 18, "bold"), bg="#6d2c00", fg="#31ded5")
    user_title.place(x=160, y=45)

    user_kd_text = Label(compare_window, text=f"KD: {user_data['kd']}", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    user_kd_text.place(x=120, y=120)

    user_winrate_text = Label(compare_window, text=f"Winrate: {user_data['winrate']}%", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    user_winrate_text.place(x=120, y=170)

    user_accuracy_text = Label(compare_window, text=f"Accuracy: {user_data['accuracy']}%", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    user_accuracy_text.place(x=120, y=220)

    user_headshots_text = Label(compare_window, text=f"Headshot rate: {user_data['headshots']}%", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    user_headshots_text.place(x=120, y=270)

    user_mvps_text = Label(compare_window, text=f"Mvp rate: {user_data['mvps']}%", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    user_mvps_text.place(x=120, y=320)

    user_total_matches_text = Label(compare_window, text=f"Total matches played: {user_data['total_matches_played']}", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    user_total_matches_text.place(x=120,y=370)

    user_play_time_text = Label(compare_window, text=f"Total time played: {user_data['total_time_played']}h", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    user_play_time_text.place(x=120, y=420)

    #-----------------------------------PLAYERS UI-------------------------------------#

    player_title = Label(compare_window, text=f"{date} stats:", font=("Arial", 18, "bold"), bg="#6d2c00", fg="#31ded5")
    player_title.place(x=660, y=45)

    players_kd_text = Label(compare_window, text=f"KD: {user_past_data['kd']}", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    players_kd_text.place(x=620, y=120)

    player_winrate_text = Label(compare_window, text=f"Winrate: {user_past_data['winrate']}%", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    player_winrate_text.place(x=620, y=170)

    player_accuracy_text = Label(compare_window, text=f"Accuracy: {user_past_data['accuracy']}%", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    player_accuracy_text.place(x=620, y=220)

    player_headshots_text = Label(compare_window, text=f"Headshot rate: {user_past_data['headshots']}%", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    player_headshots_text.place(x=620, y=270)

    player_mvps_text = Label(compare_window, text=f"Mvp rate: {user_past_data['mvps']}%", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    player_mvps_text.place(x=620, y=320)

    player_total_matches_text = Label(compare_window, text=f"Total matches played: {user_past_data['total_matches_played']}", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    player_total_matches_text.place(x=620,y=370)

    player_play_time_text = Label(compare_window, text=f"Time played: {user_past_data['total_time_played']}h", font=("Arial", 12), bg="#6d2c00", fg="#31ded5")
    player_play_time_text.place(x=620, y=420)


    #--------------------------------------------------COLORS--------------------------------------#

    if(user_data['kd'] > user_past_data['kd']):
        user_kd_text.config(font=("Arial", 14, "bold"), fg="#31ede1")
    elif(user_data['kd'] < user_past_data['kd']):
        players_kd_text.config(font=("Arial", 14, "bold"), fg="#31ede1")

    if(user_data['winrate'] > user_past_data['winrate']):
        user_winrate_text.config(font=("Arial", 14, "bold"), fg="#31ede1")
    elif(user_data['winrate'] < user_past_data['winrate']):
        player_winrate_text.config(font=("Arial", 14, "bold"), fg="#31ede1")

    if(user_data['accuracy'] > user_past_data['accuracy']):
        user_accuracy_text.config(font=("Arial", 14, "bold"), fg="#31ede1")
    elif(user_data['accuracy'] < user_past_data['accuracy']):
        player_accuracy_text.config(font=("Arial", 14, "bold"), fg="#31ede1")

    if(user_data['headshots'] > user_past_data['headshots']):
        user_headshots_text.config(font=("Arial", 14, "bold"))
    elif(user_data['headshots'] < user_past_data['headshots']):
        player_headshots_text.config(font=("Arial", 14, "bold"))

    if(user_data['mvps'] > user_past_data['mvps']):
        user_mvps_text.config(font=("Arial", 14, "bold"))
    elif(user_data['mvps'] < user_past_data['mvps']):
        player_mvps_text.config(font=("Arial", 14, "bold"))
