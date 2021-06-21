#

#This variable stores info about albums in this order:
#1. Album Title
#3. Genre/Subgenres
#2. Bandleader/Album artist
#3. Year Released
#4. Record Label
albums=[['Wave',['Jazz','Bossa Nova'],'Antonio Carlos Jobim',1967,'A&M'],
        ['Stone Flower',['Jazz','Bossa Nova'],
         'Antonio Carlos Jobim',1970,'A&M'],
        ['Tide',['Jazz','Bossa Nova'],'Antonio Carlos Jobim', 1970, 'A&M'],
        ['Out There',['Jazz','Post-Bop','Avant-Garde Jazz','Third Stream'],
         'Eric Dolphy', 1961, 'Prestige'],
        ['Naked City',['Jazz','Free Jazz','Grindcore','No Wave','Avant-Garde'],
         'John Zorn', 1990, 'Elektra'],
        ['New York, Fall 1974',['Jazz','Free Jazz','Avant-Garde Jazz',
                                'Free Improvisation','Contempary Classical'],
         'Anthony Braxton', 1974, 'Arista'],
        ['Creative Orchestra Music 1976',['Jazz','Free Jazz',
                                          'Avant-Garde Jazz'],
         'Anthony Braxton', 1976, 'Arista']]
#This variable stores the names of musicians along with their main instruments
players = [['Anthony Braxton', 'Alto Sax', 'Sopranino Sax', 'Contrabass Sax',
            'Contrabass Clarinet', 'Eb Clarinet', 'Flute', 'Piano'],
           ['Eric Dolphy', 'Alto Sax', 'Bass Clarinet', 'Flute', 'Bb Clarinet'],
           ['Rashaan Roland Kirk', 'Tenor Sax', 'Stritch', 'Manzello',
            'Bb Clarinet', 'Flute', 'Alto Sax', 'Soprano Sax']]

#list of tunes, the album they were on, and the artist.
tunes = [["Wave", "Wave", "Antonio Carlos Jobim"],
         ["Serene", "Out There", "Eric Dolphy"],
         ["6-77AR-36K (Opus 23B)", "New York, Fall 1974", "Anthony Braxton"],
         ["Tereza My Love", "Stone Flower", "Antonio Carlos Jobim"],
         ["W-138 (Opus 51)","Creative Orchestra Music 1976","Anthony Braxton"]]

print("Albums:")
for album_sublist in albums:
    #prints the info about the list of albums.
    title = album_sublist[0]
    print(f'    {title}')
    print(f"        {title}'s genres are:")
    for genre in album_sublist[1][0:-2]:
        print(f"            {genre},")
    print(f"            {album_sublist[1][-2]} and")
    print(f"            {album_sublist[1][-1]}")
    
    print(f"        {title} was made by {album_sublist[2]}")
    print(f"        {title} was released in {album_sublist[3]}")
    print(f"        The record label that released {title}"\
          f" was {album_sublist[4]} Records\n")
    
print("Musicians")
for musician in players:
    #prints a list of musicians and their main instrument(s)
    print(f"    {musician[0]}'s main instruments are/were:")
    for instrument in musician[1:-2]:
        print(f'        {instrument},')
    print(f'        {musician[-2]} and\n        {musician[-1]}')

print("Tunes")
for tune in tunes:
    #Prints a list of tunes, the album they were on, and who the artist is.
    print('    ',tune[0])
    print(f'        {tune[0]} is from the album "{tune[1]}"',\
          f'and was recorded by {tune[2]}')