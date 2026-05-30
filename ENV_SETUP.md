# Environment Setup

This project requires certain environment variables to be set up in order to function correctly.

## Setting up `.env`

1. Navigate to the `backend` directory.
2. Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```
3. Open the newly created `.env` file and fill in the required keys.

## Required Keys

### GEMINI_API_KEY
This is the API key for Google's Gemini model.

**How to get it:**
1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Sign in with your Google account.
3. Click on "Get API key" in the left sidebar.
4. Click on "Create API key in new project" or select an existing project.
5. Copy the generated key and paste it into your `backend/.env` file as `GEMINI_API_KEY=your_copied_key`.
