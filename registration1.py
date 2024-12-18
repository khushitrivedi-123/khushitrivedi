import os
import csv
import bcrypt
import re
import getpass
import sys

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("       Welcome to the Registration   ")
    print("=====================================")
    print("1. Sign Up")
    print("2. Login")
    print("3. Exit")
    
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex,email)

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'\d',password):
        return False
    if not re.search(r'[A-Za-a]',password):
        return False
    if not re.search(r'[@$!%*?&]', password):
        return False
    return True

def sign_up():
    print("==== Sign Up ====")
    username = input("Enter your username: ").strip()
    
    while  True:
        email = input("Enter your email:").strip()
        
        if not is_valid_email(email):
         print("Invalid email format! please try again.")
        else:
            break
    
    while True:
        password = getpass.getpass("Enter your password:").strip()
        
        if not is_valid_password(password):
            print("Password ")
            print("Password must be 8 characters long, contain a number, a letter, and a special character.")
        else:
            break 
    
    # if not is_valid_password(password):
    #     print("Password must be 8 characters long, contain a number, a letter, and a special character.")    
    #     input("Press enter to continue...")
    #     return

    # if not username or not password:
    #     print("Username or password cannot be empty!") 
    #     input("Press Enter to continue...")
    #     return

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    file_exists = os.path.isfile("users.csv")
    with open("users.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Username", "Password"])
        writer.writerow([username, hashed_password.decode('utf-8')])

    print("Sign Up successful! You can now log in.")
    input("Press Enter to continue...")
    
    login()



def login():
    print("==== Login ====")
    username = input("Enter your username: ").strip()
    password = getpass.getpass("Enter your password: ").strip()

    try:
        with open("users.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                if len(row) >= 2:
                    stored_username, stored_password = row[0], row[1]
                    if username == stored_username and bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                        print("Login successful!")
                        input("Press Enter to start the quiz...")
                        take_quiz(username)
                        return
            print("Invalid username or password.")
    except FileNotFoundError:
        print("No users found. Please sign up first.")
    input("Press Enter to continue...")

# Quiz function
def take_quiz(username):
    print("==== Quiz ====")
    questions = [
        {"question": "Who is known as the 'God of Cricket'?", "options": ["A. Virat Kohli", "B. Sachin Tendulkar", "C. MS Dhoni", "D. Ricky Ponting"], "answer": "B"},
        {"question": "How many players are there in a cricket team?", "options": ["A. 9", "B. 10", "C. 11", "D. 12"], "answer": "C"},
        {"question": "Which country won the first Cricket World Cup in 1975?", "options": ["A. Australia", "B. West Indies", "C. India", "D. England"], "answer": "B"},
        {"question": "What is the name of the trophy awarded in the Ashes series?", "options": ["A. Border-Gavaskar Trophy", "B. ICC Trophy", "C. The Ashes Urn", "D. Champions Trophy"], "answer": "C"},
        {"question": "Who is the first batsman to score 200 runs in an ODI match?", "options": ["A. Rohit Sharma", "B. Chris Gayle", "C. Virender Sehwag", "D. Sachin Tendulkar"], "answer": "D"},
        {"question": "What is the maximum number of overs in a T20 cricket match per team?", "options": ["A. 10", "B. 20", "C. 50", "D. 40"], "answer": "B"},
        {"question": "Which Indian cricketer is known as 'Captain Cool'?", "options": ["A. Sourav Ganguly", "B. Rahul Dravid", "C. MS Dhoni", "D. Virat Kohli"], "answer": "C"},
        {"question": "In cricket, what does LBW stand for?", "options": ["A. Leg By Wicket", "B. Left Ball Wide", "C. Leg Before Wicket", "D. Long Ball Wide"], "answer": "C"},
        {"question": "Which bowler has the most wickets in Test cricket?", "options": ["A. Shane Warne", "B. Anil Kumble", "C. Muttiah Muralitharan", "D. Glenn McGrath"], "answer": "C"},
        {"question": "What is the term for scoring 100 runs in a single innings?", "options": ["A. Century", "B. Double Century", "C. Fifty", "D. Triple Century"], "answer": "A"},
    ]

    file_exists = os.path.isfile("quiz_answers.csv")
    with open("quiz_answers.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Username",  "Answer", "Correct"])

        score = 0
        for i, q in enumerate(questions, start=1):
            print(f"Q{i}: {q['question']}")
          
            print("   ".join(q["options"]))
            answer = input("Your answer (A/B/C/D): ").strip().upper()

            is_correct = answer == q["answer"]
            writer.writerow([username,  answer, "Correct" if is_correct else "Incorrect"])
            
            if is_correct:
                score += 1
        
        
        result_file_exists = os.path.isfile("quiz_results.csv")
        with open("quiz_results.csv", mode="a", newline="") as result_file:
            result_writer = csv.writer(result_file)
            if not result_file_exists:
                result_writer.writerow(["Username", "Score"])
            result_writer.writerow([username, score])

        print(f"\nQuiz complete! Your score: {score}/10")
        
        print("Exiting the program. Goodbye!")
        sys.exit()

# Main function
def main():
    while True:
        display_menu()
        choice = input("Please choose an option (1/2/3): ").strip()

        if choice == '1':
            sign_up()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

# Run the program
if __name__ == "__main__":
    main()
    
