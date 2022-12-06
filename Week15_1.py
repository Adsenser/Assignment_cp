import math

class dot:
    x = 0
    y = 0


dot_input1 = dot()
dot_input2 = dot()

dot_input1.x = int(input("첫번째 점의 x값"))
dot_input1.y = int(input("첫번째 점의 y값"))

dot_input2.x = int(input("두번째 점의 x값"))
dot_input2.y = int(input("두번째 점의 y값"))


class line:
    line_width = 0
    line_height = 0

    def __init__(self):
        self.x1 = dot_input1.x
        self.x2 = dot_input2.x
        self.y1 = dot_input1.y
        self.y2 = dot_input2.y

    def line_calculate(self):
        self.line_width = abs((self.x1) - (self.x2))
        self.line_height = abs((self.y1) - (self.y2))
        print(math.sqrt(self.line_width ** 2 + self.line_height ** 2))


print_line = line()
print_line.line_calculate()
