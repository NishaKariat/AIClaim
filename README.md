# AI Claim Drafting Assistant

This is a Streamlit app that helps patent attorneys generate a first draft of patent claims based on an invention disclosure.

## Features

- Accepts invention disclosure
- Generates 1 independent and 3 dependent claims
- Categorizes invention type
- Lets attorneys review/edit and download the draft

## Setup Instructions (Local)

1. Install dependencies:
    ```
    pip install streamlit openai
    ```

2. Create a file `.streamlit/secrets.toml`:
    ```
    OPENAI_API_KEY = "your_openai_api_key_here"
    ```

3. Run the app:
    ```
    streamlit run claim_drafting_app.py
    ```

## Deployment to Streamlit Cloud

1. Push this repository to GitHub.
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and connect your GitHub.
3. Deploy the app and set your API key in the Secrets manager:
    ```
    OPENAI_API_KEY = "your_openai_api_key_here"
    ```

## Notes

- This is an attorney-in-the-loop tool. All AI outputs must be reviewed by a licensed professional before filing.
