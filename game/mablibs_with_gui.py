story_choice = input("Before the game begin, choose one of the following:\n"
"'The Matrix', 'Humpty Dumpty', --> ")

if story_choice == 'The Matrix':
    # Init  Variables
    TheMatrix = ""
    system = ""
    Neo = ""
    enemy = ""
    inside = ""
    save = ""
    unplugged = ""
    fight = ""

    profession = ["","","",""]
    adj = ["",""]

    # Get Input from User
    print("Welcome User!")
    print("Let's play a game of madlibs!")
    Neo = input("Please share with me your name? --> ")

    # Getting The Matrix variable from user
    print(f"Hello {Neo}! Are you ready?")
    TheMatrix = input("What is it you want to know more about? --> ")

    # Getting system variable from user
    print(f"Ooh, so you want to know more about {TheMatrix}, huh?")
    print(f"Okay, first tell me what you already know about {TheMatrix}.")
    system = input(f"What noun would you categorize {TheMatrix} as: ")

    # Getting enemy variable from user
    enemy = input(f"Give me a opposing noun to {system}. --> ")

    # Getting inside variable from user
    inside = input(f"Now give me a relaxing noun (present tense). --> ")

    # Getting all profession variable from user
    print(f"Okay, now I need 4 professions relating to {system}:")

    for i in range(len(profession)):
        profession[i] = input(f"Profession (plural) {i+1} / {len(profession)}. --> ")

    # Getting save variable
    save = input(f"Give me a helo-related verb (present tense). --> ")

    # Getting the unplugged variable
    unplugged = input(f"Now give me a verb that makes you think about relief (past tense). --> ")

    # Getting the adjectives
    print(f"Lastly I need 2 dystopian adjectives:")

    for i in range(len(adj)):
        adj[i] = input(f"Adjective {i+1} / {len(adj)}. --> ")

    # Getting the fight variable
    fight = input(f"And a verb. --> ")
    # Init Story
    madlibsStory = (f"{TheMatrix} is a {system}, {Neo}. That {system} is our {enemy}.\n " + 
    f"But when you're {inside}, you look around, what do you see?\n " +
    f"{profession[0]}, {profession[1]}, {profession[2]}, {profession[3]}.\n The very minds " +
    f"of the people we are trying to {save}.\n But until we do, " +
    f"these people are still a part of that {system} and that makes " +
    f"them our {enemy}.\n You have to understand, most of these people " +
    f"are not ready to be {unplugged}.\n And many of them are so {adj[0]}, " +
    f"so hopelessly {adj[1]} on the {system}, that they will {fight} to protect it.")

    # Print Story
    print(madlibsStory)
    input()

elif story_choice == 'Humpty Dumpty':

    # Init variables
    HumptyDumpty = ""
    wall = ""
    kings = ""
    horses = ""
    name = ""

    # Get input from user
    print("Welcome User!")
    print("Let's play a game of madlibs!")
    name = input("Please share with me your name? --> ")

    # init story
    madlibsStory = (f"{HumptyDumpty} sat on a {wall}, {HumptyDumpty} had a great fall.\n" +
    f"All the {kings} men and all the {kings} {horses}.\n" +
    f"Couldn't put him back together again.")
    
    # print story
    print(madlibsStory)
    input()