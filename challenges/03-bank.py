balance = 100

print("Welcome to Chase bank.")
print('Your current balance is')
print(balance)
direction = input(
    'What would you like to do? (deposit, withdraw, check_balance)\n')
if direction == 'deposit':
    deposit_num = input('How much do you want to deposit?\n')
    balance += int(deposit_num)
    print(balance)
elif direction == 'withdraw':
    withdraw_num = input('How much do you want to withdraw?\n')
    balance -= int(withdraw_num)
    print(balance)
else:
    print(balance)
print("Have a nice day!")
