import tkinter as tk

# Corrected function header
def correctly_formatted_function(arg1, arg2):
    print("This function header is now correct")

def correctly_formatted_function():
    print("This function is fine")

for i in range(3):
    print("Correct indentation in loop")
    if i < 2:
        print("Nested loop print", i)
    else:
        print("Else block")

# Another corrected function header
def another_correct_function(arg1, arg2):
    print("Another correct function header")

print("Print statement for count")

# Function to display the popup message
def show_message():
    window = tk.Tk()
    window.title("Message")
    message = tk.Label(window, text="Lexical and Syntax Analysis is fun in COBOL")
    message.pack()
    tk.Button(window, text="Close", command=window.destroy).pack()
    window.mainloop()

show_message()
