"""
Cameron Fabbri
2/19/2016

UAV

Dataset specific to a remote operator controlling a UAV

"""
name = "UAV"

train = [
   ('fire a missile at location A'                               ,'attack'),
   ('target coordinates x y for attack'                          ,'attack'),
   ('drop a bomb on location B'                                  ,'attack'),
   ('fire at the aeroplane incoming from the east'               ,'attack'),
   ('follow and attack that jet'                                 ,'attack'),
   ('shoot the ground when you get to your location'             ,'attack'),
   ('take a picture every 10 seconds'                            ,'observe'),
   ('take a video of the path you take'                          ,'observe'),
   ('start recording when you get to your location'              ,'observe'),
   ('use all sensors to record your actions during the flight'   ,'observe'),
   ('circle the building and take a video'                        ,'observe'),
   ('navigate around the area and take pictures every 10 seconds','observe'),
   ('fly back to the base'                                       ,'navigate'),
   ('fly to your target location'                                ,'navigate'),
   ('follow the UAV in front of you'                             ,'navigate'),
   ('locate the target'                                          ,'navigate'),
   ('circle around the building until further instructions'      ,'navigate'),
   ('go to the base and get the rest of our team'                ,'navigate'),
   ('fly away from your target immediately'                      ,'navigate'),
   ('look for any survivors in the area'                         ,'detect'),
   ('try and see if you can find any signs of activity'          ,'detect'),
   ('fly over the target location and locate any people'         ,'detect'),
   ('look for approaching jets from the north'                   ,'detect'),
   ('fly back to base, but also look for any signs of movement'  ,'detect'),
   ('call for reinforcements to your area'                       ,'communicate'),
   ('what is your location'                                      ,'communicate'),
   ('what other planes are in the area'                          ,'communicate'),
   ('tell me when you are ready to head back'                    ,'communicate'),
   ('how much battery do you have left'                          ,'communicate')
]

test = [
   ('shoot down that plane'                              ,'attack'),
   ('fire your missiles at the target'                   ,'attack'),
   ('when you get to your location, drop the bomb'       ,'attack'),
   ('navigate the building and record it'                ,'observe'),
   ('take a picture of your current location'            ,'observe'),
   ('record a video of the target'                       ,'observe'),
   ('alright fly back to base'                           ,'navigate'),
   ('circle around the target area'                      ,'navigate'),
   ('fly to your target and circle it for now'           ,'navigate'),
   ('look for signs of people on the ground'             ,'detect'),
   ('try and locate the fire'                            ,'detect'),
   ('watch out for a group of jets coming from the south','detect'),
   ('what is your current location'                      ,'communicate'),
   ('what is your battery status'                        ,'communicate'),
   ('are there any other vehicles in your location'      ,'communicate')
]