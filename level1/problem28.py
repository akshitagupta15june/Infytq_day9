#PF-Tryout
def sing_99_bottles():
   for i in range(99,-1,-1):
        if i == 0:
            print ("No more bottles of beer on the wall, no more bottles of beer.")
            print ("Go to the store and buy some more,99 bottles of beer on the wall")
        elif i == 1:
            print ("1 bottle of beer on the wall, 1 bottle of beer.")
            print ("Take one down and pass it around, no more bottles of beer to go")
        elif i == 2:
            print (i," bottles of beer on the wall, ",i," bottles of beer.")
            print ("Take one down and pass it around, ",i-1," bottle of beer on the wall.")
        else :
            print (i," bottles of beer on the wall, ",i," bottles of beer.")
            print ("Take one down and pass it around, ",i-1," bottles of beer on the wall.")
   
sing_99_bottles()
