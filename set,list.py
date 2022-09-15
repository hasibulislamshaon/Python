#name of city in bangladesh
bangladesh_city_name = ["Dhaka","Rajsahi","Sylet","Chittagong","Rangpur"]
print(bangladesh_city_name[0])

#append method to add some thing to the list at the end of the list 
bangladesh_city_name.append("Khulna")
print("Unsorted= ",bangladesh_city_name)

#sort method in list
bangladesh_city_name.sort()
print("Sorted= ",bangladesh_city_name)
print(f"All city list{bangladesh_city_name}")


#created a set
name=set()

#adding in the set
name.add(1)
name.add(2)
name.add("a")
name.add("a")
name.add(2)
name.add(4)

print(f"Set numbers {name}")
