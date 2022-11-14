eggs = int(input("Enter the total number of eggs: "))

dozens = eggs // 12

remainder = eggs % 12

if dozens > 0 and dozens < 4:
  cost = eggs * 0.50
  Rcost = remainder * (0.50 /12)
  FullCost = Rcost + cost
if dozens >= 4 and dozens < 6:
  cost = eggs * 0.45
  Rcost = remainder * (0.45 /12)
  FullCost = Rcost + cost
if dozens >= 6 and dozens < 11:
  cost = eggs * 0.40
  Rcost = remainder * (0.40 /12)
  FullCost = Rcost + cost
if dozens > 11:
  cost = eggs * 0.35
  Rcost = remainder * (0.35 /12)
  FullCost = Rcost + cost
print("The total cost of the dozens is $" + str(cost))
print("The total cost of the remainder of eggs is $" + str(Rcost))
print("The total cost of eggs is $" + str(FullCost))