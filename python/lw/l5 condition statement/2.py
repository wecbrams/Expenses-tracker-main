costprice =int(input("enter the cp: "))
sellingprice =int(input("enter the sp: "))

if(sellingprice>costprice):
  print("profit")
  pt=sellingprice-costprice
  print(pt)
else :
  print("No profit")
  pt=costprice - sellingprice
  print("-",pt)