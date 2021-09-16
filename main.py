
from tkinter import *#Imports every library from tkinter
from PIL import Image #Importing pillow module
from PIL import ImageTk #Importing pillow module
import tkinter #Importing tkinter module
import random #Importing random module

root = tkinter.Tk() #Tkinter.TK()
root.title("Rock, Paper, Scissors by AstronGaming")
root.geometry("400x500") #giving resolution of GUI

#Setting up background color of window
root.configure(bg='#fceaea')

random_number = random.randint(1, 3) #Choosing random number using random.randint
if random_number == 1:
    computer_choice = "Rock"
elif random_number == 2:
    computer_choice = "Paper"
elif random_number == 3:
    computer_choice = "Scissor"

#Defining Images
rock_image = ImageTk.PhotoImage(Image.open("img/rock.png")) #Storing images in variable
paper_image = ImageTk.PhotoImage(Image.open("img/paper.png"))#Storing images in variable
scissors_image = ImageTk.PhotoImage(Image.open("img/scissor.png"))#Storing images in variable



# Creating function of rock
def rock():
    label_user_choice['image'] = rock_image
    
    # If computerc chooses rock
    if computer_choice == "Rock":
        label_result['text'] = "TIE"
        label_computer_choice['image'] = rock_image
    elif computer_choice == "Paper":
        label_result['text'] = "Computer wins!"
        label_computer_choice['image'] = paper_image
    elif computer_choice == "Scissor":
        label_result['text'] = "Player wins!"
        label_computer_choice['image'] = scissors_image
    
#Creating function of paper
def paper():
    label_user_choice['image'] = paper_image
    
    ##If computer chooses paper
    if computer_choice == "Paper":
        label_result['text'] = "TIE"
        label_computer_choice['image'] = paper_image
    elif computer_choice == "Scissor":
        label_result['text'] = "Computer wins!"
        label_computer_choice['image'] = scissors_image
    elif computer_choice == "Rock":
        label_result['text'] = "Player wins!"
        label_computer_choice['image'] = rock_image

#Creating function of scissor
def scissors():
    label_user_choice['image'] = scissors_image
    
    #If computer chosoes scissor
    if computer_choice == "Scissor":
        label_result['text'] = "TIE"
        label_computer_choice['image'] = scissors_image
    elif computer_choice == "Rock":
        label_result['text'] = "Computer wins!"
        label_computer_choice['image'] = rock_image
    elif computer_choice == "Paper":
        label_result['text'] = "Player wins!"
        label_computer_choice['image'] = paper_image
    
#Creating reset function
def reset():
    global computer_choice
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_choice = "Rock"
    elif random_number == 2:
        computer_choice = "Paper"
    elif random_number == 3:
        computer_choice = "Scissor"
        
    label_computer_choice['image'] = "" #Clears first image after reset button
    label_user_choice['image'] = "" #Clears second image after reset button
    label_result['text'] = "Choose From Above"


# Creating Widges
button_rock = tkinter.Button(root, text="  Rock   ", command = rock) #Rock button
button_rock.pack()

button_paper = tkinter.Button(root, text="  Paper  ", command = paper) #Paper button
button_paper.pack()

button_scissors = tkinter.Button(root, text="Scissors", command = scissors) #Scissor button
button_scissors.pack()

label_user_choice = tkinter.Label(root, justify=tkinter.LEFT, font="Courier", text="") #shows user's choosed option
label_user_choice.pack()

label_computer_choice = tkinter.Label(root, justify=tkinter.LEFT, font="Courier", text="")  #Shows computer's choosed option
label_computer_choice.pack()



label_result = tkinter.Label(root, text="Choose From above") #Choose from above Label
label_result.pack()

button_reset = tkinter.Button(root, text="Reset", command = reset) #reset button
button_reset.pack()

root.mainloop()