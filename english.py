import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)


def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined


def generateBody():
    audio = AudioSegment.from_mp3('train.mp3')

    # 1-May I have your attention please
    start = 0000
    finish = 3800
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_english.mp3", format="mp3")

    # 2-Train no and name

    # 3-From
    start = 8780
    finish = 9230
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_english.mp3", format="mp3")

    # 4-is from-city

    # 5-via
    start = 10300
    finish = 10750
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_english.mp3", format="mp3")

    # 6-is via-city

    # 7-to
    start = 11290
    finish = 11760
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_english.mp3", format="mp3")

    # 8- is to-city

    # 9-Has arrived at platform no.
    start = 12500
    finish = 14570
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_english.mp3", format="mp3")

    # 10-is platform no


def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2-Train no and name
        textToSpeech(item['train_no'] + " " +
                     item['train_name'], '2_english.mp3')
        # 4-is from-city
        textToSpeech(item['from'], '4_english.mp3')
        # 6-is via-city
        textToSpeech(item['via'], '6_english.mp3')
        # 8- is to-city
        textToSpeech(item['to'], '8_english.mp3')
        # 10-is platform no
        textToSpeech(item['platform'], '10_english.mp3')

        audios = [f"{i}_english.mp3" for i in range(1, 11)]

        announcement = mergeAudios(audios)
        announcement.export(
            f"eng_announce_{item['train_no']}_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Body...")
    generateBody()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")
