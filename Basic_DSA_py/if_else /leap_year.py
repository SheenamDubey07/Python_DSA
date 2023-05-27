n = int(input())
if (n%4==0 and n%100!=0) or (n%400==0 and n%100!=0) :
    print("It is Lear Year")

else:
    print("It is not a Leap Year")
   