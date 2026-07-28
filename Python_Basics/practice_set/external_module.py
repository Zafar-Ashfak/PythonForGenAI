import pyttsx3

my_intro = "Hello, I am Md Ashfaq Alam. And I am learning Python for GenAI"

engine = pyttsx3.init()
engine.say(my_intro)
engine.runAndWait()
