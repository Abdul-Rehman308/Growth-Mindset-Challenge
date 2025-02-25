#streamlit
import streamlit as st 

st.set_page_config(page_title="Growth Mindset Project", page_icon="★")
st.title("Growth Mindset Challenge: Web App with Streamlit ")

st.header("🚀 Wellcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app help you build a growth mindset with reflection, challenges, and achievements! 🌟")


#qoute section
st.header("💡 Today's Growth Minset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to contnue that counts.-winstone Churchill")

st.header("⌛ what's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")


#condition
if user_input:
    st.success(f"💪You're facing:{user_input}. keep pushing forwards your goal!🚀")
else:
    st.warning("Tell us about your challenge to get staeted!")

    
#reflexing
st.header("Reflect on your Learning")
reflection = st.text_area("Write your reflection")

if reflection:
    st.success(f"🌟Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")

    
#acheivement
st.header("🏆 Celebrate Your Wins!")
acheivment = st.text_input("Share something you're recently accomplished:")

if acheivment:
    st.success(f"💫 Amazing! You achieved: {acheivment}")
else:
    st.info("Big or small , every achivement counts! Share one now 😍 ")


#footer
st.write("- - -")
st.write("🚀 Keep believing in yourseif. Growth is a journey, not a destination!⭐")
st.write("**⛔ created by Syed Abdul Rehman**")