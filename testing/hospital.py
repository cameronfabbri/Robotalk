"""
Cameron Fabbri
2/19/2016

Hospital

Dataset specific to training a robot being used in a hospital

"""
name = "Hospital"

train = [
   ('bring the medicine to the patient in room 110'               ,'deliver'),
   ('give these papers to a nurse on floor 3'                     ,'deliver'),
   ('take these papers and bring them back to my office'          ,'deliver'),
   ('bring this tray to room 366'                                 ,'deliver'),
   ('bring these flowers to the front desk on floor 4'            ,'deliver'),
   ('go to the operating room and give the doctor the scissors'   ,'deliver'),
   ('go to the front desk and ask for patient number 45\'s papers','get'),
   ('go to room number 32 and bring back the food trays'          ,'get'),
   ('get me my glasses from my office'                            ,'get'),
   ('bring me the stethoscope from the room next door'            ,'get'),
   ('find Mary and tell her to come here'                         ,'get'),
   ('go get the mop and bucket from the janitor\'s closet'        ,'get'),
   ('take vital signs from the patient in room 132'               ,'get'),
   ('remember this'                                               ,'note'),
   ('okay take a note'                                            ,'note'),
   ('listen up'                                                   ,'note'),
   ('sweep the hallway pleae'                                    ,'clean'),
   ('mop up the blood on the floor'                               ,'clean'),
   ('make all of the beds'                                        ,'clean'),
   ('go to room 341 and mop the floor'                            ,'clean'),
   ('don\'t let anybody else in the door'                         ,'secure'),
   ('make sure all the doors are locked on this floor'            ,'secure'),
   ('stop the people coming from the floor below'                 ,'secure')
]

test = [
   ('bring these bottles of percocet back to the lab'           ,'deliver'),
   ('take these pills and bring them to the patient in room 124','deliver'),
   ('give bob his lunch, he is in room 6'                       ,'deliver'),
   ('go get the scissors from the nurse'                        ,'get'),
   ('can you bring me the medicine from the lab'                ,'get'),
   ('go get the doctor, quickly'                                ,'get'),
   ('listen to me'                                              ,'note'),
   ('I need you to remember this'                               ,'note'),
	('alright take a note'                                       ,'note'),
   ('go to the operating room and mop up the floor'             ,'clean'),
   ('clean up the OR'                                           ,'clean'),
   ('pick up the trash in the hallway'                          ,'clean'),
   ('make sure the doors are locked'                            ,'secure'),
   ('stop that man from running away'                           ,'secure'),
   ('close that door and lock it'                               ,'secure')
]
