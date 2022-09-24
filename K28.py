from stanfordkarel import *


class ktools:
  def m(self):
    """Shorthand for Move"""
    Move()
    
  def tl(self):
    """ Turn left"""
    turn_left()
  
  def tr(self):
    """Turn Right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
    """ Turn around"""
    self.tl()
    self.tl()

  def put(self):
    put_beeper()

  def pick(self):
    pick_beeper()

  def pick5(self):
     self.pick_beeper()
     self.m()
     self.pick_beeper()
     self.m()
     self.pick_beeper()
     self.m()
     self.pick_beeper()
     self.m()
     self.pick_beeper()
     
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
    

def fic(self) -> bool:
   """front is clear"""
   return front_is_clear()

def fib(self) -> bool:
   """Front is blocked"""
   return not self.fic()
  
def ric(self) -> bool:
   """right is clear"""
   self.tr()
   if self.fic():
     self.tl()
     return True
   self.tl()
   return False
  
def mazemove(self):
   if self.fib():
    self.tl()
   else: 
     self.m()
     if self.ric():
       self.tr()
       self.m()

def k28(self):
   self.m()
   self.m()
   self.tl()
   self.m()
   self.m()
   self.ta()
   self.pick5()
   self.tr()
   self.m()
   self.m()
   self.tr()
   self.m()
   self.m()
   self.tr()
   self.put5()
  
   



def rib(self) -> bool:
      return not self.ric()



def main():
      """ Karel code goes here! """
      kt = ktools()
      kt.k28()
      pass
  
if __name__ == "__main__":
    run_karel_program()