def is_admitted_to_computer_science(jamb_score, grades):
    # Check if candidate meets admission criteria for Computer Science Department
    if (jamb_score >= 250 and
        len(grades) >= 5 and
        all(grade in {'A', 'B', 'C'} for grade in grades.values())):
        return True
    return False

def is_admitted_to_mass_communication(jamb_score, grades):
    # Check if candidate meets admission criteria for Mass Communication Department
    required_subjects = {'Math', 'English', 'C.R.S', 'Government', 'Literature'}
    if (jamb_score >= 230 and
        len(grades) >= 5 and
        all(subject in required_subjects and grades[subject] in {'A', 'B', 'C'} for subject in grades.keys())):
        return True
    return False

def main():
    print("Welcome to the Admission Portal")
    
    # Prompt user to choose department
    print("Choose your desired department:")
    print("1. Computer Science")
    print("2. Mass Communication")
    department_choice = input("Enter your choice (1 for Computer Science, 2 for Mass Communication): ")
    
    # Get JAMB score from user
    jamb_score = int(input("Enter your JAMB score: "))
    
    # Determine admission status based on department choice
    if department_choice == '1':  # Computer Science
        print("\nYou selected Computer Science.")
        # Get grades for Computer Science subjects
        grades = {}
        print("\nEnter your grades for Computer Science subjects:")
        computer_science_subjects = ['Math', 'English', 'Chemistry', 'Physics', 'Biology']
        for subject in computer_science_subjects:
            grade = input(f"Enter grade for {subject}: ").upper()
            grades[subject] = grade
        
        # Check admission status for Computer Science
        if is_admitted_to_computer_science(jamb_score, grades):
            print("\nCongratulations! You are admitted into the Computer Science Department.")
        else:
            print("\nSorry, you are not admitted into the Computer Science Department.")
    
    elif department_choice == '2':  # Mass Communication
        print("\nYou selected Mass Communication.")
        # Get grades for Mass Communication subjects
        grades = {}
        print("\nEnter your grades for Mass Communication subjects:")
        mass_communication_subjects = ['Math', 'English', 'C.R.S', 'Government', 'Literature']
        for subject in mass_communication_subjects:
            grade = input(f"Enter grade for {subject}: ").upper()
            grades[subject] = grade
        
        # Check admission status for Mass Communication
        if is_admitted_to_mass_communication(jamb_score, grades):
            print("\nCongratulations! You are admitted into the Mass Communication Department.")
        else:
            print("\nSorry, you are not admitted into the Mass Communication Department.")
    
    else:
        print("\nInvalid choice. Please enter '1' for Computer Science or '2' for Mass Communication.")

if __name__ == "__main__":
    main()
