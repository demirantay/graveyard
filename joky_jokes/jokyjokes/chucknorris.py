import random as rand

jokes = [
    ("Chuck Norris and Superman once fought each other on a bet. The loser had"
     "to start wearing his underwear on the outside of his pants."),

    "Chuck Norris threw a grenade and killed 50 people, then it exploded.",

    ("Chuck Norris died 20 years ago, Death just hasn't built up the courage"
     "to tell him yet."),

    ("While learning CPR Chuck Norris actually brought the practice dummy to"
     "life."),

    ("Chuck Norris can lift up a chair with one hand... While he's sitting on"
     " it..."),

    ("Chuck Norris doesn't check under his bed for monsters, monsters check"
     " on top of the bed to see if Chuck Norris is sleeping."),

    ("Chuck norris went skydiving and his parachute failed to open, so he took"
     "it back the next day for a refund"),

    "Chuck Norris can light a fire by rubbing two ice-cubes together.",

    ("Before going to bed, the Boogeyman always checks his closet for Chuck"
     " Norris."),

    "Ckuck Norris doesn't flush the toilet...he scares the shit out of it.",
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
