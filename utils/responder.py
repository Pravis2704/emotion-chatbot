import random

def generate_response(emotion, user_message):
    # Emotion-based response templates
    responses = {
        "sadness": [
            "I'm here for you. Want to talk more about it?",
            "That sounds tough. What’s been making you feel this way?",
            "You’re not alone. Do you want to share more about your day?"
        ],
        "joy": [
            "That's amazing! What made you feel so happy?",
            "I love hearing good news. Want to tell me more?",
            "You deserve that happiness — what happened?"
        ],
        "anger": [
            "It’s okay to feel angry. Want to vent more?",
            "I'm listening. What exactly made you feel that way?",
            "That’s frustrating. How did you respond to it?"
        ],
        "fear": [
            "That sounds scary. Want to talk it through?",
            "I'm here. What are you afraid might happen?",
            "Fear is valid. Let’s try to work through it."
        ],
        "neutral": [
            "I’m listening. Want to chat about something specific?",
            "Alright, feel free to share more.",
            "Is there something on your mind?"
        ],
        "love": [
            "That’s so wholesome. What made you feel that way?",
            "Love is powerful. Want to tell me more?",
            "That’s beautiful. I’d love to hear the story!"
        ],
        "surprise": [
            "Oh wow! That sounds unexpected!",
            "That's interesting — how did that happen?",
            "I wasn’t expecting that either!"
        ]
    }

    # Fallback
    default_responses = [
        "Tell me more about how you’re feeling.",
        "I’m here to listen.",
        "Go on, I’m with you."
    ]

    # Choose a response
    options = responses.get(emotion.lower(), default_responses)
    return random.choice(options)
