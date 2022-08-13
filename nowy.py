import subprocess, time

ile  = 10
print(f"Za {ile} sekund włączy się alarm.")
time.sleep(ile)
subprocess.Popen(["start","alarm.wav"],shell=True)
