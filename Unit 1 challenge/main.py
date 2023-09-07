def leapyear(n):
  if(n%4==0 and n%100!=0) or n%400==0:
    print("is leap year")  
  else:
    print("not leapyear")
n=int(input("Enter a year:"))
tot=leapyear(n)