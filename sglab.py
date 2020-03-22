tries1 = 1
guess1 = 500
modif = [500, 250, 125, 63, 32, 16, 8, 4, 2, 1]

def newGame():
    print("Choose a number between 1 and 1000,")
    print("and I will guess it in no more then 10 tries!")
    print("")
    print("Start Game!")
    print("1. Yes, or")
    print("2. No")
    yesorno = input("Pilihan: ")

    if (yesorno == 1):
        guess2 = 0
        tries2 = 0
        while (guess2 != 1000 and tries2 != 10) :
            print("Is Your Number 500? ")
            print("1. Yes, it is! ")
            print("2. No, it's higher")
            print("3. No, it's lower")
            print("Number of Tries: 1")
            isnumber = input("pilihan: ")

            if (isnumber == 1) :
                print("It's 500 (if it's not the right answer then you lied somewhere, shame on you!)")
                print("Number of tries: 1")
            elif (isnumber == 2) :
                guess2 = guess1 + modif[tries1]
                tries2 = tries1 + 1
                while (guess2 == 1000 or tries2 == 10):
                    if (guess2 == 1000):
                        print("It's 1000 (if it's not the right answer then you lied somewhere, shame on you!)")
                        print("Number of tries: " + tries2)
                    if (tries2 == 10):
                        print("It's " + guess2+ "if it's not the right answer then you lied somewhere, shame on you!)")
                        print("Number of tries: 10 ")
            elif (isnumber == 3) :
                guess2 = guess1 - modif[tries]
                tries2 = tries1 + 1
                while (guess2 == 0 or tries2 == 10):
                    if (guess2 == 0):
                        print("It's 0 (if it's not the right answer then you lied somewhere, shame on you!)")
                        print("Number of tries: " + tries2)
                    if (tries2 == 10):
                        print("It's " + guess2+ "if it's not the right answer then you lied somewhere, shame on you!)")
                        print("Number of tries: 10 ")
    elif (yesorno == 1) :
        print("kenapa pilih no? :( ")

newGame()