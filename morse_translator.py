import requests

def translate_to_morse(sent):
    base_url = "https://api.funtranslations.com/translate/morse.json"
    params_dict = {}
    params_dict['text'] = sent
    trans_dict_in_json = requests.get(base_url, params = params_dict)
    trans_dict_in_python = trans_dict_in_json.json()
    return trans_dict_in_python['contents']['translated']


text_in_english = input('Enter text in English: ')
encryption_in_morse = translate_to_morse(text_in_english)


print("The encryption of the entered text in Morse is : ")
print(encryption_in_morse)

