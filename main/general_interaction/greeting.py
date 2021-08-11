import random as rd


greetings = ['yo', 'hello', 'hello there uwu', 'yes yes now my g', 'welcome back master senpai']

def generate_greeting():
    greet_message = rd.choice(greetings)
    return greet_message


