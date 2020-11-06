import math

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    # user_shape = input("Enter the shape (it must be either pyramid, square, triangle, kite, parallelogram or trapezoid): ")
    user_shape = input("Shape?: ")
    while len(user_shape) == 0:
        user_shape = input("Shape?: ")
    if user_shape.lower() in ("pyramid", "square", "triangle", "kite", "parallelogram", "trapezoid"):
        return user_shape.lower()


# TODO: Step 1 - get height (it must be int!)
def get_height():
    user_height = input("Height?: ")
    while user_height.isdigit() == False:
        user_height = input("Height?: ")
    user_height = int(user_height)
    if (user_height >= 1) and (user_height<= 80):
        return user_height
    else:
        return 0

# TODO: Step 2
def draw_pyramid(height, outline):
    drawn_pyramid = ""
    x = height
    if outline == False:
        for i in range(1, height + 1):
            drawn_pyramid = drawn_pyramid + (" "*(x-1) + "*"*i + "*"*(i-1) +"\n")
            x = x -1
    else:
        for i in range(1, height + 1):
            if (i==1)or (i==height):
                drawn_pyramid = drawn_pyramid + (" "*(x-1) + "*"*i + "*"*(i-1) +"\n")
                x = x -1
            else:
                drawn_pyramid = drawn_pyramid + (" "*(x-1) + "*" + " "*(i-1) + " "*(i-2) + "*"+ "\n")
                x = x -1
    print(drawn_pyramid[:-1])


# TODO: Step 3
def draw_square(height, outline):
    drawn_square = ""
    if outline == False:
        for i in range(1,height+1):
            drawn_square = drawn_square + "*"*height + "\n"
    else:
        for i in range(1,height+1):
            if (i==1)or (i==height):
                drawn_square = drawn_square + "*"*height + "\n"
            else:
                drawn_square = drawn_square + "*" + " "*(height-2) + "*" + "\n"
    print(drawn_square[:-1])
    return drawn_square


# TODO: Step 4
def draw_triangle(height, outline):
    drawn_triangle = ""
    x = height
    if outline == False:
        for i in range(1,height+1):
            drawn_triangle = drawn_triangle + "*"*i + "\n"
    else:
        for i in range(1,height+1):
            if (i==1):
                drawn_triangle = drawn_triangle + "*" + "\n"
            elif (i==height):
                drawn_triangle = drawn_triangle + "*"*(height) + "\n"
            else:
                drawn_triangle = drawn_triangle + "*" + " "*(height-x) + "*" + "\n"
                x = x-1
    print(drawn_triangle[:-1])
    return drawn_triangle

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw_kite(height, outline):
    drawn_kite = ""
    if (height % 2) == 0: #even
        odd_even_offset = 0
        space_off = 1
    else:#odd
        odd_even_offset = 1
        space_off = 0
    mid_height = math.ceil(height/2)
    x = mid_height
    if outline == False:
        for i in range(1, mid_height+1):
            drawn_kite = drawn_kite + (" "*(x+1) + "*"*i + "*"*(i-1) +"\n")
            x = x -1  
        for i in range(mid_height-odd_even_offset, 0,-1):
            x = x +1
            drawn_kite = drawn_kite + (" "*(x+2-space_off) + "*"*i + "*"*(i-1) +"\n")
            
    else:
        for i in range(1, mid_height+1):
            if (i==1):
                drawn_kite = drawn_kite + (" "*(x+1+space_off) + "*"*i + "*"*(i-1) +"\n")
            else:
                drawn_kite = drawn_kite + (" "*(x+1+space_off) + "*" + " "*(i-1) + " "*(i-2) + "*" +"\n")
            x = x -1
        for i in range(mid_height-odd_even_offset, 0,-1):
            x = x+1
            if (i == 1):
                drawn_kite = drawn_kite + (" "*(x+2) + "*"*i + "*"*(i-1) +"\n")
            else:
                drawn_kite = drawn_kite + (" "*(x+2) + "*"+ " "*(i-1) + " "*(i-2) + "*" +"\n")
    print(drawn_kite)

def draw_parallelogram(height, outline):
    drawn_parallelogram = ""
    x = height
    if outline == False:
        for i in range(1,height+1):
            drawn_parallelogram = drawn_parallelogram +" "*(x-1) +"*"*height + "\n"
            x = x-1
    else:
        for i in range(1,height+1):
            if (i==1)or (i==height):
                drawn_parallelogram = drawn_parallelogram + " "*(x-1) + "*"*height + "\n"
            else:
                drawn_parallelogram = drawn_parallelogram + " "*(x-1) + "*" + " "*(height-2) + "*" + "\n"
            x = x-1
    print(drawn_parallelogram)
    return drawn_parallelogram

def draw_trapezoid(height, outline):
    drawn_trapezoid = ""
    x = height
    if outline == False:
        for i in range(1,height+1):
            drawn_trapezoid = drawn_trapezoid +" "*(height-i) +"*"*height + "*"*(i-1)*2 +"\n"
            x = x-1
    else:
        for i in range(1,height+1):
            if (i==1)or (i==height):
                drawn_trapezoid = drawn_trapezoid +" "*(height-i) +"*"*height + "*"*(i-1)*2 +"\n"
            else:
                drawn_trapezoid = drawn_trapezoid +" "*(height-i) +"*" + " "*(height-2) + " "*(i-1)*2 + "*" +"\n"
            x = x-1
    print(drawn_trapezoid)
    return drawn_trapezoid

def draw(shape, height, outline):
    if shape.lower() == "pyramid":
        draw_pyramid(height, outline)
    if shape.lower() == "square":
        draw_square(height, outline)
    if shape.lower() == "triangle":
        draw_triangle(height, outline)
    if shape.lower() == "kite":
        draw_kite(height, outline)
    if shape.lower() == "parallelogram":
        draw_parallelogram(height, outline)
    if shape.lower() == "trapezoid":
        draw_trapezoid(height, outline)

# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = input("Outline only? (y/N): ")
    if outline.lower() in ("y", "yes"):
        return True
    elif outline.lower() in ("n", "no", ""):
        return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline() 
    draw(shape_param, height_param, outline_param)

