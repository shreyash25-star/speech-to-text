import streamlit as st
import pyaudio
import speech_recognition as sr

# Function to continuously listen to microphone and recognize speech
def recognize_speech():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        while True:
            st.write("Listening...")
            audio = r.listen(source)

            st.write("Recognizing...")
            try:
                text = r.recognize_google(audio)
                st.write(f"You said: {text}")
            except sr.UnknownValueError:
                st.write("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                st.write(f"Could not request results from Google Speech Recognition service; {e}")

def main():
    st.title("Real-time Voice to Text App")

    st.subheader("Click the button below to start speaking")

    if st.button("Start Speaking"):
        recognize_speech()

if __name__ == "__main__":
    main()
