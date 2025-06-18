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
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"

# Hugging Face Free API (Backup)
HF_API_KEY = os.getenv("HF_API_KEY", "hf_demo")  # Demo key works for limited usage
HF_BASE_URL = "https://api-inference.huggingface.co/models"

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
    """AI API çağrısı yap - DeepSeek primary, Hugging Face fallback"""

    # Önce DeepSeek deneyelim
    if DEEPSEEK_API_KEY and DEEPSEEK_API_KEY != "your-deepseek-key-here":
        try:
            return call_deepseek_api(prompt, max_tokens, temperature)
        except Exception as e:
            print(f"🔄 DeepSeek failed, trying Hugging Face...")

    # Fallback: Hugging Face Free API
    try:
        return call_huggingface_api(prompt, max_tokens, temperature)
    except Exception as e:
        print(f"❌ All APIs failed. Generating sample content...")
        return generate_sample_content(prompt)

def call_deepseek_api(prompt, max_tokens=1200, temperature=0.8):
    """DeepSeek API çağrısı"""
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

    response = requests.post(f"{DEEPSEEK_BASE_URL}/chat/completions",
                           headers=headers,
                           json=payload,
                           timeout=30)
    response.raise_for_status()
    result = response.json()
    return result['choices'][0]['message']['content']

def call_huggingface_api(prompt, max_tokens=800, temperature=0.8):
    """Hugging Face Free API çağrısı"""
    print(f"🤗 Using Hugging Face Free API...")

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }

    # Mistral 7B model (ücretsiz)
    model_url = f"{HF_BASE_URL}/mistralai/Mistral-7B-Instruct-v0.1"

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": max_tokens,
            "temperature": temperature,
            "return_full_text": False
        }
    }

    response = requests.post(model_url, headers=headers, json=payload, timeout=60)
    response.raise_for_status()
    result = response.json()

    if isinstance(result, list) and len(result) > 0:
        return result[0].get('generated_text', '')
    return result.get('generated_text', '')

def generate_sample_content(prompt):
    """Sample viral content generator (no API needed)"""
    print(f"📝 Generating sample content...")

    topics = ["sleep", "memory", "creativity", "stress", "habits"]
    topic = random.choice(topics)

    return f'''---
title: "The Hidden Science Behind {topic.title()} That Will Change Your Life"
description: "Scientists have discovered something shocking about {topic} that could revolutionize how you think about your daily life."
date: "{datetime.now().strftime('%Y-%m-%d')}"
language: "en"
category: "psychology"
image: "{topic}_research_brain_science"
---

## 🔍 The Discovery

What if everything you thought you knew about {topic} was wrong? Recent groundbreaking research has revealed surprising insights that challenge our basic understanding.

## 📊 What Science Shows

Research from leading universities shows that {topic} affects our lives in ways we never imagined. Studies involving thousands of participants have uncovered patterns that could change everything.

## 🧠 Why This Matters

This discovery has profound implications for how we approach our daily routines and long-term goals.

## 💡 Real-World Impact

People who understand this science report significant improvements in their quality of life and overall well-being.

## ❓ Think About It

How might this change your perspective on {topic}?

## 💬 Share This Insight

> "The most powerful discoveries often hide in plain sight, waiting for science to reveal their secrets."

**Did this change how you think about {topic}? Share your thoughts!**
'''

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

    > "Create a memorable, tweetable quote related to the topic"

    **Did this change how you think about {topic}? Share your thoughts!**
    """

    return call_ai_api(prompt, max_tokens=1200, temperature=0.8)

def generate_turkish_version(english_content):
    """İngilizce içeriği Türkçe'ye çevir"""
    prompt = f"""
    Translate this blog article to Turkish while maintaining the viral, engaging tone.
    Keep the markdown structure and make sure Turkish sounds natural and compelling.
    Change 'language: "en"' to 'language: "tr"' in frontmatter.

    Original English content:
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
    print("🚀 MindPulse Daily - Multi-AI Content Generator")

    # API durumunu kontrol et
    if DEEPSEEK_API_KEY and DEEPSEEK_API_KEY != "your-deepseek-key-here":
        print("📡 Primary: DeepSeek API")
        print(f"✅ DeepSeek API Key found: {DEEPSEEK_API_KEY[:8]}...")
    else:
        print("📡 Primary: Hugging Face Free API")
        print("🤗 Using free Hugging Face models")

    print("🔄 Fallback: Sample content generation")

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
