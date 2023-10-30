import random
from tkinter import *
schema = {
    "Rock":{"Rock":1,"Paper":0,"Scissors":2},
    "Paper":{"Rock":2,"Paper":1,"Scissors":0},
    "Scissors":{"Rock":0,"Paper":2,"Scissors":1}
}
comp_score = 0
player_score = 0
def outcome_handler(user_choice):
    global comp_score
    global player_score
    outcomes=["Rock","Paper","Scissors"]
    random_number = random.randint(0,2)
    computer_choice=outcomes[random_number]
    result = schema[user_choice][computer_choice]

    player_choice_label.config(fg="magenta",text="Player Choice : "+str(user_choice))
    computer_choice_label.config(fg="orangered",text="Computer Choice : "+str(computer_choice))

    if result == 2:
        player_score = player_score + 2
        player_score_label.config(text="Player : "+str(player_score))
        outcome_label.config(fg="darkgreen",text="Result : Player won")
    elif result == 1:
        player_score = player_score+1
        comp_score = comp_score+1
        player_score_label.config(text="Player : "+str(player_score))
        computer_score_label.config(text="Computer : "+str(comp_score))
        outcome_label.config(fg="darkgreen",text="Result : Draw")
    elif result == 0:
        comp_score=comp_score+2
        computer_score_label.config(text="Computer : "+str(comp_score))
        outcome_label.config(fg="darkgreen",text="Result : Computer won")

master = Tk()
master.title("Rock Paper Scissors")


Label(master,text="Rock, Paper, Scissors",foreground="orange",font=("Times New Roman",20,"bold")).grid(row=0,sticky=N,pady=10,padx=200)
Label(master,text="Select your option",foreground="navy",font=("Times New Roman",16,"bold")).grid(row=1,sticky=N)
player_score_label=Label(master,text="Player Score",font=("Times New Roman",12,"bold"))
player_score_label.grid(row=3,sticky=W)
player_score_label=Label(master,text="Player : 0",font=("Times New Roman",12,"bold"))
player_score_label.grid(row=4,sticky=W)
computer_score_label=Label(master,text="Computer Score",font=("Times New Roman",12,"bold"))
computer_score_label.grid(row=3,sticky=E)
computer_score_label=Label(master,text="Computer : 0",font=("Times New Roman",12,"bold"))
computer_score_label.grid(row=4,sticky=E)
Label(master).grid(row=5)
player_choice_label = Label(master,font=("Times New Roman",12,"bold"))
player_choice_label.grid(row=6,sticky=W)
computer_choice_label = Label(master,font=("Times New Roman",12,"bold"))
computer_choice_label.grid(row=6,sticky=E)
outcome_label = Label(master,font=("Times New Roman",12,"bold"))
outcome_label.grid(row=8,sticky=N)
Button(master,text="Rock",width=15,bg="indianred",font=("Times New Roman",12,"bold"),command=lambda:outcome_handler("Rock")).grid(row=7,sticky=W,padx=5,pady=5)
Button(master,text="Paper",width=15,bg="aqua",font=("Times New Roman",12,"bold"),command=lambda:outcome_handler("Paper")).grid(row=7,sticky=N,pady=5)
Button(master,text="Scissors",width=15,bg="pink",font=("Times New Roman",12,"bold"),command=lambda:outcome_handler("Scissors")).grid(row=7,sticky=E,padx=5,pady=5)
Label(master).grid(row=10)
Label(master).grid(row=12)


master.mainloop()