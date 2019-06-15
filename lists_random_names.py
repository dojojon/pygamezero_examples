from random import randint

def get_name():
    name = first_names[ randint(0, len(first_names)-1)] + " " + last_names[ randint(0, len(last_names)-1)]
    return name

def get_name_2():
    name = pick_random(first_names) +" "+ pick_random(last_names)
    return name

def pick_random(list):
    index = randint(0, len(list)-1)
    return list[index]

first_names = [ "Jon", "James", "Susan" ]
last_names = [ "Smith", "Piper", "Jones", "Franks"]

print(first_names[0])
print(first_names[-1])
#print(first_names[20])

print("First Names", len(first_names))
print("Last Names", len(last_names))

player_one = get_name_2()
player_two = get_name_2()

print(player_one)
print(player_two)

players = []
while len(players) < 3:
    player = get_name_2()
    if player not in players:
        players.append(player)


print(players)

# list.remove removes first instance of an item
# list.pop removes item at index

players.insert(1, "Dr Smith")

print(players)


#replace item in a list

players[0] = "Bill Bates"


print(players)