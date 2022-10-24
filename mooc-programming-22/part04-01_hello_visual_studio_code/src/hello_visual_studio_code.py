# Write your solution here
while True:
    ide = input("Editor: ")
    if ide.lower() == "visual studio code":
        print("an excellent choice!")
        break
    if ide.lower() == "word" or ide.lower() == "notepad":
        print("awful")
    else:
        print("not good")