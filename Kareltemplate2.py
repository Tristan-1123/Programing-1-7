
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
▼
▼
▼
▼
▼
▼
▼
▼
▼
▼
▼
▼
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
      
  
def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.h()
        
    pass
  
  
if __name__ == "__main__":
    run_karel_program()