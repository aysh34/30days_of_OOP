# Question 3: Password Strength Checker
# Write a function check_password_strength that takes a string password as input and returns a message indicating the strength of the password based on the following criteria:
# Length less than 6 characters: "Weak"
# Length 6-10 characters: "Moderate"
# Length greater than 10 characters: "Strong"


def check_password_strength(password: str) -> str:
    length = len(password)
    match length:
        case length if length < 6:
            return "Weak"
        case 6 | 7 | 8 | 9 | 10:
            return "Moderate"
        case length if length > 10:
            return "Strong"

print(check_password_strength("125879"))
print(check_password_strength("129"))
print(check_password_strength("12***Ayd9870"))
print(check_password_strength("12879"))
