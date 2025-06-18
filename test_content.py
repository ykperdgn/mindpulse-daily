import openai
import os
from datetime import datetime
import uuid

def generate_test_article():
    """Test için tek bir makale üret"""
    prompt = (
        "Create a short blog article in markdown format with a catchy title, "
        "short description, and a few paragraphs of interesting content. "
        "Choose from these fascinating topics: space exploration, ocean mysteries, "
        "human psychology, history facts, wildlife behavior, science discoveries, "
        "ancient civilizations, brain science, or unusual phenomena. "
        "AVOID topics about: AI, artificial intelligence, machine learning, robots, or technology. "
        "Use the following frontmatter format:\n\n"
        "---\n"
        "title: \"\"\n"
        "description: \"\"\n"
        "date: \"2025-06-18\"\n"
        "language: \"en\"\n"
        "---\n\n"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0.9
    )

    return response['choices'][0]['message']['content']

def save_test_article(content):
    """Test makalesini kaydet"""
    date = datetime.now().strftime("%Y-%m-%d")
    slug = str(uuid.uuid4())[:8]
    filepath = f"src/content/posts/en/test-{date}-{slug}.md"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Test article saved: {filepath}")

if __name__ == "__main__":
    # OpenAI API key kontrolü
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ OPENAI_API_KEY environment variable not set!")
        print("Set it with: $env:OPENAI_API_KEY='your-api-key-here'")
        exit(1)

    openai.api_key = api_key

    try:
        print("🧠 Generating test article...")
        article = generate_test_article()
        save_test_article(article)
        print("🎉 Success! Check the new article in src/content/posts/en/")
    except Exception as e:
        print(f"❌ Error: {e}")
