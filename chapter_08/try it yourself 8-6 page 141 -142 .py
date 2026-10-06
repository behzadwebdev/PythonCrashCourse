######################8-6
def city_country(city, country):
    return f"{city.title()}, {country.title()} "
print('santiago', 'chile')
print('paris', 'france')
print('tokyo', 'japan')
#######################8-7
def make_album(artist, title, num_songs=None):
    album = {'artist': artist.title(), 'title': title.title()}
    if num_songs:
        album['songs'] = num_songs
    return album
album1 = make_album('beatles', 'abbey road')
album2 = make_album('pink floyd', 'the dark side of the moon')
album3 = make_album('radiohead', 'ok computer', num_songs=12)
print(album1)
print(album2)
print(album3)
####################  8-8
def make_album(artist, title, num_songs=None):
    album = {'artist': artist.title(), 'title': title.title()}
    if num_songs:
        album['songs'] = num_songs
    return album
while True:
    print("\nEnter album informatin (or 'q' to quit)")
    artist = input("Artist name:")
    if artist.lower() == 'q':
        break
    title = input("Album title:")
    if title.lower() == 'q':
        break
    num_songs_input = input("Number of songs (press Enter to skip):")
    if num_songs_input:
        album = make_album(artist, title, int(num_songs_input))
    else:
        album = make_album(artist, title)
    print("\nAlbum created:", album)
