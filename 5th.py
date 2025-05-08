sent = ("Emma is good developer. Emma is a writer")
subs = ("Emma")
try:
    count = sent.count(subs)
    print(f"The substring '{subs}' appears {count} times in the sentence.")
except ValueError:
    print("Please enter a valid string.")