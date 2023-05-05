# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 08:13:23 2021

@author: sanjith krishna
"""
import random 
import tkinter
from tkinter import *
from tkinter import messagebox


print("______________WELCOME TO GAME HUB__,______________","\n1=ROCK PAPER SCISSORS!","\n2=HAND CRICKET!","\n3=JUMBLED WORDS!","\n4=MAGIC 8BALL!")
you=int(input("select from the following games(1/2/3/4):"))
if you==1:
    print("------ROCK PAPER SCISSORS !------")
    user= input("Enter a choice (rock, paper, scissors): ")
    possibilities= ["rock", "paper", "scissors"]
    computer = random.choice(possibilities)
    print("\nYou chose:",user,"    computer chose :",computer)

    if user == computer:
       print("Both players selected",user," It's a tie!")
    elif user == "rock":
       if computer == "scissors":
        print("Rock smashes scissors! You win!")
       else:
        print("Paper covers rock! You lose.")
    elif user == "paper":
       if computer == "rock":
        print("Paper covers rock! You win!")
       else:
        print("Scissors cuts paper! You lose.")
    elif user == "scissors":
        if computer == "paper":
           print("Scissors cuts paper! You win!")
        else:
           print("Rock smashes scissors! You lose.")

if you==2:
    print("------WELCOME TO HAND CRICKET-------")
    a=int(input("specify no of overs: "))
    b=a*6
    batting_chances=b 
    runs=0
    chances_taken=0
    data=[1,2,3,4,5,6]

    print("------YOUR BATTING!------")
    while chances_taken<batting_chances:
        user=int(input("enter your number from 1-6:"))
        computer=random.choice(data)
        if user==computer:
          print("your choice is:",user,"\ncomputer choice is:",computer)
          print("YOUR OUT ! total runs scored by you=",runs)
          break
        elif user>6:
            print("!OUTSIDE OF PARAMETERS!")
            continue
        else:
           runs=runs+user
           print("your choice is:",user,"\ncomputer choice is:",computer)
           print("Runs scored by you =",runs)
        
        
        chances_taken=chances_taken+1
        
    print("\n\n------YOUR BOWLING NOW!!!!------")
    runs_comp=0
    chances_taken2=0

    while chances_taken2<batting_chances:
        user1=int(input("enter a number from 1-6:"))
        computer1=random.choice(data)
        if computer1==user1:
          print("your choice is:",user1,"\ncomputer choice is:",computer1)
          print("Computer is OUT! runs scored by computer=",runs_comp)
          break
        elif user1>6:
            print("!OUTSIDE OF PARMETERS!")
            continue
        else:
           runs_comp=runs_comp+computer1
           print("your choice is:",user1,"\ncomputer choice is:",computer1)
           print("runs by computer so far=",runs_comp)
        
        if runs_comp>runs:
           break 
    
        chances_taken2=chances_taken2+1
    
    print("\n******************results**********************")
    if runs_comp>runs:
       print("you LOST the game!")
       print("runs scored by you=",runs)
       print("runs scored by computer=",runs_comp)
    elif runs_comp==runs:
       print("the game is a TIE!")
    else:
       print("you WON the game !!!!")
       print("runs scored by you=",runs)
       print("runs scored by computer=" ,runs_comp)
if you==3:
   print("------JUMBLED WORDS!------")
#  words as per  requirement
   answers = [
        "python",
        "java",
        "computer",
        "swift",
        "canada",
        "india",
        "america",
        "london",
        "ishaan",
        "borgir",
        "kanye",
        "future",
        "nashville",
       ]

   words = [
        "nptoyh",
        "avja",
        "mcoptuer",
        "wfsit",
        "cdanaa",
        "aidin",
        "aiearcm",
        "odnlon",
        "sahain",
        "orgib",
        "yekan",
        "tufure",
        "anshillev"
       ]

#  by using len(words)
   num =  random.randrange(0, len(words), 1)

   def default():
        global words,answers,num
        lbl.config(text = words[num])

   def res():
        global words,answers,num
        num = random.randrange(0, len(words), 1)
        lbl.config(text = words[num])
        e1.delete(0, END)


   def checkans():  
        global words,answers,num
        var = e1.get()
        if var == answers[num]:
           messagebox.showinfo("Success", "Answer is correct :D")
           res()
        else:
           messagebox.showerror("Error", "Answer is wrong :(")
           e1.delete(0, END)



   root = tkinter.Tk()
   root.geometry("350x400+400+300")
   root.title("Jumbbled")
   root.configure(background = "#000000")

   lbl = Label(
       root,
            text = "Your here",
            font = ("Verdana", 18),
            bg = "#000000",
            fg = "#FFFFFF",
           )
   lbl.pack(pady = 30,ipady=10,ipadx=10)


   ans1 = StringVar()
   e1 = Entry(
      root,
      font = ("Verdana", 16),
      textvariable = ans1,
     )
   e1.pack(ipady=5,ipadx=5)

   btncheck = Button(
       root,
       text = "Check",
       font = ("Agency fb", 32),
       width = 16,
       bg = "#2b1c13",
       fg = "#f06c1a",
       relief = GROOVE,
       command = checkans,
      )
   btncheck.pack(pady = 40)

   btnreset = Button(
       root,
       text = "Next",
       font = ("Seaford", 16),
       width = 16,
       bg = "#230e38",
       fg = "#0685d4",
       relief = GROOVE,
       command = res,
      )
   btnreset.pack()

   default()
   root.mainloop()
   
if you==4:
    print("------MAGIC 8-BALL!------")
    while True:
        print("HEELO THERE !")
        print("EXAMPLE: WILL I WIN THE LOTTERY ?")
        a=input("Type a yes or no question :")
        replies= [ "It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
               "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
               "Yes", "Signs point to yes", "Not right now , Come back later", "Ask again later",
               "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
               "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]
        computer=random.choice(replies)
        print("Thinking...")
        print(computer)
        repeat = input("Would you like to ask another question? (Y or N)")
        if not (repeat == "y" or repeat == "Y"):
            print("Come back if you have more questions!")
            break 