print(' ___________________________________________________________________')
print('| Welcome to the game:                                              |')
print('| This game is about you who awakes with no memorie of the past     |')
print('| You will encounter choices you have to make                       |')
print('| Choose wisely because you might end up dead                       |')
print('| Good luck...                                                      |')
print('|___________________________________________________________________|')
print('|                                                                   |')
print('| You awake in total darkness, you light a candle to see that you   |')
print('| are inside an arena.                                              |')
print('| Suddenly a huge door opens and a dragon comes out.                |')
print('| You see two potential weapons:                                    |')
print('| Option 1- A comically large spoon                                 |')
print('| Option 2- A backpack filled with paper airplanes strapped with    |')
print('| bombs                                                             |')
print(' ___________________________________________________________________')
print('')
print('You wake up in total darkness, you light a candle and find yourself in an arena. ')
print('Suddenly a hatch opens and a huge dragon comes out. There are 2 potential weapons on the ground: ')
keuze1 = input('a comically large spoon and backpack full of paper planes with bombs on them, which one do you take? spoon/backpack: ')
if keuze1 == 'spoon':
    print('')
    keuze2 = input('You grab the comically large spoon. You try to kill the dragon but soon notice that it\'s a tough dragon. \nYou see a wound on his wing and think that it is his weakspot, you also see a hole in the ground with a ladder going down. What do you do? weakspot/ladder: ')
    if keuze2 == 'weakspot':
        print('')
        keuze3 = input('You go for the wing and slice it off in one go, the dragon bleeds to death and 2 doors open; one red and one blue. Which door do you choose? red/blue: ')
        if keuze3 == 'red':
            print('')
            keuze4 = input('You choose the red door. You see a large window on the left where the blue door would have been and see yourself dying. You sigh with relief. You walk out and see a helicopter and an 8x8 offroad truck, which one do you choose? heli/8x8: ')
            if keuze4 == 'heli':
                print('')
                print('You choose the helicopter. You try to start it but it doesn\'t work, you try again and the helicopter explodes while you are sitting inside, you instantly turn into ashes... RIP ')
            elif keuze4 == '8x8':
                print('')
                keuze5 = input('You choose the 8x8 Offroad truck. You drive into a cave filled with sleeping dogs, you are afraid to wake them up but see a key and a lock pick set laying on the ground, you can only take 1 with you, which one do you choose? key/lockpick: ')
                if keuze5 == 'key':
                    print('')
                    print('You choose the key. You drive out of the cave again and come across a large door with a security guard. He asks: "Do you have the key for the door?". You answer yes and take the key out of your pocket, the door opens. You see a huge paradise and live happily ever after...WIN ')
                elif keuze5 == 'lockpick':
                    print('')
                    print('You choose the lock pick set. You drive out of the cave again and come across a large door with a security guard. He asks: "Do you have the key for the door?". You answer no but show your lock pick set. The security guard thinks you were trying to break in and cuts your legs off and you bleed to death...RIP ')
    elif keuze2 == 'ladder': 
        print('')
        keuzeundefined = input('You take the ladder. It gets darker as you go down, suddenly the ladder stops and you fall down. You take out your candle and see that you have entered a cave with all sleeping dogs. You remember the saying \'don\'t wake sleeping dogs\'. You see a corridor with a weak lying at the end but also think: maybe one of these dogs can help me ')
