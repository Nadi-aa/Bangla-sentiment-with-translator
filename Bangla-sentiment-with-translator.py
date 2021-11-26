from textblob import TextBlob
from translate import Translator

text = input("Enter your Bangla text: ")

translator= Translator(from_lang="Bengali", to_lang="English")
translation_text = translator.translate(text)

print(translation_text)

txtV1 = TextBlob(translation_text)
print(txtV1.sentiment)
