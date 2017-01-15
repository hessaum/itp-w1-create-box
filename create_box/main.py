"""This is the entry point of the program."""

def create_box(height, width, character):
    box = ''
    if height and width >= 1:
        for i in range(height):
            """for each value of height, print the width of the box. 
               Create a new line and append it to the empty string"""
            box += (character * width + '\n')
        return box

"""
Bonus Meme: Only return the outer border of the box
"""

def create_empty_box(height, width, character):
    box = ''
    box += (character * width + '\n')
    for i in range(height):
        box += (character + (' ' * (width - 2) + character) + '\n')
    box += (character * width + '\n')
    return box


"""
Solution that doesnt use the return statement.

def create_box(height, width, character):
    if height and width >= 1:
    for i in range(height):
        print(character * width)
"""

if __name__ == '__main__':
    create_box(3, 4, '*')
