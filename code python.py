import RPi.GPIO as GPIO #importe la bibliotheque GPIO 
import time #importe la bibliotheque temps
GPIO.setmode(GPIO.BCM) #configuration generale de la numérotation électronique de la puce BCM quand a trouve dans la carte electronique on peut remplacer par #board
PIR_SENSOR_PIN=16 #defenir la numerisation du pin
GPIO.setup(PIR_SENSOR_PIN, GPIO.IN) #configuration de la pin du capteur 
print("lancement du capteur de presence IR(ctrl-c)")
time.sleep(1) #permet d'introduire un délai dans l'exécution de votre programme
try: 
    while True:      #verifier dans une boucle l'état d'entree du pir (capteur) 
        if GPIO.input(PIR_SENSOR_PIN):
            print("mouvement detecte ") 
        time.sleep(1)
except keyboardInterrupt: # attraper les interruptions du clavier.
    print("cleaning up") 
    GPIO.cleanup() # nettoyer tous les ports que vous avez utilisés.
