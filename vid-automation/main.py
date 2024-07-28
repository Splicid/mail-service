import json
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main():
    authenticator = IAMAuthenticator('')
    text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )

    text_to_speech.set_service_url('')

    voices = text_to_speech.list_voices().get_result()
    print(json.dumps(voices, indent=2))




if __name__ == "__main__":
    main()
