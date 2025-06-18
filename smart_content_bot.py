import openai
import os
from datetime import datetime
import uuid
import random

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

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1200,
        temperature=0.8
    )

    return response['choices'][0]['message']['content']

def generate_turkish_version(english_content):
    """İngilizce içeriği Türkçe'ye çevir"""
    prompt = f"""
    Translate this blog article to Turkish while maintaining the viral, engaging tone.
    Keep the markdown structure and make sure Turkish sounds natural and compelling.
    Change 'language: "en"' to 'language: "tr"' in frontmatter.

    Original English content:
    {english_content}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1200,
        temperature=0.7
    )

    return response['choices'][0]['message']['content']

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
    # OpenAI API key kontrolü
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ OPENAI_API_KEY environment variable not set!")
        print("Set it with: $env:OPENAI_API_KEY='your-api-key-here'")
        exit(1)

    print(f"✅ API Key found: {api_key[:8]}...")
    openai.api_key = api_key

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
