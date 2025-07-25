# Basic Password Generator
# This code generates a random password based on user input!
# By Lilly Nicholls 25/07/2025

# Importing the random module to generate random choices
import random
import tkinter as tk
from tkinter import messagebox

# Function to get the desired password length from the user
def getPassLength():

    passLength = input("Enter the length of the password you want: ")
    if passLength.isdigit():
        passLength = int(passLength)
    elif passLength == "":
        passLength = 10
    elif passLength <= 9:
        print("Password length must be at least 10 characters.")
        exit()
    else:
        print("Invalid input. Please enter a number.")
        exit()

    return passLength

# Generating characters for the password
alphabet = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
specialChars = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"

# Getting the password from length and generating the password
def generate_password(passLength): 
    password = ""
    for i in range(passLength):
        if i == 0:
            password += random.choice(alphabet)
        elif i == 1:
            password += random.choice(uppercase)
        elif i == 2:
            password += random.choice(numbers)
        elif i == 3:
            password += random.choice(specialChars)
        else:
            allChars = alphabet + uppercase + numbers + specialChars
            password += random.choice(allChars)
    return password

# Function to handle the button click event
def on_generate():
    length_str = entry_length.get()
    if length_str == "":
        passLength = 10
    elif length_str.isdigit():
        passLength = int(length_str)
        if passLength < 10:
            messagebox.showerror("Error", "Password length must be at least 10 characters.")
            return
    else:
        messagebox.showerror("Error", "Invalid input. Please enter a number.")
        return
    password = generate_password(passLength)
    label_result.pack(pady=10)
    entry_password.config(state="normal")
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)
    entry_password.config(state="readonly")
    entry_password.pack(pady=5)

# Setting up the GUI using tkinter
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x400")
root.configure(bg="#f1d2d2")

# Creating a frame for the main content
frame = tk.Frame(root, bg="#ffffff", bd=2, relief="flat")
frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=350)

# Adding widgets to the frame
tk.Label(frame, text="Password Generator", font=("Courier New", 20, "bold"), bg="#fff7f7", fg="#201f2e").pack(pady=(20, 20))
tk.Label(frame, text="Enter password length (min 10):", font=("Courier New", 11), bg="#fff7f7").pack(pady=20)
entry_length = tk.Entry(frame, font=("Courier New", 12), width=10, justify="center", relief="flat", bg="#eae3f2", fg="#201f2e"  )
entry_length.pack(pady=5)

# Button to generate the password
btn_generate = tk.Button(frame, text="Generate Password", font=("Courier New", 13, "bold"), bg="#e98b94", fg="white", command=on_generate, relief="flat", activebackground="#c4546e")
btn_generate.pack(pady=20)

# Label and entry to display the generated password
label_result = tk.Label(frame, text="Here is your Password:", font=("Courier New", 11, "bold"), bg="#fff7f7", fg="#000000")
label_result.pack(pady=10)
entry_password = tk.Entry(frame, width=30, font=("Courier New", 11), state="readonly", justify="center", relief="flat", bg="#ded1ec", fg="#201f2e")


root.mainloop()