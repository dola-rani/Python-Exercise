""" 06: Write a function named “isLandscape” that takes 2 numbers (image width
and height) as arguments and the function returns Landscape if the image width has a
higher value than height. Returns Portrait otherwise
Hints: Use condition inside the function
"""

def isLandscape(width, height):
    if width > height:
        return "Landscape"
    else:
        return "Portrait"

width = int(input("Enter width of the image: "))
height = int(input("Enter height of the image: "))

result = isLandscape(width, height)
print(result)
