import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import END

from chat import a

def start_chat_with_bot():

    global entry_user_message_with_bot, information_with_chat_bot, chat_window
    a = ''
    chat_window = tk.Tk()
    chat_window.title('Chat_With_The_Bot')
    chat_window.geometry('300x100+640+260')
    chat_window.resizable(width = False, height = False)
    chat_window_icon = tk.PhotoImage(file = 'icon/icon_chat.png')
    chat_window.iconphoto(False, chat_window_icon)

    chat_window_style_ttk = ttk.Style()
    chat_window_style_ttk.configure('.', font = ('Arial', 15,))
    chat_window_style_ttk.theme_use('alt')


    def bot_sending_messesage_user():
        
        user_message_with_bot = entry_user_message_with_bot.get()

        if user_message_with_bot == '':

            messagebox.showinfo('Empty Field Entry', 'You Entered The Empty Message')

        else:
            
            information_with_chat_bot.place_forget()
            entry_user_message_with_bot.delete(0, END)
            information_with_chat_bot_next_user_message_with_bot = tk.Label(chat_window, text = a, fg = 'black', font = ('Arial', 12))
            information_with_chat_bot_next_user_message_with_bot.place(x = 10, y = 5)


    information_with_chat_bot = tk.Label(chat_window, text = 'bot: Hello!', fg = 'black', font = ('Arial', 12))
    information_with_chat_bot.place(x = 10, y = 5)

    entry_user_message_with_bot = ttk.Entry(chat_window, width = 30, font = ('Arial', 12))
    entry_user_message_with_bot.place(x = 12, y = 35)

    button_continue_chat = ttk.Button(chat_window, text = 'Send Message For The Bot', width = 23, command = bot_sending_messesage_user)
    button_continue_chat.place(x = 80, y = 68)


    chat_window.mainloop()


start_chat_with_bot()