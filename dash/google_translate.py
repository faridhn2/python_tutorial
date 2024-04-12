from googletrans import Translator
translator = Translator()
result = translator.translate('Welcome to Flask’s documentation. Get started with Installation and then get an overview with the Quickstart. ' ,dest='fa', src='en')
print(result.text)