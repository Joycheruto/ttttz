captain_room  = "a"

# the_rest = *b ``
# *b = [2,3,4]

lst_of_rooms = []

while True:
    room = input("enter the room number: ")
    if room.lower() =="a":
        continue
    lst_of_rooms.append(room) 
      #i now have the rooms for allexcept the captain
    print("all the rooms except for the captain: ",lst_of_rooms)

    print(lst_of_rooms)


    lst_of_rooms.append(captain_room)
    if captain_room in lst_of_rooms:
        print("found the captains room: ",captain_room)
  


