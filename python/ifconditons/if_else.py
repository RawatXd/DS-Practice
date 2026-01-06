indian = [ "samosa","jalebi","pakoda"]
chinese = ['momos','fried rice','chilly potato']
italian = [ 'pizza','bburger', 'pasta']

dish = input("Enter a dish : ")

if dish in indian:
    print(f"{dish} is Indian Dish ")

elif dish in chinese :
    print(f"{dish} is Chinese Dish")

elif dish in italian:
    print(f"{dish} is Italian Dish ")
else :
    print(f"{dish} is not Available in Cuisine")