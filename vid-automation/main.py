import json
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main():
    authenticator = IAMAuthenticator('oxg622jI_ig3mTAyOBOURf9GP5HuPGSRM2mDTiYlhqUf')
    text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )

    text_to_speech.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/4e447fe0-e1f1-4767-9b90-cde953bc71e7')

    voices = text_to_speech.list_voices().get_result()
    print(json.dumps(voices, indent=2))




if __name__ == "__main__":
    main()
