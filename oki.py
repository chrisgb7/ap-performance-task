
# Workout List containing workout name, definition, and reps
workout_list = [
    {"name": "Push Day", "def": "Chest, shoulders, triceps", "reps": 12},
    {"name": "Pull Day", "def": "Back and biceps", "reps": 8},
    {"name": "Leg Day", "def": "Quads, hamstrings, calves", "reps": 10}
]

# This function retrieves a workout by name from the list
#iterates through the list, if match found, it returns the workout details
def get_workout(workout_name):
    for workout in workout_list:
        if workout["name"].lower() == workout_name.lower():
            return workout
    return None

# Show workout details by printing them out
def showworkout(workout):
    print("Workout:", workout["name"])
    print("Focus:", workout["def"])
    print("Reps:", workout["reps"])

# Adds a new workout 
def add_workout(name, focus, reps):
    workout_list.append({
        "name": name,
        "def": focus,
        "reps": reps
    })
    print("Workout added.")

def rec_workouts(max_reps):
    print("Workouts for you:")
    matches = [workout["name"] for workout in workout_list if workout["reps"] <= max_reps]
    if matches:
        for name in matches:
            print(name)
    else:
        print("Nothing found.")

# This function allows users to review workouts, add new ones, and get recommendations based on reps.
# It also collects feedback at the end.
def program():
    answer = input("Do you want to review your gym splits? (yes/no): ").lower()

    while answer == "yes":
        workouts = [w["name"] for w in workout_list]
        print("Available workouts:", workouts)

        choice = input("Choose a workout, type 'add' to add one, or type 'rec' to see workouts by max reps: ").lower()

        if choice == "add":
            name = input("Enter a new workout name: ").lower()
            focus = input("Enter the muscle groups or exercises: ")
            reps = int(input("Amount of reps: "))
            add_workout(name, focus, reps)
        elif choice == "rec":
            max_reps = int(input("Show workouts with reps at or below: "))
            rec_workouts(max_reps)
        else:
            selected = get_workout(choice)
            if selected:
                showworkout(selected)
            else:
                print("Workout doesn't exist.")

        answer = input("Do you want to check another workout? (yes/no): ").lower()

    # This code provides feedback by asking the user to rate their workout plan and whether they would recommend it
    rating = int(input("Rate your workout plan from 1–10: "))
    print(str(rating * 10) + "% satisfaction score")

    recommend = input("Would you recommend this plan? (yes/no/maybe): ").lower()
    if recommend in ["yes", "maybe"]:
        print("Great!")
    else:
        print("Time to change your split!")

program()
                                                                                                                                                                                                                                                                                                        