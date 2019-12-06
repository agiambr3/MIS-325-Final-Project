import random

print("Holiday Song Madlibs!")

r = random.randint(1,3)

if r == 1:
    song1_noun1 = input("Noun: ")
    song1_noun2 = input("Noun: ")
    song1_pluralnoun1 = input("Plural noun: ")
    song1_verbing1 = input("Verb ending in -ing: ")
    song1_liquid = input("A liquid: ")
    song1_pluralnoun2 = input("Plural noun: ")
    song1_verbing2 = input("Verb ending in -ing: ")
    song1_singular1 = input("Singular noun: ")
    song1_holiday = input("Holiday: ")
    song1_noun4 = input("Noun: ")
    song1_adjective = input("Adjective: ")

    print(f'''
    "Like It's Christmas" by the Jonas Brothers

    The {song1_noun1} on the ground
    The {song1_noun2} in the air
    The {song1_pluralnoun1} are {song1_verbing1}
    This is what it's all about
    The {song1_liquid} is warm
    The {song1_pluralnoun2} are {song1_verbing2}
    And I don't wanna miss
    A single {song1_singular1}
    Don't want to put an end to all this cheer
    But as long as you're with me it's always the time of the year

    You make every day feel like it's {song1_holiday}
    Never wanna stop
    Feeling like the first thing on my {song1_noun4}
    Right up at the top
    I can't deny what I'm feeling inside
    Nothing {song1_adjective} about the way you bring me to life
    You make every day feel like it's {song1_holiday}
    Every day that I'm with you''')


elif r == 2:
    song2_adjective1 = input("Adjective: ")
    song2_noun1 = input("Noun: ")
    song2_adjective2 = input("Adjective: ")
    song2_verb1 = input("Verb that ends in 's': ")
    song2_verb2 = input("Verb: ")
    song2_adjective3 = input("Adjective: ")
    song2_verb3 = input("Verb: ")
    song2_verb4 = input("Past Tense Verb: ")
    song2_verb5 = input("Past Tense Verb: ")
    song2_adjective4 = input("Adjective: ")


    print(f'''
    "Rudolph the Red Nose Reindeer" by Gene Autry

    Rudolph the {song2_adjective1} nosed {song2_noun1}
    Had a very {song2_adjective2} nose
    And if you ever saw it
    You would even say it {song2_verb1}
    All of the other {song2_noun1}
    Used to {song2_verb2} and call him names
    They never let poor Rudolph
    Join in any {song2_noun1} games
    Then one foggy Christmas Eve
    Santa came to say
    "Rudolph, with your nose so {song2_adjective3}
    Won't you {song2_verb3} my sleigh tonight?"
    Then how the {song2_noun1} {song2_verb4} him
    As they {song2_verb5} out with {song2_adjective4}
    "Rudolph the {song2_adjective1} nose {song2_noun1}
    You'll go down in history"''')

elif r == 3:
    song3_verb1 = input("verb: ")
    song3_verb1 = song3_verb1.title()
    song3_noun1 = input("noun: ")
    song3_noun2 = input("noun: ")
    song3_sound2 = input("sound: ")
    song3_noun3 = input("noun: ")
    song3_noun4 = input("noun: ")
    song3_noun5 = input("noun: ")
    song3_noun6 = input("noun: ")
    song3_body_part_1 = input("body part: ")
    song3_verb_ending_ing1 = input("verb ending in -ing: ")
    
    print(f'''
    "Santa's Coming for Us" by Sia
    
    {song3_verb1} it to the {song3_noun1} in the {song3_noun2}, 
    {song3_verb1} it as they {song3_sound2}, {song3_sound2}, {song3_sound2} tonight,
    {song3_verb1} it to the {song3_noun3}, set it free,
    You're the {song3_noun4} on the top of my {song3_noun5},
    {song3_verb1} it to the {song3_noun6} above,
    {song3_verb1} your {song3_body_part_1} out with all of your love, 
    Santa's {song3_verb_ending_ing1} for us''')
