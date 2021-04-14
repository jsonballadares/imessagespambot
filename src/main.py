import os
import pyautogui
from dotenv import load_dotenv, find_dotenv
from time import sleep
from twilio.rest import Client
from lyricsgenius import Genius


# get words from lyrics text
def get_lyrics(filename):
    with open(filename) as file:
        content = file.readlines()
        content = [x.strip() for x in content]
        return content


# loop throgh words
def send_messages(phone_num_to, phone_num_from, messages, client):
    for message in messages:
        send_message(phone_num_to, phone_num_from, message, client)
        sleep(3)


# function to send message
def send_message(phone_num_to, phone_num_from, message, client):
    client.messages.create(
        body=message,
        from_=phone_num_from,
        to=phone_num_to
    )


# load env file
load_dotenv(find_dotenv())
# init twilio things
twilio_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
# init lyrics genius things
lyrics_genius_client_id = os.getenv('GENIUS_CLIENT_ID')
genius = Genius(lyrics_genius_client_id)
# get artist info
#song = genius.search_song("Look At Me", "xxxtentacion")
#song = genius.search_song("WAP", "cardi b")
song = genius.search_song("fuck love", "xxxtentacion")
lyrics = song.lyrics.splitlines()

pyautogui.PAUSE = 1
sleep(2)
for line in lyrics:
    pyautogui.write(line + "\n",)
    #pyautogui.press("enter",interval=0.025, _pause=0.25)


#phone_num_to = "+17867201701"
#phone_num_from = "+17866996629"
#lyrics_file = "/Users/jasonballadares/repos/imessagespambot/data/lookatme.txt"
#lyrics = get_lyrics(lyrics_file)


# send_messages(phone_num_to, phone_num_from, lyrics,
#              Client(account_sid, auth_token))
