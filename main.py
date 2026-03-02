
from tkinter import *#Imports every library from tkinter
from tkinter import messagebox
from tkinter import ttk
from PIL import Image #Importing pillow module
from PIL import ImageTk #Importing pillow module
import tkinter #Importing tkinter module
import random #Importing random module

root = tkinter.Tk() #Tkinter.TK()
root.title("Rock, Paper, Scissors by AstronGaming")
root.geometry("600x850") #giving resolution of GUI
root.resizable(False, False) #make window non-resizable

# Set modern theme
style = ttk.Style()
style.theme_use('clam')

# Configure custom styles for ttk widgets
style.configure('Title.TLabel', font=('Helvetica', 18, 'bold'), foreground='#333333')
style.configure('Result.TLabel', font=('Helvetica', 18, 'bold'), foreground='#333333')
style.configure('Score.TLabel', font=('Helvetica', 12), foreground='#555555')
style.configure('Round.TLabel', font=('Helvetica', 12, 'bold'), foreground='#333333')
style.configure('TButton', font=('Helvetica', 12), padding=8)
style.configure('TFrame', relief='flat')

#Setting up background color of window
root.configure(bg='#f5f5f5')

# Game state variables
computer_choice = None
player_score = 0
computer_score = 0
ties = 0
round_number = 1
target_wins = 3  # first to 3 wins (default: Best of 5 means first to 3)

# Difficulty selection
difficulty_var = tkinter.StringVar(value="Best of 5")

def update_target_wins():
    """Update target_wins based on selected difficulty."""
    global target_wins
    difficulty = difficulty_var.get()
    if difficulty == "Best of 3":
        target_wins = 2
    elif difficulty == "Best of 5":
        target_wins = 3
    elif difficulty == "Best of 10":
        target_wins = 5
    elif difficulty == "Endless":
        target_wins = None
    # Update status label
    if target_wins is None:
        label_difficulty_status['text'] = "Mode: Endless (no win condition)"
    else:
        label_difficulty_status['text'] = f"First to {target_wins} wins"

#Defining Images
rock_image = ImageTk.PhotoImage(Image.open("img/rock.png")) #Storing images in variable
paper_image = ImageTk.PhotoImage(Image.open("img/paper.png"))#Storing images in variable
scissors_image = ImageTk.PhotoImage(Image.open("img/scissor.png"))#Storing images in variable

# map choices to images for easy reuse
choice_images = {
    'Rock': rock_image,
    'Paper': paper_image,
    'Scissor': scissors_image,
}

# Button colors for visual feedback
DEFAULT_BUTTON_BG = '#f0f0f0'  # light gray
BUTTON_HIGHLIGHT_BG = '#90EE90'  # light green

def flash_button(btn):
    """Flash button on click - change to highlight color for 600ms then revert."""
    btn.config(bg=BUTTON_HIGHLIGHT_BG)
    btn.after(600, lambda: btn.config(bg=DEFAULT_BUTTON_BG))



# Creating function of rock
def play(player_choice):
    global computer_choice, player_score, computer_score, ties, round_number
    # choose for computer each round
    rand = random.randint(1, 3)
    if rand == 1:
        computer_choice = "Rock"
        comp_img = rock_image
    elif rand == 2:
        computer_choice = "Paper"
        comp_img = paper_image
    else:
        computer_choice = "Scissor"
        comp_img = scissors_image

    # show images in the versus area (update/replace each round)
    label_user_choice['image'] = choice_images.get(player_choice, "")
    label_computer_choice['image'] = choice_images.get(computer_choice, "")

    # determine result with descriptive messages and colors
    # phrases for win combos (winner, loser) -> phrase
    win_phrases = {
        ('Rock', 'Scissor'): 'Rock crushes Scissors',
        ('Scissor', 'Paper'): 'Scissors cuts Paper',
        ('Paper', 'Rock'): 'Paper covers Rock',
    }

    outcome_tag = 'tie'
    if player_choice == computer_choice:
        # tie
        display_main = f"Both chose {player_choice} – It's a Tie!"
        fg = '#666666'
        ties += 1
        outcome_tag = 'tie'
    else:
        # find phrase for the matchup (order-insensitive)
        if (player_choice, computer_choice) in win_phrases:
            phrase = win_phrases[(player_choice, computer_choice)]
            display_main = f"{phrase} – You Win!"
            fg = 'green'
            player_score += 1
            outcome_tag = 'win'
        elif (computer_choice, player_choice) in win_phrases:
            phrase = win_phrases[(computer_choice, player_choice)]
            display_main = f"{phrase} – Computer Wins!"
            fg = 'red'
            computer_score += 1
            outcome_tag = 'loss'
        else:
            # fallback
            display_main = "Result"
            fg = 'black'
            outcome_tag = 'tie'

    # second line: show choices
    display_choices = f"You: {player_choice}   Computer: {computer_choice}"
    # update label with two-line message
    label_result['text'] = f"{display_main}\n{display_choices}"
    label_result['fg'] = fg

    # log to history
    history_text.config(state=NORMAL)
    history_entry = f"Round {round_number}: You → {player_choice}   Computer → {computer_choice}   → {display_main.split(' – ')[1] if ' – ' in display_main else 'Tie'}\n"
    history_text.insert(END, history_entry, outcome_tag)
    # keep only last 12 lines visible
    line_count = int(history_text.index('end-1c').split('.')[0])
    if line_count > 12:
        history_text.delete('1.0', '2.0')
    history_text.see(END)  # auto-scroll to end
    history_text.config(state=DISABLED)

    # update scoreboard and round
    update_scoreboard()
    round_number += 1
    label_round['text'] = f"Round {round_number}"

    # check for game over (only if not in endless mode)
    if target_wins is not None and (player_score >= target_wins or computer_score >= target_wins):
        if player_score > computer_score:
            end_text = "Game Over – You Win!"
        elif computer_score > player_score:
            end_text = "Game Over – You Lose!"
        else:
            end_text = "Game Over – Tie!"
        label_game_over['text'] = end_text
        label_game_over.lift()
        messagebox.showinfo("Game Over", end_text)
        disable_choice_buttons()
    
#Creating function of paper
def rock():
    flash_button(button_rock)
    play('Rock')

def paper():
    flash_button(button_paper)
    play('Paper')

#Creating function of scissor
def scissors():
    flash_button(button_scissors)
    play('Scissor')
    
#Creating reset function - full game reset
def reset():
    """Reset entire game: scores, round, UI, history, and re-enable buttons."""
    global player_score, computer_score, ties, round_number
    # Reset all game state variables
    player_score = 0
    computer_score = 0
    ties = 0
    round_number = 1
    # Clear all UI elements
    label_user_choice['image'] = ""  # Clear player choice image
    label_computer_choice['image'] = ""  # Clear computer choice image
    label_result['text'] = "Choose a move"
    label_result['fg'] = '#333333'  # reset color
    label_game_over['text'] = ""  # Clear game over message
    # Update scoreboard labels
    update_scoreboard()
    label_round['text'] = f"Round {round_number}"  # Reset round display
    # Clear history log
    history_text.config(state=NORMAL)
    history_text.delete('1.0', END)
    history_text.config(state=DISABLED)
    # Re-enable choice buttons
    enable_choice_buttons()
    # Apply current difficulty setting (preserve player's choice)
    update_target_wins()

def reset_current_round():
    """Clear only the current round display without resetting scores."""
    label_user_choice['image'] = ""
    label_computer_choice['image'] = ""
    label_result['text'] = "Choose a move"
    label_result['fg'] = '#333333'
    label_game_over['text'] = ""


# Creating Widgets with ttk
# Main container frame
main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Top: Title frame
title_frame = ttk.Frame(main_frame)
title_frame.pack(fill=X, padx=10, pady=(0, 10))

label_title = ttk.Label(title_frame, text="Rock, Paper, Scissors", style='Title.TLabel')
label_title.pack()

# Round label under title
label_round = ttk.Label(title_frame, text=f"Round {round_number}", style='Round.TLabel')
label_round.pack(pady=(5, 0))

# Difficulty selection frame
difficulty_frame = ttk.Frame(title_frame, padding=5)
difficulty_frame.pack(fill=X, pady=(10, 0))

ttk.Label(difficulty_frame, text="Game Mode:", style='Score.TLabel').pack(side=LEFT, padx=(0, 5))

difficulty_menu = ttk.OptionMenu(difficulty_frame, difficulty_var, 
                                   "Best of 3", "Best of 5", "Best of 10", "Endless",
                                   command=lambda x: update_target_wins())
difficulty_menu.pack(side=LEFT, padx=5)

label_difficulty_status = ttk.Label(difficulty_frame, text="First to 3 wins", style='Score.TLabel')
label_difficulty_status.pack(side=LEFT, padx=5)

# Middle: Buttons frame (horizontal layout)
buttons_frame = ttk.Frame(main_frame, padding=10)
buttons_frame.pack(fill=X, padx=10, pady=10)

button_rock = tkinter.Button(buttons_frame, text="Rock", command=rock, width=15, bg=DEFAULT_BUTTON_BG, font=('Helvetica', 12), activebackground='#e0e0e0') #Rock button
button_rock.pack(side=LEFT, padx=5)

button_paper = tkinter.Button(buttons_frame, text="Paper", command=paper, width=15, bg=DEFAULT_BUTTON_BG, font=('Helvetica', 12), activebackground='#e0e0e0') #Paper button
button_paper.pack(side=LEFT, padx=5)

button_scissors = tkinter.Button(buttons_frame, text="Scissors", command=scissors, width=15, bg=DEFAULT_BUTTON_BG, font=('Helvetica', 12), activebackground='#e0e0e0') #Scissor button
button_scissors.pack(side=LEFT, padx=5)

# Middle: Versus frame to show player's choice and computer's choice side-by-side
versus_frame = ttk.Frame(main_frame, padding=10)
versus_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Player side
player_side_frame = ttk.Frame(versus_frame)
player_side_frame.pack(side=LEFT, expand=True, padx=10)

ttk.Label(player_side_frame, text="You", style='Score.TLabel').pack(pady=(0, 5))
label_user_choice = ttk.Label(player_side_frame, justify=CENTER, text="")
label_user_choice.pack(pady=10)

# Computer side
computer_side_frame = ttk.Frame(versus_frame)
computer_side_frame.pack(side=LEFT, expand=True, padx=10)

ttk.Label(computer_side_frame, text="Computer", style='Score.TLabel').pack(pady=(0, 5))
label_computer_choice = ttk.Label(computer_side_frame, justify=CENTER, text="")
label_computer_choice.pack(pady=10)

# Bottom: Result frame
result_frame = ttk.Frame(main_frame, padding=10)
result_frame.pack(fill=X, padx=10, pady=10)

label_result = ttk.Label(result_frame, text="Choose a move", style='Result.TLabel', justify=CENTER) #Choose from above Label
label_result.pack(pady=10)

# Big game over label (initially empty)
label_game_over = ttk.Label(result_frame, text="", style='Title.TLabel', justify=CENTER)
label_game_over.pack(pady=5)

# Scoreboard frame
score_frame = ttk.Frame(main_frame, padding=10)
score_frame.pack(fill=X, padx=10, pady=10)

label_player_score = ttk.Label(score_frame, text=f"Player: {player_score}", style='Score.TLabel')
label_player_score.pack(side=LEFT, padx=15, expand=True)

label_computer_score = ttk.Label(score_frame, text=f"Computer: {computer_score}", style='Score.TLabel')
label_computer_score.pack(side=LEFT, padx=15, expand=True)

label_ties = ttk.Label(score_frame, text=f"Ties: {ties}", style='Score.TLabel')
label_ties.pack(side=LEFT, padx=15, expand=True)

# Control buttons frame
control_frame = ttk.Frame(main_frame, padding=10)
control_frame.pack(fill=X, padx=10, pady=10)

button_new_game = ttk.Button(control_frame, text="New Game", command=reset, width=20) #new game button
button_new_game.pack(side=LEFT, padx=5)

button_reset_round = ttk.Button(control_frame, text="Reset Round", command=reset_current_round, width=20) #reset round button
button_reset_round.pack(side=LEFT, padx=5)

# Button enable/disable functions
def disable_choice_buttons():
    button_rock.config(state=DISABLED)
    button_paper.config(state=DISABLED)
    button_scissors.config(state=DISABLED)

def enable_choice_buttons():
    button_rock.config(state=NORMAL)
    button_paper.config(state=NORMAL)
    button_scissors.config(state=NORMAL)



# History panel: scrollable text widget to show move history
history_frame = ttk.Frame(root, padding=5)
history_frame.pack(fill=BOTH, expand=False, padx=10, pady=5)

history_label = ttk.Label(history_frame, text="Move History", style='Score.TLabel')
history_label.pack(anchor=W, pady=(0, 5))

# Text widget with scrollbar
history_container = ttk.Frame(history_frame)
history_container.pack(fill=BOTH, expand=True)

scrollbar = ttk.Scrollbar(history_container)
scrollbar.pack(side=RIGHT, fill=Y)

history_text = tkinter.Text(history_container, height=8, width=75, yscrollcommand=scrollbar.set, font=('Courier', 10))
history_text.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=history_text.yview)

# Configure tags for coloring
history_text.tag_config('win', foreground='green', font=('Courier', 10, 'bold'))
history_text.tag_config('loss', foreground='red', font=('Courier', 10, 'bold'))
history_text.tag_config('tie', foreground='#666666', font=('Courier', 10))

# Make text read-only
history_text.config(state=DISABLED)

def update_scoreboard():
    label_player_score['text'] = f"Player: {player_score}"
    label_computer_score['text'] = f"Computer: {computer_score}"
    label_ties['text'] = f"Ties: {ties}"

root.mainloop()