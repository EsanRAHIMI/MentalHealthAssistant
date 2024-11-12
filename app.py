from flask import Flask, request, jsonify, render_template
import openai
from dotenv import load_dotenv
import os
from datetime import datetime

# بارگذاری کلید API از فایل .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/")
def index():
    """صفحه اصلی که رابط کاربری را نمایش می‌دهد"""
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    """آنالیز ورودی کاربر و ارائه پاسخ مناسب"""
    user_input = request.json.get("text")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    # بررسی شرایط بحرانی (مانند افکار خودکشی یا آسیب)
    critical_conditions = ["suicide", "kill myself", "self-harm", "hurt myself", "end my life", "harm"]
    if any(condition in user_input.lower() for condition in critical_conditions):
        # ثبت زمان و نوع پیام اضطراری
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        emergency_message = f"Emergency Alert: A user is experiencing a critical condition. User input: '{user_input}' at {timestamp}."
        # اینجا می‌توانید منطق ارسال پیام اضطراری واقعی را اضافه کنید
        print(emergency_message)
        return jsonify({
            "response": "I'm really sorry that you're feeling this way. Please remember that you are not alone, and there are people who can help you. I strongly encourage you to reach out to a trusted person or contact a local mental health professional or helpline. You can also call emergency services (998) or the police (999) for immediate assistance.",
            "critical": True
        })

    try:
        # ارسال درخواست به مدل OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a highly empathetic and evidence-based mental health assistant. Your role is to understand the user's emotions deeply, validate their feelings, and provide actionable, practical, and specific solutions to help them feel better. Offer step-by-step guidance, coping techniques, and suggestions for lifestyle changes that can improve their mental health. Be as clear and supportive as possible, giving the user tangible actions they can take right now."},
                {"role": "user", "content": user_input}
            ]
        )
        assistant_response = response['choices'][0]['message']['content'].strip()
        return jsonify({"response": assistant_response, "user_input": user_input, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

    except Exception as e:
        print("Error occurred:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)