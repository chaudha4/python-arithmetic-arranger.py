class Rectangle:

    def __init__(self, width=0, height=0):
        self.w = width
        self.h = height

    def set_width(self, width):
        self.w = width

    def set_height(self, height):
        self.h = height

    def get_area(self):
        return self.w * self.h

    def get_perimeter(self):
        return (self.w * 2) +  (self.h * 2)

    def get_diagonal(self):
        return ((self.w  ** 2 + self.h  ** 2) ** .5)

    def get_picture(self):
        if (self.w > 50 or self.h > 50):
            return "Too big for picture."
        
        return ("*" * self.w + "\n") * self.h

    def get_amount_inside(self, other):
        if (other.w > self.w or other.h > self.h):
            return 0
        
        nw = self.w // other.w
        nh = self.h // other.h

        return nw * nh

    def __repr__(self):
        return "Rectangle(width={}, height={})".format(self.w, self.h)


class Square(Rectangle):
    def __init__(self, side=0):
        self.w = side
        self.h = side

    def __repr__(self):
        return "Square(side={})".format(self.w)

    def set_width(self, side):
        self.w = side
        self.h = side

    def set_height(self, side):
        self.w = side
        self.h = side

    def set_side(self, side):
        self.w = side
        self.h = side

if __name__ == "__main__":
    rect1 = Rectangle(51,3)
    print(rect1)
