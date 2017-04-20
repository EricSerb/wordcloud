from os import path
import speech_recognition as sr
from wordcloud import WordCloud

"""
Get audio from mic
"""
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something")
    audio = r.listen(source, 10)

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    text = r.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

"""
Create wordcloud
"""
# d = path.dirname(__file__)
#
# Read the whole text.
# text = open(path.join(d, 'text.txt')).read()

# print(text)

# Generate a word cloud image
wordcloud = WordCloud().generate(text)
# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig("audio_wc.png")

# lower max_font_size
# wordcloud = WordCloud(max_font_size=40).generate(text)
# plt.figure()
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()

