# Atm-system-
This project is for basic understanding of ATM Simulation 
ATM Project (Python Version)
Overview:
This is a simple ATM simulation system written in Python. It simulates real ATM functionality: card insertion,
PIN login, balance check, deposit, withdrawal, PIN change, receipt printing, and admin mode.
Features:
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Change PIN
5. Print Receipt
6. Exit
Admin Mode available using PIN 9999.
How It Works:
Login using valid PIN. If PIN matches a user, login succeeds. Admin PIN opens admin panel to view all users.
User Operations:
- Check balance
- Add money
- Withdraw if sufficient balance
- Change PIN
- Print receipt containing name and balance
Program Structure:
User Class stores name, PIN, and balance.
ATM Class manages login, menus, and operations.
Default Users:
Raj (1234) - 10000
Aman (4321) - 15000
Priya (1111) - 8000
Admin PIN: 9999
Run:
1. Install Python 3
2. Save script as atm.py
3. Run using: python atm.py
