import math

'''
Author: Nguyen Duc Hoang Long
SID: 520057793
Unikey: hngu2146
'''
name = input("Please enter your name: ")
#Continually prompts user when name is not valid or when user does not enter anything
while name.isalpha() == False and not(' ' in name) or name.isspace() == True:
    print("Error: Only accept alphabetical characters and spaces for name\n")
    name = input("Please enter your name: ")
    
#Takes age input from user as a string
raw_age = input("\nPlease enter your age: ")
#Continually prompts user when input is empty, when input is not a number or when age is out of the valid range
while raw_age == "" or raw_age.isdigit() == False or not(0<= int(raw_age) <= 110):
    print("Error: The age is a number between 0 to 110\n")
    raw_age = input("Please enter your age: ")
#Typecasts age into int. This is to help in conditional statements for rep/min modifiers for elderly people
age = int(raw_age)

sex = input("\nPlease enter your biological sex (female/male): ")
#Continually prompts user when input is empty or input is not exactly "male" or "female"
while sex != "male" and sex != "female":
    print("Error: Please enter valid input\n")
    sex = input("Please enter your biological sex (female/male): ")

#No need to typecast to int, can still fulfill conditionals without being an integer
training_choice = input("""\nWhat do you want to get out of your training? 
    1. Your goal is losing weight
    2. Your goal is to staying calm and relax
    3. Your goal is increasing your heart rate
    4. Your goal is having stronger legs
    5. Your goal is having stronger ABS
    6. Your goal is having stronger shoulders and arms
Choose a number between 1 to 6: """)
#Continually prompts user when input is empty or when input is not a number from 1 to 6
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
#Continually prompts user when input is empty or when input is not a number from 1 to 7
while raw_days_per_week.isdigit() == False or not(1 <= int(raw_days_per_week) <= 7):
    print("Error: It can only be a number between 1 to 7")
    raw_days_per_week = input("How many days per week you can train: ")
#Typecasts days per week into an int for operations
days_per_week = int(raw_days_per_week)

#Initialising modifier variable for elderly people
modifier = 1
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

#Below are 10 functions for each workout, each with parameter as modifier. The modifier is initialised above and will be multiplied
#to each rep/min
#1
def fat_loss(modifier):
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
#2------------------------------------------------------
def stretch_n_relax(modifier):
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
#3------------------------------------------------------
def HIT(modifier):
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
#4------------------------------------------------------
def legs(modifier):
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
#5------------------------------------------------------
def abdom(modifier):
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
#6------------------------------------------------------
def shoulder_n_arms(modifier):
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
#7------------------------------------------------------
def male_under_18(modifier):
    male_U18_workout = f"""Gym workout for a male younger than 18 years old

High knees ({math.ceil(20*modifier)} reps x 3 sets)
Squats ({math.ceil(10*modifier)} reps x 3 sets)
Calf raises ({math.ceil(10*modifier)} reps x 3 sets)
Scissor jumps ({math.ceil(12*modifier)} reps x 3 sets)
Burpees ({math.ceil(10*modifier)} reps x 3 sets)
Treadmill ({math.ceil(10*modifier)} mins x 2 sets)"""
    return male_U18_workout
#8------------------------------------------------------
def female_under_18(modifier):
    female_U18_workout = f"""Gym workout for a female younger than 18 years old

Squats ({math.ceil(10*modifier)} reps x 3 sets)
Crunches ({math.ceil(10*modifier)} reps x 2 sets)
Jumping jacks ({math.ceil(10*modifier)} reps x 3 sets)
Push ups ({math.ceil(10*modifier)} reps x 2 sets)
Burpees ({math.ceil(10*modifier)} reps x 3 sets)
Treadmill ({math.ceil(10*modifier)} mins x 2 sets)"""
    return female_U18_workout
#9------------------------------------------------------
def male_18plus(modifier):
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
#10------------------------------------------------------
def female_18plus(modifier):
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
#------------------------------------------------------
#Creates function that calls the workouts depending on the training choice from the user
def user_workout_choice(training_choice = training_choice, modifier = modifier):
    if training_choice == "1":
       print(fat_loss(modifier))
    elif training_choice == "2":
       print(stretch_n_relax(modifier))
    elif training_choice == "3":
       print(HIT(modifier))
    elif training_choice == "4":
       print(legs(modifier))
    elif training_choice == "5":
       print(abdom(modifier))
    elif training_choice == "6":
       print(shoulder_n_arms(modifier))
#Creates function that calls the workouts based on the sex and age of the user
def age_sex_workout(sex = sex, age = age, modifier = modifier):
    if sex == "male":
        if age < 18:
           print(male_under_18(modifier))
        else:
           print(male_18plus(modifier))
    elif sex == "female":
        if age < 18:
           print(female_under_18(modifier))
        else:
           print(female_18plus(modifier))

#WORK ON MAKING A FUNCTION/LOOP TO PRINT THE FINAL WORKOUT

def final_workout(days = days_per_week):
    day_counter = 1
    if days == 1:
        print(f"\nHello {name}! Here is your training:")
        print("-------------------------------------------------------------------------------------")
        print(f"Day {day_counter}")
        user_workout_choice(training_choice)
        print("-------------------------------------------------------------------------------------")
        print(f"\nBye {name}.")
    elif days > 1:
        print(f"\nHello {name}! Here is your training:")
        while day_counter < days:
            print("-------------------------------------------------------------------------------------")
            print(f"Day {day_counter}")
            user_workout_choice(training_choice)
            print("-------------------------------------------------------------------------------------")
            day_counter += 1
            print(f"Day {day_counter}")
            age_sex_workout(sex, age)
            day_counter += 1
            
        print("-------------------------------------------------------------------------------------")
        print(f"\nBye {name}.")

final_workout()