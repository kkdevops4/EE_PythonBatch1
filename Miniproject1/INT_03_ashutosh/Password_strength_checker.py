def check_password_strength(password):
    length_ok = False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"

    # check length
    if len(password) >= 8:
        length_ok = True

    # loop through each character
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True

    # determine strength
    if length_ok and has_upper and has_lower and has_digit and has_special:
        strength = "Strong Password"
    elif length_ok and (has_upper or has_lower) and has_digit:
        strength = "Medium Password"
    else:
        strength = "Weak Password"

    # check missing conditions
    missing = []

    if not length_ok:
        missing.append("at least 8 characters")
    if not has_upper:
        missing.append("an uppercase letter")
    if not has_lower:
        missing.append("a lowercase letter")
    if not has_digit:
        missing.append("a digit")
    if not has_special:
        missing.append("a special character")

    return strength, missing


# user input
pwd = input("Enter your password: ")
strength, missing = check_password_strength(pwd)

print("Password Strength:", strength)

if missing:
    print("Suggestions to improve:")
    for item in missing:
        print("-", item)
else:
    print("Your password meets all criteria.")