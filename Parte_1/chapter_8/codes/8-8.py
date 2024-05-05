def make_album(artist, album, tracks=None):
    if tracks:
        return {"artist": artist, "album": album, "tracks": tracks}
    else:
        return {"artist": artist, "album": album}

while True:
    artist = input("Enter the artist name: ")
    if artist == "q":
        break
    album = input("Enter the album name: ")
    if album == "q":
        break
    print(make_album(artist, album))
    print("Enter 'q' to quit.")
    print("Enter 'Enter' to continue.")
    continue