name = input("What's your name? ")

match name:
    case "Harry" | "Manvendra" | "Ankit":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
