rooms = {"A": 1, "B": 1}
position = "A"
while 1 in rooms.values():
    print("Vacuum is in room", position)
    if rooms[position] == 1:
        print("Cleaning room", position)
        rooms[position] = 0
    else:
        print("Room is already clean")
    if position == "A":
        position = "B"
    else:
        position = "A"
print("All rooms are clean!")
