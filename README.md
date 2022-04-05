# LegoScript

#### Eine einfache Programmiersprache für EV3

## Befehle

### setze

 #### setzt eine Variable auf einen bestimmten wert
 #### beispiele:
 `setze x auf 3`\
 `setze variable1 auf 3 + 4`\
 `setze var auf x + 3`
 
 ----------------------------------------------------------------------
 
### sage

 #### Gibt etwas in der Konsole aus. Funktioniert nur am PC, nicht am EV3 Stein. Es können auch die Werte von Variablen ausgegeben werden.
 #### beispiele:
 `sage hallo welt`\
 `sage variable` 
 
----------------------------------------------------------------------

### falls 

 #### Führt eine Kette von Befehlen aus, wenn gewisse Vorrausetzungen erfüllt sind. Diese Befehlskette kommt in die Zeilen nach dem "falls" befehl und wird mit "ende" beendet.
 #### Beispiele
 ```setze x auf 2
falls x = 2
sage x entspricht 2
ende´´´
 ```setze x auf 5
falls x = 2 + 3
sage x entspricht 2 + 3
ende´´´
 