import random as rand

jokes = [
    ('A woman is standing looking in the bedroom mirror…\nShe is not happy'
     ' with what she sees and says to her husband, “I feel horrible\nI look'
     ' old, fat and ugly… I really need you to pay me a compliment.”\nThe '
     'husband replies, “Your eyesight’s damn near perfect.”'),

    ('One day, Little Johnny saw his grandpa smoking his cigarettes. Little'
     ' Johnny asked, "Grandpa, can I smoke some of your cigarettes?" His '
     'grandpa replied, "Can your penis reach your asshole?" "No", said Little'
     ' Johnny. His grandpa replied, "Then you are not old enough."\n\n'
     'The next day, Little Johnny saw his grandpa drinking beer. He asked,'
     ' "Grandpa, can I drink ssome of your beer?" His grandpa replied '
     '"Can your penis reach your asshole?" "No" said Little Johhny. "Then '
     'you are not old enough." his grandpa replied.\n\nThe next day, Little '
     ' Johnny was eating cookies. His grandpa asked, "Can I have some of your'
     ' cookies?" Little Johnny replied, "Can your penis reach your asshole?" '
     'His grandpa replied, "It most certainly can!" Little Johnny replied,'
     ' "Then go fuck yourself.'),

    ('A teacher asks her class, "What do you want to be when you grow up?"\n'
     'Little Johnny says "I wanna be a billionaire, going to the most'
     ' expensiveLittle Johnny says "I wanna be a billionaire, going to the'
     ' most expensive clubs, take the best bitch with me, give her a Ferrari'
     ' worth over a million bucks, an apartment in Hawaii, a mansion in Paris,'
     ' a jet to travel through Europe, an Infinite Visa Card and to make love'
     ' to her three times a day".\nThe teacher, shocked, and not knowing what'
     ' to do with the bad behavior of the child, decides not to give '
     'importance to what he said and then continues the lesson.\n"And you,'
     ' Susie? " the teacher asks.\nSusie says "I wanna be Johnnys bitch."'),

    ('A man inserted an `ad` in the classifieds: "Wife wanted."\nNext day he'
     ' received a hundred letters.\nThey all said the same thing: "You can'
     ' have mine."'),

    ('Sex is like math:\nAdd the bed\nSubtract the clothes\n'
     'Divide the legs and pray you dont multiply'),

    ('There was this man who walked into a bar and says to the bartender 10'
     ' shots of whiskey.\nThe bartender asks, "Whats the matter?"\n'
     'The man says, "I found out my brother is gay and marrying my best'
     ' friend."\nThe next day the same man comes in and orders 12 shots of'
     ' whiskey.\nThe bartenders asks, "Whats wrong this time?"\n'
     'The man says, "I found out that my son is gay."\nThe next day the same'
     ' man comes in the bar and orders 15 shots of whiskey.\n'
     'Then the bartender asks, "Doesnt anyone in your family like women?"\n'
     'The man looks up and says, "Apprently my wife does."'),

    ('Q. What do Disney World & Viagra have in common?\nA. They both make'
     ' you wait an hour for a two minute ride.'),

    ('Cop on horse says to little girl on bike, "Did Santa get you that?"\n'
     '"Yes," replies the little girl\n"Well tell him to put a reflector light'
     ' on it next year!" and fines her $5.\nThe little girl looks up at the '
     'cop and says, "Nice horse youve got there, did Santa bring you that?"\n'
     'The cop chuckles and replies, "He sure did!"\n"Well," says the little '
     'girl, "Next year tell Santa that the d*ck goes under the horse, not'
     ' on top of it!"'),

    ('A dick has a sad life.\nHis hair is a mess, his family is nuts, his '
     'neighbor is an asshole, his bestfriend is a pussy, and his owner beats'
     'him'),

    ('An 85-year-old man was requested by his doctor for a sperm count as '
     'part of his physical exam. The doctor gave the man a jar and said, '
     '"Take this jar home and bring back a semen sample tomorrow."\n'
     'The next day the 85-year-old man reappeared at the doctors office and'
     ' gave him the jar, which was as clean and empty as on the previous day\n'
     'The doctor asked, what happened and the man explained.\n"Well, doc, it'
     ' is like this--first I tried with my right hand, but nothing. Then I '
     'tried with my left hand, but still nothing. Then I asked my wife for'
     ' help. She tried with her right hand, then with her left, still'
     ' nothing. She tried with her mouth, first with the teeth in, then with '
     'her teeth out, still nothing. We even called up Arleen, the lady next '
     'door and she tried too, first with both hands, then an armpit, and she'
     ' even tried squeezing it between her knees, but still nothing."\n'
     'The doctor was shocked! "You asked your neighbor?"\nThe old man replied,'
     ' "Yep, none of us could get the jar open."'),
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
