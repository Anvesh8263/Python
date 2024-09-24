countries = ("India","Spain","Italy","England","Germany")
temp = list(countries)
temp.append("Russia") #add item
temp.pop(3) #remove item
temp[2]="Finland" #change item
countries=tuple(temp)
print(countries)



countries1 = ("India","pakistan","Australia","England","Germany")
countries2 = ("Indonesia","Sri Lanka","Italy","Austria","New Zealan")
 
south = countries1+countries2
print(south)

