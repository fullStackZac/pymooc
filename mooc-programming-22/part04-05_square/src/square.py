# Copy here code of line function from previous exercise
def line(num, text):
    i = 0
    if text == "":
            print('*' * num)
            i += 1
    else:
            print(text[0] * num)
            i += 1

def square(size, character):
    # You should call function line here with proper parameters
    i = 0
    while i < size:
        line(size, character)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")