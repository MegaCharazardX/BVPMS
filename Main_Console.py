from customtkinter import *
from subprocess import call
from PIL import Image
import os
import sqlite3
from tkinter import messagebox
from Global_Config import *

root = CTk()

print("\u0332 Hello")

global glb_color_1, glb_color_2, glb_color_3, glb_current_working_directory

glb_current_working_directory = os.path.dirname(os.path.realpath(__file__))
glb_color_1 = "darkorchid2"# #FFC125 #FFCC70
glb_color_2 = "dodgerblue3"
glb_color_3 = "#308014"# darkorchid2, #308014 #c850c0
welcome_text = "WELCOME"
Console_width = 500
Console_height = 400

centreScreen(root, root,Console_width,Console_height)
root.title("Barathya Vidhya Peedom Login")
root.maxsize(width = Console_width, height = Console_height)

#root.iconbitmap(r"icon/favicon6.ico")
set_appearance_mode("Dark")

def redirect_to_user(_isadmin = False):
    if _isadmin == 'Teacher':
        root.destroy()
        call(["python", glb_current_working_directory + "/Animal_Taxonamy_Ctk_Main.py"])


main_frame = CTkFrame(root, border_color = glb_color_1, border_width = 2, width = Console_width, height = Console_height)

welcome_message = CTkLabel(main_frame, text = "Barathya Vidhya Peedom \nCentral School", font = ("Brush Script MT" , 50, "italic" ))
welcome_message.place(x = 45, y = 100)

# welcome_message = CTkLabel(main_frame, text = "To the world of animals", font = ("Brush Script MT" , 18, "italic" ))
# welcome_message.place(x = (600/2-len(welcome_text)//2)-50, y = 280)

teacher_mode_btn = CTkButton(main_frame, text = "Login as a Teacher", fg_color = glb_color_2,hover_color = glb_color_3,corner_radius = 35,
                               width = 240, command = lambda :(redirect_to_user("Teacher")))
teacher_mode_btn.place(x = 140, y = 250)

admin_mode_btn = CTkButton(main_frame, text = "Login as a Admin", fg_color = glb_color_2,hover_color = glb_color_3,corner_radius = 35,
                                width = 240,command = lambda :(redirect_to_user(True)))
admin_mode_btn.place(x = 140, y = 300)

create_login_btn = CTkButton(main_frame, text = "Create Login", fg_color = "#2b2b2b",corner_radius = 35,
                                width = 240,command = lambda :(redirect_to_user("Create")))
create_login_btn.place(x = 140, y = 350)


main_frame.place(x = 0, y = 0)


root.mainloop()