costprice = int(input("How much did you buy the item for? : "))
sellingprice = int(input("\n How much did you sell the item for? :"))

if sellingprice > costprice : 
    print("\n You have made a profit of " , sellingprice - costprice)
else :
    print("You have not made profit")
