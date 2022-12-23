# Password-Manager-App
Created a password manager app using python and the tkinter package for the GUI.

## What does the project do ##

All of us here at some point in our lives have forgotten our passwords or find it hard to generate a new password for a new account we are creating. This won’t be the case anymore with my new app called “PASSME.” PASSME is a password manager app that will store, generate, and copy passwords for the user. After entering all the required information in the entries, when the user clicks add, the data is automatically added into a text file locally. The project also asks the user (by displaying a pop-up and dialog box) whether they would like to continue using the password manager app and ensures the user that the data was successfully saved. Furthermore, if any of the entries are blank, another pop-up is displayed to the user indicating that everything needs to be filled out and the data is not saved. You can also generate a strong password, which is automatically copied so the user can paste it into the website they are creating a new account in. 

## Who are the users and What problem does it solve? ##

A user that wants to keep track of their passwords because they might be forgetful or generate a password for a user that might be having a hard time coming up with a password. Most users don’t know this, but according to the MLA citation below, the number of characters a safe password should have is between 11-15 characters. 

Goldberg, Jeffrey, et al. “Want to Stay Safe Online? This Is How Long Your Passwords Should Be: 1password.” 1Password Blog, 10 Oct. 2018, 

https://blog.1password.com/how-long-should-my-passwords-be/#:~:text=When%20a%20password%20is%20properly,secure%20with%20a%20longer%20version. 


Therefore, keeping the security aspect in mind, I coded my program in such a way that the generate password button produces a password of 16 characters. Another potential user could be someone that doesn’t trust internet-based services (e.g., Google Chrome Password Manager) and would prefer to store their passwords locally. 

With the above in mind, my program helps users solve the problem of helping them generate passwords that are strong and save the information in a text file locally so they can never forget it.

## Data Plan and Visual Layout ##


<img width="416" alt="Screen Shot 2022-12-22 at 7 58 12 PM" src="https://user-images.githubusercontent.com/76918821/209250245-355e77e1-03c7-499a-8468-ecb1f2d7f4f4.png">


I set up the window using Tk() package and then the canvas by setting up the dimensions (width and height) using the Canvas() Class. I then displayed the image on the Canvas by calling the ImageTk.PhotoImage(Image.open()) Object Class.


I also used the canvas.config() object Class to allow whitespaces between the window and the canvas. Moreover, I set up the label using the Label() class. A label can be added with two lines of text. The first line defines the label and the text. The second line sets the two dimensional position using the .grid() method (explained in detail later on). The entry widget, next to the labels, is supposed to accept single-line text from a user. The syntax of displaying the entry widget is as follows -> w = Entry(master,option) where master represents the parent window and the options represents the key value pairs separated by the commas.![image](https://user-images.githubusercontent.com/76918821/209250314-e36250d3-9532-407b-b985-7572b1a60222.png)










