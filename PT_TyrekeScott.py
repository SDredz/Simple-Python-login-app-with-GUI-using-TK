'''
Author: Tyreke Scott
Date: March 31, 2021
Purpose: To create a program that has a simple GUI interface, using tkinter
blue: 0059FF
grey: C6C1B9
'''

# Imported libraries
import os
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox

def log_in():
    # Here I make the needed variables in this function global. Why is it a fucntion?
    # Well it's the only way I could get the main hub page to go back to the login page.....aka logout...
    # IDK why I wanted that.
    '''Update it works now, I think by declearing the varibles that I would've used literally everywhere else
    as global while setting the main window into a function then calling that function after, it would work as
    if it was not in a function. even though it is. Now that I've done that I can now "logout" or rather go back
    to the login screen..... not sure if it is actually logged though......... tbh I think I need to go to sleep
    it's currently "11:27 PM April 11, 2021" and this final assignment doesn't need some of this ...... i think...'''
    global myframe, acc_info  

    # Created a window to place my GUI items, and added a title
    
    acc_info = { }
    myframe = Tk()
    myframe.geometry("500x250+400+200")
    myframe.resizable(False, False)
    myframe.title("Sython Hub")
    myframe["background"] = "#000000"
    head = Label(myframe, text = "Welcome to the Sython Hub", fg = "#136E7C", bg = "#000000", font = "SegoeUI 18")
    head.place(x=90, y=10)

    # This allows the user to log into the hub
    login_page()

    myframe.mainloop()



# Here to allow the user to exit the program
def exit_sy(event):
    exit()



'''====================================================
This is the interface for the main login page 
===================================================='''
def login_page():
    global log_stat, enter_username, username, enter_password, password

    # This is the format for the textbox
    username = StringVar()
    password = StringVar()

    # This is for the username entry box
    Label(myframe, bg = "#000000", fg = "#FFFD72", text = "Username").place(x=215, y=70)
    enter_username = Entry(myframe, bg = "#C3F1F8", width = 25, textvariable = username)
    enter_username.place(x=180, y=100)

    # This is for the password entry box
    Label(myframe, bg = "#000000", fg = "#FFFD72", text = "Password").place(x=220, y=130)
    enter_password = Entry(myframe, bg = "#C3F1F8", width = 25, show = "*", textvariable = password)
    enter_password.place(x=180, y=150)

    enter_username.focus()
    enter_password.focus()

    # This is for the login button on the interface
    login_button = Button(myframe,fg = "#FFFD72", bg = "#000000", text = "login", command = login_check)
    login_button.place(x=230, y=175)

    # Login status
    log_stat = Label(myframe, bg = "#000000", fg = "#FFFD72", text = "")
    #log_stat.pack(y=200)
    log_stat.place(y=200)#(x=230, 

    # This is for the hyperlink for signing up in the  interface
    new_reg = Label(myframe, text = "New to Sython? Create an account here!", fg = "#AAFFFB", bg = "#000000", cursor = "hand2")
    new_reg.place(x=0, y=230)
    new_reg.bind("<Button-1>", signup_new)



# Start of the login function
def login_check():
    log_stat.config(text="loading..", bg = "#000000")

    if username.get() == "":
        messagebox.showinfo("Sython Hub", "Please enter a username.")

    else:
        if password.get() == "":
            messagebox.showinfo("Sython Hub", "Please enter a password.")

        else:
            login_checking()
    


# Part 2 of the login check
def login_checking():
    global user

    # retriving the required info
    '''This line in particular allows me to retrive the username and use it to navigate the
    account files when I automatically save them by the username in the files' name'''
    user = username.get()

    # Open the file location where the user information is stored
    listdr_files = open(f"account_data/{user}_accounts.txt", "r")


    # Making the login verification conditions
    try:
        # checking the username with the file data already stored
        for line in listdr_files:
            
            if(':' in line):
                key,value = line.split(':',1)
                tempvalue = len(value)-1
                value = value[0:tempvalue]
                acc_info[key]=value
            
            else:
                pass
        

        # Retriving the information form the dictionaries that are stored within the text file
        save_username = acc_info.get('username')
        save_passw = acc_info.get('password')
        

        if save_username == enter_username.get():
            # Deleting the entry box after login
            username.set("")
            

            if save_passw == enter_password.get():
                # Deleting the entry box after login
                password.set("")
                myframe.destroy()
                sy_hub_main()
            
            
            # Stating to the user that the password might be incorrect
            else:
                log_stat.config(text="Password not recognised", bg = "#000000")

        # Stating to the user that the username entered is incorrect
        else:
            log_stat.config(text="Username not recognised", bg = "#000000")
    

    # This is if for some reason the something else happens and the above code does not work......
    except ValueError:
        log_stat.config(text = "Error please try again", bg = "#000000")



'''====================================================
This is the interface for the sign up page 
===================================================='''
def signup_new(event):
    global mainframe_signup
    global username_new, username_sign, passw_new, passw_sign, fonenum_new, fonenum_sign, email_adr_new, email_adr_sign

    mainframe_signup = Toplevel()
    fonenum_new = StringVar()
    username_new = StringVar()
    passw_new = StringVar()
    email_adr_new = StringVar()
    mainframe_signup.title("User Registration")
    mainframe_signup.geometry("500x325+400+200")
    mainframe_signup["background"] = "#000000"

    # The heading for user the window title
    Label(mainframe_signup, text = "Create a Sython Hub \n Account", fg = "#136E7C", bg = "#000000", font = "SegoeUI 18").place(x=120, y=10)

    # The username register entry box
    Label(mainframe_signup, bg = "#000000", fg = "#FFFD72", text = "Username").place(x=215, y=70)
    username_sign = Entry(mainframe_signup, bg = "#C3F1F8", width = 25, textvariable = username_new)
    username_sign.place(x=180, y=100)

    # The password register entry box
    Label(mainframe_signup, bg = "#000000", fg = "#FFFD72", text = "Email").place(x=220, y=130)
    email_adr_sign = Entry(mainframe_signup, bg = "#C3F1F8", width = 25, textvariable = email_adr_new)
    email_adr_sign.place(x=180, y=150)

    # The phone number entry box
    Label(mainframe_signup, bg = "#000000", fg = "#FFFD72", text = "Phone").place(x=220, y=180)
    fonenum_sign = Entry(mainframe_signup, bg = "#C3F1F8", width = 25, textvariable = fonenum_new)
    fonenum_sign.place(x=180, y=200)

    # The email entry box
    Label(mainframe_signup, bg = "#000000", fg = "#FFFD72", text = "Password").place(x=220, y=230)
    passw_sign = Entry(mainframe_signup, bg = "#C3F1F8", width = 25, textvariable = passw_new)
    passw_sign.place(x=180, y=250)

    # The button to save/register the new user
    register_button = Button(mainframe_signup, fg = "#FFFD72", bg = "#000000", text = "save", command = create_acc)
    register_button.place(x=230, y=275)

    # This is for the hyperlink for signing up in the  interface
    new_reg = Label(mainframe_signup, text = "<-- Back to Login page", fg = "#AAFFFB",bg = "#000000", cursor = "hand2")
    new_reg.place(x=0, y=300)
    new_reg.bind("<Button-1>", return_to_home)

    mainloop()



def create_acc():
    global acc_info
    # Getting the needed info-
    '''This line allows me to save retrive the  inputted username to use it to organize and
    save multiple accounts in a orderly way'''
    user = username_sign.get()

    # (4/11/2021. 11:36pm) This is where I start to create the dictionary to save the account info to. Just below
    # This comment I retrive the input information from the user.
    # ...... (!Personal note!)btw Mi juss notice seh di line weh 'phone' deh a wah comment.......wi nuh fi ave fone numba and address tuh?.
    # Mi afi guh ad ih bifor mi figet ih....... (4/11/2021. 11:39pm) mi tink a email address???? mnk.......
    acc_info["username"]  = username_sign.get()
    acc_info["phone"]  = fonenum_new.get()
    acc_info["Email"] = email_adr_sign.get()
    acc_info["password"]  = passw_sign.get()

    # Opening the file to write the new account info,
    '''This uses the user variable that I created prior and set it into the text file name so 
    the program can save multiple files with different names without overwriting the last one
    (This was an issue I discovered in the example code that my lecturer gave to us)'''
    create_acc = open(f"account_data/{user}_accounts.txt", "w") # I think this "w" opens the file in write mode


    # Write the new account info to the file
    for key, value in  acc_info.items():
        create_acc.write("%s:%s\n" %(key, value))
    create_acc.close()


    # (4/11/2021. 11:34pm)I'm pretty sure when I typed these lines here a few hours ago it was to delete whatever
    # the user entered after it was saved in whatever text file 
    username_sign.delete(0, END)
    fonenum_sign.delete(0, END)
    email_adr_sign.delete(0, END)
    passw_sign.delete(0, END)

    # success message
    messagebox.showinfo("Sython Hub", "Account Successfully created")
    mainframe_signup.destroy()



'''========================================
These allow me to return to the login window. 
=======================================''' 
# This one is from the signup window
def return_to_home(event=None):
    mainframe_signup.destroy()
    login_page()



'''================================================
Here I create the Hub screen where I have the menu
================================================'''
def sy_hub_main():
    # Declearing the window as global so I can open it elsewhere
    global hub_main
    
    # Here I create another window to place my menu
    hub_main = Tk()
    hub_main.geometry("400x250+400+200")
    hub_main.title("Sython Hub")
    hub_main["background"] = "#000000"
    head = Label(hub_main, text = "Main Menu", fg = "#136E7C", bg = "#000000", font = "SegoeUI 18")
    head.place(x=90, y=10)

    # Just a logout button to get back to the login window which also closes the current window
    log_out = Label(hub_main, text = "<---Logout", fg = "#136E7C", bg = "#000000", cursor = "hand2")
    log_out.place(x=0, y=230)
    log_out.bind("<Button-1>", hub_log_out)

    '''========
    (4/12/2021. 12:31am) Ok.... The next day has started so this is the last thing imma work on rn..... What
    Imma try to do here is to attempt to display the user's file who is currently logged in onto the main hub
    window...... It gonna a easier last thing to figure out then imma go to bed..... or watch anime ......
    ======'''

    # (4/16/2021, 3:25pm) This is to diplay the user infomation on the main menu screen after login

    user_info = open(f"account_data/{user}_accounts.txt")

    user_file = user_info.readlines()

    Label(hub_main, fg = "#136E7C", bg = "#000000", text='User Info',  font = "SegoeUI 18").pack(anchor = NE)
    acc_usern = Label(hub_main, fg = "#AAFFFB", bg = "#000000", text= f'{user_file[0]}')
    acc_usern.pack(anchor = NE)

    #Label(hub_main, fg = "#136E7C", bg = "#000000", text='Phone',  font = "SegoeUI 18").pack(anchor = NE)
    acc_fone = Label(hub_main, fg = "#AAFFFB", bg = "#000000", text= f'{user_file[1]}')
    acc_fone.pack(anchor = NE)

    #Label(hub_main, fg = "#136E7C", bg = "#000000", text='Email --> ',  font = "SegoeUI 18").pack(anchor = NE)
    acc_email = Label(hub_main, fg = "#AAFFFB", bg = "#000000", text= f'{user_file[2]}')
    acc_email.pack(anchor = NE)

    #user_info_disp = Text(hub_main, width = 20, height = 5)# text = user_info)
    #user_info_disp.pack( anchor = NE)
    #user_info_disp.insert(END, user_info.readlines())

    '''(4/12/2021. 12:52am) !Update! It's been 20 minutes and I have gotten no where so imma stop here for rn
    I made allot of progress....... Check the (4/12/2021. 12:31am if you dont remember where you were for whatever
    reason..... You never know......GN'''
    
    # (4/16/2021, 3:27pm) Now I place the menu items here 
    card_v = Label(hub_main, text = "Credit card validator", fg = "#FFFD72", bg = "#000000", cursor = "hand2")
    card_v.place(x=90, y=60)
    card_v.bind("<Button-1>", cred_validator)

    '''(4/17/2021. 11:55pm) I'm placing the game in now for extra points cuz, yh.'''

    game_bt = Label(hub_main, text = "Game (Madlibs)", fg = "#FFFD72", bg = "#000000", cursor = "hand2")
    game_bt.place(x=90, y=80)
    game_bt.bind("<Button-1>", game)

    '''(4/18/2021. 1:52pm) This is the exit button here now'''

    exit_sython = Label(hub_main, text = "Exit", fg = "#FFFD72", bg = "#000000", cursor = "hand2")
    exit_sython.place(x=90, y=120)
    exit_sython.bind("<Button-1>", exit_sy)

    '''The help menus option that links to the "README" file'''
    help_sython = Label(hub_main, text = "Help", fg = "#FFFD72", bg = "#000000", cursor = "hand2")
    help_sython.place(x=90, y=100)
    help_sython.bind("<Button-1>", help_readme)

    hub_main.mainloop()
    


'''=============================================================
This is the line of code I used to get to the game I made.
============================================================='''
def game(event):
    # A message box to inform the user where the game is launched
    messagebox.showinfo("Sython Hub", "Game opened in the Command Window.")
    #  This is the line of code I used to l
    os.system('c:game/mablibs_with_gui.py')


'''=============================================================
This is the line of code I used to get to the game I made.
============================================================='''
def help_readme(event):
    # A message box to inform the user where the game is launched
    messagebox.showinfo("Sython Hub", "The 'README' text file will now open in a new window.")
    #  This is the line of code I used to l
    os.system('c:help/README.txt')



'''========================================================================================
Here I inputed my updated credit validation code (which I only got working on the last day).
========================================================================================='''
def sy_val():

    def sython_va(sy_cr_num):
        
        # Here I use Luhns algorithm to validate the credit card number.
        def sy_cr_dig_of(sy_n):
            return [int(d) for d in str(sy_n)]

        sy_cr_dig = sy_cr_dig_of(sy_cr_num)
        sy_cr_dig_fi = sy_cr_dig[-1::-2]
        sy_cr_dig_se = sy_cr_dig[-2::-2]
        sy_cr_dchk = 0
        sy_cr_dchk += sum(sy_cr_dig_fi)

        for d in sy_cr_dig_se:
            sy_cr_dchk += sum(sy_cr_dig_of(d*2))
        

        # If the result is divisible by 10 this message will appear
        if sy_cr_dchk % 10 == 0:
            messagebox.showinfo("Scott's Card Validator", f"{sy_cr_num} is a valid card number")


        # If the result is not divisible by 10 this message will appear
        else:
            messagebox.showinfo("Scott's Card Validator", f"{sy_cr_num} is a invalid card number")


    def is_luhn_valid(sy_cr_num):
        return sython_va(sy_cr_num) == 0
    # The lines retrive the list of numbers to use in the credit validation.
    sy_cr_num = sython_cr.get()
    sy_vad = is_luhn_valid(sy_cr_num)


        
def cred_validator(event):
    messagebox.showinfo("Sython Hub","The Credit Card Validator will \nappear in a new window.")
    global card_frame, sython_cr

    card_frame = Toplevel()
    card_frame.geometry("310x200+400+200")
    card_frame.title("Sython Card Validator")
    card_frame["background"] = "#000000"
    head = Label(card_frame, text = "Welcome to Sython card \n validation system.", fg = "#136E7C", bg = "#000000", font = "Aerial 18")
    head.place(x=15, y=10)

    # Here I declear the input "sython_cr" as a string.
    sython_cr = StringVar()

    # The label for the card number input box is made. 
    label_1 = Label(card_frame, bg = "#000000", fg = "#FFFD72", text = "Card Number")
    label_1.place(x=30, y=70)

    # The entry box for the  card number is also created.
    card_space = Entry(card_frame, bg = "#C3F1F8", width = 20, textvariable = sython_cr)
    card_space.place(x=120, y=70)

    # A button is also created to run the function "sy_val".
    button_1 = Button(card_frame, bg = "#000000", fg = "#FFFD72", text = "validate card number", command = sy_val)
    button_1.place(x=120, y=100)

    mainloop()



'''This function and the one above is get back to the login page this one is from the hub page after login'''
def hub_log_out(event=None):
    hub_main.destroy()
    log_in()



log_in()