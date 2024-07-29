import json, os
from os.path import join, dirname
from dotenv import load_dotenv

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



def main():
    print(os.environ.get("TEXT_TO_SPEECH_APIKEY"))
    # driver = webdriver.Firefox()
    # driver.get("https://www.reddit.com/r/ProRevenge/")
    # driver.find_element(By.CLASS_NAME, "absolute inset-0").click()

    # # Action mouse movement
    # Action = webdriver.ActionChains

    # Action(driver).move_to_element()

def audio():
    authenticator = IAMAuthenticator(os.environ.get("TEXT_TO_SPEECH_APIKEY"), disable_ssl_verification=True)
    text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )

    text_to_speech.set_service_url(os.environ.get("TEXT_TO_SPEECH_URL"))
    text_to_speech.set_disable_ssl_verification(True)
    voices = text_to_speech.list_voices().get_result()

    text = "Kenny sucks at rainbow six siege"

    response = text_to_speech.synthesize(
        text=text,
        voice='en-GB_JamesV3Voice',
        accept='audio/mp3'
    ).get_result()

    with open('hello_world.mp3', 'wb') as audio_file:
        audio_file.write(response.content)

    print(json.dumps(voices, indent=2))


if __name__ == "__main__":
    dotenv_path = '../ibm-credentials.env'
    load_dotenv(dotenv_path)
    main()