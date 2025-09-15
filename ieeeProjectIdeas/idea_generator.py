# idea_generator.py

def generate_project_idea(title, summary):
    text = (title + " " + summary).lower()

    if "medical" in text or "health" in text:
        return "Build an AI model to detect diseases from X-ray or health reports."
    elif "traffic" in text or "vehicle" in text:
        return "Create a smart traffic management simulation using real-time data."
    elif "education" in text or "learning" in text:
        return "Design a personalized learning assistant using AI for student support."
    elif "robot" in text:
        return "Develop a robot that can perform daily human tasks autonomously."
    elif "finance" in text or "stock" in text:
        return "Build a stock prediction system using historical data and AI models."
    elif "iot" in text:
        return "Create a smart home system using IoT devices and cloud control."
    elif "agriculture" in text or "crop" in text:
        return "Detect crop diseases using image classification and support farmers."
    else:
        return f"Apply the concept from this paper on '{title}' to a practical real-world project."
