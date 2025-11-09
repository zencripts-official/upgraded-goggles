# upgraded-goggles

A Google Gemini 2.0 Flash AI-powered web application with interactive frontend and Python backend integration.

## Overview

This project demonstrates integration with Google's Gemini 2.0 Flash AI model, featuring:
- **Frontend**: Interactive web interface (HTML/CSS/JavaScript) deployed on Netlify/Vercel
- **Backend**: Python API configuration for Gemini AI integration
- **Deployment**: Ready-to-deploy configuration for web hosting

## Project Structure

```
upgraded-goggles/
├── index.html/         # Frontend web application
├── gemini_config.py    # Python Gemini API configuration
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── netlify.toml        # Netlify deployment config
├── vercel.json         # Vercel deployment config
├── .gitignore          # Git ignore rules
└── README-FRONTEND.md  # Frontend-specific documentation
```

## Prerequisites

- **Frontend**: Modern web browser
- **Backend**: 
  - Python 3.9 or higher
  - Google Cloud account with Gemini API access
  - API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Setup Instructions

### Frontend Setup

1. Clone the repository:
```bash
git clone https://github.com/zencripts-official/upgraded-goggles.git
cd upgraded-goggles
```

2. Open `index.html` in a web browser or deploy to Netlify/Vercel:
```bash
# For local development
open index.html/index.html

# Or deploy to Netlify (automatic with netlify.toml)
# Or deploy to Vercel (automatic with vercel.json)
```

### Backend Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

4. Use the Gemini configuration:
```python
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.0-flash')

response = model.generate_content('Your prompt here')
print(response.text)
```

## Features

- ✨ Interactive web interface for AI interactions
- 🚀 Google Gemini 2.0 Flash multimodal AI capabilities
- 💡 Advanced reasoning and problem-solving
- 🔧 Easy deployment to Netlify or Vercel
- 📦 Pre-configured Python backend integration
- 🎨 Responsive frontend design

## Deployment

### Netlify
- Push to GitHub and connect repository to Netlify
- Configuration is handled by `netlify.toml`

### Vercel
- Push to GitHub and connect repository to Vercel
- Configuration is handled by `vercel.json`

## Resources

- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [Gemini 2.0 Flash Overview](https://deepmind.google/technologies/gemini/)
- [Python SDK Reference](https://ai.google.dev/api/python)
- [Frontend Documentation](./README-FRONTEND.md)

## Contributing

Contributions are welcome! Please submit a Pull Request with your improvements.

## License

MIT License - Open source and free to use.

## Support

For issues or questions, please open an issue in this repository.
