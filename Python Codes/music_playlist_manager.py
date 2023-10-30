"""
Music Playlist Manager in python
"""

print("Welcome to Music Playlist Manager!")

menu = {
    "a": "Add a song to the playlist",
    "b": "Remove a song from the playlist",
    "c": "View the currect playlist",
    "d": "Quit",
}

# empty list
playlist = []

while True:
    choice = str(input("enter your choice : "))
    print(choice)
    if choice == "a":
        add_song = str(input("Enter the song name= "))
        playlist.append(add_song)
        print(f"{add_song} has benn added to your playlist")
    elif choice == "b":
        if not playlist:
            print("Empty playlist")
        elif playlist:
            remove_song = str(input("Enter the song name=  "))
            playlist.remove(remove_song)
    elif choice == "c":
        if not playlist:
            print("Playlist is empty")
        else:
            print("Current playlist: ")
            print(playlist)
    elif choice == "d":
        print("Quit!")
