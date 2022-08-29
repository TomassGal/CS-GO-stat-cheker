import ui
import steam_api
import data_converter
from tkinter import *
from tkinter import messagebox



def get_data(steam_link):
    '''
    Input: players steam link
    Output: "data" and "name" in a dictionary
    '''
    steamid = steam_api.get_steamid(steam_link)
    if steamid == None:
        messagebox.showerror(title="This user does not exist", message="The given steam link was invalid.")
        return None

    name = steam_api.get_player_name(steamid)
    if name == None:
        messagebox.showerror(title="This user does not exist", message="The given steam link was invalid.")
        return None

    data_json = steam_api.get_stats(steamid)

    if data_json == None:
        return {"name": name, "data": None}

    data = data_converter.convert_user_data(data_json)
    return{"name": name, "data": data}

def new_player_window():
    '''
    Input: None (gets steam link from player_link_input)
    Output: None (Creates a new player data window)
    '''
    player_data = get_data(player_link_input.get())
    if player_data == None:
        return
    ui.player_ui(player_data["data"], player_data["name"], window, small_backround_image)

def new_player_window_link(link):
    '''
    Input: Players steam link
    Output: None (Creates a new player data window)
    '''
    user_data = get_data(link)
    ui.player_ui(user_data["data"], user_data["name"], window, small_backround_image)

def new_compare_window():
    '''
    Input: None (gets steam links from player_link_input and user_link_input)
    Output: None (Creates a new player compare data window)
    '''
    player_data = get_data(player_link_input.get())
    user_data = get_data(user_link_input.get())
    ui.compare_ui(user_data["data"], user_data["name"],player_data["data"], player_data["name"], window, big_backround_image)

def new_saved_users_window():
    ui.saved_users_window(window, new_player_window_link)

def save_active_user():
    '''
    Input: None
    Output: None (Creates a new saved player window)
    '''
    with open("data\\active_user.txt", "w") as file:
        file.write(user_link_input.get())

def get_saved_active_user():
    '''
    Input: None
    Output: Last active users steam link
    '''
    try:
        with open(".\\data\\active_user.txt", "r") as file:
            user = file.read()
        return user
    except FileNotFoundError:
        return ""

def save_new_user():
    '''
    Input: None (Gets steam link from user_link_input)
    Output: None (Adds steam link to saved users and active user)
    '''
    if get_data(user_link_input.get()) == None:
        return
    users = data_converter.get_saved_users()
    for user in users:
        with open(f".\\data\\saved_users\\{user}") as file:
            link = file.readline()
            if link == user_link_input.get():
                messagebox.showerror(title="This user already exist", message="This user has already been saved.")
                return
    with open(f".\\data\\saved_users\\{steam_api.get_steamid(user_link_input.get())}.txt", "w") as file:
        file.write(user_link_input.get())
    messagebox.showinfo(title="User saved", message="User has been successfully saved")
    save_active_user()

#-----------------------------------UI----------------------------------#

window = Tk()

backround_image = PhotoImage(file="resources\\backround.png")
small_backround_image = PhotoImage(file="resources\\small_backround.png")
big_backround_image = PhotoImage(file="resources\\big_backround.png")

window.config(bg="#4A4A4A")
window.geometry("700x160")
window.title("CS:GO Stats")
window.iconbitmap("resources\\csgo_93786.ico")
window.minsize(width=700, height=160)
window.maxsize(width=700, height=160)

image_canvas = Canvas(width=700, height=160, borderwidth=0, highlightthickness=0)
image_canvas.create_image(350, 80, image=backround_image)
image_canvas.place(x=0,y=0)

user_link_text = Label(text="Your Steam proflie link: ", font=("Arial", 12))
user_link_text.config(bg="#4b4b4b", fg="#FF9700")
user_link_text.place(x=20, y=25)

user_link_input_border = Frame(window, highlightbackground="black", highlightthickness=2, bd=0)

user_link_input = Entry(user_link_input_border, width=55, font=("Arial", 8))
user_link_input_border.place(x=190, y=30)
user_link_input.config(bg="#C27300", borderwidth=0)
user_link_input.insert(0, get_saved_active_user())
user_link_input.pack()

user_save_button_border = Frame(window, highlightbackground="black", highlightthickness=2, bd=0)

user_save_button = Button(user_save_button_border, text="Save", font=("Arial", 10), command=save_new_user, padx=12, pady=2)
user_save_button.config(bg="#C27300", borderwidth=0)
user_save_button_border.place(x=532, y=25)
user_save_button.pack()

saved_users_button_border = Frame(window, highlightbackground="black", highlightthickness=2, bd=0)

saved_users_button = Button(saved_users_button_border, text="Saved users", font=("Arial", 10), command=new_saved_users_window, padx=4, pady=2)
saved_users_button_border.place(x=605, y=25)
saved_users_button.config(bg="#C27300", borderwidth=0)
saved_users_button.pack()

player_link_text = Label(text="Steam proflie link: ", font=("Arial", 12))
player_link_text.config(bg="#4b4b4b", fg="#FF9700")
player_link_text.place(x=20, y=90)

player_link_input_border = Frame(window, highlightbackground="black", highlightthickness=2, bd=0)

player_link_input = Entry(player_link_input_border, width=55, font=("Arial", 8))
player_link_input.config(bg="#C27300", borderwidth=0)
player_link_input_border.place(x=190, y=95)
player_link_input.pack()

player_search_button_border = Frame(window, highlightbackground="black", highlightthickness=2, bd=0)

player_search_button = Button(player_search_button_border, text="Search", font=("Arial", 10), command=new_player_window, padx=6, pady=2)
player_search_button.config(bg="#C27300", borderwidth=0)
player_search_button_border.place(x=532, y=90)
player_search_button.pack()

compare_button_border = Frame(window, highlightbackground="black", highlightthickness=2, bd=0)

compare_button = Button(compare_button_border, text="Compare", font=("Arial", 10), command=new_compare_window, padx=13, pady=2)
compare_button.config(bg="#C27300", borderwidth=0)
compare_button_border.place(x=605, y=90)
compare_button.pack()

window.mainloop()