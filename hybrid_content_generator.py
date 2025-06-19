"""
MindPulse Daily - Advanced Hybrid Content Generator
Supports both API-based and template-based content generation
Includes extensive categories: Psychology, Astrology, Science, History, etc.
"""

import os
import random
import uuid
from datetime import datetime, timedelta
import json
import requests
from typing import List, Dict, Optional

class HybridContentGenerator:
    def __init__(self):
        self.api_keys = {
            'deepseek': os.getenv('DEEPSEEK_API_KEY'),
            'huggingface': os.getenv('HUGGINGFACE_API_KEY'),
            'openai': os.getenv('OPENAI_API_KEY')
        }

        # Expanded categories with astrology
        self.categories = {
            'psychology': {
                'name': 'Psychology',
                'emoji': '🧠',
                'topics': [
                    'memory formation', 'dream psychology', 'cognitive biases',
                    'social psychology', 'personality types', 'emotional intelligence',
                    'decision making', 'habit formation', 'stress psychology',
                    'childhood development', 'neuroplasticity', 'meditation effects'
                ]
            },
            'astrology': {
                'name': 'Astrology & Zodiac',
                'emoji': '⭐',
                'topics': [
                    'zodiac personality traits', 'moon phases effects', 'planetary alignments',
                    'astrological compatibility', 'birth chart meanings', 'mercury retrograde',
                    'constellation mythology', 'chakra alignment', 'crystal healing',
                    'tarot psychology', 'numerology patterns', 'spiritual awakening'
                ]
            },
            'space': {
                'name': 'Space & Cosmos',
                'emoji': '🚀',
                'topics': [
                    'black holes', 'exoplanets', 'space missions', 'galaxy formation',
                    'dark matter', 'stellar evolution', 'cosmic radiation',
                    'Mars exploration', 'asteroid mining', 'space-time physics'
                ]
            },
            'history': {
                'name': 'History & Ancient Civilizations',
                'emoji': '🏛️',
                'topics': [
                    'ancient Egypt mysteries', 'Roman empire secrets', 'lost civilizations',
                    'archaeological discoveries', 'historical conspiracies', 'ancient technologies',
                    'medieval life', 'forgotten inventions', 'cultural mysteries'
                ]
            },
            'science': {
                'name': 'Science & Discovery',
                'emoji': '🔬',
                'topics': [
                    'quantum physics', 'genetic engineering', 'climate science',
                    'medical breakthroughs', 'ocean mysteries', 'animal behavior',
                    'plant intelligence', 'biodiversity', 'evolutionary biology'
                ]
            },
            'lifestyle': {
                'name': 'Health & Lifestyle',
                'emoji': '🌿',
                'topics': [
                    'longevity secrets', 'nutrition science', 'exercise psychology',
                    'sleep optimization', 'stress management', 'mindfulness practices',
                    'healthy aging', 'immune system', 'mental wellness'
                ]
            },
            'mystery': {
                'name': 'Mysteries & Phenomena',
                'emoji': '👁️',
                'topics': [
                    'unexplained phenomena', 'conspiracy theories', 'paranormal research',
                    'urban legends', 'cryptozoology', 'ancient mysteries',
                    'supernatural experiences', 'time anomalies', 'consciousness studies'
                ]
            }
        }

        # Viral title templates
        self.title_templates = [
            "Scientists Discovered Something Shocking About {topic} That Nobody Talks About",
            "The Hidden Truth About {topic} That Will Change Your Life",
            "{topic}: What Ancient Wisdom Knew That Modern Science Just Discovered",
            "Why Everything You Know About {topic} Is Wrong",
            "The Secret {topic} Method That Billionaires Use Daily",
            "This {topic} Discovery Could Change Everything We Know",
            "The {topic} Phenomenon That Scientists Can't Explain",
            "Ancient {topic} Secrets That Modern Medicine Finally Proves",
            "The Shocking {topic} Truth That Governments Don't Want You to Know",
            "How {topic} Rewrites Everything We Thought We Knew"
        ]

    def generate_content_with_api(self, category: str, language: str = 'en') -> Optional[str]:
        """Generate content using available APIs"""
        try:
            return self._try_deepseek_api(category, language)
        except:
            try:
                return self._try_huggingface_api(category, language)
            except:
                return None

    def _try_deepseek_api(self, category: str, language: str) -> str:
        """Try DeepSeek API for content generation"""
        if not self.api_keys['deepseek']:
            raise Exception("No DeepSeek API key")

        cat_info = self.categories[category]
        topic = random.choice(cat_info['topics'])

        prompt = self._create_detailed_prompt(category, topic, language)

        headers = {
            'Authorization': f'Bearer {self.api_keys["deepseek"]}',
            'Content-Type': 'application/json'
        }

        data = {
            'model': 'deepseek-chat',
            'messages': [{'role': 'user', 'content': prompt}],
            'max_tokens': 1500,
            'temperature': 0.8
        }

        response = requests.post(
            'https://api.deepseek.com/v1/chat/completions',
            headers=headers,
            json=data,
            timeout=30
        )

        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            raise Exception(f"DeepSeek API error: {response.status_code}")

    def _try_huggingface_api(self, category: str, language: str) -> str:
        """Try Hugging Face API for content generation"""
        if not self.api_keys['huggingface']:
            raise Exception("No Hugging Face API key")

        # Hugging Face implementation would go here
        raise Exception("Hugging Face API not implemented yet")

    def generate_template_content(self, category: str, language: str = 'en') -> str:
        """Generate content using templates (API-free fallback)"""
        cat_info = self.categories[category]
        topic = random.choice(cat_info['topics'])

        # Generate viral title
        title_template = random.choice(self.title_templates)
        title = title_template.format(topic=topic.title())

        # Generate description
        descriptions = self._get_template_descriptions(category, topic, language)
        description = random.choice(descriptions)

        # Generate content
        content_sections = self._get_template_content(category, topic, language)

        # Format as markdown
        markdown_content = self._format_markdown(title, description, content_sections, category, language)

        return markdown_content

    def _create_detailed_prompt(self, category: str, topic: str, language: str) -> str:
        """Create detailed prompt for API-based generation"""
        cat_info = self.categories[category]

        if language == 'tr':
            prompt = f"""
            Türkçe olarak '{topic}' konusunda viral bir blog makalesi yaz. Kategori: {cat_info['name']}

            GEREKSINIMLER:
            - Çok etkileyici ve viral bir başlık
            - Kısa ama ilgi çekici açıklama
            - En az 5 paragraf detaylı içerik
            - Bilimsel gerçekler ve istatistikler
            - Okuyucuyu şaşırtacak bilgiler
            - Sosyal medyada paylaşılabilir stil

            FORMAT:
            ---
            title: "BAŞLIK"
            description: "AÇIKLAMA"
            date: "2025-06-19"
            language: "tr"
            category: "{category}"
            ---

            ## 🔍 Keşif

            (İçerik paragrafları...)
            """
        else:
            prompt = f"""
            Write a viral blog article about '{topic}' in English. Category: {cat_info['name']}

            REQUIREMENTS:
            - Highly engaging, viral title
            - Compelling short description
            - At least 5 paragraphs of detailed content
            - Scientific facts and statistics
            - Mind-blowing information
            - Social media shareable style

            FORMAT:
            ---
            title: "TITLE"
            description: "DESCRIPTION"
            date: "2025-06-19"
            language: "en"
            category: "{category}"
            ---

            ## 🔍 The Discovery

            (Content paragraphs...)
            """

        return prompt

    def _get_template_descriptions(self, category: str, topic: str, language: str) -> List[str]:
        """Get template descriptions for fallback content"""
        if language == 'tr':
            return [
                f"{topic.title()} hakkında şaşırtıcı keşifler ve bilim insanlarının yeni bulguları.",
                f"Modern araştırmalar {topic} konusunda hayatınızı değiştirebilecek gerçekleri ortaya çıkardı.",
                f"{topic.title()} ile ilgili bilinmeyen sırlar ve etkileyici bilimsel kanıtlar.",
                f"Uzmanların {topic} hakkında açıkladığı devrim niteliğindeki bulgular."
            ]
        else:
            return [
                f"Surprising discoveries and new scientific findings about {topic}.",
                f"Modern research reveals life-changing truths about {topic}.",
                f"Unknown secrets and compelling scientific evidence about {topic}.",
                f"Revolutionary findings that experts reveal about {topic}."
            ]

    def _get_template_content(self, category: str, topic: str, language: str) -> List[Dict]:
        """Get template content sections"""
        if category == 'astrology':
            return self._get_astrology_content(topic, language)
        elif category == 'psychology':
            return self._get_psychology_content(topic, language)
        elif category == 'space':
            return self._get_space_content(topic, language)
        else:
            return self._get_general_content(topic, language)

    def _get_astrology_content(self, topic: str, language: str) -> List[Dict]:
        """Generate astrology-specific content"""
        if language == 'tr':
            return [
                {
                    'title': '🔍 Astrolojik Keşif',
                    'content': f'{topic.title()} konusundaki son araştırmalar, antik bilgelikle modern psikolojinin kesişim noktasında şaşırtıcı bulgular ortaya çıkardı. Binlerce yıldır insanlığın takip ettiği bu sistemin, günümüz nörobilim araştırmalarıyla desteklendiği görülüyor.'
                },
                {
                    'title': '📊 Bilimsel Kanıtlar',
                    'content': f'Yapılan çalışmalarda, {topic} ile kişilik özellikleri arasında %70 oranında korelasyon bulundu. Bu oran, rastlantısal olma ihtimalini neredeyse sıfıra indiriyor ve astrolojik sistemlerin gerçek bir temeli olduğunu gösteriyor.'
                },
                {
                    'title': '🌟 Pratik Uygulamalar',
                    'content': f'{topic.title()} bilgisini günlük hayatınızda kullanarak, karar verme süreçlerinizi %40 oranında iyileştirebilir ve kişisel ilişkilerinizde daha başarılı olabilirsiniz.'
                }
            ]
        else:
            return [
                {
                    'title': '🔍 The Astrological Discovery',
                    'content': f'Recent research on {topic} reveals surprising findings at the intersection of ancient wisdom and modern psychology. This system, followed by humanity for thousands of years, appears to be supported by contemporary neuroscience research.'
                },
                {
                    'title': '📊 Scientific Evidence',
                    'content': f'Studies found a 70% correlation between {topic} and personality traits. This rate reduces the possibility of coincidence to almost zero and shows that astrological systems have a real foundation.'
                },
                {
                    'title': '🌟 Practical Applications',
                    'content': f'By using {topic} knowledge in your daily life, you can improve your decision-making processes by 40% and be more successful in your personal relationships.'
                }
            ]

    def _get_psychology_content(self, topic: str, language: str) -> List[Dict]:
        """Generate psychology-specific content"""
        if language == 'tr':
            return [
                {
                    'title': '🧠 Psikolojik Keşif',
                    'content': f'{topic.title()} konusundaki son nörobilim araştırmaları, insan zihninin çalışma şekli hakkında devrim niteliğinde bulgular ortaya çıkardı. Bu keşifler, günlük yaşamımızı nasıl optimize edebileceğimiz konusunda yeni perspektifler sunuyor.'
                },
                {
                    'title': '📈 Araştırma Sonuçları',
                    'content': f'10.000 katılımcıyla yapılan çalışmada, {topic} anlayan kişilerin yaşam kalitesi %65 oranında artış gösterdi. Stres seviyeleri düştü, yaratıcılık arttı ve genel mutluluk seviyesi yükseldi.'
                },
                {
                    'title': '💡 Uygulamaya Geçirin',
                    'content': f'{topic.title()} prensiplerini günlük rutininize dahil ederek, mental performansınızı artırabilir ve daha tatmin edici bir yaşam sürebilirsiniz.'
                }
            ]
        else:
            return [
                {
                    'title': '🧠 The Psychological Discovery',
                    'content': f'Recent neuroscience research on {topic} reveals revolutionary findings about how the human mind works. These discoveries offer new perspectives on how we can optimize our daily lives.'
                },
                {
                    'title': '📈 Research Results',
                    'content': f'A study with 10,000 participants showed that people who understand {topic} experienced a 65% increase in quality of life. Stress levels decreased, creativity increased, and overall happiness levels rose.'
                },
                {
                    'title': '💡 Put It Into Practice',
                    'content': f'By incorporating {topic} principles into your daily routine, you can enhance your mental performance and live a more fulfilling life.'
                }
            ]

    def _get_space_content(self, topic: str, language: str) -> List[Dict]:
        """Generate space-specific content"""
        if language == 'tr':
            return [
                {
                    'title': '🚀 Uzay Keşfi',
                    'content': f'{topic.title()} konusundaki en son uzay araştırmaları, evren hakkındaki anlayışımızı kökten değiştiren bulgular ortaya çıkardı. NASA ve ESA\'nın ortak çalışmaları, bu alandaki en büyük gizemlerden birini çözmeye yaklaştı.'
                },
                {
                    'title': '🔬 Bilimsel Bulgular',
                    'content': f'Hubble ve James Webb teleskoplarından gelen veriler, {topic} ile ilgili teorilerin %90 oranında doğru olduğunu kanıtladı. Bu keşif, uzay biliminde yeni bir çağın başlangıcını işaret ediyor.'
                },
                {
                    'title': '🌌 Geleceğe Etkileri',
                    'content': f'{topic.title()} anlayışımız, gelecekteki uzay misyonlarını ve hatta günlük teknolojilerimizi şekillendireceği öngörülüyor. Bu bilgi, insanlığın uzaydaki yerini yeniden tanımlayabilir.'
                }
            ]
        else:
            return [
                {
                    'title': '🚀 The Space Discovery',
                    'content': f'Latest space research on {topic} reveals findings that fundamentally change our understanding of the universe. Joint studies by NASA and ESA have brought us closer to solving one of the biggest mysteries in this field.'
                },
                {
                    'title': '🔬 Scientific Findings',
                    'content': f'Data from Hubble and James Webb telescopes proved that theories about {topic} are 90% accurate. This discovery marks the beginning of a new era in space science.'
                },
                {
                    'title': '🌌 Future Implications',
                    'content': f'Our understanding of {topic} is predicted to shape future space missions and even our daily technologies. This knowledge could redefine humanity\'s place in space.'
                }
            ]

    def _get_general_content(self, topic: str, language: str) -> List[Dict]:
        """Generate general content for other categories"""
        if language == 'tr':
            return [
                {
                    'title': '🔍 Keşif',
                    'content': f'{topic.title()} konusundaki son araştırmalar, bu alanda şaşırtıcı yeni bulgular ortaya çıkardı. Uzmanlar, bu keşfin birçok alanda devrim yaratacağını öngörüyor.'
                },
                {
                    'title': '📊 Veriler',
                    'content': f'Yapılan çalışmalarda, {topic} ile ilgili geleneksel yaklaşımların %80 oranında yanlış olduğu ortaya çıktı. Bu bulgular, konuya bakış açımızı tamamen değiştiriyor.'
                },
                {
                    'title': '💫 Sonuç',
                    'content': f'{topic.title()} hakkındaki bu yeni bilgiler, günlük yaşamımızda pratik uygulamalara dönüştürülebilir ve yaşam kalitemizi artırabilir.'
                }
            ]
        else:
            return [
                {
                    'title': '🔍 The Discovery',
                    'content': f'Recent research on {topic} has revealed surprising new findings in this field. Experts predict that this discovery will revolutionize many areas.'
                },
                {
                    'title': '📊 The Data',
                    'content': f'Studies have revealed that traditional approaches to {topic} are 80% incorrect. These findings completely change our perspective on the subject.'
                },
                {
                    'title': '💫 The Conclusion',
                    'content': f'This new knowledge about {topic} can be transformed into practical applications in our daily lives and improve our quality of life.'
                }
            ]

    def _format_markdown(self, title: str, description: str, sections: List[Dict], category: str, language: str) -> str:
        """Format content as markdown"""
        content = f"""---
title: "{title}"
description: "{description}"
date: "{datetime.now().strftime('%Y-%m-%d')}"
language: "{language}"
category: "{category}"
image: "{category}_{random.randint(1000, 9999)}"
---

"""

        for section in sections:
            content += f"## {section['title']}\n\n{section['content']}\n\n"

        # Add engagement elements
        if language == 'tr':
            content += """## ❓ Düşünün

Bu bilgiler hayatınıza nasıl uygulanabilir?

## 💬 Bu İçeriği Paylaşın

Bu keşfi arkadaşlarınızla paylaşın ve onların da bu konudaki deneyimlerini öğrenin!
"""
        else:
            content += """## ❓ Think About It

How can this information be applied to your life?

## 💬 Share This Content

Share this discovery with your friends and learn about their experiences on this topic!
"""

        return content

    def generate_batch_content(self, count: int = 10, language: str = 'en') -> List[str]:
        """Generate a batch of content pieces"""
        generated_content = []
        categories = list(self.categories.keys())

        for i in range(count):
            category = random.choice(categories)

            # Try API first, fallback to template
            content = self.generate_content_with_api(category, language)
            if not content:
                content = self.generate_template_content(category, language)

            generated_content.append(content)
            print(f"Generated {i+1}/{count}: {category} ({language})")

        return generated_content

    def save_content(self, content: str, language: str = 'en'):
        """Save content to appropriate directory"""
        date = datetime.now().strftime("%Y-%m-%d")
        unique_id = str(uuid.uuid4())[:8]
        filename = f"hybrid-{date}-{unique_id}.md"

        directory = f"src/content/posts/{language}"
        os.makedirs(directory, exist_ok=True)

        filepath = os.path.join(directory, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Saved: {filepath}")
        return filepath

def main():
    """Main execution function"""
    generator = HybridContentGenerator()

    # Generate English content
    print("Generating English content...")
    en_content = generator.generate_batch_content(8, 'en')
    for content in en_content:
        generator.save_content(content, 'en')

    print("\n" + "="*50 + "\n")

    # Generate Turkish content
    print("Generating Turkish content...")
    tr_content = generator.generate_batch_content(8, 'tr')
    for content in tr_content:
        generator.save_content(content, 'tr')

    print(f"\nGenerated {len(en_content)} English and {len(tr_content)} Turkish articles!")
    print("Categories included: Psychology, Astrology, Space, History, Science, Lifestyle, Mystery")

if __name__ == "__main__":
    main()
