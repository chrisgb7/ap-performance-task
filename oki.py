
# Workout list (each entry is a dictionary)
workout_list = [
    {"name": "Push Day", "def": "Chest, shoulders, triceps", "reps": 10},
    {"name": "Pull Day", "def": "Back and biceps", "reps": 8},
    {"name": "Leg Day", "def": "Quads, hamstrings, calves", "reps": 10}
]

# Get a workout by name
def get_workout(workout_name):
    for workout in workout_list:
        if workout["name"].lower() == workout_name.lower():
            return workout
    return None

# Show workout details
def tell_workout(workout):
    print("Workout:", workout["name"])
    print("Focus:", workout["def"])
    print("Reps:", workout["reps"])

# Add a new workout
def add_new_workout(new_name=None, new_def=None, new_reps=None):
    if new_name is None:
        new_name = input("Enter a new workout name: ").lower()
    if new_def is None:
        new_def = input("Enter the muscle groups or exercises: ")
    if new_reps is None:
        new_reps = int(input("Amount of reps: "))
    
    new_workout = {"name": new_name, "def": new_def, "reps": new_reps}
    workout_list.append(new_workout)
    print("Workout added.")

def rec_workouts(max_reps):
    print("Workouts for you:")
    for workout in workout_list:
        if workout["reps"] <= max_reps:
            print(workout["name"])

# Main program
def program():
    answer = input("Do you want to review your gym splits? (yes/no): ").lower()

    while answer == "yes":
        workouts = [w["name"] for w in workout_list]
        print("Available workouts:", workouts)

        choice = input("Choose a workout or type 'add' to add a new one: ").lower()

        if choice == "add":
            add_new_workout()
        else:
            selected = get_workout(choice)
            if selected:
                tell_workout(selected)
            else:
                print("Workout doesn't exist.")

        answer = input("Do you want to check another workout? (yes/no): ").lower()

    # Feedback section
    rating = int(input("Rate your workout plan from 1–10: "))
    print(str(rating * 10) + "% satisfaction score")

    recommend = input("Would you recommend this plan? (yes/no/maybe): ").lower()
    if recommend in ["yes", "maybe"]:
        print("Great!")
    else:
        print("Time to change your split!")

# Run program
program()
                                                                                                                                                                                                                                                                                                        