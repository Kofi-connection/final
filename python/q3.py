def is_leap(year):
  if year%4!=0:
    return False
  if year%100==0 and  (year%400!=0):
    return False
  else:
    return True




year=raw_input("Enter a year:\n")

iyear=int (year)
if is_leap(iyear):
  
   print("It is a leap year")

else:
 print("It is not a leap year")

