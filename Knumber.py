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
       
     

def rib(self) -> bool:
  return not self.ric()




def mm(self,num):
  """Move Multiple"""
  for number in range (0, num):
    self.m()

def putm(self, num):
  """put multiple"""
  for i in range(num -1 ):
    self.put()
    self.m()
    self.put()

def pickm(self,num):
  """pick multiple"""
  for _ in range(num-1):
    self.pick()
    self.m()
    self.pick()



def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.mm(5)
    kt.ta()
    kt.putm(5)
    kt.tl()
    kt.mm(2)


    pass



if __name__ == "__main__":
    run_karel_program()