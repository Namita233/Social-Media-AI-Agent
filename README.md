AI SOCIAL MEDIA AGENT — README
Demo:
• Live App: https://social-media-ai-agent.streamlit.app/
• Demo Video: https://drive.google.com/file/d/1RBNtZ8SCdULpYQlC8PR-DGNTJlzFfnWp/preview

Overview:
The AI Social Media Agent is a Streamlit-based application that generates captions, hashtags, ideas,
and posting plans using OpenAI models.

Features:
• Login & register system
• Platform selection (Instagram, Facebook, YouTube)
• AI content generator (captions, hashtags, ideas, 8-day plan)
• Embedded tutorial video
• Clean UI styling

Limitations:
• Basic authentication (not secure)
• No database
• Only 3 platforms supported
• AI quality depends on model
• No scheduling features

Tech Stack:
• Streamlit (frontend)
• Python (backend)
• OpenAI API (gpt-4o-mini)
• HTML/CSS
• python-dotenv

Setup Instructions:
1. Clone repo:
git clone
cd project-folder
2. Install dependencies:
pip install -r requirements.txt
3. Add API key:
In .streamlit/secrets.toml:
OPENAI_API_KEY = "your_key"
4. Run app:
streamlit run app.py

Potential Improvements:
• Secure authentication (Firebase/JWT)
• Save user history and dashboard
• AI image/video generation
• Analytics for performance
• Auto-post scheduler
• Multi-language support
• Pre-made templates
