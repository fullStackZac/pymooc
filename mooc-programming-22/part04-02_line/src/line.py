# Write your solution here
def line(num, text):
    i = 0
    if text == "":
            print('*' * num)
            i += 1
    else:
            print(text[0] * num)
            i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")