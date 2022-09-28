from stanfordkarel import *


class ktools:

    def m(self):
        """Shorthand for Move"""
        move()

    def tl(self):
        """Turn Left"""
        turn_left()

    def tr(self):
        """Turn Right"""
        self.tl()
        self.tl()
        self.tl()

    def ta(self):
        """Turn Around"""
        self.tl()
        self.tl()

    def pick(self):
        """Pick Beeper"""
        pick_beeper()

    def put(self):
        """Put Beeper"""
        put_beeper()

    def put2(self):
        """Put 2 beepers in a line"""
        self.put()
        self.m()
        self.put()

    def put5(self):
        """Put 5 beepers in a line"""
        self.put2()
        self.m()
        self.put2()
        self.m()
        self.put()

    def h(self):
        """Print H using beepers"""
        self.tl()
        self.put5()
        self.tr()
        self.m()
        self.m()
        self.m()
        self.tr()
        self.put5()
        self.ta()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.put2()
        self.tl()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.m()
        self.m()
        self.m()

    def fic(self) -> bool:
        """Front is Clear"""
        return front_is_clear()

    def fib(self) -> bool:
        """Front is Blocked"""
        return not self.fic()

    def ric(self) -> bool:
        """Right is Clear"""
        self.tr()
        if self.fic():
            self.tl()
            return True
        self.tl()
        return False

    def rib(self) -> bool:
        """Right is Blocked"""
        return not self.ric()

    def mazemove(self):
        """Maze Move"""
        if self.fib():
            self.tl()
        else:
            self.m()
            if self.ric():
                self.tr()
                self.m()
                if self.ric():
                    self.tr()
                    self.m()
        pass

    def mm(self, num):
        """Move Multiple"""
        for number in range(0, num):
            self.m()

    def putm(self, num):
        """Put Multiple"""
        for i in range(num - 1):
            self.put()
            self.m()
        self.put()

    def pickm(self, num):
        """Pick Multiple"""
        for _ in range(num - 1):
            self.pick()
            self.m()
        self.pick()


    def pos(self):
        self.mm(5)
        self.tl()

    def k34(self):
     self.pos()
     self.m()
     self.pick()
     self.mm(2)
     self.pick()
     self.mm(2)
     self.pick()
     self.mm(2)
     self.pick()
     self.ta()
     self.m()
     self.tr()
     self.m()
     self.pick()
     self.tl()
     self.m()
     self.tr()
     self.m()
     self.pick()
     self.tl()
     self.m()
     self.tr()
     self.m()
     self.pick()
     self.tl()
     self.m()
     self.tl()
     self.m()
     self.pick()
     self.tr()
     self.m()
     self.tr()
     self.tr()
     self.tr()
     self.m()
     self.pick()
     self.tl()
     self.mm(2)
     self.pick()
     self.tr()
     self.mm(2)
     self.pick()
     self.mm(2)
     self.pick()
     self.tl()
     self.m()
     self.tl()
     self.m()
     self.pick()
     self.m()
     self.tr()
     self.m()
     self.pick()
     self.ta()
     self.mm(4)
     self.pick()
     self.ta()
     self.m()
     self.tr()
     self.m()
     self.pick()



def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.k34()
    pass


if __name__ == "__main__":
    run_karel_program()
