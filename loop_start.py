# Example Python file with loop
# 4th Sep 2022


def main():

    x = 0
    # TODO : define a while loop
    # while(x < 5):
    #     print(x)
    #     x = x + 1
    # print(x) # output: x is still going to 5


    # TODO : define a for loop
    # for i in range(3,11):
    #     print(i)
    
    
    # TODO : use a for loop over a collection
    # days = ["Mon","Tue","Wed","Thurs","Fri","Sat","Sun",]
    # for d in days:
    #     print(d)

    # TODO : use the break and continue statement
    # for i in range(3,20):
    #     # if i == 8:
    #     #     break

    #     if i % 2 == 1:
    #         continue
    #     print(i)

    # TODO : using the enumerate() function to get index
    days = ["Mon","Tue","Wed","Thurs","Fri","Sat","Sun",]
    for i,d in enumerate(days):
        print(i,d)
    
# if __name__ == "__main__":
main()
