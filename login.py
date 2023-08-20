from cProfile import label
from ctypes import alignment
from email.mime import image
from tkinter import *
from tkinter import messagebox
from traceback import print_tb
from turtle import Screen, color, heading, width
from unicodedata import name

root=Tk()
root.title("Login") #page title
root.minsize(height=500,width=925) #Page minimium Size
root.geometry("925x500")
root.configure(bg="#fff")#Bg Color
root.resizable(width=False, height=False)#Not Resizeable
root.iconbitmap("image\Home-Icon.ico")#Page Icon/Logo

#Function to hide and unhide password filed text
def show_hide_password():
    if code["show"]=="*":
       code.config(show="")
       show_hide_btn.configure(text=show_face)
    else:
        code.configure(show="*")
        show_hide_btn.configure(text=hide_face)
        
#Function for getting text from user        
def signin():
    username=user.get()
    password=code.get()

###-------------DASH BOARD-------------------------------------------------------------------------
    if username=="admin" and password=="1234":
        messagebox.showinfo("Maxi-Touch (Success Message)","Login Succefull.! 'Welcome'" + " " + username)
        Screen=Toplevel(root)
        Screen.title("Dash Board")
        Screen.geometry("925x500")
        Screen.config(bg="white")
        Screen.iconbitmap("image\Home-Icon.ico")
        Label(Screen,text="Hello Everyone!",bg="#fff",font=("Calibri(Body)",50,"bold")).pack(expand=True)
        sidebar=Frame(Screen, width=250,height=925,bg="gray")
        sidebar.place(x=0,y=0)
        heading1=Label(sidebar,text="Menue",bg="gray",fg="white",font=("Calibri(Body)",25,"bold","underline"))
        heading1.place(x=65,y=5)
        Button(sidebar,width=21,text="Report",bg="gray",fg="white",border=0,font=("Calibri(Body)",14,"bold")).place(x=1,y=60)
        Screen.mainloop()       
    elif username!="admin" and password!="1234":
        messagebox.showerror("Maxi-Touch (Error Message)","Invalid Username or Password")
    elif password!="1234":
        messagebox.showerror("Maxi-Touch (Error Message)","Invalid Password Entered")
    elif username!="admin":
        messagebox.showerror("Maxi-Touch (Error Message)","Invalid Username Entered")
##-----------------END DASHBOARD----------------------------------------------------------------------

###----------------------LOGIN CODE------------------------------
img = PhotoImage(file='image/Log.png')
Label(root,image=img,bg='white').place(x=50,y=50)

show_face="*"
hide_face=""

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=120)
heading=Label(frame,text="Sign In",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x=100,y=5)
show_hide_btn=Button(frame,text=hide_face,font=("bold"),border=0, command=show_hide_password)
show_hide_btn.place(x=23,y=30)

#######-----------------------TexBox------------------------------------
def on_enter(e):
    user.delete(0,"end")   
def  on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,"Username")  
user = Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11,"bold"))
user.place(x=30,y=80)
user.insert(0,"Username")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
#######-----------------------TexBox------------------------------------
def on_enter(e):
    code.delete(0,"end")    
def  on_leave(e):
    name=code.get()
    if name=="":
        code.insert(0,"Password") 
code = Entry(frame,width=25,fg="black",border=0,show="*",bg="white",font=("Microsoft YaHei UI Light",11,"bold"))
code.place(x=30,y=150)
code.insert(0,"Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
#######-----------------------------------------------------------

#######-----------------------Button------------------------------------
Button(frame,width=39,pady=7,text="Sign In",bg="#57a1f8",fg="white",border=0, command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
label.place(x=75,y=270)
###----------------------END OF LOGIN CODE------------------------------

######-----------------------SIGN UP-------------------------------------------------------------------------

def signup():
    Screen=Toplevel(root)
    Screen.title("Creat Account")
    Screen.geometry("925x500")
    Screen.resizable(width=False, height=False)
    Screen.config(bg="white")
    Screen.iconbitmap("image\Home-Icon.ico")
    img = PhotoImage(file='image/Sign.png')
    Label(Screen,image=img,bg='white').place(x=50,y=50)   
     
    ##-------------Frame for Heading--------------------
    frame=Frame(Screen,width=500,height=500,bg="white")
    frame.place(x=450,y=80)
    heading=Label(frame,text="Create Account",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
    heading.place(x=80,y=5)
     
    #######------------Declear SignUp-----------------
    def SignUp1():
        SignUsername=signuser.get()
        Signpassword=signcode.get()
        Signconfirm=signconfirm.get()
    #######-----------------------TexBox------------------------------------
    def on_enter1(e):
        signuser.delete(0,"end")   
    def on_leave1(e):
        name=signuser.get()
        if name=="":
            signuser.insert(0,"Username")  
    signuser = Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
    signuser.place(x=60,y=80)
    signuser.insert(0,"Username")
    signuser.bind('<FocusIn>', on_enter1)
    signuser.bind('<FocusOut>', on_leave1)
    Frame(frame,width=295,height=2,bg="black").place(x=60,y=107)
     
    def on_enter1(e):
        signcode.delete(0,"end")    
    def  on_leave1(e):
        name=signcode.get()
        if name=="":
           signcode.insert(0,"Password") 
    signcode = Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
    signcode.place(x=60,y=150)
    signcode.insert(0,"Password")
    signcode.bind("<FocusIn>", on_enter1)
    signcode.bind("<FocusOut>", on_leave1)
    Frame(frame,width=295,height=2,bg="black").place(x=60,y=177)   
     
    def on_enter1(e):
        signconfirm.delete(0,"end")    
    def  on_leave1(e):
        name=signconfirm.get()
        if name=="":
           signconfirm.insert(0,"Confirm Password") 
    signconfirm = Entry(frame,width=35,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
    signconfirm.place(x=60,y=220)
    signconfirm.insert(0,"Confirm Password")
    signconfirm.bind("<FocusIn>", on_enter1)
    signconfirm.bind("<FocusOut>", on_leave1)
    Frame(frame,width=295,height=2,bg="black").place(x=60,y=247)  
    ##----------Back-----  
    def Loginbtn():
        Screen.destroy()
    ##----------Back-----  
    #######-----------------------Button------------------------------------
    Button(frame,width=39,pady=7,text="Sign Up",bg="#57a1f8",fg="white",border=0).place(x=70,y=270)
    label=Label(frame,text="Already have an account?",fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
    label.place(x=95,y=315)
    sign_up= Button(frame,width=6,text="Login In",border=0,bg="white",cursor="hand2",fg="#57a1f8", command=Loginbtn)
    sign_up.place(x=245,y=315)
     
    Screen.mainloop()
     
sign_up= Button(frame,width=6,text="Sign Up",border=0,bg="white",cursor="hand2",fg="#57a1f8", command=signup)
sign_up.place(x=215,y=270)

##----------------END MAIN ROOT------------------
root.mainloop()
##----------------END MAIN ROOT------------------
