
# -*- coding: UTF-8 -*-
__author__ = 'boboyo'
location="Awakening"
game=True
while game:
	if location == "Awakening":
		print "Unkown Figure: SUP GRIMBO ITS ME SHADOW JESUS!!!"
		print "Shadow Jesus: I'VE COME TO TAKE UR NUTTER BUTTERS!!?"
		print "  1. \"Pull up on me catch a body boi\""
		print "  2. Punch Shodow Moses"
		print "  4. ak  jsndk jansdjj asnhdkjn"
		choice=raw_input()
		if choice=="1":
			location = "dool"
		if choice=="2":
			print "Shadow Jesus: I'm not shadow Moses you idiot"
			print "*SHADOW JESIUS HAS TAKEN UR NUTTER BUTTERS*"
			location = "start"
		if choice=="3":
			print "Shadow Jesus: Try learning to read before playing this game"
			print "You realize your mistake"
			print "There was no third option"
			print "It was 4"
			print "You meant to select 4"
			print "Why must you always do this Grimbo?"
			print "The shame wells up inside you"
			print "*You unsheath your dagger*"
			while choice != "1":
				print "  1. Commit suicide"
				choice = raw_input()
			print "*You plunge the dagger into your abdomen*"
			print "*You bleed out*"
			print "You have commit suicide"
			game = False
        	if choice=="4":
			print "*YOU STROKE OUT!! YOU ARE DEAD!!!*"
			print "Shadow Jesus: damn boi now i jus feel bad imma leav u b"
			game=False

	if location == "dool":
		print "Shadow Jesus: PULL UP ON ME CATCHA STROKE!1!"
		print "Shadow Jess: d-d-d-DOOOOOL"
		print "  1. Play digimoon"
		print "  2. Activate Trap Card"
		print "  3. \"i dont play pokemon u fuckin nerd\""
		choice=raw_input()
		if choice=="1":
			print "SHADOW JESUS wants to fight!"
			print "SHADOW JESUS sent out PIDGEOT!"
			print "Go! GYARADOS!"
			print "FIGHT   BAG"
			print "POKéMON RUN"
			choice=raw_input()
			if choice.lower()=="bag":
				print "HP/PP RESTORE"
				print "POKé BALLS"
				print "STATUS HEALERS"
				print "BATTLE ITEMS"
				choice=raw_input()
				if choice.lower()=="hp/pp restore" or choice=="1":
					pass
				if choice.lower()=="poké balls" or choice=="2":
					balls = {"Poké":1,"Luxury":128,"Timer":187,"Dusk":45,"Master":1,"Cherish":1}
					descriptions = {
						"poké ball" : "A device for catching wild Pokémon.\n It is thrown like a ball at the target.\n It is designed as a capsule system.",
						"cherish ball" : "A quite rare Poké Ball that has been \nspecially crafted to commemorate \nan occasion of some sort.",
						"master ball" : "The best Ball with the ultimate level of \nperformance. It will catch any wild \nPokémon without fail.",
						"dusk ball" : "A somewhat different Poké Ball that \nmakes it easier to catch wild pokemon \nat night or in dark places like caves.",
						"timer ball" : "A somewhat different Ball that \nbecomes progressively better the \nmore turns there are in a battle.",
						"luxury ball" : "A comfortable Poké Ball that makes a \ncaught wild Pokémon quickly grow \nfriendly."
					}
					for ball, amount in balls.iteritems():
						print ball,"Ball"
						print "    x"+str(amount)
					choice = raw_input().lower()
					if choice in descriptions:
						cap = lambda x:x[0].upper()+x[1:]
						print ' '.join(map(cap,choice.split(" ")))+'       x'+str(balls[cap(choice.split(" ")[0])])
						print descriptions[choice]
						ptiny "USE"
						raw_input()
			if choice.lower()=="fight":
				print "HYPER BEAM"
				print "TRASH"
				print "EARTHQUAKE"
				print "SPLASH"
				choice=raw_input()
		if choice=="2":
			print "Shadow Jesus doesn't have the time to play a stupid card game with you and leaves with your Nutter Butters"
			location=start
		if choice=="3":
			print "This upsets Shadow Jesus greatly!"
			print "Shadow Jesus: YOU HAVE BEEN SENTENCED TO THE SHADOW ZONE"
			location="Shadow Zone"
