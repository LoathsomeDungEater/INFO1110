import math

'''
Author: Nguyen Duc Hoang Long
SID: 520057793
Unikey: hngu2146
'''
name = input("Please enter your name: ")

def digit_in_name(name = name):
    """Function that checks if there are digits in name input

    Parameter:
    Takes in name input as argument. Defaults to name.

    Returns:
    True or False
    """
    i = 0
    while i < len(name):
        has_digit = name[i].isdigit()
        i+=1
        if has_digit == True:
            return has_digit      
#Continually prompts user when name is not valid - only digits, only spaces, or has digits in name -
#or when user does not enter anything.
while name.isalpha() == False and not(' ' in name) or name.isspace() == True or (digit_in_name(name) == True):
    print("Error: Only accept alphabetical characters and spaces for name\n")
    name = input("Please enter your name: ")
    
#Takes age input from user as a string.
raw_age = input("\nPlease enter your age: ")
#Continually prompts user when input is empty, when input is not a number or when age is out of the valid range.
while raw_age == "" or raw_age.isdigit() == False or not(0<= int(raw_age) <= 110):
    print("Error: The age is a number between 0 to 110\n")
    raw_age = input("Please enter your age: ")
#Typecasts age into int. This is to help in conditional statements for rep/min modifiers for elderly people.
age = int(raw_age)

sex = input("\nPlease enter your biological sex (female/male): ")
#Continually prompts user when input is empty or input is not exactly "male" or "female".
while sex != "male" and sex != "female":
    print("Error: Please enter valid input\n")
    sex = input("Please enter your biological sex (female/male): ")

#No need to typecast to int, can still fulfill conditionals without being an integer.
#Used docstrings over escape characters for multi-line strings as it's easier to look at
#and spot errors in spelling whitespace.
training_choice = input("""\nWhat do you want to get out of your training? 
    1. Your goal is losing weight
    2. Your goal is to staying calm and relax
    3. Your goal is increasing your heart rate
    4. Your goal is having stronger legs
    5. Your goal is having stronger ABS
    6. Your goal is having stronger shoulders and arms
Choose a number between 1 to 6: """)
#Continually prompts user when input is empty or when input is not a number from 1 to 6.
while training_choice.isdigit() == False or not (1 <= int(training_choice) <= 6):
    print("Error - It can only be a number between 1 to 6")
    training_choice = input("""\nWhat do you want to get out of your training? 
    1. Your goal is losing weight
    2. Your goal is to staying calm and relax
    3. Your goal is increasing your heart rate
    4. Your goal is having stronger legs
    5. Your goal is having stronger ABS
    6. Your goal is having stronger shoulders and arms
Choose a number between 1 to 6: """)

#Takes days per week input as a string
raw_days_per_week = input("\nHow many days per week you can train: ")
#Continually prompts user when input is empty or when input is not a number from 1 to 7.
while raw_days_per_week.isdigit() == False or not(1 <= int(raw_days_per_week) <= 7):
    print("Error: It can only be a number between 1 to 7\n")
    raw_days_per_week = input("How many days per week you can train: ")
#Typecasts days per week into an int for operations in later functions.
days_per_week = int(raw_days_per_week)

#Initialising modifier variable for elderly people.
modifier = 1
#Conditional statements that will reduce the modifier value depending on the age group.
if 60 <= age <= 64:
    modifier *= (1 - (1/100)* (age - 60))
elif 65 <= age <= 74:
    modifier *= ((95/100) - (2/100) * (age - 65))
elif 75 <= age <= 79:
    modifier *= ((75/100) - (3/100) * (age - 75))
elif age >= 80:
    #Setting a variable in order to ensure that the reduction is only up to 80%
    after_reduction = ((60/100) - (4/100) * (age - 80))
    if after_reduction < (20/100):
        after_reduction = (20/100)
    #
    modifier *= (after_reduction)

#Below are 10 functions for each workout. The modifier is initialised above and will be multiplied to each rep/min when appropriate.
def fat_loss():
    """Function that calculates reps for fat loss workout
    Returns: fat_loss_workout as fstring
    """
    fat_loss_workout = f"""Gym workout for fat loss

Plate thrusters ({math.ceil(15*modifier)} reps x 3 sets)
Mountain climbers ({math.ceil(20*modifier)} reps x 3 sets)
Box jumps ({math.ceil(10*modifier)} reps x 3 sets)
Lunges ({math.ceil(10*modifier)} reps x 3 sets)
Renegade rows ({math.ceil(10*modifier)} reps x 3 sets)
Press ups ({math.ceil(15*modifier)} reps x 3 sets)
Treadmill ({math.ceil(10*modifier)} mins x 3 sets)
Supermans ({math.ceil(10*modifier)} reps x 3 sets)
Crunches ({math.ceil(10*modifier)} reps x 3 sets)"""
    return fat_loss_workout

def stretch_n_relax():
    """Function that calculates reps for stretch and relax
    Returns: stretch_workout as fstring
    """
    stretch_workout = f"""Gym workout for stretch and relax

Quad stretchs ({math.ceil(2*modifier)} mins x 3 sets)
Hamstring stretchs ({math.ceil(2*modifier)} mins x 3 sets)
Chest and shoulder stretchs ({math.ceil(2*modifier)} mins x 2 sets)
Upper back stretchs ({math.ceil(3*modifier)} mins x 2 sets)
Biceps stretchs ({math.ceil(2*modifier)} mins x 2 sets)
Triceps stretchs ({math.ceil(2*modifier)} mins x 3 sets)
Hip flexors ({math.ceil(2*modifier)} mins x 3 sets)
Calf stretchs ({math.ceil(2*modifier)} mins x 3 sets)
Lower back stretchs ({math.ceil(2*modifier)} mins x 3 sets)"""

    return stretch_workout

def high_intensity():
    """Function that calculates reps for high intensity workout
    Returns: HIT_workout as fstring
    """
    HIT_workout = f"""Gym workout for high-intensity exercises

Jumping jacks ({math.ceil(20*modifier)} reps x 4 sets)
Sprints ({math.ceil(20*modifier)} reps x 3 sets)
Mountain climbers ({math.ceil(20*modifier)} reps x 4 sets)
Squat jumps ({math.ceil(20*modifier)} reps x 4 sets)
Lunges ({math.ceil(20*modifier)} reps x 3 sets)
Crunches ({math.ceil(20*modifier)} reps x 3 sets)
Treadmill ({math.ceil(15*modifier)} mins x 2 sets)
Side planks ({math.ceil(15*modifier)} reps x 3 sets)
Burpees ({math.ceil(15*modifier)} reps x 3 sets)"""
    return HIT_workout

def legs():
    """Function that calculates reps for leg workout
    Returns: leg_workout as fstring
    """
    leg_workout = f"""Gym workout for strong legs

Back squats ({math.ceil(10*modifier)} reps x 5 sets)
Hip thrusts ({math.ceil(12*modifier)} reps x 3 sets)
Overhead presses ({math.ceil(10*modifier)} reps x 5 sets)
Rack pulls ({math.ceil(10*modifier)} reps x 5 sets)
Squats ({math.ceil(10*modifier)} reps x 4 sets)
Dumbbell lunges ({math.ceil(10*modifier)} reps x 3 sets)
Leg curls ({math.ceil(15*modifier)} reps x 3 sets)
Standing calf raises ({math.ceil(20*modifier)} reps x 2 sets)"""
    return leg_workout

def abdom():
    """Function that caclulates reps for ab exercises
    Returns: ab_workout as fstring
    """
    ab_workout = f"""Gym workout for strong ABS

Cross crunchs ({math.ceil(12*modifier)} reps x 3 sets)
Knee ups ({math.ceil(15*modifier)} reps x 5 sets)
Hip thrusts ({math.ceil(15*modifier)} reps x 3 sets)
Mountain climbers ({math.ceil(15*modifier)} reps x 3 sets)
Vertical hip thrusts ({math.ceil(12*modifier)} reps x 3 sets)
Bicycles ({math.ceil(15*modifier)} mins x 2 sets)
Front planks ({math.ceil(15*modifier)} mins x 3 sets)
Dragon flags ({math.ceil(12*modifier)} reps x 4 sets)
Reverse crunches ({math.ceil(10*modifier)} reps x 3 sets)"""
    return ab_workout

def shoulder_n_arms():
    """Function that calculates reps for shoulder and arms workout
    Returns: shoulder_n_arm_workout as fstring
    """
    shoulder_n_arm_workout = f"""Gym workout for strong shoulder and arms

Bench presses ({math.ceil(10*modifier)} reps x 5 sets)
Triceps dips ({math.ceil(10*modifier)} reps x 5 sets)
Incline dumbbell presses ({math.ceil(12*modifier)} x 3 sets)
dumbbell flyes ({math.ceil(15*modifier)} reps x 3 sets)
Triceps extensions ({math.ceil(15*modifier)} reps x 3 sets)
Pull ups ({math.ceil(10*modifier)} reps x 5 sets)
Treadmill ({math.ceil(15*modifier)} mins x 2 sets)
Bent over rows ({math.ceil(10*modifier)} reps x 5 sets)
Chin ups ({math.ceil(10*modifier)} reps x 3 sets)"""
    return shoulder_n_arm_workout
#For males and females under 18, there isn't a need to use modifier to calculate since they will never reach the conditional to
#trigger the change in the modifier value.
def male_under_18() -> str:
    """Function that returns reps for U18 Males
    Returns: male_U18_workout as string
    """
    male_U18_workout = """Gym workout for a male younger than 18 years old

High knees (20 reps x 3 sets)
Squats (10 reps x 3 sets)
Calf raises (10 reps x 3 sets)
Scissor jumps (12 reps x 3 sets)
Burpees (10 reps x 3 sets)
Treadmill (10 mins x 2 sets)"""
    return male_U18_workout

def female_under_18() -> str:
    """Function that returns reps for U18 Females
    Returns: female_U18_workout as string
    """
    female_U18_workout = """Gym workout for a female younger than 18 years old

Squats (10 reps x 3 sets)
Crunches (10 reps x 2 sets)
Jumping jacks (10 reps x 3 sets)
Push ups (10 reps x 2 sets)
Burpees (10 reps x 3 sets)
Treadmill (10 mins x 2 sets)"""
    return female_U18_workout

def male_18plus():
    """Function that calculates the reps for 18+ Males
    Returns: male_18plus_workout as fstring
    """
    male_18plus_workout = f"""Gym workout for a male at least 18 years old

Standing biceps curls ({math.ceil(20*modifier)} reps x 3 sets)
Seated incline curls ({math.ceil(18*modifier)} reps x 3 sets)
Seated dumbbell presses ({math.ceil(12*modifier)} reps x 3 sets)
Leg presses ({math.ceil(15*modifier)} reps x 3 sets)
Bench presses ({math.ceil(10*modifier)} reps x 4 sets)
Tricep kickbacks ({math.ceil(15*modifier)} reps x 3 sets)
Hip thrusts ({math.ceil(12*modifier)} reps x 3 sets)
Seated rows ({math.ceil(10*modifier)} reps x 4 sets)"""
    return male_18plus_workout

def female_18plus():
    """Function that calculates reps for 18+ Females
    Returns: female_18plus_workout as fstring
    """
    female_18plus_workout = f"""Gym workout for a female at least 18 years old

Lateral raises ({math.ceil(15*modifier)} reps x 3 sets)
Reverse flyes ({math.ceil(12*modifier)} reps x 3 sets)
Hip thrusts ({math.ceil(12*modifier)} reps x 3 sets)
Incline dumbbell presses ({math.ceil(15*modifier)} reps x 3 sets)
Squats ({math.ceil(10*modifier)} reps x 4 sets)
Dumbbell lunges ({math.ceil(10*modifier)} reps x 3 sets)
Leg presses ({math.ceil(12*modifier)} reps x 3 sets)
Dumbbell presses ({math.ceil(10*modifier)} reps x 4 sets)"""
    return female_18plus_workout
#The 10 workout functions end here, below are the other functions that help to print the final workout plan.
def user_workout_choice():
    """Function that calls workouts depending on the training_choice from user input
    Output: Prints the respective workouts
    """
    if training_choice == "1":
       print(fat_loss())
    elif training_choice == "2":
       print(stretch_n_relax())
    elif training_choice == "3":
       print(high_intensity())
    elif training_choice == "4":
       print(legs())
    elif training_choice == "5":
       print(abdom())
    elif training_choice == "6":
       print(shoulder_n_arms())

def age_sex_workout():
    """Function that calls the age & sex workouts depending on user input
    Output: Prints the respective age & sex workouts
    """
    if sex == "male":
        if age < 18:
           print(male_under_18())
        else:
           print(male_18plus())
    elif sex == "female":
        if age < 18:
           print(female_under_18())
        else:
           print(female_18plus())

def final_workout():
    """Function that prints out the finalised workout scheme for the user
    Output: Alternating workouts from training choice and age & sex groups depending on number of training days
    """
    #Initialises day_counter = 0 for the while loop
    day_counter = 0
    print(f"\nHello {name}! Here is your training:")
    #While loop that prints out the training choice workout first, then if the training days are larger than 1, print the
    #age & sex workout, then back to the training choice, and so on and so forth.
    while day_counter < days_per_week:
        day_counter += 1
        print("-------------------------------------------------------------------------------------")
        print(f"Day {day_counter}")
        user_workout_choice()
        #if-else statement here to check if the day_counter is equal to the training days. Breaks the loop if condition is met,
        #otherwise continue and print the age & sex workout and increment day_counter by 1
        if day_counter == days_per_week:
            break
        else:
            print("-------------------------------------------------------------------------------------")
            day_counter += 1
            print(f"Day {day_counter}")
            age_sex_workout()

    print("-------------------------------------------------------------------------------------")
    print(f"\nBye {name}.")

#Calls final workout
final_workout()