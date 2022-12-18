from tkinter import *
# creates window
root = Tk()
# determines title, image, and size included in window
root.title("Fetch! Training Academy")
root.geometry("200x150")

# calls the images needed for the dogs
two_dogs= ["Sophie.png", "Jackson.png"]

# defines the message when submitted
def submitClick():
    # allows the dog name tag to be used in both windows
    global dogName
    # defines messages given depending on dog behavior enered by user
    messages = {
        "Barking": "Try crate training and complete silence for periods of time.",
        "Jumping": "Try turning away from your dog when the dog jumps up.",
        "Aggression": "Try resource guarding training if the aggression is with items the dog sees as valuable."
    }
    # validation for user entered information allows for both upper and lower case responses
    # while creating an error if one of those specific responses are not entered
    message = messages.get(dogName.get().title(), "Error. Please enter either barking, jumping or aggression.")
    # defines submit button
    submitMessage = Label(newWindow, text=message)
    submitMessage.grid(row=20, column=6, padx=5, pady=15)

# defines openWindowClick function
def openWindowClick():
    # using global allows use in both windows
    global newWindow
    global dogName
    # defines the second window title, image and size
    newWindow = Toplevel(root)
    newWindow.title("Behavior Window")
    newWindow.geometry("1000x800")
    # message when new window is opened
    text = Label(newWindow, text="Let's get started. Choose the issue with your dog's behavior that you want to work on today: barking, jumping, or aggression?")
    # the behavior of the dog entered by the user
    dogName = Entry(newWindow, width=25, fg='white', bg='blue')
    # defines submit button
    submitButton = Button(newWindow, text="Submit", command=submitClick, fg='white', bg='black', padx=25, pady=15)
    # defines exit button
    exitButton = Button(newWindow, text="Close", command=lambda: newWindow.destroy(), fg='white', bg='black', padx=25, pady=15)
    Sophie=PhotoImage(file="./Sophie.png")
    SophieLabel=Label(newWindow, image=Sophie)
    Jackson=PhotoImage(file="./Jackson.png")
    JacksonLabel=Label(newWindow, image=Jackson)

    # defines grid placement of each
    text.grid(row=0, column=6)
    dogName.grid(row=15, column=6, padx=5, pady=15)
    submitButton.grid(row=18, column=6, padx=5, pady=15)
    exitButton.grid(row=35, column=6, padx=5, pady=15)
    SophieLabel.grid(row=1, column=1, sticky="w")
    JacksonLabel.grid(row=19, column=1, sticky="e")
    newWindow.pack()
    # I am aware that this pack line generates an error but the images will not paint without it



# exit function
def exitClick():
    exit()

# opening message
welcomeMessage = Label(root, text='Welcome to Fetch! Training Academy!')
# opens second window when clicked
readyMessage = Label(root, text='Do you want a well-behaved dog?')
yesButton = Button(root, text="Yes", command=openWindowClick, fg='white', bg='black', padx=25, pady=15)

# gets user name
nameMessage = Label(root, text="What is your name?")
nameEntry= Entry(root)
# defines grid placement
welcomeMessage.grid(row=0, column=6)
readyMessage.grid(row=4, column=6)
yesButton.grid(row=5, column=6)
nameMessage.grid(row=2, column=6)
nameEntry.grid(row=3,column=6)
# ends Loop
root.mainloop()
