mport streamlit as st
from openai import OpenAI
import os

# === CONFIG ===
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# === APP TITLE ===
st.set_page_config(page_title="AI Claim Drafting Assistant", page_icon="🧠")
st.title("🧠 AI Claim Drafting Assistant")

# === SIDEBAR ===
st.sidebar.header("🛠️ Drafting Parameters")
claim_type = st.sidebar.selectbox("Select claim type", ["Utility", "Design", "Provisional"])
field = st.sidebar.text_input("Field of invention", placeholder="e.g., wearable tech, robotics, etc.")

# === MAIN INPUT ===
prompt = st.text_area("Enter a brief description of the invention:", height=200, placeholder="Describe the invention to draft a claim...")

# === GENERATE BUTTON ===
if st.button("Generate Patent Claim"):
    if not prompt:
        st.warning("Please enter a description of the invention.")
    else:
        with st.spinner("Drafting claim using GPT-4..."):
            try:
                system_prompt = f"You are an expert patent attorney. Write a well-structured {claim_type.lower()} patent claim in the field of {field or 'technology'}."
                user_prompt = f"Here is the invention description:\n\n{prompt}"

                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.5
                )

                output = response.choices[0].message.content
                st.success("Claim Drafted Successfully:")
                st.text_area("📄 Drafted Claim", output, height=300)
            except Exception as e:
                st.error(f"Error generating claim: {e}")
