import tkinter as tk
from tkinter import ttk, scrolledtext

# Class to represent the GUI for the bank system
class BankSystemGUI:
    def __init__(self):
        # Attributes for the bank account
        self.account_holder = ""  # Account holder's name
        self.balance = 0.0  # Account balance

        # Setting up the main window for the application
        self.root = tk.Tk()  # Create main Tkinter window
        self.root.title("Bank System (e.g, Bank of Kigali) created by Dr. Josbert")  # Set window title
        self.root.geometry("500x400")  # Set window dimensions

        # Creating the input frame to hold input widgets
        input_frame = ttk.Frame(self.root, padding="10", style="TFrame")  # Frame with padding and style
        input_frame.pack(fill=tk.BOTH, expand=True)  # Add the frame to the main window

        # Configure styles for the GUI elements
        style = ttk.Style()
        style.configure("TFrame", background="green")  # Frame background color
        style.configure("TLabel", background="green", foreground="orange", font=("Arial", 12, "bold"))  # Label styling
        style.configure("TButton", background="blue", foreground="black")  # Button styling
        style.configure("Title.TLabel", background="green", foreground="white", font=("Arial", 16, "bold"))  # Title styling

        # Title label for the bank system
        label_title = ttk.Label(input_frame, text="Bank of Kigali (BK)", style="Title.TLabel")
        label_title.grid(row=0, column=0, columnspan=2, pady=(0, 10))  # Place the title in the grid

        # Creating and placing input widgets for account holder name and transaction amounts
        ttk.Label(input_frame, text="Account Holder:", style="TLabel").grid(row=1, column=0, sticky=tk.W)  # Label for account holder
        self.txt_account_holder = ttk.Entry(input_frame)  # Entry field for account holder's name
        self.txt_account_holder.grid(row=1, column=1, sticky=(tk.W, tk.E))  # Place entry in grid

        ttk.Label(input_frame, text="Deposit Amount:", style="TLabel").grid(row=2, column=0, sticky=tk.W)  # Label for deposit
        self.txt_deposit = ttk.Entry(input_frame)  # Entry field for deposit amount
        self.txt_deposit.grid(row=2, column=1, sticky=(tk.W, tk.E))  # Place entry in grid

        ttk.Label(input_frame, text="Withdraw Amount:", style="TLabel").grid(row=3, column=0, sticky=tk.W)  # Label for withdrawal
        self.txt_withdraw = ttk.Entry(input_frame)  # Entry field for withdraw amount
        self.txt_withdraw.grid(row=3, column=1, sticky=(tk.W, tk.E))  # Place entry in grid

        # Buttons for account actions
        self.btn_create_account = ttk.Button(input_frame, text="Create Account", command=self.create_account, style="TButton")  # Create account button
        self.btn_create_account.grid(row=4, column=0, sticky=(tk.W, tk.E))  # Place button in grid

        self.btn_deposit = ttk.Button(input_frame, text="Deposit", command=self.deposit, style="TButton")  # Deposit button
        self.btn_deposit.grid(row=4, column=1, sticky=(tk.W, tk.E))  # Place button in grid

        self.btn_withdraw = ttk.Button(input_frame, text="Withdraw", command=self.withdraw, style="TButton")  # Withdraw button
        self.btn_withdraw.grid(row=5, column=0, sticky=(tk.W, tk.E))  # Place button in grid

        self.btn_check_balance = ttk.Button(input_frame, text="Check Balance", command=self.check_balance, style="TButton")  # Check balance button
        self.btn_check_balance.grid(row=5, column=1, sticky=(tk.W, tk.E))  # Place button in grid

        # Output area to display transaction summary
        self.txt_area_output = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=10)  # Create a scrolled text area
        self.txt_area_output.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)  # Add scrolled text area to main window

        # Initial placeholders for column labels in the output area
        self.txt_area_output.insert(tk.END, f"{'Transactions:':<20} | {'Amounts (in FRW):':<10}\n")  # Header row for output
        self.txt_area_output.insert(tk.END, "-" * 40 + "\n")  # Separator line

        # Configure the grid layout
        input_frame.columnconfigure(1, weight=1)  # Allow the second column to expand

        # Start the Tkinter main loop to run the application
        self.root.mainloop()

    # Method to create a bank account
    def create_account(self):
        self.account_holder = self.txt_account_holder.get().strip()  # Get account holder's name from input
        if self.account_holder:
            self.balance = 0.0  # Initializing balance to zero
            self.txt_area_output.insert(tk.END, f"{'Account Created':<20} | {self.account_holder}\n")  # Show confirmation message
        else:
            self.txt_area_output.insert(tk.END, f"{'Error':<20} | {'Please enter an account holder name.'}\n")  # Error message for missing name

    # Method to handle deposit transactions
    def deposit(self):
        try:
            amount = float(self.txt_deposit.get().strip())  # Get and convert deposit amount from input
            if amount > 0:
                self.balance += amount  # Increment the balance
                self.txt_area_output.insert(tk.END, f"{'Deposit':<20} | FRW:{amount:.2f}\n")  # Log the deposit in the output area
            else:
                self.txt_area_output.insert(tk.END, f"{'Error':<20} | {'Deposit amount must be positive.'}\n")  # Error for non-positive amount
        except ValueError:
            self.txt_area_output.insert(tk.END, f"{'Error':<20} | {'Invalid deposit amount.'}\n")  # Error for invalid amount format

    # Method to handle withdrawal transactions
    def withdraw(self):
        try:
            amount = float(self.txt_withdraw.get().strip())  # Get and convert withdraw amount from input
            if amount > 0 and amount <= self.balance:
                self.balance -= amount  # Decrease the balance
                self.txt_area_output.insert(tk.END, f"{'Withdraw':<20} | FRW:{amount:.2f}\n")  # Log the withdrawal
            else:
                self.txt_area_output.insert(tk.END, f"{'Error':<20} | {'Insufficient funds or invalid amount.'}\n")  # Error for insufficient funds or invalid amount
        except ValueError:
            self.txt_area_output.insert(tk.END, f"{'Error':<20} | {'Invalid withdrawal amount.'}\n")  # Error for invalid amount format

    # Method to check and display the current balance
    def check_balance(self):
        self.txt_area_output.insert(tk.END, f"{'Balance':<20} | FRW:{self.balance:.2f}\n")  # Log the current balance

# Main program execution
if __name__ == "__main__":
    BankSystemGUI()  # Create an instance of the bank system GUI