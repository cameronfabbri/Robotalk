"""
Cameron Fabbri
2/19/2016

Under water robot

Dataset specific to a robot working underwater with a team on a boat

"""
name = "Under Water"

train = [
   ('Come back to the boat'   ,'navigate'),
   ('dive deeper'                                 ,'navigate'),
   ('circle around the boat', 'navigate'),
   ('go over to that pipe', 'navigate'),
   ('navigate towards the cable near the bottom', 'navigate'),
   ('look for any stray cables on the bottom', 'search'),
   ('go into the cave and see if there are any other divers in there', 'search'),
   ('go look for any stray pipes near that ship', 'search'),
   ('locate the mine entrance', 'search'),
   ('search for the ship that\'s supposed to be nearby', 'search'),
   ('swim around the drill and monitor it', 'monitor'),
   ('watch for any incoming animals near the divers', 'monitor'),
   ('make sure the pipe does\'n break during repairment', 'monitor'),
   ('monitor the environment and watch for any danger', 'monitor'),
   ('keep a lookout for other boats coming our way', 'monitor'),
   ('go check out that pipe for any damage', 'inspect'),
   ('go in that sunken ship and make sure there aren\'t any animals inside', 'inspect'),
   ('inspect the bottom of our boat and see if there\'s any damage to the hull', 'inspect'),
   ('go see if there has been any damage to the drill', 'inspect'),
   ('navigate along the cable and find where it is broken', 'inspect')
]

test = [
   ('circle the boat','navigate'),
   ('okay, you can come back to the boat now','navigate'),
   ('go down to the sea floor','navigate'),
   ('look for any divers in the area','search'),
   ('go look for the entrance of the cave','search'),
   ('go look for anything man made on the floor','search'),
   ('watch the divers and alert them for any approaching animals','monitor'),
   ('watch the area for incoming boats','monitor'),
   ('monitor the drill and let us know if it breaks','monitor'),
   ('try and find the break along the cable','inspect'),
   ('go see if the drill has been damaged','inspect'),
   ('check our hull to see if it has been damaged','inspect')
]
