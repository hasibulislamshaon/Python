from cmath import pi


number=int(input("1=circle \n2=rectangle\n3=Triangle\n4=cube\n"))

if number<5:
 if number==3:
  hight0 =int(input("Give the hight value = "))
  base0 = int(input("Give the base value = "))
  def name(hight,base):
      area=float(.5*(hight*base))
  
      return area
  
  print(name(hight0,base0))
 elif number==2:
  lenth0 =int(input("Give the lenth value = "))
  bredth0 = int(input("Give the bredth value = "))
  def name(benth,bredth):
      area=(benth*bredth)
  
      return area
  
  print(name(lenth0,bredth0))
 
 elif number==1:
  radious0 = int(input("Give the radious value = "))
  def name(radious):
      area=(pi*(radious*radious))
  
      return area
  print(name(radious0))
 elif number==4:
  side0 = int(input("Give the radious value = "))
  def name(side):
      area=(6*(side*side))
 
      return area 
  print(name(side0))
else:
    print("Give the appropriate value") 
