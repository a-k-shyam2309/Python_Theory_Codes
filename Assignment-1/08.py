def validatepassword(password):
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")

    if not any(ch.isupper() for ch in password):
        errors.append("Password must contain at least one uppercase letter (A–Z).")

    if not any(ch.islower() for ch in password):
        errors.append("Password must contain at least one lowercase letter (a–z).")

    if not any(ch.isdigit() for ch in password):
        errors.append("Password must contain at least one digit (0–9).")

    special_characters = "!@#$%"
    if not any(ch in special_characters for ch in password):
        errors.append("Password must contain at least one special character (! @ # $ %).")

    if any(ch.isspace() for ch in password):
        errors.append("Password must not contain white spaces.")

    if len(errors) == 0:
        return True, []
    else:
        return False, errors


password = input("Enter your password: ")
valid, msgs = validatepassword(password)

if valid:
    print("Password is VALID.")
else:
    print("Password is INVALID.")
    print("Issues found:")
    for m in msgs:
        print("-", m)
