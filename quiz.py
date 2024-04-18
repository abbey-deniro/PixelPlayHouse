import os

science_questions = [
        ("What is the most abundant gas in the Earth's atmosphere", "Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen", "4"),
        ("What is the chemical symbol for gold?", "Au", "Ag", "Ga", "Ge", "1"),
        ("Which planet is known as the Red Planet?", "Jupiter", "Mars", "Saturn", "Venus", "2"),
        ("What type of animal is a Komodo dragon?", "Bird", "Reptile", "Mammal", "Fish", "2"),
        ("How long does it take for the Earth to orbit the Sun?", "24 hours", "365 days", "30 days", "12 hours", "2"),
        ("Which of the following is NOT a type of rock?", "Igneous", "Sedimentary", "Basalt", "Metamorphic", "3"),
        ("What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", "Quartz", "3"),
        ("What does DNA stand for?", "Deoxyribonucleic Acid", "Deoxyribogenetic Acid", "Dichloronucleic Acid", "Dinucleotide Acid", "1"),
        ("Which vitamin is primarily obtained from sunlight?", "Vitamin A", "Vitamin B12", "Vitamin D", "Vitamin E", "3"),
        ("What gas do plants absorb from the atmosphere for photosynthesis?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Argon", "3")
    ]

books_authors_questions = [
        ("Who wrote '1984'?", "Aldous Huxley", "George Orwell", "Ray Bradbury", "Philip K. Dick", "2"),
        ("What is the title of the first Harry Potter book?", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Sorcerer's Stone", "Harry Potter and the Goblet of Fire", "Harry Potter and the Order of the Phoenix", "2"),
        ("Which author created the character Sherlock Holmes?", "Charles Dickens", "Arthur Conan Doyle", "Agatha Christie", "Ian Fleming", "2"),
        ("'To Kill a Mockingbird' was written by which author?", "Harper Lee", "Truman Capote", "John Steinbeck", "Ernest Hemingway", "1"),
        ("Who is the author of 'Pride and Prejudice'?", "Charlotte Brontë", "Jane Austen", "Emily Brontë", "Louisa May Alcott", "2"),
        ("Which book is attributed to the author Gabriel Garcia Marquez?", "Love in the Time of Cholera", "One Hundred Years of Solitude", "The Alchemist", "Don Quixote", "3"),
        ("'The Great Gatsby' was authored by which writer?", "F. Scott Fitzgerald", "William Faulkner", "Ernest Hemingway", "John Steinbeck", "1"),
        ("Which of these novels was written by J.R.R. Tolkien?", "The Silmarillion", "Watership Down", "Chronicles of Narnia", "Dune", "1"),
        ("Who wrote 'The Catcher in the Rye'?", "J.D. Salinger", "F. Scott Fitzgerald", "George Orwell", "Mark Twain", "1"),
        ("What novel is written by Leo Tolstoy?", "Crime and Punishment", "War and Peace", "The Brothers Karamazov", "Anna Karenina", "2")
    ]

music_questions = [
        ("Who is known as the 'King of Pop'?", "Elvis Presley", "Michael Jackson", "Prince", "James Brown", "2"),
        ("What band was Freddie Mercury a part of?", "The Beatles", "Queen", "Led Zeppelin", "Pink Floyd", "2"),
        ("Which musician is famous for the hit 'Like a Rolling Stone'?", "Bob Dylan", "Bruce Springsteen", "Neil Young", "Tom Petty", "1"),
        ("What is Madonna's full birth name?", "Madonna Louise Ciccone", "Madonna Francesca Ciccone", "Madonna Veronica Ciccone", "Madonna Antonia Ciccone", "1"),
        ("Which artist released 'Thriller', the best-selling album of all time?", "Michael Jackson", "Prince", "David Bowie", "Elton John", "1"),
        ("Who composed the Four Seasons?", "Wolfgang Amadeus Mozart", "Antonio Vivaldi", "Johann Sebastian Bach", "Ludwig van Beethoven", "1"),
        ("Which singer is known for the song 'Respect'?", "Aretha Franklin", "Whitney Houston", "Diana Ross", "Tina Turner", "1"),
        ("Which artist is known for their alter ego Ziggy Stardust?", "Elton John", "Freddie Mercury", "David Bowie", "Mick Jagger", "3"),
        ("Who wrote the iconic song 'Imagine'?", "Paul McCartney", "John Lennon", "Bob Dylan", "George Harrison", "2"),
        ("Which band is known for the song 'Hotel California'?", "The Eagles", "The Beatles", "Led Zeppelin", "Fleetwood Mac", "1")
    ]

cinema_questions = [
        ("Which film won the Best Picture Oscar in 1994?", "Forrest Gump", "Pulp Fiction", "The Shawshank Redemption", "Jurassic Park", "1"),
        ("Who directed the epic sci-fi movie 'Avatar'?", "Steven Spielberg", "George Lucas", "James Cameron", "Ridley Scott", "3"),
        ("What is the name of the fictional British spy in the film series created by Ian Fleming?", "Jason Bourne", "Jack Ryan", "James Bond", "Ethan Hunt", "3"),
        ("Which actor played the Joker in the 2008 film 'The Dark Knight'?", "Jack Nicholson", "Heath Ledger", "Jared Leto", "Joaquin Phoenix", "2"),
        ("In which film did the character 'Forrest Gump' appear?", "Big", "Cast Away", "The Green Mile", "Forrest Gump", "4"),
        ("What year was the movie 'Titanic' released?", "1995", "1997", "2000", "1992", "2"),
        ("Who directed the horror film 'Psycho'?", "Alfred Hitchcock", "Stanley Kubrick", "Steven Spielberg", "Francis Ford Coppola", "1"),
        ("Which movie features a famous dance scene with John Travolta and Uma Thurman?", "Saturday Night Fever", "Grease", "Pulp Fiction", "Face/Off", "3"),
        ("What is the highest-grossing film of all time (not adjusted for inflation)?", "Avatar", "Titanic", "Star Wars: The Force Awakens", "Avengers: Endgame", "1"),
        ("Which actress stars as the lead character in the 'Lara Croft: Tomb Raider' films originally?", "Angelina Jolie", "Kate Winslet", "Scarlett Johansson", "Jennifer Lawrence", "1")
    ]


def quiz_menu():
    print("1: Science and Nature ")
    print("2: Famous Books and Authors ")
    print("3: Music and Musicians ")
    print("4: Cinema and Film ")
    choice = input("\nChoose a category to get started: " )
    return choice


def print_q(question_list, count, score):
    print("\n" + question_list[count][0]);
    print("1: " + question_list[count][1])
    print("2: " + question_list[count][2])
    print("3: " + question_list[count][3])
    print("4: " + question_list[count][4])

    answer_choice = input("Choose the number that you think is the correct answer: ")
    correct_answer = question_list[count][5]
    if(answer_choice == correct_answer):
        score += 10
        print("============================================")
        print("Yay! you got it right! Your score is now: " + str(score))
        print("\nNext Question: ")
    else:
        print("============================================")
        print("Oh no! :( you got the answer incorrect, lets try again with a different question. \nYour score is: " + str(score))

    count += 1
    return count, score


def quiz_game(choice):
    score = 0
    question_count = 0
    if(choice == "1"):
        print("You chose Science and Nature! Let's get started with the first question!")
        while(question_count < len(science_questions)):
            question_count, score = print_q(science_questions, question_count, score)
        print("You finished all questions in this category! Final score: " + str(score))
    elif(choice == "2"):
        print("You chose Famous Books and Authors! Let's get started with the first question!")
        while(question_count < len(books_authors_questions)):
            question_count, score = print_q(books_authors_questions, question_count, score)
        print("You finished all questions in this category! Final score: " + str(score))
    elif(choice == "3"):
        print("You chose Music and Musicians! Let's get started with the first question!")
        while(question_count < len(music_questions)):
            question_count, score = print_q(music_questions, question_count, score)
        print("You finished all questions in this category! Final score: " + str(score))
    elif(choice == "4"):
        print("You chose Cinema and Film! Let's get started with the first question!")
        while(question_count < len(cinema_questions)):
            question_count, score = print_q(cinema_questions, question_count, score)
        print("You finished all questions in this category! Final score: " + str(score))
    else:
        print("Please choose a number 1-4!")


def fact_frenzy():
    print("Welcome to Fact Frenzy! \n")
    choice = quiz_menu()
    quiz_game(choice)


if __name__ == "__main__":
    fact_frenzy()

