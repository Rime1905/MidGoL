from tkinter import *
from random import randint

class Ground:
    def __init__(self, c, row, col, width, height):
        self.c = c
        self.array = []
        self.array2 = []
        self.row = row + 2
        self.col = col + 2
        self.width = width
        self.height = height
        self.count = 0
        for u in range(self.row):
            self.array.append([])
            self.array2.append([])
            for d in range(self.col):
                self.array[u].append(0)
                self.array2[u].append(0)
                if (randint(1, 20) == 1) and self.array[u][d] == 0:
                    self.array[u][d] = 1
                elif (randint(1, 7) == 1) and self.array[u][d] == 0:
                    self.array[u][d] = 2
                elif (randint(1, 5) == 1) and self.array[u][d] == 0:
                    self.array[u][d] = 3
        self.array[1 + 10][1 + 10] = 1
        self.array[1 + 10][3 + 10] = 1
        self.array[2 + 10][3 + 10] = 1
        self.array[2 + 10][2 + 10] = 1
        self.array[3 + 10][2 + 10] = 1
        self.draw()
        for u in range(1, self.row - 1):
            for d in range(1, self.col - 1):
                print(self.array[u][d], end="")
            print()

    def rules(self):
        for u in range(1, self.row - 1):
            for d in range(1, self.col - 1):

                if self.array2[u][d] == 0:
                    if self.array[u][d] == 1:
                        un = 0
                        if self.array[u - 1][d - 1] == 1:
                            un = un + 1
                        if self.array[u - 1][d] == 1:
                            un = un + 1
                        if self.array[u - 1][d + 1] == 1:
                            un = un + 1
                        if self.array[u][d + 1] == 1:
                            un = un + 1
                        if self.array[u + 1][d + 1] == 1:
                            un = un + 1
                        if self.array[u + 1][d + 1] == 1:
                            un = un + 1
                        if self.array[u + 1][d] == 1:
                            un = un + 1
                        if self.array[u + 1][d - 1] == 1:
                            un = un + 1
                        if self.array[u][d - 1] == 1:
                            un = un + 1
                        if un > 5:
                            self.array[u][d] = 0
                            self.array2[u][d] = 1
                        elif self.array[u - 1][d] == 2 and self.array2[u - 1][d] == 0:
                            self.array[u - 1][d] = 1
                            self.array[u][d] = 0
                            self.array2[u][d] = 1
                            self.array2[u - 1][d] = 1
                        elif self.array[u][d + 1] == 2 and self.array2[u][d + 1] == 0:
                            self.array[u][d + 1] = 1
                            self.array[u][d] = 0
                            self.array2[u][d] = 1
                            self.array2[u][d + 1] = 1
                        elif self.array[u + 1][d + 1] == 2 and self.array2[u + 1][d + 1] == 0:
                            self.array[u + 1][d + 1] = 1
                            self.array[u][d] = 0
                            self.array2[u][d] = 1
                            self.array2[u + 1][d + 1] = 1
                        elif self.array[u + 1][d - 1] == 2 and self.array2[u + 1][d - 1] == 0:
                            self.array[u + 1][d - 1] = 1
                            self.array[u][d] = 0
                            self.array2[u][d] = 1
                            self.array2[u + 1][d - 1] = 1
                        if randint(1, 5) == 1:
                            if self.array[u - 1][d - 1] == 1 and self.array2[u - 1][d - 1] == 0:
                                if self.array[u - 1][d] == 0 and self.array2[u - 1][d] == 0:
                                    self.array[u - 1][d] = 1
                                    self.array2[u - 1][d - 1] = 1
                                    self.array2[u - 1][d] = 1
                                    self.array2[u][d] = 1
                                elif self.array[u][d - 1] == 0 and self.array2[u][d - 1] == 1:
                                    self.array[u][d - 1] = 1
                                    self.array2[u - 1][d - 1] = 1
                                    self.array2[u][d] = 1
                                    self.array2[u][d - 1] = 1

                            elif self.array[u - 1][d] == 1 and self.array2[u - 1][d] == 0:
                                if self.array[u - 1][d - 1] == 0 and self.array2[u - 1][d - 1] == 0:
                                    self.array[u - 1][d - 1] = 1
                                    self.array2[u - 1][d] = 1
                                    self.array2[u][d] = 1
                                    self.array2[u - 1][d - 1] = 1
                                elif self.array[u - 1][d + 1] == 0 and self.array2[u - 1][d + 1] == 0:
                                    self.array[u - 1][d + 1] = 1
                                    self.array2[u][d] = 1
                                    self.array2[u - 1][d] = 1
                                    self.array2[u - 1][d + 1] = 1
                                elif self.array[u][d + 1] == 1 and self.array2[u][d + 1] == 0:
                                    self.array[u][d + 1] = 1
                                    self.array2[u][d + 1] = 1
                                    self.array2[u][d] = 1
                                    self.array2[u][d + 1] = 1

                            elif self.array[u - 1][d + 1] == 1 and self.array2[u - 1][d + 1] == 0:
                                if self.array[u - 1][d] == 0 and self.array2[u - 1][d] == 0:
                                    self.array[u - 1][d] = 1
                                    self.array2[u - 1][d] = 1
                                    self.array2[u][d] = 1
                                    self.array2[u - 1][d + 1] = 1
                                elif self.array[u][d + 1] == 0 and self.array2[u][d + 1] == 0:
                                    self.array[u][d + 1] = 1
                                    self.array2[u][d + 1] = 1
                                    self.array2[u][d] = 1
                                    self.array[u - 1][d + 1] = 1
                            elif self.array[u][d + 1] == 1 and self.array2[u][d + 1] == 0:
                                if self.array[u - 1][d] == 0 and self.array2[u - 1][d] == 0:
                                    self.array[u - 1][d] = 1
                                    self.array2[u - 1][d] = 1
                                    self.array2[u][d] = 1
                                    self.array2[u][d + 1] = 1
                                elif self.array[u - 1][d + 1] == 0 and self.array2[u - 1][d + 1] == 0:
                                    self.array[u - 1][d + 1] = 1
                                    self.array2[u - 1][d + 1] = 1
                                    self.array2[u][d] = 1
                                    self.array2[u][d + 1] = 1
                                elif self.array[u + 1][d + 1] == 0 and self.array2[u + 1][d + 1] == 0:
                                    self.array[u + 1][d + 1] = 1
                                    self.array2[u + 1][d + 1] = 1
                                    self.array2[u][d] = 1
                                    self.array2[u][d + 1] = 1
                            elif self.array[u + 1][d + 1] == 1 and self.array2[u + 1][d + 1] == 0:
                                if self.array[u][d + 1] == 0 and self.array2[u][d + 1] == 0:
                                    self.array[u][d + 1] = 1
                                    self.array2[u][d + 1] = 1
                                    self.array2[u][d] = 1
                                    self.array2[u + 1][d + 1] = 1
                                elif self.array[u + 1][d] == 0 and self.array2[u + 1][d] == 0:
                                    self.array[u + 1][d] = 1
                                    self.array2[u + 1][d] = 1
                                    self.array2[u][d] = 1
                                    self.array2[u + 1][d + 1] = 1
                            elif self.array[u + 1][d] == 1 and self.array2[u + 1][d] == 0:
                                if self.array[u][d + 1] == 0 and self.array2[u][d + 1] == 0:
                                    self.array[u][d + 1] = 1
                                    self.array2[u][d + 1] = 1
                                    self.array2[u][d] = 1
                                    self.array2[u + 1][d] = 1
                                elif self.array[u + 1][d + 1] == 0 and self.array2[u + 1][d + 1] == 0:
                                    self.array[u + 1][d + 1] = 1
                                    self.array2[u + 1][d + 1] = 1
                                    self.array2[u][d] = 1
                                    self.array2[u + 1][d] = 1
                                elif self.array[u][d - 1] == 0 and self.array2[u][d - 1] == 0:
                                    self.array[u][d - 1] = 1
                                    self.array2[u][d - 1] = 1
                                    self.array[u][d] = 1
                                    self.array[u + 1][d] = 1
                            elif self.array[u + 1][d - 1] == 1 and self.array2[u + 1][d - 1] == 0:
                                if self.array[u][d - 1] == 0 and self.array2[u][d - 1] == 0:
                                    self.array[u][d - 1] = 1
                                    self.array2[u][d - 1] = 1
                                    self.array2[u][d] = 1
                                    self.array2[u + 1][d - 1] = 1
                                elif self.array[u + 1][d] == 0 and self.array2[u + 1][d] == 0:
                                    self.array[u + 1][d] = 1
                                    self.array2[u + 1][d] = 1
                                    self.array2[u][d] = 1
                                    self.array2[u + 1][d - 1] = 1
                            elif self.array[u][d - 1] == 1 and self.array2[u][d - 1] == 0:
                                if self.array[u - 1][d] == 0 and self.array2[u - 1][d] == 0:
                                    self.array[u - 1][d] = 1
                                    self.array2[u - 1][d] = 1
                                    self.array2[u][d] = 1
                                    self.array2[u][d + 1] = 1
                                elif self.array[u - 1][d - 1] == 0 and self.array2[u - 1][d - 1] == 0:
                                    self.array[u - 1][d - 1] = 1
                                    self.array2[u - 1][d - 1] = 1
                                    self.array2[u][d] = 1
                                    self.array2[u][d - 1] = 1
                                elif self.array[u + 1][d] == 0 and self.array2[u + 1][d] == 0:
                                    self.array[u + 1][d] = 1
                                    self.array2[u + 1][d] = 1
                                    self.array2[u][d] = 1
                                    self.array2[u][d + 1] = 1
                                elif self.array[u + 1][d - 1] == 0 and self.array2[u + 1][d - 1] == 0:
                                    self.array[u + 1][d - 1] = 1
                                    self.array2[u + 1][d - 1] = 1
                                    self.array2[u][d] = 1
                                    self.array2[u][d - 1] = 1


        for u in range(1, self.row - 1):
            for d in range(1, self.col - 1):
                if self.array2[u][d] == 0:

                    if self.array[u][d] == 2:
                        if self.array[u - 1][d - 1] == 3 and self.array2[u - 1][d - 1] == 0:
                            self.array[u - 1][d - 1] = 2
                            self.array[u][d] = 0
                            self.array2[u][d] = 1
                            self.array2[u - 1][d - 1] = 1
                        elif self.array[u - 1][d] == 3 and self.array2[u - 1][d] == 0:
                            self.array[u - 1][d] = 2
                            self.array[u][d] = 0
                            self.array2[u][d] = 1
                            self.array2[u - 1][d] = 1
                        elif self.array[u + 1][d + 1] == 3 and self.array2[u + 1][d + 1] == 0:
                            self.array[u + 1][d + 1] = 2
                            self.array[u][d] = 0
                            self.array2[u][d] = 1
                            self.array2[u + 1][d + 1] = 1
                        elif self.array[u + 1][d] == 3 and self.array2[u + 1][d] == 0:
                            self.array[u + 1][d] = 2
                            self.array[u][d] = 0
                            self.array2[u][d] = 1
                            self.array2[u + 1][d] = 1
                        elif self.array[u + 1][d - 1] == 3 and self.array2[u + 1][d - 1] == 0:
                            self.array[u + 1][d - 1] = 2
                            self.array[u][d] = 0
                            self.array2[u][d] = 1
                            self.array2[u + 1][d - 1] = 1
                        elif self.array[u][d - 1] == 3 and self.array2[u][d - 1] == 0:
                            self.array[u][d - 1] = 2
                            self.array[u][d] = 0
                            self.array2[u][d] = 1
                            self.array2[u][d - 1] = 1
                        elif self.array[u - 1][d - 1] == 2 and self.array2[u - 1][d - 1] == 0:  # pop
                            if self.array[u - 1][d] == 0 and self.array2[u - 1][d] == 0:
                                self.array[u - 1][d] = 2
                                self.array2[u - 1][d - 1] = 1
                                self.array2[u - 1][d] = 1
                                self.array2[u][d] = 1
                            elif self.array[u][d - 1] == 0 and self.array2[u][d - 1] == 1:
                                self.array[u][d - 1] = 2
                                self.array2[u - 1][d - 1] = 1
                                self.array2[u][d] = 1
                                self.array2[u][d - 1] = 1

                        elif self.array[u - 1][d] == 2 and self.array2[u - 1][d] == 0:
                            if self.array[u - 1][d - 1] == 0 and self.array2[u - 1][d - 1] == 0:
                                self.array[u - 1][d - 1] = 2
                                self.array2[u - 1][d] = 1
                                self.array2[u][d] = 1
                                self.array2[u - 1][d - 1] = 1
                            elif self.array[u][d - 1] == 0 and self.array2[u][d - 1] == 0:
                                self.array[u][d - 1] = 2
                                self.array2[u][d] = 1
                                self.array2[u][d - 1] = 1
                                self.array2[u - 1][d] = 1
                            elif self.array[u - 1][d + 1] == 0 and self.array2[u - 1][d + 1] == 0:
                                self.array[u - 1][d + 1] = 2
                                self.array2[u][d] = 1
                                self.array2[u - 1][d] = 1
                                self.array2[u - 1][d + 1] = 1
                            elif self.array[u][d + 1] == 1 and self.array2[u][d + 1] == 0:
                                self.array[u][d + 1] = 2
                                self.array2[u][d + 1] = 1
                                self.array2[u][d] = 1
                                self.array2[u][d + 1] = 1

                        elif self.array[u - 1][d + 1] == 2 and self.array2[u - 1][d + 1] == 0:
                            if self.array[u - 1][d] == 0 and self.array2[u - 1][d] == 0:
                                self.array[u - 1][d] = 2
                                self.array2[u - 1][d] = 1
                                self.array2[u][d] = 1
                                self.array2[u - 1][d + 1] = 1
                            elif self.array[u][d + 1] == 0 and self.array2[u][d + 1] == 0:
                                self.array[u][d + 1] = 2
                                self.array2[u][d + 1] = 1
                                self.array2[u][d] = 1
                                self.array[u - 1][d + 1] = 1
                        elif self.array[u][d + 1] == 2 and self.array2[u][d + 1] == 0:
                            if self.array[u - 1][d] == 0 and self.array2[u - 1][d] == 0:
                                self.array[u - 1][d] = 2
                                self.array2[u - 1][d] = 1
                                self.array2[u][d] = 1
                                self.array2[u][d + 1] = 1
                            elif self.array[u - 1][d + 1] == 0 and self.array2[u - 1][d + 1] == 0:
                                self.array[u - 1][d + 1] = 2
                                self.array2[u - 1][d + 1] = 1
                                self.array2[u][d] = 1
                                self.array2[u][d + 1] = 1
                            elif self.array[u + 1][d] == 0 and self.array2[u + 1][d] == 0:
                                self.array[u + 1][d] = 2
                                self.array2[u + 1][d] = 1
                                self.array2[u][d] = 1
                                self.array2[u][d + 1] = 1
                            elif self.array[u + 1][d + 1] == 0 and self.array2[u + 1][d + 1] == 0:
                                self.array[u + 1][d + 1] = 2
                                self.array2[u + 1][d + 1] = 1
                                self.array2[u][d] = 1
                                self.array2[u][d + 1] = 1
                        elif self.array[u + 1][d + 1] == 2 and self.array2[u + 1][d + 1] == 0:
                            if self.array[u][d + 1] == 0 and self.array2[u][d + 1] == 0:
                                self.array[u][d + 1] = 2
                                self.array2[u][d + 1] = 1
                                self.array2[u][d] = 1
                                self.array2[u + 1][d + 1] = 1
                            elif self.array[u + 1][d] == 0 and self.array2[u + 1][d] == 0:
                                self.array[u + 1][d] = 2
                                self.array2[u + 1][d] = 1
                                self.array2[u][d] = 1
                                self.array2[u + 1][d + 1] = 1
                        elif self.array[u + 1][d] == 2 and self.array2[u + 1][d] == 0:
                            if self.array[u][d + 1] == 0 and self.array2[u][d + 1] == 0:
                                self.array[u][d + 1] = 2
                                self.array2[u][d + 1] = 1
                                self.array2[u][d] = 1
                                self.array2[u + 1][d] = 1
                            elif self.array[u + 1][d + 1] == 0 and self.array2[u + 1][d + 1] == 0:
                                self.array[u + 1][d + 1] = 2
                                self.array2[u + 1][d + 1] = 1
                                self.array2[u][d] = 1
                                self.array2[u + 1][d] = 1
                            elif self.array[u][d - 1] == 0 and self.array2[u][d - 1] == 0:
                                self.array[u][d - 1] = 2
                                self.array2[u][d - 1] = 1
                                self.array2[u][d] = 1
                                self.array2[u + 1][d] = 1
                            elif self.array[u + 1][d - 1] == 0 and self.array2[u + 1][d - 1] == 0:
                                self.array[u + 1][d - 1] = 2
                                self.array2[u + 1][d - 1] = 1
                                self.array2[u][d] = 1
                                self.array2[u + 1][d] = 1
                        elif self.array[u + 1][d - 1] == 2 and self.array2[u + 1][d - 1] == 0:
                            if self.array[u][d - 1] == 0 and self.array2[u][d - 1] == 0:
                                self.array[u][d - 1] = 2
                                self.array2[u][d - 1] = 1
                                self.array2[u][d] == 1
                                self.array2[u + 1][d - 1] = 1
                            elif self.array[u + 1][d] == 0 and self.array2[u + 1][d] == 0:
                                self.array[u + 1][d] = 2
                                self.array2[u + 1][d] = 1
                                self.array2[u][d] = 1
                                self.array2[u + 1][d - 1] = 1
                        elif self.array[u][d - 1] == 2 and self.array2[u][d - 1] == 0:
                            if self.array[u - 1][d] == 0 and self.array2[u - 1][d] == 0:
                                self.array[u - 1][d] = 2
                                self.array2[u - 1][d] = 1
                                self.array2[u][d] = 1
                                self.array2[u][d + 1] = 1
                            elif self.array[u - 1][d - 1] == 0 and self.array2[u - 1][d - 1] == 0:
                                self.array[u - 1][d - 1] = 2
                                self.array2[u - 1][d - 1] = 1
                                self.array2[u][d] = 1
                                self.array2[u][d - 1] = 1
                            elif self.array[u + 1][d] == 0 and self.array2[u + 1][d] == 0:
                                self.array[u + 1][d] = 2
                                self.array2[u + 1][d] = 1
                                self.array2[u][d] = 1
                                self.array2[u][d + 1] = 1
                            elif self.array[u + 1][d - 1] == 0 and self.array2[u + 1][d - 1] == 0:
                                self.array[u + 1][d - 1] = 2
                                self.array2[u + 1][d - 1] = 1
                                self.array2[u][d] = 1
                                self.array2[u][d - 1] = 1

        for u in range(1, self.row - 1):
            for d in range(1, self.col - 1):
                self.array2[u][d] = 0
                if randint(1, 50) == 1 and self.array[u][d] == 0:
                    self.array[u][d] = 3

    def print_ground(self):
        for u in range(self.row):
            for d in range(self.col):
                print(self.array[u][d], end="")
            print()

    def draw(self):
        sizen = self.width // (self.row - 2)
        sizem = self.height // (self.col - 2)
        for u in range(1, self.row - 1):
            for d in range(1, self.col - 1):
                print(self.array[u][d], end="")
            print()
        for u in range(1, self.row - 1):
            for d in range(1, self.col - 1):
                if (self.array[u][d] == 1):
                    color = "#03DDFF"
                elif (self.array[u][d] == 2):
                    color = "#0334FF"
                elif (self.array[u][d] == 3):
                    color = "#03ECFF"
                else:
                    color = "white"
                self.c.create_rectangle((u - 1) * sizen, (d - 1) * sizem, (u) * sizen, (d) * sizem, fill=color)
        try:
            if self.running is True:
                self.rules()
        except AttributeError:
            pass
        self.c.after(500, self.draw)

    def startgame(self, event):
        """Start the game."""
        self.running = True
        print('running')

    def stopgame(self, event):
        """Stop the game."""
        self.running = False
        print('''
              not running
              ''')

key = Tk()
key.geometry("400x400")
c = Canvas(key, width=400, height=400)
c.pack()


f = Ground(c, 40, 40, 400, 400)

key.bind('<space>', f.startgame)  # space
key.bind('s', f.stopgame)  # s


key.mainloop()

# Press Space to start game and S to stop


