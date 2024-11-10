import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Entry field
        self.input_text = tk.StringVar()
        self.entry = tk.Entry(root, font=("Arial", 24), textvariable=self.input_text, bd=20, insertwidth=2, width=15, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Creating buttons
        buttons = [
            '7', '8', '9', 'DEL',
            '4', '5', '6', '+',
            '1', '2', '3', '-',
            '.', '0', '/', '*',
            'RESET', '='
        ]
        row, col = 1, 0

        # Add buttons to the GUI
        for button_text in buttons:
            if button_text == 'RESET':
                btn = tk.Button(root, text=button_text, width=32, height=3, command=self.reset)
                btn.grid(row=row, column=0, columnspan=2)
            elif button_text == '=':
                btn = tk.Button(root, text=button_text, width=32, height=3, command=self.calculate)
                btn.grid(row=row, column=2, columnspan=2)
            elif button_text == 'DEL':
                btn = tk.Button(root, text=button_text, width=10, height=3, command=self.delete)
                btn.grid(row=row, column=col)
            else:
                btn = tk.Button(root, text=button_text, width=10, height=3, command=lambda x=button_text: self.on_button_click(x))
                btn.grid(row=row, column=col)

            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, char):
        self.input_text.set(self.input_text.get() + str(char))

    def reset(self):
        self.input_text.set("")

    def delete(self):
        current_text = self.input_text.get()
        self.input_text.set(current_text[:-1])

    def calculate(self):
        try:
            result = eval(self.input_text.get())
            self.input_text.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Input")

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
