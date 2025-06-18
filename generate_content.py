import openai
import os
from datetime import datetime
import uuid

# OpenAI API anahtarını ortam değişkeni olarak kullanın
def generate_article():
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

def save_article(content):
    date = datetime.now().strftime("%Y-%m-%d")
    slug = str(uuid.uuid4())[:8]
    filepath = f"src/content/posts/en/{date}-{slug}.md"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    openai.api_key = os.getenv("OPENAI_API_KEY")
    for _ in range(3):
        article = generate_article()
        save_article(article)
