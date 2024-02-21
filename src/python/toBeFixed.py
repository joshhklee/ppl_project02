import tkinter as tk

# Function with incorrect header
defincorrectly formatted_function(arg1, arg2):
 print("This function header is incorrect")

def correctly_formatted_function():
    print("This function is fine")

for i in range(3):
print("Incorrect indentation in loop")
    if i < 2:
    print("Nested loop print", i)
 else:
    print("Else block")

def another_incorrect_function arg1, arg2):
    print("Another incorrect function header")

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
