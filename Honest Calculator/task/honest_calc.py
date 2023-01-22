messages = ["Enter an equation ",
            "Do you even know what numbers are? Stay focused!",
            "Yes ... an interesting math operation. "
            "You've slept through all classes, haven't you?",
            "Yeah... division by zero. Smart move...",
            "Do you want to store the result? (y / n):",
            "Do you want to continue calculations? (y / n):",
            " ... lazy",
            " ... very lazy",
            " ... very, very lazy",
            "You are",
            "Are you sure? It is only one digit! (y / n)",
            "Don't be silly! It's just one number! Add to the memory? (y / n)",
            "Last chance! Do you really want to embarrass yourself? (y / n)"]

operators = ["+", "-", "*", "/"]


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + messages[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + messages[7]
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + messages[8]
    if msg != "":
        msg = messages[9] + msg
    print(msg)


def main():
    memory = 0
    on_of = True
    while on_of:
        user_input = input(messages[0]).split(" ")
        x = user_input[0]
        operator = user_input[1]
        y = user_input[2]
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        try:
            x = float(x)
            y = float(y)
            if operator not in operators:
                print(messages[2])
                continue
            check(x, y, operator)
            if operator == "+":
                result = x + y
            elif operator == "-":
                result = x - y
            elif operator == "*":
                result = x * y
            else:
                result = x / y
            print(result)

            while True:
                user_input = input(messages[4])
                if user_input == "y":

                    if is_one_digit(result):
                        msg_index = 10

                        while True:
                            user_input = input(messages[msg_index])
                            if user_input == "y":
                                if msg_index < 12:
                                    msg_index += 1
                                else:
                                    memory = result
                                    break
                            elif user_input == "n":
                                break
                    else:
                        memory = result
                        break
                    break
                elif user_input == "n":
                    break







            while True:
                user_input = input(messages[5])
                if user_input == "y":
                    break
                elif user_input == "n":
                    on_of = False
                    break
                else:
                    continue

        except ValueError:
            print(messages[1])
        except ZeroDivisionError:
            print(messages[3])

        if not on_of:
            break


main()
