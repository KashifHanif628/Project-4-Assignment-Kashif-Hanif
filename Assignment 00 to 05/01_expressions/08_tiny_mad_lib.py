SENTENCE_START: str = "Coding is amazing. I built a/an "

def main():
    # Get the three inputs from the user to complete the sentence
    adjective: str = input("Please type an adjective and press enter: ") # intelligent as an adjective 
    noun: str = input("Please type a noun and press enter: ") # robot as a noun
    verb: str = input("Please type a verb and press enter: ") # dance as verb

    # Join the inputs together with the sentence starter
    print(SENTENCE_START + adjective + " " + noun + " that can " + verb + "!")

if __name__ == '__main__':
    main()
