# Mental Health Assistant

A voice-enabled mental health support application powered by AI that provides empathetic, evidence-based assistance through natural conversation.

![Mental Health Assistant](https://via.placeholder.com/800x400?text=Mental+Health+Assistant)

## 🧠 Overview

Mental Health Assistant is a Flask-based web application that combines OpenAI's GPT-3.5 API with speech recognition technology to provide accessible mental health support. Users can interact with the system through voice or text, receiving personalized responses based on their concerns, age, and needs.

The application features real-time crisis detection, emergency protocols, and delivers evidence-based mental health guidance in an accessible format.

## ✨ Features

- **Voice-Enabled Interface**: Speak directly to the assistant using your device's microphone
- **Text-to-Speech**: Listen to responses through high-quality speech synthesis
- **Personalized Support**: Customized responses based on user name and age
- **Crisis Detection**: Automatic identification of critical mental health concerns
- **Emergency Protocols**: Built-in safety measures for crisis situations
- **Modern UI**: Responsive design with glass-morphism and material design principles
- **Accessibility**: Multiple interaction methods for diverse user needs

## 🛠️ Technical Architecture

### Backend
- **Framework**: Flask 3.0.3 with Gunicorn WSGI server
- **AI Integration**: OpenAI GPT-3.5 Turbo with specialized mental health prompting
- **Configuration**: Python-dotenv for environment variable management
- **Deployment**: Production-ready with Gunicorn worker process management

### Frontend
- **Speech Processing**: WebkitSpeechRecognition API & SpeechSynthesis
- **UI Framework**: HTML5, CSS3, Vanilla JavaScript
- **Design System**: Custom CSS with variables, glass-morphism effects and responsive breakpoints
- **Async Operations**: Fetch API with visual feedback overlays

### Key Technical Features
- **Crisis Detection Algorithm**: Keyword analysis with emergency protocol triggers
- **Personalization Engine**: Name/age-based response customization
- **Voice Interface**: Bidirectional speech-text conversion for accessibility
- **Safety Protocols**: Timestamp logging and emergency contact system

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- OpenAI API key

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/mental-health-assistant.git
cd mental-health-assistant
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key
```
OPENAI_API_KEY=your_api_key_here
FLASK_APP_NAME="Mental Health Assistant"
FLASK_ENV=development
FLASK_PORT=5005
FLASK_APPLICATION_ROOT="/assistant"
FLASK_STATIC_URL_PATH="/assistant/static"
```

5. Run the application
```bash
python app.py
```

6. Open your browser and navigate to `http://localhost:5005/assistant/`

### Deployment

The application includes a Procfile for easy deployment to platforms like Heroku:

```bash
heroku create
git push heroku main
```

## 💡 How It Works

1. **User Interaction**: Users provide their name and age, then speak or type their concerns
2. **Speech Processing**: Voice input is converted to text using the Web Speech API
3. **Crisis Detection**: Input is analyzed for critical keywords indicating potential emergencies
4. **AI Processing**: Text is sent to OpenAI's GPT-3.5 with specialized mental health prompting
5. **Response Generation**: AI generates empathetic, evidence-based responses tailored to the user
6. **Voice Synthesis**: Responses are converted to speech for audio playback
7. **Emergency Protocols**: Crisis situations trigger immediate support resources and alerts

## 🔒 Privacy & Ethics

- No conversation data is permanently stored
- Crisis detection is performed locally before API transmission
- Minimal personal information is collected (optional name and age only)
- System prompts emphasize evidence-based approaches and appropriate support
- Emergency resources are provided for critical situations

## 📋 Future Enhancements

- User account system with conversation history
- Integration with professional mental health resources
- Multi-language support
- Expanded crisis resource database by region
- Progressive Web App (PWA) capabilities for offline access

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- OpenAI for GPT API access
- Web Speech API contributors
- Mental health professionals who provided guidance on prompt engineering