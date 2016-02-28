"""
Cameron Fabbri
2/19/2016

Search and rescue

Dataset specific to a robot working with a search and rescue team

"""
name = "Search and Rescue"

train = [
   ('start recording and send me the video stream'             ,'observe'),
   ('take a picture'                                           ,'observe'),
   ('can you zoom in some more and take a picture'             ,'observe'),
   ('okay start recording'                                     ,'observe'),
   ('if you find a survivor send back a picture'               ,'observe'),
   ('start taking pictures every minute'                      ,'observe'),
   ('fly back to base'                                         ,'navigate'),
   ('follow me'                                                ,'navigate'),
   ('okay follow us'                                           ,'navigate'),
   ('go over to that pile of rubble'                           ,'navigate'),
   ('go up that hill and let me know what you see'             ,'navigate'),
   ('go to the base and get the rest of our team'              ,'navigate'),
   ('head over to group A and report your findings'            ,'navigate'),
   ('look for any survivors in the area'                       ,'detect'),
   ('try and see if you can find any signs of activity'        ,'detect'),
   ('fly overhead and try to find where the fire is'           ,'detect'),
   ('follow this path and try to find footprints'              ,'detect'),
   ('fly back to base, but also look for any signs of movement','detect'),
   ('call for reinforcements to your area'                     ,'communicate'),
   ('hey robot where are you right now'                        ,'communicate'),
   ('hey have you found anything'                              ,'communicate'),
   ('what can you see'                                         ,'communicate'),
   ('how much battery do you have left'                        ,'communicate')
]

test = [
   ('hey take a picture'                           ,'observe'),
   ('start taking a video'                         ,'observe'),
   ('every thirty seconds take a photo'            ,'observe'),
   ('alright fly back to base'                     ,'navigate'),
   ('follow that group up there'                   ,'navigate'),
   ('fly up overhead and follow us'                ,'navigate'),
   ('look over there and try to find any survivors','detect'),
   ('try and locate the fire'                      ,'detect'),
   ('can you see any people down there'            ,'detect'),
   ('how much battery is left'                     , 'communicate'),
   ('what\'s your location'                        , 'communicate'),
   ('do you have any information updates'          , 'communicate')
]
