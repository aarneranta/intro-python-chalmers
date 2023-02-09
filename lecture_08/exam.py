# exam

# Q 1

def bmi(weight, height):
    b = weight/(height ** 2)
    if b < 18.5:
        cat = 'Underweight'
    elif 18.5 <= b < 25.0:
        cat = 'Normal'
    elif 25.0 <= b <= 30.0:
        cat = 'Overweight'
    else:
        cat = 'Obese'
    return(b, cat)

"""
for w in range(50, 150, 10):
    print(w, bmi(w, 1.80))
"""

def ask_bmi():
    w = float(input('weight in kg:' ))
    h = float(input('height in m:' ))
    b, c = bmi(w, h)
    print('your bmi is', b, 'which means', c)


# ask_bmi()


# Q 2
def analyse_text(keywords, text):
    words = text.split()
    name = words[-1]
    toys = [w for w in words if w in keywords]
    return name, toys

"""
toys = ['bil', 'dator', 'häst']
letter = 'Jag vill ha en häst och en dator önskar Aarne'
print(analyse_text(toys, letter))
"""

def read_letter(filename, keywords):
    with open(filename) as file:
        text = file.read()
    return analyse_text(keywords, text)


toys = ['bil', 'dator', 'häst']
letter = 'till_tomten.txt'

print(read_letter(letter, toys))







    
