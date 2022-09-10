people = int(input(f"How many people will be in a room?\n>"))
knowCheck = (input(f"Do you know exact square meters of room? Type y or n \n>"))
peoplePlurality = "people"
checkArea = people * 3
if people == 1:
    peoplePlurality = "guy"
  
if knowCheck == "y":
  area = int(input(f"What is area of the room?\n>"))
  maxPeople = int(area/3)
  if area > checkArea:
    print(f"Room is good for {people} {peoplePlurality}")
    print(f"Max count of people in this room is {maxPeople}")
  else:
    print(f"Room is not good for {people} {peoplePlurality}")
    print(f"Max count of people in this room is {maxPeople}")
else:
  lenth = int(input(f"What is the lenth of the room?\n>"))
  width = int(input(f"What is the width of the room?\n>"))
  area = lenth * width 
  checkArea = people * 3
  maxPeople = int(area/3)
  if area > checkArea:
    print(f"Room is good for {people} {peoplePlurality}")
    print(f"Max count of people in this room is {maxPeople}")
  else:
    print(f"Room is not good for {people} {peoplePlurality}")
    print(f"Max count of people in this room is {maxPeople}")
