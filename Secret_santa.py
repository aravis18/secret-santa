import random

# List of participants
PARTICIPANTS = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank']

# Make a copy of the list and shuffle it
secret_santas = list(PARTICIPANTS)
random.shuffle(secret_santas)

# -------- Print out the pairing ------------------
pairs = zip(PARTICIPANTS, secret_santas)
for giver, receiver in pairs:
    print(f'{giver} will be buying a gift for {receiver}')

# ------------- Output the name of who to buy for -----------------------
# Zip the two lists together and create a dictionary mapping givers to receivers
giver_to_receiver = dict(zip(PARTICIPANTS, secret_santas))

def get_receiver(giver):
    return giver_to_receiver[giver]

# Test the function
print(get_receiver('Alice'))  # prints the name of Alice's Secret Santa
print(get_receiver('Bob'))  # prints the name of Bob's Secret Santa
print(get_receiver('Charlie'))  # prints the name of Charlie's Secret Santa