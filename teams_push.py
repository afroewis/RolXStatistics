import logging
import requests
import json
import os

def __get_teams_hook():
    if 'TEAMS_HOOK' in os.environ:
        return os.environ['TEAMS_HOOK']
    else:
        raise ValueError('TEAMS_HOOK nicht in Umgebungsvariablen gefunden')

def send_teams_message(title, message):
    teams_hook = __get_teams_hook()
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        '@context': 'https://schema.org/extensions',
        '@type': 'MessageCard',
        'title': title,
        'text': message
    }
    response = requests.post(teams_hook, headers=headers, data=json.dumps(data))
    if response.status_code != 200:
        raise ValueError(
            'Anfrage an Teams gesendet, aber fehlgeschlagen: Rückgabecode={}, Antwort={}'.format(
            response.status_code, response.text
            )
        )
    logging.info("Message sent to Teams")