
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

def test_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables.")
        return
    
    # Masked Key verification
    masked_key = f"{api_key[:4]}...{api_key[-4:]}" if len(api_key) > 8 else "****"
    print(f"DEBUG: Loaded API Key: {masked_key}")

    client = genai.Client(api_key=api_key)
    model_name = "gemini-2.0-flash" 

    print(f"Testing Gemini API with model: {model_name}")

    try:
        response = client.models.generate_content(
            model=model_name,
            contents="Hello, are you working?",
            config=types.GenerateContentConfig(response_mime_type="text/plain")
        )
        print("Success! Response:")
        print(response.text)
    except Exception as e:
        print(f"Error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_gemini()
