import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Invalid input. Please enter a positive integer.")
        else:
            password = generate_password(length)
            result_label.config(text="Generated Password: " + password)
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid integer.")


app = tk.Tk()
app.title("Password Generator")


length_label = tk.Label(app, text="Enter the desired length of the password:")
length_label.pack()

length_entry = tk.Entry(app)
length_entry.pack()

generate_button = tk.Button(app, text="Generate Password", command=generate_and_display_password)
generate_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
