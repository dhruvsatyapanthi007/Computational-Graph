s = "1/2*tran(x)@A@x-x@c"

operators = {"+", "-", "*", "/", "^", "@"}
functions = {"tran", "exp", "inv"}

o_index = []

for i in range(0, len(s)):
    if s[i] in operators:
        o_index.append(i)

for function in functions:
    print(function)
