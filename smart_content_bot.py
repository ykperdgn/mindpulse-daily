from openai import OpenAI
import os
import requests
import json
from datetime import datetime
import uuid
import random

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not installed, use system env vars

# API Configuration
AI_PROVIDER = os.getenv("AI_PROVIDER", "openai")  # openai, deepseek
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"

# Viral başlık şablonları
VIRAL_TITLE_TEMPLATES = [
    "Scientists Discovered Something Shocking About {topic}",
    "The Hidden Truth About {topic} That Nobody Talks About",
    "Why {topic} Is More Powerful Than You Think",
    "The Secret Psychology Behind {topic}",
    "What {topic} Reveals About Human Nature",
    "The Surprising Science of {topic}",
    "Why Experts Are Worried About {topic}",
    "The {topic} Mystery That Changed Everything",
    "What Ancient Civilizations Knew About {topic}",
    "The Dark Side of {topic} Scientists Don't Want You to Know"
]

# Tıklama odaklı giriş cümleleri
HOOK_STARTERS = [
    "What if everything you thought you knew about",
    "Scientists have just discovered that",
    "For centuries, humans believed",
    "A groundbreaking study reveals",
    "The most shocking discovery about",
    "Ancient wisdom meets modern science:",
    "Researchers were stunned to find"
]

# Tartışma soruları
DISCUSSION_QUESTIONS = [
    "What's your take on this discovery?",
    "How does this change your perspective?",
    "Have you ever experienced something similar?",
    "Do you think this applies to everyone?",
    "What would you do with this knowledge?",
    "Does this surprise you or confirm what you suspected?",
    "How might this impact future generations?"
]

def call_ai_api(prompt, max_tokens=1200, temperature=0.8):
    """AI API çağrısı yap - DeepSeek veya OpenAI"""

    if AI_PROVIDER == "deepseek" and DEEPSEEK_API_KEY:
        print(f"🧠 Using DeepSeek API...")

        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stream": False
        }

        try:
            response = requests.post(f"{DEEPSEEK_BASE_URL}/chat/completions",
                                   headers=headers,
                                   json=payload,
                                   timeout=30)
            response.raise_for_status()
            result = response.json()
            return result['choices'][0]['message']['content']
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 402:
                print(f"💳 DeepSeek API: Payment Required - Check your account balance")
            else:
                print(f"❌ DeepSeek API HTTP error: {e}")

            # Fallback to OpenAI if available
            if OPENAI_API_KEY:
                print("🔄 Falling back to OpenAI...")
                return call_openai_api(prompt, max_tokens, temperature)
            raise e
        except Exception as e:
            print(f"❌ DeepSeek API error: {e}")
            # Fallback to OpenAI if available
            if OPENAI_API_KEY:
                print("🔄 Falling back to OpenAI...")
                return call_openai_api(prompt, max_tokens, temperature)
            raise e

    elif OPENAI_API_KEY:
        print(f"🤖 Using OpenAI API...")
        return call_openai_api(prompt, max_tokens, temperature)

    else:
        raise ValueError("❌ No API key found! Set DEEPSEEK_API_KEY or OPENAI_API_KEY")

def call_openai_api(prompt, max_tokens=1200, temperature=0.8):
    """OpenAI API çağrısı - Yeni v1.0+ API"""
    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=temperature
    )

    return response.choices[0].message.content

def generate_viral_content():
    """Viral potansiyeli yüksek içerik üret"""

    # Rastgele konu seç
    topics = [
        "human memory", "sleep patterns", "decision making", "social behavior",
        "creativity", "fear responses", "learning abilities", "emotional intelligence",
        "intuition", "habit formation", "stress response", "social influence",
        "brain plasticity", "perception", "consciousness", "empathy"
    ]

    topic = random.choice(topics)
    title_template = random.choice(VIRAL_TITLE_TEMPLATES)
    hook_starter = random.choice(HOOK_STARTERS)
    discussion_q = random.choice(DISCUSSION_QUESTIONS)

    prompt = f"""
    Create an engaging, viral-potential blog article about {topic}.

    REQUIREMENTS:
    - Title: Use this template and make it compelling: "{title_template.format(topic=topic)}"
    - Hook: Start with: "{hook_starter} {topic}..."
    - Structure: Use the format below
    - Length: 400-600 words
    - Tone: Conversational, intriguing, shareworthy
    - Include: Statistics, examples, surprising facts
    - End with: Discussion question and shareable quote

    Use this EXACT markdown structure:

    ---
    title: "Your compelling title here"
    description: "A 2-sentence description that makes people want to click"
    date: "2025-06-18"
    language: "en"
    category: "psychology"
    image: "suggested_image_description_for_dalle"
    ---

    ## 🔍 The Discovery

    [Hook sentence with surprising fact or statistic]

    ## 📊 What Science Shows

    [Research findings, studies, data]

    ## 🧠 Why This Matters

    [Deep explanation of implications]

    ## 💡 Real-World Impact

    [Examples, applications, stories]

    ## ❓ Think About It

    {discussion_q}

    ## 💬 Share This Insight

    > "Create a memorable, tweetable quote related to the topic"    **Did this change how you think about {topic}? Share your thoughts!**
    """

    return call_ai_api(prompt, max_tokens=1200, temperature=0.8)

def generate_turkish_version(english_content):
    """İngilizce içeriği Türkçe'ye çevir"""
    prompt = f"""
    Translate this blog article to Turkish while maintaining the viral, engaging tone.
    Keep the markdown structure and make sure Turkish sounds natural and compelling.
    Change 'language: "en"' to 'language: "tr"' in frontmatter.    Original English content:
    {english_content}
    """

    return call_ai_api(prompt, max_tokens=1200, temperature=0.7)

def save_content(content, language="en"):
    """İçeriği kaydet"""
    date = datetime.now().strftime("%Y-%m-%d")
    slug = str(uuid.uuid4())[:8]

    if language == "en":
        filepath = f"src/content/posts/en/viral-{date}-{slug}.md"
    else:
        filepath = f"src/content/posts/tr/viral-{date}-{slug}.md"

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Viral content saved: {filepath}")
    return filepath

def generate_batch_content(count=3):
    """Toplu viral içerik üret"""
    print(f"🧠 Generating {count} viral articles...")

    for i in range(count):
        print(f"📝 Generating article {i+1}/{count}...")

        # İngilizce içerik üret
        english_content = generate_viral_content()
        en_path = save_content(english_content, "en")

        # Türkçe çeviri üret
        print(f"🇹🇷 Translating to Turkish...")
        turkish_content = generate_turkish_version(english_content)
        tr_path = save_content(turkish_content, "tr")

        print(f"✨ Article {i+1} completed!")
        print(f"   EN: {en_path}")
        print(f"   TR: {tr_path}")
        print()

if __name__ == "__main__":
    print("🚀 MindPulse Daily - AI Content Generator")
    print(f"📡 Provider: {AI_PROVIDER.upper()}")

    # API key kontrolü
    if AI_PROVIDER == "deepseek":
        if not DEEPSEEK_API_KEY:
            print("❌ DEEPSEEK_API_KEY environment variable not set!")
            print("Set it with: $env:DEEPSEEK_API_KEY='your-deepseek-api-key'")
            if OPENAI_API_KEY:
                print("🔄 Falling back to OpenAI...")
            else:
                print("❌ No API keys available!")
                exit(1)
        else:
            print(f"✅ DeepSeek API Key found: {DEEPSEEK_API_KEY[:8]}...")

    elif AI_PROVIDER == "openai":
        if not OPENAI_API_KEY:
            print("❌ OPENAI_API_KEY environment variable not set!")
            print("Set it with: $env:OPENAI_API_KEY='your-openai-api-key'")
            exit(1)
        else:
            print(f"✅ OpenAI API Key found: {OPENAI_API_KEY[:8]}...")

    try:
        print("🤖 Starting viral content generation...")
        generate_batch_content(3)
        print("🎉 Viral content generation complete!")
        print("🚀 Your MindPulse site now has compelling, shareable content!")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
