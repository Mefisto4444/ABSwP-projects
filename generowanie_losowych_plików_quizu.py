import random as r
stanyFUll = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'Kalifornia': 'Sacramento', 'Kolorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Floryda': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaje': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Luizjana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'Nowy Meksyk': 'Santa Fe', 'Nowy Jork': 'Albany',
   'Północna Karolina': 'Raleigh', 'Północna Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'Południowa Karolina': 'Columbia', 'Południowa Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Teksas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Wirginia': 'Richmond', 'Washington': 'Olympia', 'Wirginia Zachodnia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}



for plik in range(35):#......................................35 plików quizu
    quizFile = open(f"D:\\jakub\\reddit\\quizFile{plik+1}.txt",'w')
    nagłówek = "Imię i nazwisko:\nKlasa:\nData:\n\n\n" + 20 * " " + f"Quiz stolic stanów  Quiz {plik + 1}\n\n"
    stany = list(stanyFUll.keys())
    r.shuffle(stany)#.............................................Losowa kolejność pytań
    quizFile.write(f"{nagłówek}")
    for stan in range(50):#.........................50 pytań, iteracja przez 50 stanów
        quizFile.write(f"Stolica stanu {stany[stan]} to:\n")
        prawidłowa = stanyFUll[stany[stan]]
        nieprawidłowa = list(stanyFUll.values())
        del nieprawidłowa[nieprawidłowa.index(prawidłowa)]
        nieprawidłowa = r.sample(nieprawidłowa,3)
        opcje = [prawidłowa] + nieprawidłowa
        r.shuffle(opcje)
        for i in range(4):
            quizFile.write("ABCD"[i] + f" {opcje[i]}\n")
    quizFile.close()

