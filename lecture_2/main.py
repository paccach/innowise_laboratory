def generate_profile(age: int):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif 20 <= age:
        return "Adult"

user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year
hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby == "stop":
        break
    hobbies.append(hobby)

life_stage = generate_profile(current_age)
user_profile = {
    "Name" : user_name,
    "Age" : current_age,
    "Life Stage" : life_stage,
    "Favorite Hobbies" : hobbies,
}



