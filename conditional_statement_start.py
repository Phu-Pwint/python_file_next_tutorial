# Example Python file with conditional statement 
# 4th Sep 2022


def main():

    x,y = 10,100

    # conditional flow using if,else,elif
    # if x < y:
    #     result = "x is less than y"

    # elif x == y:
    #     result = "x is the same as y"

    # else:
    #     result = "x is greater than y"

    # print(result)

    # conditional statement let you use "a if C else b"
    # result = "x is less than y" if x < y else "x is greater than or equal to y"
    # print(result)

    # match-case makes it easy to compare multiple values
    # only in Python version 3.10
    value = "one"
    match value:
        case "one": result = 1
        case "two": result = 2
        case "three": result = 3
        case _:     # default
            result = -1
        
    print(result)
    
if __name__ == "__main__":
    main()
