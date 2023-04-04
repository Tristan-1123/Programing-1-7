def main():
  Weight = int(input("Enter Weight of package:"))
  length = int(input("Enter Length of package:"))
  Width = int(input("Enter Width of package:"))
  Height = int(input("Enter Height of package:"))
  Size = Height * Width * length
  if Weight > 27 and Size > 0.1:
    print("Too Heavy and Too Large")
  elif Weight > 27:
    print("Too Heavy")
  elif Size > 0.1:
    print("Too Large")
  else:
    print("Package Viable")
  pass
if __name__ == "__main__":
  main()
  
  

