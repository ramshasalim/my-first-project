print("Welcome to Ramsha Salim's Project👽")
# Quiz Questions and Answers
quiz_questions = {
    
    "📅 What year was our college established?": "2008 📅",
    "🌳 How large is the RRGI campus?": "20 acres 🌳",
    "🎉 What is the name of our annual cultural fest?": "Pragyan 🎉",
    "🎓 Which university is RRGI affiliated with?": "AKTU 🎓",
    "🏢 Who is the chairman of RRGI?": "Anil Kumar Agarwal 🏢",
    "✅ Which government body has approved RRGI?": "AICTE ✅",
    "📍 Where is RRIMT located?": "BKT 📍",
    "👩‍🏫 Who is the dean of T&P?": "Aarti Singh 👩‍🏫"

}

# Function for campus tour
def campus_loc(loc):
    location={}
    location = {
        "1": {
            "location📍": "First floor, Academic block",
            "features👾": "So many books 📚, quiet study rooms 📖, and some faculties that you have never seen before.",
            "fun_fact✨": "To be honest most of the rrimtians visited library during their first year to issue and return the books probably with the fine🫣"
        },
        "2": {
            "location📍": "Left to btech building",
            "features👾": "Variety of meals 🥪, and crowd favorite maggie 🍜 and samosa.",
            "fun_fact✨": "Most of the time this place is used to eat our home made lunch 🍽, for gossips and secret meet up point for some 😉"
        },
        "3": {
            "location📍": "Building 1, near entrance to the college",
            "features👾": "All fee submissions and official tasks are handled here, central hub where all your paperwork gets sorted and processed!📂📝",
            "fun_fact✨": "During exams, this place becomes the busiest spot, so make sure to submit your fee in advance—otherwise, you might just find yourself with the perfect excuse to skip a few lectures! 🤫"
        },
        "4": {
            "location📍": "Building 2, behind academic block",
            "features👾": "Lecture halls, endless whiteboards, and the dean’s office—where even the bravest students get nervous 😗",
            "fun_fact✨": "This building is where the real action happens—the hub of all the hustle 😄, confusion 😵, and drama on campus 😮‍💨. Step in with caution, or you’ll get swept up in the chaos! 🙂‍↔️"
        },
        "5": {
            "location📍": "Building 1, second floor, academic block",
            "features👾": "cozy shared rooms, midnight snacks 🍪, and late-night study sessions ",
            "fun_fact✨": "It’s the ultimate spot for drama, deep convos 🤍, and spontaneous dance-offs in the hallway! 💃"
        },
        
        
    }
    
    

    # Check if the selected location exists in the dictionary
     
    if loc in location:  # Check if the location exists in the dictionary
        value = location[loc]  # Get the value (details) for the selected location

        if loc == "5":  # For Girls Hostel (location "5")
            gender = input("Are you a girl or a boy? 👧🏽👦🏽 ").strip().lower()
            if gender == "girl":
                print(f"\n📍 Location: {value['location📍']}")
                print(f"👾 Features: {value['features👾']}")
                print(f"✨ Fun Fact: {value['fun_fact✨']}")
            elif gender == "boy":
                print("\nWhy do you even want to know about the girls hostel??? 😏")
            else:
                print("\nBruh, enter your correct gender!")
        else:
            # For other locations, just print the description
            print(f"\n📍 Location: {value['location📍']}")
            print(f"👾 Features: {value['features👾']}")
            print(f"✨ Fun Fact: {value['fun_fact✨']}")
    else:
        print("\nChoose from the above locations!")
# Function for location selection
def loc_select():
    
    print("\n📍 Welcome to the Campus Tour Guide! 📍")
    print("Select a location to explore:")
    print("1️⃣ - Library 📚")
    print("2️⃣ - Cafeteria 🍛")
    print("3️⃣ - Academic cell 🏬")
    print("4️⃣ - b.tech building 🏢")
    print("5️⃣ - Girls hostel 🏩")
    print("0️⃣ - Exit")
    
    while True:
        try:
            loc = input("Choose and enter the location you want to know about from the above choices: ").strip()
            
            # Check if the location is valid
            if loc not in ["1", "2", "3", "4", "5", "0"]:
                raise ValueError("Invalid location choice. Please select a valid option.")
            
            # If the choice is valid, return it
            return loc
        
        except ValueError as e:
            # Show error message and continue the loop for another attempt
            print(f"❌ {e}")

    

# Function for the campus quiz
def campus_quiz():
    print("\n🧠 Welcome to the Campus Quiz! 🧠")
    print("Let's see how well you know about RR 🤭. Answer the questions below!🤠\n")

    score = 0 
    total_questions = len(quiz_questions)

    for question, correct_answer in quiz_questions.items():
        print(f"❓ {question}")
        user_answer = input("Your answer: ").strip()

        # Split the answers and compare the first word (ignoring case)
        if user_answer.split()[0].lower() == correct_answer.split()[0].lower():
            print(f"Correct!✅👏 The answer was: {correct_answer}\n")
            score += 1
        else:
            print(f"❌ Oops! The correct answer was: {correct_answer}\n")
    
    print(f"🏁 Quiz Complete! You scored {score}/{total_questions}.\n")
    if score == total_questions:
        print("🎉 Wow, you’re a campus expert!")
    elif score >= total_questions // 2:
        print("👍 Good job! You know RR quite well. You are a true RRIMTian 🫡")
    else:
        print("🤔 Hey engineer, here just for attendance? 🫢 Time to explore your campus more! 😉")

# Main program to call the options
def option_select():
    print("\nHello RRIMTians 🙌, Welcome to RRIMT's world!🧑‍🎓🏫")
    while True:
        print("\n✨Select from the given options✨")
        print("1️⃣ - CAMPUS TOUR GUIDE 🤖")
        print("2️⃣ - COLLEGE'S TRIVIA 🧩")
        print("0️⃣ - EXIT")  # Add an option to exit the program
        try:
            opt = int(input("Choose the number: "))
            if opt == 1:
                locate = loc_select()
                campus_loc(locate)
            elif opt == 2:
                campus_quiz()
            elif opt == 0:
                print("\nGoodbye! See you again! 👋")
                break
            else:
                print("❌ Invalid choice. Please select a valid option.")
        except ValueError:
            print("❌ Please enter a valid number.")

# Start the program
option_select()
