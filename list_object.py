array=[1,2,3,5,5,6,7]
array2=[100,200,300,100,200,500]
list1=["cow","cat"]
list2=["sheep","mouse"]
#start of insert method
array.insert(2,5)
print("in place 2 add 5",array)
array.insert(1,"t")
print("in place 1 add t",array)
#End of insert method
#Expend method started
list1.extend(list2)
print(list1)
array2.extend(array)
print(array2)
#end of extand method
#start of adding method with append
array.append(3)
print(array)
list1.append("copycat")
print(list1)
#End of append method
#start of remove method
array.remove(5)
print(array)
list1.remove("cow")
print(list1)
#end of remove method
#Start of pop method
list1.pop(2)
print(list1)
array.pop(4)
print(array)
#ENd of pop method
#Start of clear method
"""list1.clear()
print(list1)"""
#ENd of clear
#start of index method
print(array.index(5))
print(list1.index("cat"))
#end of inxex
#start of count
print(array2.count(100))
#end of count
#start reverse method
array.reverse()
print (array)


