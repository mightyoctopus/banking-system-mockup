from tkinter import *
from bank_account_logic import BankAccount

class BankInterface:
    def __init__(self, customer_list, bank_account_logic: BankAccount):
        self.customers = customer_list
        self.bank_logic = bank_account_logic

        self.window = Tk()
        self.window.title("Online Banking System")
        self.window.config(width=600, height=500, padx=20, pady=20)

        self.canvas = Canvas(bg="white", width=250, height=240)
        self.canvas.grid(row=0, column=0, columnspan=3)
        self.canvas.create_text(100, 120, text="Please, Select Your Option.", fill="black")

        self.view_btn = Button(text="View", command=self.view_balance)
        self.view_btn.grid(row=1, column=0, pady=(20, 0))
        self.deposit_btn = Button(text="Deposit", command=self.deposit)
        self.deposit_btn.grid(row=1, column=1, pady=(20, 0))
        self.withdrawal_btn = Button(text="Withdrawal", command=self.withdrawal)
        self.withdrawal_btn.grid(row=2, column=0)

        self.customer_listbox = Listbox(height=4)
        customer_names = [name for name, details in self.customers.items()]
        for index, name in enumerate(customer_names):
            self.customer_listbox.insert(index, name)
        self.customer_listbox.grid(row=2, column=1)
        self.customer_listbox.bind("<<ListboxSelect>>", self.on_customer_list_selected)

        self.selected_name = None

        self.deposit_entry = None
        self.withdrawal_entry = None
        self.withdrawal_text = None

        self.window.mainloop()

    def on_customer_list_selected(self, event):
        selection = self.customer_listbox.curselection()
        if selection:
            self.selected_name = self.customer_listbox.get(selection)

    def view_balance(self):
        self.canvas.delete("all")
        if self.selected_name:
            self.canvas.create_text(130, 100, text=f"Account Holder: {self.selected_name}", fill="black")
            self.canvas.create_text(130, 120, text=f"Account Balance: ${self.customers[self.selected_name]["balance"]}", fill="black")
        else:
            self.canvas.create_text(100, 120, text="Please select a customer first.")

    def deposit(self):
        self.canvas.delete("all")
        if self.selected_name:
            deposit_text = Label(text="How much money will you deposit?", background="white", fg="black")
            deposit_text.place(x=37, y=50)

            self.deposit_entry = Entry(self.window)
            self.canvas.create_window(130, 100, window=self.deposit_entry)

            submit_btn = Button(self.window, text="Submit", command=self.deposit_submit_btn, highlightbackground="white")
            submit_btn.place(x=106, y=130)

    def deposit_submit_btn(self):
        try:
            amount = int(self.deposit_entry.get())
        except ValueError:
            self.canvas.delete("all")
            self.canvas.create_text(130, 120, text="Please enter a valid number.")
        else:
            self.bank_logic.deposit(amount, self.selected_name)
            self.view_balance()

    def withdrawal(self):
        self.canvas.delete("all")
        if self.selected_name:
            self.withdrawal_text = Label(text="How much will you withdrawal?", background="white", fg="black")
            self.withdrawal_text.place(x=37, y=50)

            self.withdrawal_entry = Entry(self.window)
            self.canvas.create_window(130, 100, window=self.withdrawal_entry)
            withdrawal_btn = Button(
                self.window,
                text="Submit",
                command=self.withdrawal_submit_btn,
                highlightbackground="white",
                # width= 230
            )
            withdrawal_btn.place(x=106, y=130)

    def withdrawal_submit_btn(self):
        try:
            amount = int(self.withdrawal_entry.get())
        except ValueError:
            self.canvas.delete("all")
            self.canvas.create_text(130, 120, text="Please enter a valid number.")
        else:
            if self.bank_logic.withdrawal(amount, self.selected_name):
                self.view_balance()
            else:
                self.withdrawal_text.destroy()
                self.canvas.create_text(127, 60, text="Sorry, the withdrawal amount \ncan't exceed the total balance.", fill="black")











