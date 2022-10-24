# Copy here code of line function from previous exercise
def line(num, text):
    i = 0
    if text == "":
            print('*' * num)
            i += 1
    else:
            print(text[0] * num)
            i += 1

def triangle(size):
    # You should call function line here with proper parameters
    i = 1
    while i <= size:
        line(i, "#")
        i += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
