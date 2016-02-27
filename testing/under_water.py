"""
Cameron Fabbri
2/19/2016

Under water robot

Dataset specific to a robot working underwater with a team on a boat

"""
name = "Aqua"

train = [
   ('Come back to the boat'   ,'navigate'),
   ('put my clothes in the hamper'                                 ,'navigate'),
   ('put my mug into the dishwasher please'                        ,'navigate'),
   ('bring my trash outside and put it in the barrel'              ,'navigate'),
   ('throw my shoes in the closet'                                 ,'navigate'),
   ('take this glass to the kitchen'                               ,'navigate'),
   ('get me my shoes from the closet'                              ,'get'),
   ('bring me the remote'                                          ,'get'),
   ('go grab my clothes from the dryer'                            ,'get'),
   ('can you go get the mail please'                               ,'get'),
   ('can you go to the cellar and get me a bottle of soda'         ,'get'),
   ('hurry up and get me my keys, we\'re late.'                    ,'get'),
   ('clean up this mess'                                           ,'clean'),
   ('sweep up the kitchen'                                         ,'clean'),
   ('pick up all of my clothes off of the ground and put them away','clean'),
   ('get the vacuum out of the closet and vacuum the hallway'      ,'clean'),
   ('can you pick up all this junk on the ground'                  , 'clean')
]

test = [
   ('take my plate and glass back to the kitchen please'   ,'navigate'),
   ('put this shirt on my bed please'                      ,'navigate'),
   ('can you put all of the dishes into the dishwasher'    ,'navigate'),
   ('get my car keys from the drawer'                      ,'get'),
   ('go to the fridge and grab me a beer please'           ,'get'),
   ('go get me another pair of socks from my dresser'      ,'get'),
   ('sweep up all of these crumbs on the floor'            ,'clean'),
   ('can you vacuum all of the bedrooms?'                  ,'clean'),
   ('pick all of this garbage off of the ground'           ,'clean')
]