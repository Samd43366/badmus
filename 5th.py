sent = input("Enter your sentence here:")
subs = input("Enter the substring to know how many it is:")
try:
    count = sent.count(subs)
    print(f"The substring '{subs}' appears {count} times in the sentence.")
except ValueError:
    print("Please enter a valid string.")