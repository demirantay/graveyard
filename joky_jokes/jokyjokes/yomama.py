import random as rand

jokes = [
    "Yo momma so ugly she threw a boomerang and it refused to come back.",

    ("Yo momma so stupid, when I told her that she lost her mind, she went"
     " looking for it."),

    "Yo Momma So Fat The Only Letters She Knows In The Alphabet Are K.F.C!",

    'Yo mamma so ugly even Bob the Builder said, "We cant fix it."',

    ("Yo Mamas so stupid she was yelling into the mailbox.\n"
     "We ask her whats she doing and she said, she was sending a voice-mail."),

    ("Yo momma’s so ugly, the army doesn’t use guns any more – they use her"
     " picture."),

    "Yo' Mama's cooking is so bad, the homeless give it back.",

    ("Yo mama so ugly when Santa came down the chimney he said ho! ho!"
     " hoooollly shit!"),

    ("Your mamma is so fat when she steps on the scales it says one at a"
     " time please."),

    "Yo mama so fat Mount Everest tried to climb her.",
]


# Return a random Chuck Norris Joke
def random():
    random_joke = jokes[rand.randint(0, len(jokes))]
    return random_joke


# Return a specific joke
def joke(number):
    joke = jokes[number]
    return joke


# Return all jokes
def all_jokes():
    all_jokes = ""
    for i in range(len(jokes)):
        all_jokes += jokes[i] + "\n\n"
    return all_jokes
