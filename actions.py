# UTILS AND FUNCTIONALITY
from data import population, clubs
from components import Club, Person

my_name = ""
my_age = -1
my_bio = ""
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("\nHello, %s. Welcome to our portal." % my_name)

def options():
    # your code goes here!
    print("""--------------------------------------------
 Would you like to:
   1) Create a new club.
   or
   2) Browse and join clubs.
   or
   3) View existing clubs.
   or
   4) Display members of a club.
   or
   -1) Close application.""")
    option = input(" > ")
    options = [1,2,3,4,-1]
    for option in options:
	    if option == 1:
	    	return create_club()
	    elif option == 2:
	    	return join_clubs()
	    elif option == 3:
	    	return view_clubs()
	    elif option == 4:
	    	return view_club_members()
	    elif option == -1:
	    	print("Goodbye")

	# if option == 1:
	# 	return create_club()
	# elif option == 2:
	# 	return join_clubs()
	# elif option == 3:
	# 	return view_clubs()
	# elif option == 4:
	# 	return view_club_members()
	# elif option == -1:
	# 	print("Goodbye")

    # while True:
    # 	if option == 1:
    # 		return create_club()
    # 	elif option == 2:
    # 		return join_clubs()
    # 	elif option == 3:
    # 		return view_clubs()
    # 	elif option == 4:
    # 		return view_club_members()
    # 	elif option == -1:
    # 		print("Goodbye")
    # 		break

def create_club():
    # your code goes here!
    club_name = input("\nPick a name for your awesome new club: ")
    club_description = input("What is your club about?\n")
    # new_club = Club(club_name, club_description)
    # new_club.append(club_name,club_description)
    person = type(Person)   
    view_club_members()
    # print("")
    recruit = input("Enter the numbers of the people you would like to recruit to your new club (-1 to stop):\n > ")
    for club in clubs:
    	for person in population:
    		if recruit in range[15]:
    			return club.recruit_member(recruit)
    		elif recruit == -1:
    			print("your club: %s, %s, Members: %s, %s, %s" % (club_name, club_description, population(person).name, person.bio, person.age))

    # for i in range(0,15):
    # 	# recruit = i
    # 	print("""\nHere's your club: 
    #   			%s
    #   			%s
    #   			Members: 
    #   	 		 - %s""" % (club_name, club_description, person.name))
    
    # while recruit != -1:
    # 	if recruit in population[0:15]:
    # 		return club.recruit_member(recruit)
    # 		print("""\nHere's your club: 
    # 				   %s
    # 				   %s
    # 				   Members: 
    # 				   	- %s""" % (club_name, club_description, person.name))
    # 	else:
    # 		try_again = input("Invalid input. Please try again. ")
    # new_club.recruit_member(person)

    # for club in clubs:
    # 	for i, recruit in enumerate(population):
    # 		if recruit == (i+1) and i<=16:
    # 			return club.recruit_member(recruit)
    # 		else:
    # 			print("""\nHere's your club: 
				# 		%s
				# 		%s
				# 		Members: 
				# 		 - %s""" % (club_name, club_description, population[i].name))

    # for club in clubs:
    # 	for person in population:
    # 		# for i in range(0,15):
    # 		# 	x = i
    # 		# 	return club.recruit_member(recruit)
    		
    # 		if recruit == 1:
    # 			return club.recruit_member(population[0])
    # 		elif recruit == 2:
    # 			return club.recruit_member(population[1])
    # 		elif recruit == 3:
    # 			return club.recruit_member(population[2])
    # 		elif recruit == 4:
    # 			return club.recruit_member(population[3])
    # 		elif recruit == 5:
    # 			return club.recruit_member(population[4])
    # 		elif recruit == 6:
    # 			return club.recruit_member(population[5])
    # 		elif recruit == 7:
    # 			return club.recruit_member(population[6])
    # 		elif recruit == 8:
    # 			return club.recruit_member(population[7])
    # 		elif recruit == 9:
    # 			return club.recruit_member(population[8])
    # 		elif recruit == 10:
    # 			return club.recruit_member(population[9])
    # 		elif recruit == 11:
    # 			return club.recruit_member(population[10])
    # 		elif recruit == 12:
    # 			return club.recruit_member(population[11])
    # 		elif recruit == 13:
    # 			return club.recruit_member(population[12])
    # 		elif recruit == 14:
    # 			return club.recruit_member(population[13])
    # 		elif recruit == 15:
    # 			return club.recruit_member(population[14])
    # 		elif recruit == -1:	
    # 			print("""\nHere's your club:
    # 				%s
    # 				%s
    # 				Members:
    # 				 - %s """ % (club_name, club_description, person.name))
    		# else:
    		# 	print("Invalid")
    # new_club.recruit_member(person)

    # if(new_club):
    # 	view_club_members()
    # 	Club.recruit_member(new_club,person)
    # elif (Club.recruit_member(new_club,person)):
    # 	print("""Here's your club: 
    # 		 %s
    # 		 %s
    # 		 Members: 
    # 		  - %s""" % (club_name, club_description, person))
    # president = ""
    # Club.assign_president(new_club, president)
    # elif (Club.recruit_member(new_club,person)):

def view_clubs():
    # your code goes here!
    for club in clubs:
    	size = len(population)
    	print("""\nName: %s \nDescription: %s \nMembers: %s""" % (club.name, club.description, size))
    # fix number of members!

def view_club_members():
    # your code goes here!
    print("\nMembers: ")
    for i in range(0,15):
    	# x = i
    	print(str(i+1) + ") " + population[i].name)
    # print("\n")
    # Club.recruit_member(club.name, person.name)

    # for club in clubs:
    # 	Club.print_member_list(club)

#     for club in clubs:
# #     	return club.print_member_list() 
#     print("Enter the numbers of the people you would like to recruit to your new club (-1 to stop):\n")
#         print("--------------------------------------------------")
#         print("1) " + person.name)
#         print("2) " + person.name)
#         print("3) " + person.name)
#         print("4) " + person.name)
#         print("5) " + person.name)
#         print("6) " + person.name)
#         user_input = input(" > ")
#         for person in population:
#             if user_input in range[user_input]:
#                 return person.index(user_input)

def join_clubs():
    # your code goes here!
    view_clubs()
    for club in clubs:
    	choice = input("Enter the name of the club you would like to join: ")
    	if(choice.lower()):
    		print("%s just joined %s" % (my_name,choice))
    	else: 
    		print("Please enter a valid club name!")
    	break
    #fix input check!!!
    # print(clubs.list)
    # print("""Name: %s
    # 		 Description: %s
    # 		 Members: %s""" % (club.))

    # club = Club(name, description)
    # choice = input("Enter the name of the club you would like to join: ")
    # if choice.lower() in clubs:
    # 	print("%s just joined %s" % (my_name,choice))
    # else:
    # 	print("Please enter a valid club name!")

def application():
    introduction()
    # your code goes here!
    options()
    # create_club()
    # view_clubs()
    # view_club_members()
    # join_clubs()
    
