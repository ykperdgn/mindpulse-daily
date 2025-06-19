#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MindPulse Daily - Advanced Long-Form Content Generator
Minimum 800 words, high-quality bilingual content generator
Auto-scheduled for daily 16:05 Turkey time
"""

import os
import json
import random
import hashlib
from datetime import datetime, timedelta
import schedule
import time
from pathlib import Path

class AdvancedContentGenerator:
    def __init__(self):
        self.content_dir = Path("src/content/posts")
        self.min_words = 800
        self.max_words = 1500        # Advanced topic templates for long-form content
        self.advanced_topics = {
            "science": [
                {
                    "title_en": "The Revolutionary Discovery That's Rewriting {topic} Science",
                    "title_tr": "{topic} Bilimini Yeniden Yazan Devrimci Keşif",
                    "template": "discovery_deep_dive"
                },
                {
                    "title_en": "Scientists Just Proved Everything We Knew About {topic} Was Wrong",
                    "title_tr": "Bilim İnsanları {topic} Hakkında Bildiklerimizin Yanlış Olduğunu Kanıtladı",
                    "template": "paradigm_shift"
                },
                {
                    "title_en": "The Hidden Truth About {topic} That Changes Everything",
                    "title_tr": "{topic} Hakkındaki Gizli Gerçek Her Şeyi Değiştiriyor",
                    "template": "hidden_truth"
                }
            ],
            "technology": [
                {
                    "title_en": "The {topic} Revolution: How It's Secretly Transforming Our World",
                    "title_tr": "{topic} Devrimi: Dünyamızı Gizlice Nasıl Dönüştürüyor",
                    "template": "tech_revolution"
                },
                {
                    "title_en": "Inside the {topic} Breakthrough That Will Change Your Life Forever",
                    "title_tr": "Hayatınızı Sonsuza Dek Değiştirecek {topic} Atılımının İçyüzü",
                    "template": "life_changing_tech"
                }
            ],
            "psychology": [
                {
                    "title_en": "The Psychology Secret That Explains Why {topic} Controls Your Mind",
                    "title_tr": "{topic}'in Zihninizi Neden Kontrol Ettiğini Açıklayan Psikoloji Sırrı",
                    "template": "mind_control"
                },
                {
                    "title_en": "Neuroscientists Discover How {topic} Rewires Your Brain in 30 Days",
                    "title_tr": "Nörologlar {topic}'in Beyninizi 30 Günde Nasıl Yeniden Şekillendirdiğini Keşfetti",
                    "template": "brain_rewiring"
                }
            ],
            "space": [
                {
                    "title_en": "The Space Discovery About {topic} That NASA Doesn't Want You to Know",
                    "title_tr": "NASA'nın Bilmenizi İstemediği {topic} Hakkındaki Uzay Keşfi",
                    "template": "nasa_secret"
                },
                {
                    "title_en": "Astronomers Just Found Something Impossible About {topic}",
                    "title_tr": "Astronomlar {topic} Hakkında İmkansız Bir Şey Keşfetti",
                    "template": "impossible_discovery"
                }
            ],
            "astrology": [
                {
                    "title_en": "The Ancient {topic} Secret That Modern Science Just Confirmed",
                    "title_tr": "Modern Bilimin Az Önce Doğruladığı Antik {topic} Sırrı",
                    "template": "discovery_deep_dive"
                },
                {
                    "title_en": "Why Everything You Know About {topic} Is Wrong",
                    "title_tr": "{topic} Hakkında Bildiklerinizin Neden Yanlış Olduğu",
                    "template": "paradigm_shift"
                }
            ],
            "lifestyle": [
                {
                    "title_en": "The Life-Changing {topic} Method That Everyone's Talking About",
                    "title_tr": "Herkesin Konuştuğu Hayat Değiştiren {topic} Metodu",
                    "template": "discovery_deep_dive"
                },
                {
                    "title_en": "Scientists Discover Why {topic} Is The Key to Happiness",
                    "title_tr": "Bilim İnsanları {topic}'in Mutluluğun Anahtarı Olduğunu Keşfetti",
                    "template": "paradigm_shift"
                }
            ]
        }        # Specific topics for each category
        self.topic_specifics = {
            "science": ["quantum physics", "DNA repair", "cellular regeneration", "neural plasticity", "epigenetics", "microbiome", "photosynthesis", "protein folding"],
            "technology": ["artificial intelligence", "quantum computing", "blockchain", "nanotechnology", "biotechnology", "neural interfaces", "fusion energy", "space technology"],
            "psychology": ["cognitive bias", "memory formation", "decision making", "emotional intelligence", "social psychology", "behavioral economics", "consciousness", "learning theory"],
            "space": ["black holes", "exoplanets", "dark matter", "cosmic radiation", "stellar formation", "galactic evolution", "space-time", "quantum mechanics"],
            "astrology": ["planetary alignments", "zodiac patterns", "celestial influences", "astrological cycles", "cosmic energies", "lunar phases", "solar patterns", "stellar connections"],
            "lifestyle": ["nutrition science", "sleep optimization", "stress management", "productivity methods", "mindfulness", "exercise science", "habit formation", "work-life balance"]
        }

        # Long-form content templates
        self.content_templates = {
            "discovery_deep_dive": {
                "en": {
                    "intro": "In a groundbreaking study that has sent shockwaves through the scientific community, researchers have uncovered revolutionary findings about {topic} that fundamentally challenge our understanding of {field}. This discovery, published in the latest issue of a prestigious scientific journal, promises to reshape how we approach {application_area} and could lead to unprecedented breakthroughs in the coming decades.",
                    "sections": [
                        {
                            "title": "The Revolutionary Discovery",
                            "content": "The research team, led by Dr. {researcher_name} at {institution}, spent over {timeframe} investigating the intricate mechanisms behind {topic}. Using cutting-edge {methodology}, they discovered that {main_finding}. This finding directly contradicts the widely accepted {old_theory} theory that has dominated the field for {time_period}.\n\nWhat makes this discovery particularly remarkable is {unique_aspect}. The implications extend far beyond academic circles, potentially impacting {real_world_applications}. The research involved {study_details} and utilized {advanced_techniques} to achieve unprecedented precision in their measurements."
                        },
                        {
                            "title": "Breaking Down the Science",
                            "content": "To understand the magnitude of this breakthrough, we need to examine the fundamental principles at work. {topic} operates through a complex network of {mechanisms} that interact in ways previously thought impossible. The traditional model suggested {old_understanding}, but the new evidence reveals {new_understanding}.\n\nThe research methodology employed {specific_techniques} to isolate and study {target_phenomenon}. Through {experimental_approach}, the team was able to demonstrate {key_evidence}. This evidence was corroborated by {validation_methods} and peer-reviewed by leading experts in {related_fields}.\n\nThe statistical significance of their findings is remarkable, with {statistical_data} showing {confidence_level} certainty. This level of precision eliminates any doubt about the validity of their conclusions and establishes a new foundation for future research in this area."
                        },
                        {
                            "title": "Real-World Applications",
                            "content": "The practical implications of this discovery are staggering. In the field of {application_field_1}, this could lead to {benefit_1}. Healthcare professionals are particularly excited about the potential for {medical_applications}, which could revolutionize treatment approaches for {conditions}.\n\nMoreover, the technology sector stands to benefit enormously from these findings. Companies working on {tech_applications} could see dramatic improvements in {performance_metrics}. Early prototypes based on these principles have already shown {promising_results}.\n\nEnvironmental scientists are also exploring how this discovery could contribute to {environmental_solutions}. The potential for {sustainability_benefits} represents a crucial step forward in addressing {global_challenges}."
                        },
                        {
                            "title": "The Path Forward",
                            "content": "As we stand on the brink of this scientific revolution, the research community is mobilizing to explore the full potential of these findings. Multiple institutions have announced {follow_up_studies} to investigate {specific_aspects}. The timeline for practical applications is estimated at {implementation_timeline}, with initial phases focusing on {priority_areas}.\n\nFunding agencies have already committed {investment_amount} to support continued research in this area. The collaborative effort involves {international_partnerships} and represents one of the largest scientific undertakings of the decade.\n\nFor the general public, the benefits will likely manifest as {public_benefits} within the next {timeframe}. This discovery exemplifies how fundamental research can lead to transformative changes that improve human life and our understanding of the world around us."
                        }
                    ],
                    "conclusion": "This groundbreaking discovery about {topic} represents more than just scientific advancement—it embodies humanity's relentless pursuit of knowledge and our capacity to challenge established paradigms. As researchers continue to explore the implications of these findings, we can expect a cascade of innovations that will reshape {affected_industries} and potentially solve some of our most pressing global challenges. The future has never looked more promising, and this discovery will undoubtedly be remembered as a pivotal moment in the history of {field} science."
                },
                "tr": {
                    "intro": "Bilim dünyasını sarsan çığır açan bir çalışmada, araştırmacılar {topic} hakkında {field} anlayışımızı temelden sorgulatan devrimci bulgular ortaya çıkardı. Prestijli bir bilim dergisinin son sayısında yayınlanan bu keşif, {application_area} yaklaşımımızı yeniden şekillendirme vaadiyle gelecek on yıllarda eşi görülmemiş atılımlara yol açabilir.",
                    "sections": [
                        {
                            "title": "Devrimci Keşif",
                            "content": "{institution}'da Dr. {researcher_name} liderliğindeki araştırma ekibi, {timeframe} boyunca {topic}'in karmaşık mekanizmalarını araştırdı. En son teknoloji {methodology} kullanarak, {main_finding} keşfettiler. Bu bulgu, alanı {time_period} boyunca domine eden yaygın kabul görmüş {old_theory} teorisiyle doğrudan çelişiyor.\n\nBu keşfi özellikle dikkat çekici kılan {unique_aspect}'tir. Etkiler akademik çevrelerin çok ötesine uzanıyor ve {real_world_applications} potansiyel olarak etkileyebilir. Araştırma {study_details} içeriyordu ve ölçümlerinde eşi görülmemiş hassasiyet elde etmek için {advanced_techniques} kullandı."
                        },
                        {
                            "title": "Bilimin Derinliklerine İniş",
                            "content": "Bu atılımın büyüklüğünü anlamak için, işleyen temel prensipleri incelememiz gerekiyor. {topic}, daha önce imkansız olduğu düşünülen şekillerde etkileşime giren karmaşık bir {mechanisms} ağı aracılığıyla çalışıyor. Geleneksel model {old_understanding} öneriyordu, ancak yeni kanıtlar {new_understanding} ortaya çıkarıyor.\n\nAraştırma metodolojisi {target_phenomenon}'u izole etmek ve incelemek için {specific_techniques} kullandı. {experimental_approach} aracılığıyla, ekip {key_evidence} gösterebilmeyi başardı. Bu kanıt {validation_methods} tarafından doğrulandı ve {related_fields} alanındaki önde gelen uzmanlar tarafından hakemlik yapıldı.\n\nBulgularının istatistiksel anlamlılığı dikkat çekici, {statistical_data} ile {confidence_level} kesinlik gösteriyor. Bu hassasiyet seviyesi sonuçlarının geçerliliği hakkındaki tüm şüpheleri ortadan kaldırıyor ve bu alandaki gelecekteki araştırmalar için yeni bir temel oluşturuyor."
                        },
                        {
                            "title": "Gerçek Dünya Uygulamaları",
                            "content": "Bu keşfin pratik sonuçları şaşırtıcı. {application_field_1} alanında, bu {benefit_1}'e yol açabilir. Sağlık profesyonelleri özellikle {medical_applications} potansiyeli konusunda heyecanlı, bu da {conditions} için tedavi yaklaşımlarını devrimleştirebilir.\n\nAyrıca, teknoloji sektörü bu bulgulardan muazzam fayda sağlayabilir. {tech_applications} üzerinde çalışan şirketler {performance_metrics}'te dramatik iyileştirmeler görebilir. Bu prensiplere dayanan erken prototipler zaten {promising_results} gösterdi.\n\nÇevre bilimcileri de bu keşfin {environmental_solutions}'a nasıl katkıda bulunabileceğini araştırıyor. {sustainability_benefits} potansiyeli, {global_challenges} ile başa çıkmada kritik bir adımı temsil ediyor."
                        },
                        {
                            "title": "İleriye Doğru Yol",
                            "content": "Bu bilimsel devrimin eşiğinde dururken, araştırma topluluğu bu bulguların tam potansiyelini keşfetmek için seferber oluyor. Birden fazla kurum {specific_aspects}'i araştırmak için {follow_up_studies} duyurdu. Pratik uygulamalar için zaman çizelgesi {implementation_timeline} olarak tahmin ediliyor, ilk aşamalar {priority_areas}'e odaklanıyor.\n\nFinansman ajansları bu alandaki devam eden araştırmaları desteklemek için zaten {investment_amount} taahhüt etti. İşbirlikçi çaba {international_partnerships} içeriyor ve on yılın en büyük bilimsel girişimlerinden birini temsil ediyor.\n\nGenel halk için faydalar muhtemelen önümüzdeki {timeframe} içinde {public_benefits} olarak kendini gösterecek. Bu keşif, temel araştırmanın insan yaşamını iyileştiren ve çevremizdeki dünya anlayışımızı geliştiren dönüştürücü değişikliklere nasıl yol açabileceğinin mükemmel bir örneğidir."
                        }
                    ],
                    "conclusion": "{topic} hakkındaki bu çığır açan keşif sadece bilimsel ilerlemeyi değil, insanlığın amansız bilgi arayışını ve yerleşik paradigmalara meydan okuma kapasitemizi temsil ediyor. Araştırmacılar bu bulguların etkilerini keşfetmeye devam ederken, {affected_industries}'i yeniden şekillendirecek ve en acil küresel zorluklarımızdan bazılarını potansiyel olarak çözecek bir yenilik kaskadı bekleyebiliriz. Gelecek hiç bu kadar umut verici görünmedi ve bu keşif şüphesiz {field} bilimi tarihinde çok önemli bir an olarak hatırlanacak."
                }
            }
        }

    def generate_long_content(self, category, language="en", min_words=800):
        """Generate comprehensive long-form content with minimum word count"""

        # Select topic and template
        topic_data = random.choice(self.advanced_topics[category])
        specific_topic = random.choice(self.topic_specifics[category])
        template_name = topic_data["template"]

        # Generate title
        title_template = topic_data[f"title_{language}"]
        title = title_template.format(topic=specific_topic)        # Get content template (fallback to discovery_deep_dive if template not found)
        template_name = topic_data["template"]
        if template_name not in self.content_templates:
            template_name = "discovery_deep_dive"
        template = self.content_templates[template_name][language]

        # Generate detailed content with placeholders filled
        content_vars = self.generate_content_variables(specific_topic, category)

        # Build full article
        intro = template["intro"].format(**content_vars)

        sections_content = []
        for section in template["sections"]:
            section_title = section["title"]
            section_content = section["content"].format(**content_vars)
            sections_content.append(f"## {section_title}\n\n{section_content}")

        conclusion = template["conclusion"].format(**content_vars)

        # Combine all content
        full_content = f"{intro}\n\n" + "\n\n".join(sections_content) + f"\n\n## Sonuç\n\n{conclusion}"

        # Ensure minimum word count
        word_count = len(full_content.split())
        if word_count < min_words:
            # Add more detailed sections if needed
            full_content = self.expand_content(full_content, min_words - word_count, language)

        return {
            "title": title,
            "content": full_content,
            "word_count": len(full_content.split()),
            "topic": specific_topic,
            "category": category
        }

    def generate_content_variables(self, topic, category):
        """Generate realistic variables for content templates"""

        researchers = ["Sarah Chen", "Marcus Rodriguez", "Elena Volkov", "James Patterson", "Aria Nakamura"]
        institutions = ["Stanford University", "MIT", "Oxford University", "Harvard Medical School", "CERN"]
        timeframes = ["three years", "five years", "eighteen months", "two decades"]

        return {
            "topic": topic,
            "field": category,
            "researcher_name": random.choice(researchers),
            "institution": random.choice(institutions),
            "timeframe": random.choice(timeframes),
            "application_area": f"{topic} applications",
            "main_finding": f"the traditional understanding of {topic} is fundamentally incomplete",
            "old_theory": f"classical {topic}",
            "time_period": "over 50 years",
            "unique_aspect": f"its potential to revolutionize {category}",
            "real_world_applications": f"medicine, technology, and environmental science",
            "study_details": "over 10,000 data points across multiple research centers",
            "advanced_techniques": "quantum sensors and AI-powered analysis",
            "mechanisms": f"{topic} pathways",
            "old_understanding": f"that {topic} follows predictable patterns",
            "new_understanding": f"that {topic} operates through quantum-level interactions",
            "specific_techniques": "advanced spectroscopy and machine learning algorithms",
            "target_phenomenon": f"the core {topic} processes",
            "experimental_approach": "controlled laboratory conditions",
            "key_evidence": f"measurable changes in {topic} behavior",
            "validation_methods": "independent replication studies",
            "related_fields": f"{category} and related disciplines",
            "statistical_data": "comprehensive statistical analysis",
            "confidence_level": "99.7%",
            "application_field_1": "medical research",
            "benefit_1": "revolutionary treatment options",
            "medical_applications": f"{topic}-based therapies",
            "conditions": f"conditions related to {topic}",
            "tech_applications": f"{topic} technology",
            "performance_metrics": "efficiency and accuracy",
            "promising_results": "remarkable improvements",
            "environmental_solutions": "sustainable technologies",
            "sustainability_benefits": f"eco-friendly {topic} applications",
            "global_challenges": "climate change and resource scarcity",
            "follow_up_studies": "comprehensive research programs",
            "specific_aspects": f"various {topic} mechanisms",
            "implementation_timeline": "5-10 years",
            "priority_areas": f"high-impact {topic} applications",
            "investment_amount": "$2.5 billion",
            "international_partnerships": "collaborations across 15 countries",
            "public_benefits": f"improved {topic}-related services",
            "affected_industries": f"{category} and technology sectors"
        }

    def expand_content(self, content, additional_words_needed, language):
        """Expand content to meet minimum word requirements"""

        expansion_sections = {
            "en": [
                "## Historical Context\n\nTo fully appreciate the significance of this breakthrough, we must examine the historical development of our understanding in this field. For decades, scientists have struggled with fundamental questions that seemed impossible to answer. The journey to this discovery began with early observations that didn't fit existing theoretical frameworks, leading researchers down a path of rigorous investigation that would ultimately reshape our entire perspective.",

                "## Technical Deep Dive\n\nThe technical aspects of this research involve sophisticated methodologies that push the boundaries of current scientific capabilities. Advanced computational models were employed to simulate complex interactions at the molecular level, while cutting-edge instrumentation provided unprecedented precision in measurements. The integration of artificial intelligence and machine learning algorithms enabled pattern recognition that would have been impossible through traditional analytical approaches.",

                "## Global Impact Assessment\n\nThe ramifications of this discovery extend far beyond the immediate scientific community. Economic analysts predict significant market disruptions as industries adapt to incorporate these new findings. Educational institutions are already revising curricula to include these groundbreaking concepts, ensuring that the next generation of scientists and professionals will be equipped with this revolutionary knowledge.",

                "## Future Research Directions\n\nThis discovery opens numerous avenues for future investigation. Research teams worldwide are developing proposals to explore specific aspects of these findings, with particular emphasis on practical applications that could benefit society. The collaborative nature of modern science ensures that progress will be rapid, with multiple institutions contributing expertise and resources to accelerate development."
            ],
            "tr": [
                "## Tarihsel Bağlam\n\nBu atılımın önemini tam olarak takdir etmek için, bu alandaki anlayışımızın tarihsel gelişimini incelememiz gerekiyor. On yıllardır bilim insanları, cevaplanması imkansız görünen temel sorularla boğuştu. Bu keşfe giden yolculuk, mevcut teorik çerçevelere uymayan erken gözlemlerle başladı ve araştırmacıları, sonuçta tüm perspektifimizi yeniden şekillendirecek titiz bir araştırma yoluna yönlendirdi.",

                "## Teknik Derinlemesine İnceleme\n\nBu araştırmanın teknik yönleri, mevcut bilimsel yeteneklerin sınırlarını zorlayan sofistike metodolojileri içeriyor. Moleküler düzeyde karmaşık etkileşimleri simüle etmek için gelişmiş hesaplama modelleri kullanıldı, en son enstrümantasyon ise ölçümlerde eşi görülmemiş hassasiyet sağladı. Yapay zeka ve makine öğrenmesi algoritmalarının entegrasyonu, geleneksel analitik yaklaşımlarla imkansız olan kalıp tanıma olanağı sağladı.",

                "## Küresel Etki Değerlendirmesi\n\nBu keşfin yansımaları, yakın bilim topluluğunun çok ötesine uzanıyor. Ekonomik analistler, endüstriler bu yeni bulguları dahil etmek için adapte olurken önemli pazar bozulmaları öngörüyor. Eğitim kurumları zaten bu çığır açan kavramları içerecek şekilde müfredatlarını revize ediyor, böylece gelecek nesil bilim insanları ve profesyonellerin bu devrimci bilgiyle donatılmasını sağlıyor.",

                "## Gelecekteki Araştırma Yönleri\n\nBu keşif, gelecek araştırmalar için sayısız yol açıyor. Dünya çapındaki araştırma ekipleri, bu bulguların belirli yönlerini keşfetmek için öneriler geliştiriyor, özellikle topluma fayda sağlayabilecek pratik uygulamalara vurgu yapıyor. Modern bilimin işbirlikçi doğası, ilerlemenin hızlı olacağını, birden fazla kurumun gelişimi hızlandırmak için uzmanlık ve kaynak katkısında bulunacağını garanti ediyor."
            ]
        }

        # Add expansion sections until word count is met
        sections_to_add = expansion_sections[language]
        for section in sections_to_add:
            if len(content.split()) >= self.min_words:
                break
            content += f"\n\n{section}"

        return content

    def create_article_file(self, article_data, language):
        """Create markdown file for the article"""

        # Generate unique filename
        date_str = datetime.now().strftime("%Y-%m-%d")
        title_hash = hashlib.md5(article_data["title"].encode()).hexdigest()[:8]
        filename = f"enhanced-{date_str}-{title_hash}.md"

        # Create directory if it doesn't exist
        lang_dir = self.content_dir / language
        lang_dir.mkdir(parents=True, exist_ok=True)

        # Generate frontmatter
        frontmatter = f"""---
title: "{article_data['title']}"
description: "Comprehensive analysis of {article_data['topic']} with latest scientific findings and practical applications."
date: "{date_str}"
language: "{language}"
category: "{article_data['category']}"
image: "{article_data['category']}_enhanced"
tags: ["{article_data['topic']}", "{article_data['category']}", "science", "research", "breakthrough"]
readingTime: "{max(5, article_data['word_count'] // 200)} min read"
wordCount: {article_data['word_count']}
author: "MindPulse Research Team"
seo:
  canonical: "https://mindpulse-daily.vercel.app/{language}/posts/{filename.replace('.md', '')}"
  robots: "index, follow"
  schema: "Article"
---"""

        # Write file
        file_path = lang_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter + "\n\n" + article_data['content'])

        print(f"✅ Created enhanced article: {filename} ({article_data['word_count']} words)")
        return file_path

    def scheduled_content_generation(self):
        """Generate daily content at 16:05 Turkey time"""

        print(f"🚀 Starting scheduled content generation at {datetime.now()}")

        # Generate one English and one Turkish article daily
        categories = ["science", "technology", "psychology", "space"]
        selected_category = random.choice(categories)

        # Generate English article
        en_article = self.generate_long_content(selected_category, "en", self.min_words)
        en_file = self.create_article_file(en_article, "en")

        # Generate Turkish article
        tr_article = self.generate_long_content(selected_category, "tr", self.min_words)
        tr_file = self.create_article_file(tr_article, "tr")

        print(f"📝 Daily content generated successfully!")
        print(f"🇺🇸 English: {en_file} ({en_article['word_count']} words)")
        print(f"🇹🇷 Turkish: {tr_file} ({tr_article['word_count']} words)")

        return [en_file, tr_file]

    def update_all_short_articles(self):
        """Update all existing short articles to meet minimum word requirements"""

        print("🔄 Scanning for short articles to update...")

        updated_count = 0
        for lang in ["en", "tr"]:
            lang_dir = self.content_dir / lang
            if not lang_dir.exists():
                continue

            for file_path in lang_dir.glob("hybrid-*.md"):
                # Read existing file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Count words in content (excluding frontmatter)
                content_parts = content.split('---', 2)
                if len(content_parts) >= 3:
                    article_content = content_parts[2].strip()
                    word_count = len(article_content.split())

                    if word_count < self.min_words:
                        print(f"📝 Updating short article: {file_path.name} ({word_count} words -> {self.min_words}+ words)")

                        # Extract category from frontmatter
                        frontmatter = content_parts[1]
                        category = "science"  # default
                        for line in frontmatter.split('\n'):
                            if 'category:' in line:
                                category = line.split(':')[1].strip().strip('"')
                                break

                        # Generate new enhanced content
                        new_article = self.generate_long_content(category, lang, self.min_words)

                        # Keep original frontmatter but update content
                        new_content = f"---{frontmatter}---\n\n{new_article['content']}"

                        # Write back to file
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)

                        updated_count += 1

        print(f"✅ Updated {updated_count} short articles to meet minimum word requirements")
        return updated_count

def main():
    """Main function to run content generation"""

    generator = AdvancedContentGenerator()

    # First, update all existing short articles
    print("🔧 Phase 1: Updating existing short articles...")
    generator.update_all_short_articles()

    # Generate immediate sample content
    print("\n🚀 Phase 2: Generating sample enhanced content...")
    sample_en = generator.generate_long_content("science", "en")
    sample_tr = generator.generate_long_content("technology", "tr")

    generator.create_article_file(sample_en, "en")
    generator.create_article_file(sample_tr, "tr")

    # Setup scheduled generation for 16:05 Turkey time
    print("\n⏰ Phase 3: Setting up daily scheduled generation...")
    schedule.every().day.at("16:05").do(generator.scheduled_content_generation)

    print("✅ Advanced content generator setup complete!")
    print("📅 Daily generation scheduled for 16:05 Turkey time")
    print(f"📊 Minimum words per article: {generator.min_words}")

    # Keep the scheduler running
    print("🔄 Content generator is now running... (Press Ctrl+C to stop)")
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        print("\n👋 Content generator stopped.")

if __name__ == "__main__":
    main()
