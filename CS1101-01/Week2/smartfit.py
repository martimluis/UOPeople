# SmartFit Decision-Making Assistant
# ---------- Q1: Conditional statements (if, elif, else) ----------
age = int(input("Enter your age: "))

if age < 18:
    print("You are eligible for the Teen Fitness Program.")
elif age <= 40:  # age is between 18 and 40
    print("You are eligible for the Regular Fitness Program.")
else:
    print("You are eligible for the Senior Wellness Program.")

# ---------- Q2: Logical operators (and, or, not) ----------
medical = input("Any medical conditions? (yes/no): ").strip().lower()

if medical not in ("yes", "no"):
    print("Invalid input. Please enter 'yes' or 'no'.")
elif age >= 40 and medical == "yes":
    print("Medical clearance required before joining.")
elif age < 40 or medical == "no":
    print("You can proceed with registration.")

has_medical = medical == "yes"  # Boolean: True or False

# ---------- Q3.1: Nested conditional statements ----------
membership = input("Membership type (Basic/Premium): ").strip().lower()
training = ""  # stays empty unless the user chooses Basic

if membership == "basic":
    training = input("Personal training? (yes/no): ").strip().lower()
    if training == "yes":
        print("Basic plan with personal training: $45 per month.")
    elif training == "no":
        print("Basic plan: $30 per month.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
elif membership == "premium":
    print("Premium plan: $60 per month.")
else:
    print("Invalid membership type. Please choose Basic or Premium.")

# ---------- Q3.2: Nested conditionals with logical operators ----------
if membership == "basic" or membership == "premium":
    if membership == "premium" and age < 30:
        print("You qualify for a youth discount! 10% off your plan.")
    if membership == "basic" and training == "no":
        print("Consider upgrading to Premium for more benefits!")
    if has_medical and membership == "premium":
        print("We recommend a free consultation before starting.")