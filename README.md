# RolXStatistics

Dieses Programm fragt die Live RolX Datenbank ab, um Statistiken über 
die Verrechenbarkeit der Mitarbeitenden zu berechnen und auf einen Teams-
Kanal zu Pushen.

## Installation

1. Stelle sicher, dass Python auf deinem Computer installiert ist.
2. Lade das Programm herunter und speichere es in einem Verzeichnis deiner Wahl.
3. Öffne die Kommandozeile oder das Terminal.
4. Navigiere zum Verzeichnis, in dem du das Programm gespeichert hast.
5. Installiere alle Abhängigkeiten und das venv mit dem Befehl `install.bat`
7. Setze das Passwort für die RolX-Datenbank: `set ROLX_PASSWORD=....`

## Konfiguration

Die Datenbank-Verbindung ist in `rolx_connector.py` definiert. Standardmässig ist 
```
host="rolx-database.mariadb.database.azure.com",
user="rolx_prod_readonly@rolx-database",
password=password,
database="rolx_production"
```

Falls die Resultate in einen Teams-Kanal gepushed werden sollen, kann im
Teams für den Kanal ein incoming Webhook konfiguriert werden (siehe https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=newteams%2Cdotnet)

Die Adresse des Webhooks muss danach im `teams_push.py` eingetragen werden:
```
TEAMS_HOOK = "https://mfeng.webhook.office.com/webhookb2/...."`
```

## Verwendung

Test auf der Konsole, ohne Teams-Pushnachricht:
```
python main.py
```

Ausführen mit Teams-Push:

```
python main.py --sendteams
```






## Lizenz

Copyright (c) 2024 Reto Bättig (reto@baettig.org)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
