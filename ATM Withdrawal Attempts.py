# Using a while loop, simulate a user with only 3 attempts to enter the correct PIN (1234). 
# Keep asking (or comparing against a fixed list of guesses) until either the PIN is correct 
# or attempts run out. Print "Access granted" or "Card blocked" accordingly.



correct_pin = "1234"
attempts = 3

while attempts > 0:
    user = int(input("Please enter your PIN: "))
    if user == int(correct_pin):
        print("Access granted")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. You have {attempts} attempts left.")
        if attempts == 0:
            print("Card blocked")
      
            