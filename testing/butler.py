"""
Cameron Fabbri
2/19/2016

Butler

Data set specific to using a robot as a personal butler

"""
name = "Butler"

train = [
   ('bring my plates to the kitchen and put them on the counter'   ,'deliver'),
   ('put my clothes in the hamper'                                 ,'deliver'),
   ('put my mug into the dishwasher please'                        ,'deliver'),
   ('bring my trash outside and put it in the barrel'              ,'deliver'),
   ('throw my shoes in the closet'                                 ,'deliver'),
   ('take this glass to the kitchen'                               ,'deliver'),
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
   ('can you pick up all this junk on the ground'                  ,'clean'),
   ('how much battery do you have left'                            ,'communicate'),
   ('hey robot where are you right now'                            ,'communicate'),
   ('what time is it'                                              ,'communicate'),
   ('do you know where I left my car keys'                         ,'communicate'),
   ('what is the temperature in here'                              ,'communicate')
]

test = [
   ('take my plate and glass back to the kitchen please'   ,'deliver'),
   ('put this shirt on my bed please'                      ,'deliver'),
   ('can you put all of the dishes into the dishwasher'    ,'deliver'),
   ('get my car keys from the drawer'                      ,'get'),
   ('go to the fridge and grab me a beer please'           ,'get'),
   ('go get me another pair of socks from my dresser'      ,'get'),
   ('sweep up all of these crumbs on the floor'            ,'clean'),
   ('can you vacuum all of the bedrooms?'                  ,'clean'),
   ('pick all of this garbage off of the ground'           ,'clean'),
   ('how much battery do you have'                         ,'communicate'),
   ('what\'s the time'                                     ,'communicate'),
   ('do you know where I put my wallet'                    ,'communicate')
]