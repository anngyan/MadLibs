print("Hi, let's play a game! You're gonna choose a template, "
      "give me some words and i'm gonna make a story for you. Let's go!")

template = input("Input a template number(1, 2, or 3): ")
template = int(template)
arr = []
if template == 1:
    num1 = input("Input a Number: ")
    arr.append(num1)  # 0
    measure = input("Input a Measure of time: ")
    arr.append(measure)  # 1
    transport = input("Input a Mode of Transportation: ")
    arr.append(transport)  # 2
    adjective = input("Input an Adjective: ")
    arr.append(adjective)  # 3
    adjective2 = input("Input an Adjective again: ")
    arr.append(adjective2)  # 4
    noun = input("Input a Noun(plural): ")
    arr.append(noun)  # 5
    color = input("Input a Color: ")
    arr.append(color)  # 6
    partOfBody = input("Input a Part of the Body(plural): ")
    arr.append(partOfBody)  # 7
    verb = input("Input a Verb: ")
    arr.append(verb)  # 8
    num2 = input("Input a Number: ")
    arr.append(num2)  # 9
    if int(num2) > 1:
        noun2 = input("Input a Noun(plural): ")
    else:
        noun2 = input("Input a Noun: ")
    arr.append(noun2)  # 10
    noun3 = input("Input a Noun again: ")
    arr.append(noun3)  # 11
    partOfBody2 = input("Input a Part of the Body: ")
    arr.append(partOfBody2)  # 12
    verb2 = input("Input a Verb: ")
    arr.append(verb2)  # 13
    noun4 = input("Input a Noun: ")
    arr.append(noun4)  # 14
    adjective3 = input("Input an Adjective: ")
    arr.append(adjective3)  # 15
    silly = input("Input a Silly Word: ")
    arr.append(silly)  # 16
    noun5 = input("Input a Noun: ")
    arr.append(noun5)  # 17

    if int(num1) > 1 and measure[-1] != "s":
        if measure == "century":
            arr[1] = "centuries"
        else:
            arr[1] = measure + "s"

    if transport[0] == 'a' or transport[0] == 'A' or transport[0] == 'e' or transport[0] == 'E' or transport[0] == 'o' or transport[0] == 'O' or transport[0] == 'i' or transport[0] == 'I' or transport[0] == 'u' or transport[0] == 'U':
        arr[2] = "an " + transport
    else:
        arr[2] = "a " + transport

    if adjective[0] == 'a' or adjective[0] == 'A' or adjective[0] == 'e' or adjective[0] == 'E' or adjective[0] == 'o' or adjective[0] == 'O' or adjective[0] == 'i' or adjective[0] == 'I' or adjective[0] == 'u' or adjective[0] == 'U':
        arr[3] = "an " + adjective
    else:
        arr[3] = "a " + adjective

    if noun3[0] == 'a' or noun3[0] == 'A' or noun3[0] == 'e' or noun3[0] == 'E' or noun3[0] == 'o' or noun3[0] == 'O' or noun3[0] == 'i' or noun3[0] == 'I' or noun3[0] == 'u' or noun3[0] == 'U':
        arr[11] = "an " + noun3
    else:
        arr[11] = "a " + noun3

    print("\nHere is your story:\n")
    print(f"It was about {arr[0]} {arr[1]} ago when I arrived at the hospital in {arr[2]}."
          f"The hospital is {arr[3]} place, there are a lot of {arr[4]} {arr[5]} here. \n There are nurses "
          f"here who have {arr[6]} {arr[7]}. If someone wants to come into my room I told them that they "
          f"have to {arr[8]} first. I've decorated my room with {arr[9]} {arr[10]}. \n Today I talked to a doctor "
          f"and they were wearing {arr[11]} on their {arr[12]}. I heard that all doctors {arr[13]} {arr[14]} every "
          f"day for breakfast. \n The most {arr[15]} thing about being in the hospital is the {arr[16]} {arr[17]}!")

if template == 2:
    person = input("Input Person Name: ")
    arr.append(person)  # 0
    noun = input("Input a Noun: ")
    arr.append(noun)  # 1
    adjective = input("Input an Adjective(feeling): ")
    arr.append(adjective)  # 2
    verb = input("Input a Verb: ")
    arr.append(verb)  # 3
    adjective2 = input("Input an Adjective(feeling): ")
    arr.append(adjective2)  # 4
    animal = input("Input an Animal: ")
    arr.append(animal)  # 5
    verb2 = input("Input a Verb: ")
    arr.append(verb2)  # 6
    color = input("Input a Color: ")
    arr.append(color)  # 7
    verb3 = input("Input a Verb(ending in -ing): ")
    arr.append(verb3)  # 8
    adverb = input("Input an Adverb(ending in -ly): ")
    arr.append(adverb)  # 9
    num1 = input("Input a Number: ")
    arr.append(num1)  # 10
    measure = input("Input a Measure of time: ")
    arr.append(measure)  # 11
    color2 = input("Input a Color: ")
    arr.append(color2)  # 12
    animal2 = input("Input an Animal: ")
    arr.append(animal2)  # 13
    num2 = input("Input a Number: ")
    arr.append(num2)  # 14
    silly = input("Input a Silly Word: ")
    arr.append(silly)  # 15
    noun2 = input("Input a Noun: ")
    arr.append(noun2)  # 16

    if animal[0] == 'a' or animal[0] == 'A' or animal[0] == 'e' or animal[0] == 'E' or animal[0] == 'o' or animal[0] == 'O' or animal[0] == 'i' or animal[0] == 'I' or animal[0] == 'u' or animal[0] == 'U':
        arr[5] = "an " + animal
    else:
        arr[5] = "a " + animal

    if int(num1) > 1 and measure[-1] != "s":
        if measure == "century":
            arr[11] = "centuries"
        else:
            arr[11] = measure + "s"

    if color2[0] == 'a' or color2[0] == 'A' or color2[0] == 'e' or color2[0] == 'E' or color2[0] == 'o' or color2[0] == 'O' or color2[0] == 'i' or color2[0] == 'I' or color2[0] == 'u' or color2[0] == 'U':
        arr[12] = "an " + color2
    else:
        arr[12] = "a " + color2

    print("\nHere is your story:\n")
    print(f"This weekend I am going camping with {arr[0]}. I packed my lantern, sleeping bag, and {arr[1]}. I am so "
          f"{arr[2]} to {arr[3]} in a tent. I am {arr[4]} we might see {arr[5]}, I hear they're kind of dangerous.\n "
          f"While we're camping, we are going to hike, fish, and {arr[6]}. I have heard that the {arr[7]} lake is "
          f"great for {arr[8]}. Then we will {arr[9]} hike through the forest for {arr[10]} {arr[11]}.\n If I see "
          f"{arr[12]} {arr[13]} while hiking, I am going to bring it home as a pet! At night we will tell {arr[14]} "
          f"{arr[15]} stories and roast {arr[16]} around the campfire!!")

if template == 3:
    person = input("Input Person Name: ")
    arr.append(person)  # 0
    adjective = input("Input an Adjective: ")
    arr.append(adjective)  # 1
    color = input("Input a Color: ")
    arr.append(color)  # 2
    animal = input("Input an Animal: ")
    arr.append(animal)  # 3
    place = input("Input a Place: ")
    arr.append(place)  # 4
    adjective2 = input("Input an Adjective: ")
    arr.append(adjective2)  # 5
    magCr = input("Input a Magical Creature(plural): ")
    arr.append(magCr)  # 6
    adjective3 = input("Input an Adjective: ")
    arr.append(adjective3)  # 7
    magCr2 = input("Input a Magical Creature(plural): ")
    arr.append(magCr2)  # 8
    room = input("Input a room in a house: ")
    arr.append(room)  # 9
    noun = input("Input a Noun: ")
    arr.append(noun)  # 10
    noun2 = input("Input a Noun again: ")
    arr.append(noun2)  # 11
    noun3 = input("Input a Noun again(plural): ")
    arr.append(noun3)  # 12
    adjective4 = input("Input an Adjective: ")
    arr.append(adjective4)  # 13
    noun4 = input("Input a Noun again(plural): ")
    arr.append(noun4)  # 14
    num1 = input("Input a Number: ")
    arr.append(num1)  # 15
    measure = input("Input a Measure of time: ")
    arr.append(measure)  # 16
    verb = input("Input a Verb(ending in -ing): ")
    arr.append(verb)  # 17
    adjective5 = input("Input an Adjective: ")
    arr.append(adjective5)  # 18
    noun5 = input("Input a Noun: ")
    arr.append(noun5)  # 19

    if adjective[0] == 'a' or adjective[0] == 'A' or adjective[0] == 'e' or adjective[0] == 'E' or adjective[0] == 'o' or adjective[0] == 'O' or adjective[0] == 'i' or adjective[0] == 'I' or adjective[0] == 'u' or adjective[0] == 'U':
        arr[1] = "an " + adjective
    else:
        arr[1] = "a " + adjective

    if color[0] == 'a' or color[0] == 'A' or color[0] == 'e' or color[0] == 'E' or color[0] == 'o' or color[0] == 'O' or color[0] == 'i' or color[0] == 'I' or color[0] == 'u' or color[0] == 'U':
        arr[2] = "an " + color
    else:
        arr[2] = "a " + color

    if noun2[0] == 'a' or noun2[0] == 'A' or noun2[0] == 'e' or noun2[0] == 'E' or noun2[0] == 'o' or noun2[0] == 'O' or noun2[0] == 'i' or noun2[0] == 'I' or noun2[0] == 'u' or noun2[0] == 'U':
        arr[11] = "an " + noun2
    else:
        arr[11] = "a " + noun2

    if int(num1) > 1 and measure[-1] != "s":
        if measure == "century":
            arr[16] = "centuries"
        else:
            arr[16] = measure + "s"

    if adjective5[0] == 'a' or adjective5[0] == 'A' or adjective5[0] == 'e' or adjective5[0] == 'E' or adjective5[0] == 'o' or adjective5[0] == 'O' or adjective5[0] == 'i' or adjective5[0] == 'I' or adjective5[0] == 'u' or adjective5[0] == 'U':
        arr[18] = "an " + adjective5
    else:
        arr[18] = "a " + adjective5

    print("\nHere is your story:\n")
    print(f"Dear {arr[0]}, I am writing to you from {arr[1]} castle in an enchanted forest. I found myself here "
          f"one day after going for a ride on {arr[2]} {arr[3]} in {arr[4]}.\n There are {arr[5]} {arr[6]} and "
          f"{arr[7]} {arr[8]} here! In the {arr[9]} there is a pool full of {arr[10]}. I fall asleep each night "
          f"on {arr[11]} of {arr[12]} and dream of {arr[13]} {arr[14]}.\n It feels as though I have lived here for "
          f"{arr[15]} {arr[16]}. I hope one day you can visit, although the only way to get here now is {arr[17]} "
          f"on {arr[18]} {arr[19]}!!")
