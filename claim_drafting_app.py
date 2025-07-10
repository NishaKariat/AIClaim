import streamlit as st
import openai

# === CONFIG ===
openai.api_key = st.secrets["OPENAI_API_KEY"]  # Set in Streamlit Cloud settings

# === APP TITLE ===
st.title("🧠 AI Claim Drafting Assistant")
st.markdown("Assist attorneys with initial claim drafting. All output requires human legal review.")

# === USER INPUT ===
invention_type = st.selectbox("Type of invention", ["method", "system", "composition"])
disclosure_text = st.text_area("Paste Invention Disclosure", height=300)

# === PROMPT FUNCTION ===
def generate_claims(disclosure, invention_type):
    prompt = f"""
You are a US patent attorney drafting claims. Based on the invention disclosure below, generate one broad independent claim and three dependent claims.

Ensure:
- Clarity and structure appropriate for patent claims
- Support under 35 U.S.C. §112
- Proper use of antecedents and dependencies

Invention type: {invention_type}

Disclosure:
"""
{disclosure}
"""

Output format:
1. Independent claim:
2. Dependent claim 1:
3. Dependent claim 2:
4. Dependent claim 3:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0.4,
        messages=[
            {"role": "system", "content": "You are a highly skilled US patent attorney."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

# === GENERATE BUTTON ===
if st.button("Generate Claims"):
    if disclosure_text:
        with st.spinner("Drafting claims..."):
            try:
                output = generate_claims(disclosure_text, invention_type)
                st.subheader("💡 AI-Generated Claims")
                st.text_area("Review and edit below:", value=output, height=400)
                st.download_button("Download as .txt", output, file_name="ai_claim_draft.txt")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please paste an invention disclosure.")
