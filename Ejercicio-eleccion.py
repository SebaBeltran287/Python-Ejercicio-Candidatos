import os
os.system("cls")
import time 

jose=0
maria=0
miguel=0
salir=False

while salir==False:
    os.system("cls")
    print("1. Jose ")
    print("2. Maria ")
    print("3. Miguel ")
    print("4. Salir ")
    opcion = int(input("seleccione una opción de candidato: "))
    if opcion==1:
        jose+=1
    elif opcion==2:
        maria+=1
    elif opcion==3:
        miguel+=1
    elif opcion==4:
        salir=True
    else:
        print("no seleccionó ninguna opción. ")
        time.sleep(1)
        
total = jose+maria+miguel
porc_jose = round(jose/total*100)
porc_maria = round(maria/total*100)
porc_miguel = round(miguel/total*100)

print(f" Jose: {jose} votos, {porc_jose}%")
print(f" Maria: {maria} votos, {porc_maria}%")
print(f" Miguel: {miguel} votos, {porc_miguel}%")

if maria > jose and maria > miguel:
    print(" La ganadora es Maria ")
elif jose > maria and jose > miguel:
    print(" El ganador es Jose ")
else:
    print(" El ganador es Miguel ")
