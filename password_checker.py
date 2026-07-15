# ==========================================
# DecodeLabs Cyber Security Project 1
# Password Strength Checker
# ==========================================

password = input("Enter your password for strength checking: ")

print("\n-----------------------------------------")
print("      PROJECT 1 : DEFENSIVE LOGIC REPORT")
print("\n-----------------------------------------")

# Check password length
if len(password) < 8:
    print("\nRESULT : FAIL")
    print("STRENGTH : WEAK - Password length is less than 8 characters")
    
else:

    # Security checks
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() and not char.isspace() for char in password)

    score = 0

    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    print("\nPROJECT 1 : DEFENSIVE LOGIC REPORT")

    if score == 4:
        print("RESULT : PASS")
        print("STRENGTH : STRONG - Absolute Precision Secured")

    elif score >= 2:
        print("RESULT : WARNING")
        print("STRENGTH : MEDIUM - Some requirements are missing")

        print("\nMissing Requirements:")
        if not has_upper:
            print("- Add at least one uppercase letter")
        if not has_lower:
            print("- Add at least one lowercase letter")
        if not has_digit:
            print("- Add at least one number")
        if not has_special:
            print("- Add at least one special symbol")

    else:
        print("RESULT : FAIL")
        print("STRENGTH : WEAK - Password does not meet security requirements")

        print("\nMissing Requirements:")
        if not has_upper:
            print("- Add at least one uppercase letter")
        if not has_lower:
            print("- Add at least one lowercase letter")
        if not has_digit:
            print("- Add at least one number")
        if not has_special:
            print("- Add at least one special symbol")

print("Thank you for using Password Strength Checker")
