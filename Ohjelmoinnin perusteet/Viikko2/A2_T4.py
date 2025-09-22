print("Program starting.")
print("Estimate how many minutes you spent on prograamming...\n")
T1 = int(input("A1_T1: "))
T2 = int(input("A1_T2: "))
T3 = int(input("A1_T3: "))
T4 = int(input("A1_T4: "))
T5 = int(input("A1_T5: "))
T6 = int(input("A1_T6: "))
T7 = int(input("A1_T7: "))
Total = T1 + T2 + T3 + T4 + T5 + T6 + T7
Average = Total / 7
print(f"\nIn total you spent {Total} minutes on programming.")
print(f"Average time spent per exercise is {round(Average,2)} min and same rounded to the nearest integer {round(Average)} min.\n")
print("Program ending.")