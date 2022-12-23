import random, pyperclip
from tkinter import *
from PIL import ImageTk, Image


from tkinter import messagebox


gui = Tk()
gui.title("PASSME Password Manager") 
gui.config(background="lightgrey")

canvas = Canvas(height=250, width=250)
img = ImageTk.PhotoImage(Image.open("Pass me.png"))
canvas.create_image(125, 125, image=img)
gui.config(padx=45, pady=45)

canvas.grid(row=0, column=1)
canvas.config(background="lightgrey")

website = Label(text="Website:") 
website.grid(row=1,column=0)
email = Label(text="Email/Username:")
email.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

entry1= Entry(width=30)
entry1.focus()
entry1.grid(row=1,column=1, columnspan=2)
entry2= Entry(width=30)
entry2.grid(row=2,column=1, columnspan=2)
entry3= Entry(width=30, show="*")
entry3.grid(row=3, column=1, columnspan=2)

def generatepassword():
  char=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
  '!', '#', '$', '%', '&', '(', ')', '*', '+']
  random.shuffle(char)
  passwordlist=[]
  for i in range(0,16):
    passwordlist.append(random.choice(char))
  newpassword = "".join(passwordlist)
  entry3.insert(0, newpassword)
  pyperclip.copy(newpassword) 


password_button = Button(text = "Generate Password", command = generatepassword)
password_button.grid(row=4, column=1)

def addpassword():


  website = entry1.get()
  email = entry2.get()
  password = entry3.get()

  if website == '' or email == '' or password == '':
    messagebox.showinfo(title="Error!",message="Please don't leave anything blank")
  else:
    with open("password_list.txt", "a") as f:
      f.write(f"Website = {website}\nEmail = {email}\nPassword = {password}\n----------------------------------\n")
      entry1.delete(0,END)
      entry2.delete(0,END)
      entry3.delete(0, END)
      answer = messagebox.askyesno(title='confiramtion',
      message="Thank you for using the application! The data was successfully added! Would you like to leave the application?")
      if answer:
        gui.destroy()


    
add_button = Button(text="add", width=29, command=lambda:[addpassword()])
add_button.grid(row=5, column=1, columnspan=2)



def show_password():
  if entry3.cget('show') == "*":
    entry3.config(show='')
  else:
    entry3.config(show="*")


show = Checkbutton(text = "Show Password", command=show_password)
show.grid(row=3, column = 2)



gui.mainloop()