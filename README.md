# upgraded-goggles

Google Gemini 2.0 Flash AI project - Development setup and configuration

## Overview

This repository contains a project configured for development with Google Gemini 2.0 Flash, Google's advanced AI model for multimodal understanding and generation.

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Google Cloud account with Gemini API access
- API key for Google AI Studio or Vertex AI

## Installation

1. Clone the repository:
```bash
git clone https://github.com/zencripts-official/upgraded-goggles.git
cd upgraded-goggles
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install google-generativeai
pip install python-dotenv
```

## Configuration

1. Create a `.env` file in the root directory:
```bash
GEMINI_API_KEY=your_api_key_here
```

2. Set up your API key:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Generate an API key
   - Add it to your `.env` file

## Usage

```python
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Initialize Gemini 2.0 Flash model
model = genai.GenerativeModel('gemini-2.0-flash')

# Generate content
response = model.generate_content('Your prompt here')
print(response.text)
```

## Features

- ✨ Multimodal AI capabilities (text, images, audio, video)
- 🚀 Fast inference with Flash architecture
- 💡 Advanced reasoning and problem-solving
- 🔧 Easy-to-use Python SDK
- 📦 Pre-configured development environment

## Project Structure

```
upgraded-goggles/
├── .gitignore          # Python gitignore template
├── README.md           # This file
├── .env.example        # Example environment variables
└── src/                # Source code directory
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Resources

- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [Gemini 2.0 Flash Overview](https://deepmind.google/technologies/gemini/)
- [Python SDK Reference](https://ai.google.dev/api/python)

## Support

For issues, questions, or contributions, please open an issue in this repository.
