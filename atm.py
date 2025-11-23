import time
import os
import sys

# Beep Support for Windows
try:
    import winsound
    def beep(freq, dur):
        winsound.Beep(freq, dur)
except ImportError:
    def beep(freq, dur):
        pass


def loading_animation(msg):
    print(msg, end="")
    for i in range(5):
        print(".", end="")
        beep(700, 100)
        time.sleep(0.3)
    print()


def card_insert_animation():
    print("\nInsert your ATM Card -> ", end="")
    for i in range(8):
        print("■", end="")
        beep(600, 90)
        time.sleep(0.2)
    print("\nCard Detected Successfully!\n")


class User:
    def _init_(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance


class ATM:
    def _init_(self):
        self.users = [
            User("Raj", 1234, 10000),
            User("Aman", 4321, 15000),
            User("Priya", 1111, 8000),
        ]
        self.currentUserIndex = -1

    def login(self):
        card_insert_animation()
        loading_animation("Reading Card")

        pin = int(input("Enter PIN: "))

        # Check normal users
        for i, user in enumerate(self.users):
            if user.pin == pin:
                self.currentUserIndex = i
                beep(1000, 200)
                loading_animation("Logging in")
                print(f"Welcome {user.name}!")
                return True

        # Admin PIN
        if pin == 9999:
            beep(800, 200)
            self.admin_panel()
            return False

        beep(400, 400)
        print("Invalid PIN!")
        return False

    def menu(self):
        while True:
            print("\n====== ATM MENU ======")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Change PIN")
            print("5. Print Receipt")
            print("6. Exit")
            choice = int(input("Enter Choice: "))

            if choice == 1:
                self.check_balance()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.withdraw()
            elif choice == 4:
                self.change_pin()
            elif choice == 5:
                self.print_receipt()
            elif choice == 6:
                loading_animation("Processing Exit")
                print("Thank you for using ATM!")
                break
            else:
                beep(400, 400)
                print("Invalid Choice!")

    def check_balance(self):
        loading_animation("Fetching Balance")
        beep(900, 200)
        print(f"\nCurrent Balance: ₹{self.users[self.currentUserIndex].balance}")

    def deposit(self):
        amt = float(input("Enter amount to deposit: ₹"))
        if amt > 0:
            self.users[self.currentUserIndex].balance += amt
            loading_animation("Processing Deposit")
            beep(1000, 300)
            print("Amount Deposited Successfully!")
        else:
            beep(400, 400)
            print("Invalid Amount!")

    def withdraw(self):
        amt = float(input("Enter amount to withdraw: ₹"))
        user = self.users[self.currentUserIndex]

        if amt <= 0:
            beep(400, 400)
            print("Invalid Amount!")
        elif amt > user.balance:
            beep(400, 400)
            print("Insufficient Balance!")
        else:
            user.balance -= amt
            loading_animation("Counting Cash")
            beep(1200, 400)
            print("\nPlease Collect Your Cash.")

    def change_pin(self):
        new_pin = int(input("Enter new PIN: "))
        self.users[self.currentUserIndex].pin = new_pin
        beep(1000, 300)
        print("PIN Changed Successfully!")

    def print_receipt(self):
        loading_animation("Generating Receipt")
        beep(900, 200)

        user = self.users[self.currentUserIndex]

        print("\n========== RECEIPT ==========")
        print(f"User: {user.name}")
        print(f"Remaining Balance: ₹{user.balance}")
        print("Thank You for Using the ATM!")
        print("=============================\n")

    def admin_panel(self):
        print("\n===== ADMIN MODE =====")
        beep(700, 300)

        print(f"{'Name':15}{'PIN':10}{'Balance'}")
        print("-" * 35)

        for u in self.users:
            print(f"{u.name:15}{u.pin:<10}₹{u.balance}")

        input("\nPress Enter to exit admin mode...")


# ----------------- MAIN FUNCTION -----------------
if _name_ == "_main_":
    atm = ATM()

    while True:
        if atm.login():
            atm.menu()
