#!pip install googletrans==3.1.0a0

from googletrans import Translator
from textblob import TextBlob

text = input("Enter your Bangla text: ")
translator = Translator()
my_translation = translator.translate(text, src='bn', dest='English')
print(my_translation.text)

txtV1 = TextBlob(my_translation.text)
if txtV1.sentiment.polarity < 0:
  textpol = "negative"
elif txtV1.sentiment.polarity == 0:
  textpol = "neutral"
else:
  textpol = "positive"
print(textpol)
