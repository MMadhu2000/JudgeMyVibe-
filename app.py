import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- CONFIGURATION ---
# Replace with your actual key from Step 1
API_KEY = "AIzaSyAnYUtuuzWiKeczVndOwVwMwyooWGRkZ80"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

# --- THE APP UI ---
st.set_page_config(page_title="JudgeMyVibe", page_icon="🔥")

st.title("🔥 Roast My... Everything")
st.write("Upload a photo. Our AI will judge it. Harshly.")

# Dropdown to choose the "Personality"
personality = st.selectbox(
    "Choose your Judge:",
    ["Gordon Ramsay (Savage)", "Gen Z (Slang heavy)", "Supportive Grandma (Too nice)", "Silicon Valley Tech Bro"]
)

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button('Judge Me!'):
        with st.spinner('Analyzing your bad choices...'):
            # Create the prompt based on personality
            if personality == "Gordon Ramsay (Savage)":
                prompt = "Look at this image. Roast it aggressively and brutally like Gordon Ramsay. Point out every flaw. Be funny but mean."
            elif personality == "Gen Z (Slang heavy)":
                prompt = "Look at this image. Roast it using Gen Z slang (no cap, cringe, cheugy, etc). Be effortlessly cool and judgmental."
            elif personality == "Supportive Grandma (Too nice)":
                prompt = "Look at this image. Find the positives even if it's terrible. Be overly sweet and supportive like a grandma."
            else:
                prompt = "Look at this image. Critique it like an arrogant Silicon Valley Tech Bro who thinks they know everything about optimization and aesthetic."

            # The Magic AI Call
            try:
                response = model.generate_content([prompt, image])
                st.success("The Verdict is in:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")