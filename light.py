def password_checker(password, difficulty):
    if difficulty == "Easy":
        if len(password) >= 6:
            return True
        else:
            return "Password must be at least 6 characters long."
    elif difficulty == "Medium":
        if len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
            return True
        else:
            missing_requirements = []
            if len(password) < 8:
                missing_requirements.append("Password must be at least 8 characters long.")
            if not any(char.isupper() for char in password):
                missing_requirements.append("Missing uppercase letter.")
            if not any(char.islower() for char in password):
                missing_requirements.append("Missing lowercase letter.")
            if not any(char.isdigit() for char in password):
                missing_requirements.append("Missing digit.")
            return ", ".join(missing_requirements)
    elif difficulty == "Hard":
        if len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(not char.isalnum() for char in password):
            return True
        else:
            missing_requirements = []
            if len(password) < 8:
                missing_requirements.append("Password must be at least 8 characters long.")
            if not any(char.isupper() for char in password):
                missing_requirements.append("Missing uppercase letter.")
            if not any(char.islower() for char in password):
                missing_requirements.append("Missing lowercase letter.")
            if not any(char.isdigit() for char in password):
                missing_requirements.append("Missing digit.")
            if not any(not char.isalnum() for char in password):
                missing_requirements.append("Missing special character.")
            return ", ".join(missing_requirements)
    else:
        return "Invalid difficulty level."


# Main program
password = input("Enter your password: ")
difficulty = input("Choose difficulty level (Easy, Medium, Hard): ")

result = password_checker(password, difficulty)
if result == True:
    print("Password meets the complexity requirements.")
else:
    print("Password does not meet the complexity requirements:")
    print(result)
