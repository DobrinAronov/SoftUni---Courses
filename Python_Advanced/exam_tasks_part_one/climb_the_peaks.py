from collections import deque

portions_stack = [int(num) for num in input().split(', ')]
stamina_dqu = deque(int(num) for num in input().split(', '))

PEAKS_DIFFICULT = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70
}

conquered_peaks = []

for peak_name, difficult in PEAKS_DIFFICULT.items():
    while portions_stack and stamina_dqu:
        portion = portions_stack.pop()
        stamina = stamina_dqu.popleft()
        result = portion + stamina

        if result < PEAKS_DIFFICULT["Polezhan"]:
            continue
        if result >= difficult:
            conquered_peaks.append(peak_name)
            break

if len(conquered_peaks) == len(PEAKS_DIFFICULT):
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print(f"Conquered peaks:")
    [print(peak) for peak in conquered_peaks]
