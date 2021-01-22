userstring = input("Please enter a string")
#asking user for input
if "python" in userstring:
    stringrevise = userstring.replace("python","pythons")
    print (stringrevise + "  (Successfully replaced)")
elif "Python" in userstring:
    stringrevise = userstring.replace("Python","Pythons")
    print (stringrevise + "  (Successfully replaced)")
#if the word python is in the user inputted string, it will be replaced with pythons and outputted with all other text
#remaining the same - accounting for python being at beginning too
else:
    print (userstring + " (Unchanged)")
#otherwise, the text will be outputted as it originally was