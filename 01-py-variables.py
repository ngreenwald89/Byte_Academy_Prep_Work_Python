Michaela = {'Name': 'Michaela', 'Gender': 'Female', 'Height': 178, 'Job': 'Visual Artist', 'Parents': ['Aimee', 'Louis'], 'Pets': ['Fezzy', 'Rufus']};
Steve = {'Name': 'Steve', 'Gender': 'Male', 'Height': 160, 'Job': 'Graphic Designer', 'Nickname': 'The Cow', 'Friends': ['Stephen', 'Stephanie', 'Stefan'], 'Jobs': ['Graphic Designer at Acme Corp', 'Bartender at Banter']};
print(Michaela.items())

def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
