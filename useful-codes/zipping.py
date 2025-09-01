usernames = ["Zach", "Benedict", "Hallare"]
passwords = ("p@ssword", "abc123", "guest")

# combines the elements of username and passwords.
users = dict(zip(usernames, passwords))

for key, value in users.items():
    print(key + " : " + value)


