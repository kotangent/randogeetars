import random

guitars =["SG", 
		"Les Paul", 
		"ES-335", 
		"Stratocaster", 
		"Telecaster", 
		"Jaguar", 
		"Jazzmaster", 
		"Iceman"]

effects = ["Wah Wah", 
		"Big Muff", 
		"OSD", 
		"Phaser", 
		"Chorus", 
		"Delay", 
		"Echo", 
		"Reverb", 
		"Metal Zone"]

amps = ["Marshall Stack", 
		"Jazz Chorus", 
		"Fender Deluxe", 
		"AC30"
		"Dumble"]

random_guitar = random.choice(guitars)
random_effect = random.choice(effects)
random_amp = random.choice(amps)

print(f"Welcome to RandoGeetar Outfitters! Today's special is: a beautiful {random_guitar} played through a vintage {random_amp} and colored with a {random_effect} effect")