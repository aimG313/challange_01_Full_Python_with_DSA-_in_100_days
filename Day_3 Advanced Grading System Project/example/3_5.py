mark_sub1 = int(input("Enter mark 1: "))
mark_sub2 = int(input("Enter mark 2: "))
mark_sub3 = int(input("Enter mark 3: "))

total_percentage = ((mark_sub1 + mark_sub2 + mark_sub3)/300)*100

if(total_percentage>=40 and mark_sub1>=33 and mark_sub2>=33 and mark_sub2>=33):
  print("Your're Passed")

else:
  print("You're Failed")