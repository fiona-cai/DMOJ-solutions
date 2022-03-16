#https://dmoj.ca/problem/ccc07j2
#CCC '07 J2 - I Speak TXTMSG

x = 0

while x == 0:
    s = input()
    if s == "CU":
        print("see you")
    elif s == ":-)":
        print("I'm happy")
    elif s == ":-(":
        print("I'm unhappy")
    elif s == ";-)":
        print("wink")
    elif s == ":-p":
        print("stick out my tongue")
    elif s == "(~.~)":
        print("sleepy")
    elif s == "TA":
        print("totally awesome")
    elif s == "CCC":
        print("Canadian Computing Competition")
    elif s == "CUZ":
        print("because")
    elif s == "TY":
        print("thank-you")
    elif s == "YW":
        print("you're welcome")
    elif s == "TTYL":
        print("talk to you later")
        x = 1
    else:
        print(s)
