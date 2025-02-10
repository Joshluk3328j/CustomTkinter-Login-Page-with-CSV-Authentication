import tkinter 
import customtkinter
from PIL import ImageTk, Image
import csv


with open("users.csv",mode="r",newline="") as infile:
    reader=csv.reader(infile)
    # with open("users_new.csv",mode="w") as outfile:
    #     writer=csv.write(outfile)
    users={rows[0]:rows[1] for rows in reader}
    # users.pop("user")

print(users)

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()

window.title("User Authentication")
window.geometry("600x600")

logged_frm=customtkinter.CTkFrame(master=window, width=320, height=360, corner_radius=15, border_color="white", border_width=1)
logged_frm.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)

frm = customtkinter.CTkFrame(master=window, width=320, height=360, corner_radius=15, border_color="white", border_width=1)
frm.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)

global signin_frm, signup_frm
signin_frm=customtkinter.CTkFrame(master=frm)

username = tkinter.StringVar()
passkey = tkinter.Variable()
passkey1=tkinter.StringVar()
passkey2=tkinter.StringVar()
passkey3=tkinter.StringVar()
show_key=tkinter.BooleanVar()

def logged_in(user):
    l5=customtkinter.CTkLabel(master=logged_frm, text=f"welcome {user}", font=("century Gothic", 20), text_color="white")
    l5.place(relx=0.5,rely=0.1, anchor=tkinter.CENTER)

def clear_frame():
    for widget in frm.winfo_children():
        widget.destroy()

def login():
    user=username.get()
    password = passkey.get() 
    
    if user not in users.keys():
        l5=customtkinter.CTkLabel(master=frm, text="Invalid Username or password", font=("century Gothic", 12), text_color="red")
        l5.place(x=70,y=70)
    elif password not in users.values():
        l5=customtkinter.CTkLabel(master=frm, text="Invalid Username or password", font=("century Gothic", 12), text_color="red")
        l5.place(x=70,y=70)
    else:
        frm.destroy()
        logged_in(user)

def signedup(user,password1):
    l5=customtkinter.CTkLabel(master=logged_frm, text=f"{user}\n your account has been created", font=("century Gothic", 15), text_color="white")
    l5.place(relx=0.5,rely=0.1, anchor=tkinter.CENTER)
    users[f"{user}"] = f"{password1}"
    with open("users.csv",mode="w",newline="") as outfile:
        writer=csv.writer(outfile)
        for key, value in users.items():
            writer.writerow([key,value])
    print(users)
    
def signin(self):
    # frm.destroy()
    # frm = customtkinter.CTkFrame(master=window, width=320, height=360, corner_radius=15, border_color="white", border_width=1)
    # frm.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)

    def show():
        if show_key.get()==True:
            entry2.configure(show="")
            print(True)
        elif show_key.get()==False:
            entry2.configure(show="*")

            print(False)

    signin_frm = customtkinter.CTkFrame(master=frm, width=320, height=360, corner_radius=15, border_color="white", border_width=1)
    signin_frm.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)
    show_key.set(False)

    l2=customtkinter.CTkLabel(master=signin_frm, text="Log into your Account", font=("century Gothic", 20))
    l2.place(x=50,y=45)

    label1=customtkinter.CTkLabel(master=signin_frm, text="Username", font=("century Gothic",15) )
    label1.place(x=30,y=110)
    entry1=customtkinter.CTkEntry(master=signin_frm, width=180, textvariable=username, placeholder_text="Username")
    entry1.place(x=110,y=110)

    label2=customtkinter.CTkLabel(master=signin_frm, text="Password", font=("century Gothic",15))
    label2.place(x=30,y=165)
    entry2=customtkinter.CTkEntry(master=signin_frm, width=180, textvariable=passkey, placeholder_text="Password")
    entry2.place(x=110,y=165)
    entry2.configure(show="*")

    checkbox1=customtkinter.CTkCheckBox(master=signin_frm, text="show password",command=show, variable=show_key, onvalue=True,offvalue=False ,font=("century Gothic",10), checkbox_height=12,checkbox_width=12, checkmark_color="green",border_width=2)
    checkbox1.place(relx=0.6,rely=0.58, anchor=tkinter.W)

    # l2=customtkinter.CTkLabel(master=frm, text="Forgot password?", font=("century Gothic", 12))
    # l2.place(x=185,y=195)

    l2=customtkinter.CTkLabel(master=signin_frm, text="Forgot password?", font=("century Gothic", 9),text_color="light green")
    l2.place(x=110,y=300)

    button1=customtkinter.CTkButton(master=signin_frm,width=220, text="Login", corner_radius=6, command=login)
    button1.place(x=50,y=240)

    l3=customtkinter.CTkLabel(master=signin_frm, text="Dont have an Account?", font=("century Gothic", 10))
    l3.place(x=82,y=280)

    sign_up=customtkinter.CTkLabel(master=signin_frm, text="Sign Up", font=("century Gothic", 10),text_color="light green")
    sign_up.place(x=204,y=280)
    sign_up.bind("<Button-1>", signup)

def signup(self):
    # clear_frame()
    signin_frm.destroy()
    signup_frm = customtkinter.CTkFrame(master=frm, width=320, height=360, corner_radius=15, border_color="white", border_width=1)
    signup_frm.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)
    show_key.set(False)

    def to_sign_up():
        user=username.get()
        password1 = passkey1.get()
        password2 = passkey2.get()

        print(f"first is {password1} second is {password2}")
        
        if user in users.keys():
            l5=customtkinter.CTkLabel(master=signup_frm, text="Username already taken", font=("century Gothic", 12), text_color="red")
            l5.place(relx=0.5,rely=0.16,anchor=tkinter.CENTER)
            # l5.configure()
        elif passkey1.get() == passkey2.get():
            frm.destroy()
            signedup(user,password1)
            print("success")
            print(user,password1)
        else:
            l5=customtkinter.CTkLabel(master=signup_frm, text="password mismatch", font=("century Gothic", 12), text_color="red")
            l5.place(relx=0.5,rely=0.16,anchor=tkinter.CENTER)
            print("error")

    def show():
        if show_key.get()==True:
            entry2.configure(show="")
            entry3.configure(show="")
            # entry4.configure(show="")
            print(True)
        elif show_key.get()==False:
            entry2.configure(show="*")
            entry3.configure(show="*")
            # entry4.configure(show="")

            print(False)

    l2=customtkinter.CTkLabel(master=signup_frm, text="create an Account", font=("century Gothic", 20))
    l2.place(relx=0.5,rely=0.1,anchor=tkinter.CENTER)

    label1=customtkinter.CTkLabel(master=signup_frm, text="Username", font=("century Gothic",15) )
    label1.place(x=30,y=80)
    entry1=customtkinter.CTkEntry(master=signup_frm, width=180, textvariable=username, placeholder_text="Username")
    entry1.place(x=110,y=80)

    label2=customtkinter.CTkLabel(master=signup_frm, text="Password", font=("century Gothic",15))
    label2.place(x=30,y=135)
    entry2=customtkinter.CTkEntry(master=signup_frm, width=180, textvariable=passkey1, placeholder_text="Password")
    entry2.place(x=110,y=135)
    entry2.configure(show="*")

    label3=customtkinter.CTkLabel(master=signup_frm, text="Confirm", font=("century Gothic",15))
    label3.place(x=30,y=190)
    entry3=customtkinter.CTkEntry(master=signup_frm, width=180, textvariable=passkey2, placeholder_text="Password")
    entry3.place(x=110,y=190)
    entry3.configure(show="*")

    checkbox1=customtkinter.CTkCheckBox(master=signup_frm, text="show password", variable=show_key,command=show, onvalue=True,offvalue=False ,font=("century Gothic",10), checkbox_height=12,checkbox_width=12, checkmark_color="green",border_width=2)
    checkbox1.place(relx=0.6,rely=0.49, anchor=tkinter.W)

    # l2=customtkinter.CTkLabel(master=frm, text="Forgot password?", font=("century Gothic", 12))
    # l2.place(x=185,y=195)

    # show_pass=customtkinter.CTkLabel(master=frm, text="Forgot password?", font=("century Gothic", 9),text_color="light green")
    # show_pass.place(x=110,y=300)

    button2=customtkinter.CTkButton(master=signup_frm,width=220, text="Sign Up", corner_radius=6, command=to_sign_up)
    button2.place(x=50,y=240)

    l3=customtkinter.CTkLabel(master=signup_frm, text="Aready have an Account?", font=("century Gothic", 10))
    l3.place(x=76,y=280)

    sign_in=customtkinter.CTkLabel(master=signup_frm, text="Sign In", font=("century Gothic", 10),text_color="light green")
    sign_in.place(x=211,y=280)
    sign_in.bind("<Button-1>",signin)

signin("")

window.mainloop()