import random
import cars_list
from cars_list import *

while True:
    main = True
    while main:                                                                 
        print("Welcome to Goce's car recommendation! Let's choose your ideal vehicle.")

        choice = input("First thing first - do you want a quick suggestion, or a more elabore one? Enter 'quick' or 'elaborate': ")
        valid_choice = ('quick', 'elaborate')                                       
        while choice not in valid_choice:                                   
            print("Invalid choice. Please enter 'quick' or 'elaborate' to continue.")                       
            choice = input("First thing first - do you want a quick suggestion, or a more elabore one?")

        if choice == 'quick':
            quick_choice = True
            while quick_choice:
                print("I'll try to be quick. Please choose from the following: ")
                print("*******************************************************")
                quick_engine = input("Petrol, diesel, or electric car? ")
                valid_quick_engine = ('petrol', 'diesel', 'electric')
                while quick_engine not in valid_quick_engine:
                    print("Invalid choice. Please enter 'petrol', 'diesel', or 'electric'.")
                    quick_engine = input("Petrol, diesel, or electric car? ")

                quick_gearbox = input("Manual or automatic gearbox? ")
                valid_quick_gearbox = ('manual', 'auto', 'automatic')
                while quick_gearbox not in valid_quick_gearbox:
                    print("Invalid choise. Please choose 'manual' or 'automatic' gearbox.")
                    quick_gearbox = input("Manual or automatic? ")

                quick_style = input("Choose a body style: SUV, city car, hatchback, sedan, or estate? ")
                valid_quick_style = ('SUV', 'suv', 'city car', 'city', 'hatchback', 'sedan', 'estate')
                while quick_style not in valid_quick_style:
                    print("Invalid choice. Please pick one body style.")
                    quick_style = input("Choose a body style: SUV, city car, hatchback, sedan, or estate? ") 

                if quick_engine == 'petrol':   
                    q_1 = tuple(petrol)
                elif quick_engine == 'diesel':
                    q_1 = tuple(diesel)
                elif quick_engine == 'electric':
                    q_1 = tuple(electric)

                if quick_gearbox == 'manual':       
                    q_2 = tuple(manual)
                elif quick_gearbox == 'automatic':
                    q_2 = tuple(automatic)          
                elif quick_gearbox == 'auto':
                    q_2 = tuple(automatic)

                if quick_style == 'SUV':             
                    q_3 = tuple(SUV) 
                elif quick_style == 'city car':             
                    q_3 = tuple(city_car)
                elif quick_style == 'city':
                    q_3 = tuple(city_car)         
                elif quick_style == 'hatchback':
                    q_3 = tuple(hatchback)          
                elif quick_style == 'sedan':
                    q_3 = tuple(sedan)
                elif quick_style == 'estate':
                    q_3 = tuple(estate)          

                q_1_as_set = set(q_1)   
                q_2_as_set = set(q_2)
                q_3_as_set = set(q_3)
                q_result_as_set = q_1_as_set.intersection(q_2_as_set, q_3_as_set)  

                if len(q_result_as_set) > 0:
                    q_suggestion = random.choice(list(q_result_as_set))
                    print('-------------------------------------------------------------------------------') 
                    final_quick_choice = ("You chose a {0} engine, paired with {1} gearbox, and a {2} body style.".format(quick_engine.lower(), 
                    quick_gearbox.lower(), quick_style))
                    print(final_quick_choice)
                    print('-------------------------------------------------------------------------------')
                    print("I suggest you try the {0}".format(quick_style), str(q_suggestion)+', ' 
                    "{0} version, with {1} transmission.".format(quick_engine.lower(), quick_gearbox.lower()))
                    print('-------------------------------------------------------------------------------')
                    quick_choice = False
                    main = False
                else:
                    print("********************************************************************************")
                    q_suggestion = print("Hmm, I can't really recommend anything with these criteria. Care to try again?")
                    quick_choice = False
                    main = False

        elif choice == 'elaborate':
            elaborate_choice = True
            while elaborate_choice:
                print("Let's find your perfect vehicle. Please choose from the following: ")
                print("******************************************************************")

                elb_engine = input("Petrol, diesel, or alternative fuel vehicle? ")
                valid_elb_engine = ('petrol', 'diesel', 'alternative', 'alternative fuel')
                while elb_engine not in valid_elb_engine:
                    print("Invalid choice. Please enter one of the following: 'petrol', 'diesel', or 'alternative fuel'. ")
                    elb_engine = input("Petrol, diesel, or alternative fuel car? ")
                valid_alt_fuel = ('alternative', 'alternative fuel')
                if elb_engine in valid_alt_fuel:
                    elb_engine = input("Way to go! Please choose from the following: electric, phev, mhev, natural gas, lpg, hydrogen, or ethanol: ")
                    valid_alt_fuel = ('electric', 'phev', 'mhev', 'natural gas', 'lpg', 'hydrogen', 'ethanol')
                    while elb_engine not in valid_alt_fuel:
                        print("Invalid choice. Please choose from the following: electric, phev, mhev, natural gas, lpg, hydrogen, or ethanol.")
                        elb_engine = input("Please choose from one of the following: electric, phev, mhev, natural gas, lpg, hydrogen, or ethanol. ")
                else:
                    pass

                elb_gearbox = input("What kind of transmision would you prefer? Pick 'manual' or 'automatic'. ")
                valid_elb_gearbox = ('manual', 'auto', 'automatic')
                while elb_gearbox not in valid_elb_gearbox:
                    print("Invalid choice. Please pick 'manual' or 'automatic'.")
                    elb_gearbox = input("What kind of transmision would you prefer? Pick 'manual' or 'automatic'. ")

                elb_use = input("Your ideal vehicle should be better suited for highway, or city driving? ")
                valid_elb_use = ('city', 'highway')
                while elb_use not in valid_elb_use:
                    print("Invalid choice. Please pick 'city', or 'highway'.")
                    elb_use = input("Your ideal vehicle should be better suited for highway, or city driving? ")

                elb_style = input("Choose a body style: SUV, crossover, city car, hatchback, sedan, or estate? ")
                valid_elb_style = ('SUV', 'crossover', 'city car', 'hatchback', 'sedan', 'estate')
                while elb_style not in valid_elb_style:
                    print("Invalid choice. Please pick a body style from the ones provided.")
                    elb_style = input("Choose a body style: SUV, crossover, city car, hatchback, sedan, or estate? ")

                if elb_engine == 'petrol':   
                    q_1 = tuple(petrol)
                elif elb_engine == 'diesel':
                    q_1 = tuple(diesel)
                elif elb_engine == 'electric':
                    q_1 = tuple(electric)
                elif elb_engine == 'mhev':
                    q_1 = tuple(mhev)
                elif elb_engine == 'phev':
                    q_1 = tuple(phev)
                elif elb_engine == 'natural gas':
                    q_1 = tuple(natural_gas)
                elif elb_engine == 'lpg':
                    q_1 = tuple(lpg)
                elif elb_engine == 'hydrogen':
                    q_1 = tuple(hydrogen)
                elif elb_engine == 'ethanol':
                    q_1 = tuple(ethanol)
                
                if elb_gearbox == 'manual':       
                    q_2 = tuple(manual)
                elif elb_gearbox == 'automatic':
                    q_2 = tuple(automatic)          
                elif elb_gearbox == 'auto':
                    q_2 = tuple(automatic)

                if elb_use == 'city':
                    q_3 = tuple(city)
                elif elb_use == 'highway':
                    q_3 = tuple(highway)                            

                if elb_style == 'SUV':             
                    q_4 = tuple(SUV) 
                elif elb_style == 'city car':
                    q_4 = tuple(city_car)  
                elif elb_style == 'crossover':
                    q_4 = tuple(crossover)
                elif elb_style == 'hatchback':
                    q_4 = tuple(hatchback)          
                elif elb_style == 'sedan':
                    q_4 = tuple(sedan)
                elif elb_style == 'estate':
                    q_4 = tuple(estate)          

                q_1_as_set = set(q_1)   
                q_2_as_set = set(q_2)
                q_3_as_set = set(q_3)
                q_4_as_set = set(q_4)
                q_result_as_set = q_1_as_set.intersection(q_2_as_set, q_3_as_set, q_4_as_set)

                if len(q_result_as_set) > 0:
                    q_suggestion = random.choice(list(q_result_as_set))
                    print('-------------------------------------------------------------------------------') 
                    final_elb_choice = ("You chose a {0} engine, paired with {1} gearbox, and a {2} body style, primarily used for {3} driving.".format(elb_engine.lower(), 
                    elb_gearbox.lower(), elb_style, elb_use.lower()))
                    print(final_elb_choice)
                    print('-------------------------------------------------------------------------------')
                    final_elb_suggestion = ("I suggest you try the {0}".format(elb_style) + ' ' + str(q_suggestion)+', '
                    "{0} version, with {1} transmission.".format(elb_engine.lower(), elb_gearbox.lower()))
                    print(final_elb_suggestion)
                    print('-------------------------------------------------------------------------------')
                    elaborate_choice = False
                    main = False
                else:
                    print("********************************************************************************")
                    q_suggestion = print("Hmm, I can't really recommend anything with these criteria. Care to try again?")
                    elaborate_choice = False
                    main = False                

        restart = input("Type 'yes' to try again. ") 
        if restart.lower() == 'yes': 
            main = True
        else:
            exit()
    