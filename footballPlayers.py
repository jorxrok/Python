# Create a list of 10 random players in a football team, display the list, sort it, and remove the first item with the specified value.
football_players =["ronaldo","messi","neymar","suarez"]
print("list of football players",football_players)
football_players.sort()
print("Sorted list of foot ball players: ",football_players)
to_remove = input("Name of the player to remove: ")
if to_remove in football_players:
    football_players.remove(to_remove)
    print("updated list of football players",football_players)
else:
    print("Player not found")
