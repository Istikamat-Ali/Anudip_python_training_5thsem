# Windsurf Sign In
# Simple username/password sign-in simulation for Windsurf

accounts = {
    "windsurfer": "surf2026",
    "admin": "admin123",
    "guest": "wave2026"
}

print("=== Windsurf Sign In ===")

max_attempts = 3
for attempt in range(1, max_attempts + 1):
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if accounts.get(username) == password:
        print(f"Welcome, {username}! You have signed in successfully.")
        break
    else:
        print("Invalid username or password.")
        if attempt < max_attempts:
            print(f"Attempt {attempt} of {max_attempts}. Please try again.\n")
else:
    print("You have reached the maximum number of sign-in attempts.")
