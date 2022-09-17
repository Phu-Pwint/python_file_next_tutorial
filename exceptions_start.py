#TODO: this code will cause an error bec you can't divide by zero
# x = 10/0

# TODO: Exceptions provide a way of catching errors and then handling them in seperate section
# try:
#     x=10/0
# except:
    # print("Error! 10 cannot be divided by 0")


# TODO: You can also catch specific exceptions
try:
    answer = input("10 / 0 : ")
    num = int(answer)
    print(10/0)

except ZeroDivisionError as e:
    print("You cannot divide 10 by 0")
except ValueError as e:
    print("Invalid number")
    print(e)
finally:
    print("The code always runs")

