import time, pprint, pyperclip

start_time = time.time()
last_time = start_time
laps = 0
wynik = []
try:
    while True:
        input("")
        lap_time = round(time.time() - last_time,2)
        total_time = round(time.time() - start_time,2)
        print(f"Okrążenie #{laps}: {str(round(total_time,2)).rjust(2)}",f"( {round(lap_time,2)})".rjust(2))
        wynik.append(f"Okrążenie #{laps}: {str(round(total_time,2)).rjust(2)}"+f"( {round(lap_time,2)})".rjust(2))
        laps = laps + 1 
        last_time = time.time()
except KeyboardInterrupt:
    print("\nKoniec programu.")

pyperclip.copy(pprint.pformat(wynik))