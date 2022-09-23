from stanfordkarel import *


class ktools:
  def m(self):
    """Shorthand for Move"""
    move()
    
  def tl(self):
    """ Turn left"""
    turn_left()
  
  def tr(self):
    """Turn Right"""
    Self.tl()
    Self.tl()
    Self.tl()

  def ta(self):
    """ Turn around"""
    Self.tl()
    Self.tl()

  def pick(self):
    pick_beeper()

  def put(self):
    put_beeper()

  def put2(self):
    """Put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """put 5 beepers in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def h(self):
    """print H with beepers"""
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
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()

  def e(self):
    self.tr()
    self.m()
    self.ta()
    self.put5()
    """" From alley 6 """
    self.tr()
    self.m()
    self.put2()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    """Row 3 Colum 8 facing right"""
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.m()
    self.m()

  def l(self): 
    self.tl()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.m()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.m()
    self.m()
    

  def o(self):
    self.tl() 
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.put5()
    
   
  
def main(self):  
     """ Karel code goes here! """
     kt = ktools()
     kt.h()
     kt.e()
     kt.l()
     kt.l()
     kt.o()
     pass


if __name__ == "__main__":
    run_karel_program()