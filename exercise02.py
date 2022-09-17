# time = int(input())
# def part_time_job(time):
#     if(time == 7):
#         print("Got 1000 yen at that time")

#     if (time == 9):
#         print("You only get 953 yen")

# part_time_job(time)
current_balance = int(input('Current balance: '))
amount = int(input('Amount: '))
def withdrawal(current_balance,amount):
    if(current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance

balance = withdrawal(current_balance,amount)
print('Current balance after function is: ')
if (balance <= 20):
    print('We need to make deposit',balance)

else:
    print('It is okay')
