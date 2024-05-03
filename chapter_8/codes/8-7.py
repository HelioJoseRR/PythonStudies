def make_album(artist, album, tracks=None):
    if tracks:
        return {"artist": artist, "album": album, "tracks": tracks}
    else:
        return {"artist": artist, "album": album}


print(make_album("The Beatles", "Abbey Road"))
print(make_album("The Beatles", "Let It Be"))
print(make_album("The Beatles", "Sgt. Pepper's Lonely Hearts Club Band"))

print(make_album("The Beatles", "Abbey Road", 17))