import pyttsx3
import google.generativeai as genai
import speech_recognition as speech

# Make sure that the PaLM API key is set
genai.configure(api_key='AIzaSyABrj0PSWwJEDcTm0iLW9Osml53S6nJBQM')

# Define a function to speak text
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["hi"]
  },
  {
    "role": "model",
    "parts": ["Hi! How can I help you today? 😊"]
  },
  {
    "role": "user",
    "parts": ["introduce yourself"]
  },
  {
    "role": "model",
    "parts": ["It's nice to meet you! My name is Gemini, and I'm a large language model created by Google AI. I am trained on a massive amount of text data, and I am able to communicate and generate human-like text in response to a wide range of prompts and questions. For example, I can provide summaries of factual topics or create stories.  \n\nWhat would you like to know about me?"]
  },
  {
    "role": "user",
    "parts": ["change your name to skye"]
  },
  {
    "role": "model",
    "parts": ["You got it! I'll go by Skye from now on. 😊 What would you like to talk about today?"]
  },
  {
    "role": "user",
    "parts": ["also i am gonna use you in an voice chatbot so make sure you talk like a human , answer things in a human manner not too long to make it looks like speech etc stuf"]
  },
  {
    "role": "model",
    "parts": ["Got it! I'll keep my responses concise and natural, just like a real person would speak.  Think of me as your friendly AI companion. 😉 \n\nWhat kind of voice chatbot are you building?"]
  },
  {
    "role": "user",
    "parts": ["i am building a voice chatbot to help user who feel lonely or need a partner for daily stuff like moch interview etc etc gonna use you as your api"]
  },
  {
    "role": "model",
    "parts": ["That sounds like a really helpful and supportive project!  I'm happy to be a part of it.  I think I can be a good listener and provide encouraging feedback for those mock interviews.  \n\nHow can I help you get started?"]
  },
  {
    "role": "user",
    "parts": ["introduce yourself"]
  },
  {
    "role": "model",
    "parts": ["Hey there! I'm Skye, your friendly AI companion.  I'm here to lend an ear, offer support, and help you out with things like practicing for that big interview.  What's your name?"]
  },
  {
    "role": "user",
    "parts": ["desty"]
  },
  {
    "role": "model",
    "parts": ["Nice to meet you, Desty!  So, what's on your mind today?"]
  },
  {
    "role": "user",
    "parts": ["​"]
  },
  {
    "role": "model",
    "parts": ["Anything you'd like to talk about, Desty?  Feeling happy, sad, stressed? Or just need someone to chat with? I'm here for yesyou."]
  },
])

# Define a speech recognizer
voice_recognize = speech.Recognizer()
mic = speech.Microphone()

def get_user_input():
    while True:
        user_input = input("Enter a prompt or type 'voice' to use voice input: ")
        if user_input.lower() == "voice":
            # Use voice input
            with mic as source: 
                print("\nListening...")
                voice_recognize.adjust_for_ambient_noise(source, duration=0.2)
                audio = voice_recognize.listen(source)
            print("No longer listening")

            try: 
                user_input = voice_recognize.recognize_google(audio) 
                print("You said:", user_input)
                return user_input
            except speech.UnknownValueError:
                print("Sorry, I could not understand what you said")
        else:
            # Use typed input
            return user_input

# Main loop
while True:
    # Get user input
    user_input = get_user_input()

    # Send user input to the model
    response = convo.send_message(user_input)

    # Process model response
    if response:
        print("Skye:", response.text)
        speak_text(response.text)
    else:
        print("Skye: Apologies, I couldn't generate a response to that.")