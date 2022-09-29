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

        def lic(self) -> bool:
            """Left is Clear"""
            self.tl()
            if self.fic():
              self.tr()
              return True
        self.tr()
        return False

    def lib(self) -> bool:
        return not self.lic()

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

    def SOB(self) -> bool:
        """standing on beeper"""
        return beepers_present()

    def jump(self):
        """Jume for 510"""
        while self.fic():
            self.m()
        self.tl()
        while self.rib():
            self.m()
        self.tr()
        self.m()
        self.tr()
        while self.fic():
            self.m()
        self.tl()

    def find(self):
        """find 515"""
        while not facing_north():
            self.tl()
        self.m
        if not self.SOB():
            self.tl()
            self.m()
            self.tl()
            self.m()
        for _ in range(2):
            self.m()
            self.tl()
            self.m()

        pass

    def k411(self, num):
        for _ in range(num - 1):
            self.m()
            if self.fic():
                if self.ric():
                    if self.lic():
                        self.put()
                        self.ta()
                        self.m()
                        self.tl()
                        self.m()
                        self.tl()
            else:
                self.ta()
                self.m()
                self.tl()
                self.m()
                self.tl()


def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.tl()
    kt.k411(9)
    pass


if __name__ == "__main__":
    run_karel_program()
