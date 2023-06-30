
import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import openai
import random



chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = ""
    chatStr += f"pious: {query}\n PiousChatBot: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

openai.api_key = "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"

def ai(prompt):
    openai.api_key ""
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)


# Usage example
prompt = "Your prompt text goes here..."
ai(prompt)

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry from Jarvis"
if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am pious chatbot")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"],["wikipedia", "https://www.wikipedia.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Open {site[0]})sir")
                webbrowser.open(site[1])
            if "open music" in query:
                musicPath = r"C:\Users\Windows\Desktop\summer-walk-152722.mp3"
                os.startfile(musicPath)
            elif "open spotify" in query:
                spotifyPath =r"C:\Users\Windows\AppData\Local\Microsoft\WindowsApps\spotify.exe"
                os.startfile(spotifyPath)
            elif "using intelligence" .lower() in query.lower():
                ai(prompt=query)
            elif "reset chat".lower() in query.lower():
                chatStr = ""

            else:
                print("Chatting...")
                chat(query)

