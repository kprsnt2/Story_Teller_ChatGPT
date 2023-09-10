import streamlit as st
import openai
from gtts import gTTS
import os

# Set your OpenAI API key here
openai.api_key = "Your_API_Key"

def generate_story(keyword):
    # Use OpenAI API to generate the story based on the keyword
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"I want you to Tell me a story about {keyword}, I am 5 years old and I want creative, fun and message-oriented interesting stories and tell me the moral of the story at the end",
        max_tokens=150
    )
    story = response.choices[0].text.strip()
    return story

def text_to_audio(text):
    # Convert text to speech using gTTS
    speech = gTTS(text, lang='en', slow=False)  # Adjust language and other parameters as needed
    
    # Save the speech to a temporary audio file
    audio_path = "temp_audio.mp3"
    speech.save(audio_path)
    
    # Return the path to the saved audio file
    return audio_path

def main():
    st.title("Storyteller for Kids")
    
    keyword = st.text_input("Enter a keyword for the story:")
    
    if st.button("Generate Story"):
        story = generate_story(keyword)
        
        # Convert the story to audio
        audio_path = text_to_audio(story)
        
        # Provide an option for iOS users to download the audio
        st.write("You can listen to or download the story audio:")
        st.audio(audio_path, format="audio/mp3")
        
if __name__ == "__main__":
    main()
