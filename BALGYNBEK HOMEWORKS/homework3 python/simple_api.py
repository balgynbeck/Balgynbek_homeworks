# Task 3: Simple API Call

import requests

print("=== Getting a Programming Joke ===")
print()

try:
    # Call a simple joke API
    response = requests.get("https://official-joke-api.appspot.com/jokes/programming/random")
    
    if response.status_code == 200:
        joke_data = response.json()
        joke = joke_data[0]  # Get first joke
        
        print("Here's a joke for you:")
        print(joke["setup"])
        print(joke["punchline"])
    else:
        print("Sorry, couldn't get a joke right now")
        print("But here's one for you:")
        print("Why do programmers prefer dark mode?")
        print("Because light attracts bugs!")

except:
    # If API fails, show a backup joke
    print("Here's a joke for you:")
    print("Why do programmers prefer dark mode?")
    print("Because light attracts bugs!")

print()
print("Thanks for using the joke API! 😄")
