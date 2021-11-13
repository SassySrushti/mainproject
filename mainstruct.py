import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)


def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined


def generateBody():
    audio = AudioSegment.from_mp3('train.mp3')

    # 1-Generate kripya dhyan dijiye
    start = 16300
    finish = 19200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2-is from city

    # 3-Generate se chalkar
    start = 21400
    finish = 22200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 4-is via-city

    # 5-Generate ke raaste
    start = 19900
    finish = 20660
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6-is to-city

    # 7-Generate ko jaani vali
    start = 23100
    finish = 24000
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8- is train no and name

    # 9-Generate  platform
    start = 28900
    finish = 29920
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10-is platform no

    # 11-Generate par aa chuki hai
    start = 30400
    finish = 32270
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")


def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2-Generate from-city
        textToSpeech(item['from'], '2_hindi.mp3')
        # 4-Generate via-city
        textToSpeech(item['via'], '4_hindi.mp3')
        # 6-Generate to-city
        textToSpeech(item['to'], '6_hindi.mp3')
        # 8-Generate train no and name
        textToSpeech(item['train_no'] + " "+item['train_name'], '8_hindi.mp3')
        # 10=Generate platform number
        textToSpeech(item['platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1, 12)]

        announcement = mergeAudios(audios)
        announcement.export(
            f"hin_announce_{item['train_no']}_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Body...")
    generateBody()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")
