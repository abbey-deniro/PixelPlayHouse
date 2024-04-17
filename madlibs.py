import random, os


def get_mad_lib():
    print("Welcome to MadLibs! Lets get started by entering the blank spaces!\n")
    adj1 = input("Adjective: ")
    noun1 = input("Noun: ")
    plural_noun = input("Plural Noun: ")
    animal1 = input("Animal: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")
    animal2 = input("Animal: ")
    noun2 = input("Noun: ")
    adj4 = input("Adjective: ")

    mad_libs = [
    f"During my visit to the {adj1} blogosphere, I saw a {noun1} writing about {plural_noun}. One {animal1} was especially {adj2}, typing away furiously.\nThe author, a {adj3} {animal2}, used a tiny {noun2} as a desk. It was the most {adj4} thing I'd ever seen.",
    f"During my visit to the {adj1} zoo, I saw a {noun1} teaching yoga to a group of {plural_noun}. One {animal1} was especially {adj2}, doing poses I couldn’t even attempt.\nThe instructor, a {adj3} {animal2}, handed out tiny {noun2}. It was the most {adj4} thing I'd ever seen.",
    f"During my visit to the {adj1} eating contest, I saw a {noun1} gobbling {plural_noun}. One {animal1} was especially {adj2}, munching faster than the rest.\nThe champion, a {adj3} {animal2}, used a giant {noun2} as a spoon. It was the most {adj4} thing I'd ever seen.",
    f"During my visit to the {adj1} ship, I saw a {noun1} mimicking the crew. One {animal1} was especially {adj2}, repeating everything loudly.\nThe mischievous, a {adj3} {animal2}, stole the captain’s {noun2}. It was the most {adj4} thing I'd ever seen.",
    f"During my visit to the {adj1} fair, I saw a {noun1} hurling {plural_noun} at targets. One {animal1} was especially {adj2}, hitting the bullseye every time.\nThe winner, a {adj3} {animal2}, received a giant {noun2} as a prize. It was the most {adj4} thing I'd ever seen.",
    f"During my visit to the {adj1} neighborhood, I saw a {noun1} parading with {plural_noun}. One {animal1} was especially {adj2}, dressed in a {adj3} outfit.\nThe local, a {adj3} {animal2}, tried to give out {noun2} but failed hilariously. It was the most {adj4} thing I'd ever seen.",
    f"During my visit to the {adj1} picnic, I saw a {noun1} singing karaoke. One {animal1} was especially {adj2}, belting out tunes flawlessly.\nThe performer, a {adj3} {animal2}, forgot the {noun2} but improvised brilliantly. It was the most {adj4} thing I'd ever seen.",
    f"During my visit to the {adj1} kitchen, I saw a {noun1} organizing {plural_noun}. One {animal1} was especially {adj2}, sorting meticulously.\nThe conspirator, a {adj3} {animal2}, had plans for a {noun2} takeover. It was the most {adj4} thing I'd ever seen.",
    f"During my visit to the {adj1} party, I saw a {noun1} attempting to bake a cake. One {animal1} was especially {adj2}, trying hard but failing.\nThe baker, a {adj3} {animal2}, ended up with a cake that looked like a {noun2}. It was the most {adj4} thing I'd ever seen.",
    f"During my visit to the {adj1} town square, I saw a {noun1} commanding {plural_noun}. One {animal1} was especially {adj2}, issuing quirky demands.\nThe leader, a {adj3} {animal2}, negotiated for a {noun2} parade. It was the most {adj4} thing I'd ever seen."
    ]

    return print("\n" + random.choice(mad_libs))

if __name__ == "__main__":
    get_mad_lib()

