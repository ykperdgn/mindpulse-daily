#!/usr/bin/env python3
"""
🔍 MindPulse Daily - SEO Analytics & Optimization Bot
Analyzes content performance and optimizes for search engines
"""

import os
import json
import requests
from datetime import datetime, timedelta
from pathlib import Path
import xml.etree.ElementTree as ET
from collections import defaultdict

class SEOOptimizer:
    def __init__(self):
        self.base_url = "https://mindpulse-daily.vercel.app"
        self.analytics_data = {}
        
    def generate_sitemap(self):
        """Generate XML sitemap for better SEO"""
        print("🗺️ Generating SEO sitemap...")
        
        # Create sitemap root
        urlset = ET.Element("urlset")
        urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
        urlset.set("xmlns:news", "http://www.google.com/schemas/sitemap-news/0.9")
        urlset.set("xmlns:xhtml", "http://www.w3.org/1999/xhtml")
        
        # Add homepage
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = self.base_url
        ET.SubElement(url, "changefreq").text = "daily"
        ET.SubElement(url, "priority").text = "1.0"
        ET.SubElement(url, "lastmod").text = datetime.now().strftime("%Y-%m-%d")
        
        # Add Turkish homepage
        url_tr = ET.SubElement(urlset, "url")
        ET.SubElement(url_tr, "loc").text = f"{self.base_url}/tr"
        ET.SubElement(url_tr, "changefreq").text = "daily"
        ET.SubElement(url_tr, "priority").text = "1.0"
        ET.SubElement(url_tr, "lastmod").text = datetime.now().strftime("%Y-%m-%d")
        
        # Add hreflang links for homepage
        hreflang_en = ET.SubElement(url, "xhtml:link")
        hreflang_en.set("rel", "alternate")
        hreflang_en.set("hreflang", "en")
        hreflang_en.set("href", self.base_url)
        
        hreflang_tr = ET.SubElement(url, "xhtml:link")
        hreflang_tr.set("rel", "alternate") 
        hreflang_tr.set("hreflang", "tr")
        hreflang_tr.set("href", f"{self.base_url}/tr")
        
        # Add English posts
        en_dir = Path("src/content/posts/en")
        if en_dir.exists():
            for post_file in en_dir.glob("*.md"):
                url = ET.SubElement(urlset, "url")
                slug = post_file.stem
                ET.SubElement(url, "loc").text = f"{self.base_url}/posts/{slug}"
                ET.SubElement(url, "changefreq").text = "weekly"
                ET.SubElement(url, "priority").text = "0.8"
                
                # Get file modification date
                mod_time = datetime.fromtimestamp(post_file.stat().st_mtime)
                ET.SubElement(url, "lastmod").text = mod_time.strftime("%Y-%m-%d")
                
                # Add hreflang if Turkish version exists
                tr_file = Path(f"src/content/posts/tr/{slug}.md")
                if tr_file.exists():
                    hreflang_en = ET.SubElement(url, "xhtml:link")
                    hreflang_en.set("rel", "alternate")
                    hreflang_en.set("hreflang", "en")
                    hreflang_en.set("href", f"{self.base_url}/posts/{slug}")
                    
                    hreflang_tr = ET.SubElement(url, "xhtml:link")
                    hreflang_tr.set("rel", "alternate")
                    hreflang_tr.set("hreflang", "tr")
                    hreflang_tr.set("href", f"{self.base_url}/tr/posts/{slug}")
        
        # Add Turkish posts
        tr_dir = Path("src/content/posts/tr")
        if tr_dir.exists():
            for post_file in tr_dir.glob("*.md"):
                url = ET.SubElement(urlset, "url")
                slug = post_file.stem
                ET.SubElement(url, "loc").text = f"{self.base_url}/tr/posts/{slug}"
                ET.SubElement(url, "changefreq").text = "weekly"
                ET.SubElement(url, "priority").text = "0.8"
                
                mod_time = datetime.fromtimestamp(post_file.stat().st_mtime)
                ET.SubElement(url, "lastmod").text = mod_time.strftime("%Y-%m-%d")
                
                # Check if this is a recent post for news sitemap
                if mod_time > datetime.now() - timedelta(days=2):
                    news = ET.SubElement(url, "news:news")
                    publication = ET.SubElement(news, "news:publication")
                    ET.SubElement(publication, "news:name").text = "MindPulse Daily"
                    ET.SubElement(publication, "news:language").text = "tr"
                    
                    news_article = ET.SubElement(news, "news:publication_date")
                    news_article.text = mod_time.strftime("%Y-%m-%d")
                    
                    # Extract title from frontmatter
                    content = post_file.read_text(encoding='utf-8')
                    if content.startswith('---'):
                        parts = content.split('---', 2)
                        if len(parts) >= 3:
                            frontmatter = parts[1].strip()
                            for line in frontmatter.split('\n'):
                                if line.startswith('title:'):
                                    title = line.split('title:', 1)[1].strip().strip('"')
                                    ET.SubElement(news, "news:title").text = title
                                    break
        
        # Write sitemap
        tree = ET.ElementTree(urlset)
        ET.indent(tree, space="  ", level=0)
        tree.write("public/sitemap.xml", encoding="utf-8", xml_declaration=True)
        print("✅ Sitemap generated: public/sitemap.xml")
        
    def generate_robots_txt(self):
        """Generate robots.txt for SEO"""
        robots_content = f"""User-agent: *
Allow: /

# Sitemaps
Sitemap: {self.base_url}/sitemap.xml

# Crawl-delay for respectful crawling
Crawl-delay: 1

# Allow all content for search engines
Allow: /posts/
Allow: /tr/
Allow: /tr/posts/

# Disallow admin or private areas (if any)
Disallow: /admin/
Disallow: /_astro/
Disallow: /api/

# Cache policy
Cache-delay: 86400
"""
        
        with open("public/robots.txt", "w", encoding="utf-8") as f:
            f.write(robots_content)
        print("✅ Robots.txt generated: public/robots.txt")
    
    def analyze_content_performance(self):
        """Analyze content for SEO performance"""
        print("📊 Analyzing content performance...")
        
        performance_data = {
            "total_posts": 0,
            "languages": {"en": 0, "tr": 0},
            "categories": defaultdict(int),
            "recent_posts": [],
            "top_keywords": defaultdict(int),
            "seo_scores": []
        }
        
        # Analyze English posts
        en_dir = Path("src/content/posts/en")
        if en_dir.exists():
            for post_file in en_dir.glob("*.md"):
                performance_data["total_posts"] += 1
                performance_data["languages"]["en"] += 1
                
                content = post_file.read_text(encoding='utf-8')
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        frontmatter = parts[1].strip()
                        post_content = parts[2].strip()
                        
                        # Extract metadata
                        title = ""
                        category = ""
                        date = ""
                        
                        for line in frontmatter.split('\n'):
                            if line.startswith('title:'):
                                title = line.split('title:', 1)[1].strip().strip('"')
                            elif line.startswith('category:'):
                                category = line.split('category:', 1)[1].strip().strip('"')
                                performance_data["categories"][category] += 1
                            elif line.startswith('date:'):
                                date = line.split('date:', 1)[1].strip().strip('"')
                        
                        # Check if recent
                        try:
                            post_date = datetime.strptime(date, "%Y-%m-%d")
                            if post_date > datetime.now() - timedelta(days=7):
                                performance_data["recent_posts"].append({
                                    "title": title,
                                    "file": post_file.name,
                                    "date": date,
                                    "language": "en"
                                })
                        except:
                            pass
                        
                        # Basic SEO score calculation
                        seo_score = self.calculate_seo_score(title, post_content)
                        performance_data["seo_scores"].append({
                            "file": post_file.name,
                            "title": title,
                            "score": seo_score,
                            "language": "en"
                        })
        
        # Analyze Turkish posts
        tr_dir = Path("src/content/posts/tr")
        if tr_dir.exists():
            for post_file in tr_dir.glob("*.md"):
                performance_data["total_posts"] += 1
                performance_data["languages"]["tr"] += 1
                
                content = post_file.read_text(encoding='utf-8')
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        frontmatter = parts[1].strip()
                        post_content = parts[2].strip()
                        
                        title = ""
                        category = ""
                        date = ""
                        
                        for line in frontmatter.split('\n'):
                            if line.startswith('title:'):
                                title = line.split('title:', 1)[1].strip().strip('"')
                            elif line.startswith('category:'):
                                category = line.split('category:', 1)[1].strip().strip('"')
                                performance_data["categories"][category] += 1
                            elif line.startswith('date:'):
                                date = line.split('date:', 1)[1].strip().strip('"')
                        
                        try:
                            post_date = datetime.strptime(date, "%Y-%m-%d")
                            if post_date > datetime.now() - timedelta(days=7):
                                performance_data["recent_posts"].append({
                                    "title": title,
                                    "file": post_file.name,
                                    "date": date,
                                    "language": "tr"
                                })
                        except:
                            pass
                        
                        seo_score = self.calculate_seo_score(title, post_content)
                        performance_data["seo_scores"].append({
                            "file": post_file.name,
                            "title": title,
                            "score": seo_score,
                            "language": "tr"
                        })
        
        # Save performance data
        with open("seo_analytics.json", "w", encoding="utf-8") as f:
            json.dump(performance_data, f, indent=2, ensure_ascii=False)
        
        # Print summary
        print(f"📈 Content Analysis Complete:")
        print(f"   Total Posts: {performance_data['total_posts']}")
        print(f"   English: {performance_data['languages']['en']}")
        print(f"   Turkish: {performance_data['languages']['tr']}")
        print(f"   Recent Posts (7 days): {len(performance_data['recent_posts'])}")
        print(f"   Top Categories: {dict(performance_data['categories'])}")
        
        # Find top and bottom performing posts
        sorted_scores = sorted(performance_data["seo_scores"], key=lambda x: x["score"], reverse=True)
        if sorted_scores:
            print(f"   Best SEO Score: {sorted_scores[0]['title']} ({sorted_scores[0]['score']:.1f}/100)")
            print(f"   Needs Improvement: {sorted_scores[-1]['title']} ({sorted_scores[-1]['score']:.1f}/100)")
    
    def calculate_seo_score(self, title, content):
        """Calculate basic SEO score for content"""
        score = 0
        
        # Title optimization (30 points)
        if title:
            if 30 <= len(title) <= 60:
                score += 15
            elif len(title) > 0:
                score += 5
                
            # Viral keywords in title
            viral_keywords = ["hidden", "shocking", "secret", "amazing", "mind-blowing", "surprising"]
            if any(keyword in title.lower() for keyword in viral_keywords):
                score += 15
        
        # Content length (25 points)
        word_count = len(content.split())
        if word_count >= 500:
            score += 25
        elif word_count >= 300:
            score += 15
        elif word_count >= 200:
            score += 10
        
        # Headers and structure (20 points)
        if "##" in content:
            score += 10
        if "###" in content:
            score += 5
        if content.count("##") >= 3:
            score += 5
        
        # Engagement elements (15 points)
        if "?" in content:
            score += 5
        if any(emoji in content for emoji in ["🧠", "🔍", "💡", "🚀", "🤔", "🌟"]):
            score += 5
        if "Discussion Questions" in content or "🤔" in content:
            score += 5
        
        # Lists and formatting (10 points)
        if "-" in content or "*" in content:
            score += 5
        if content.count("\n") >= 10:
            score += 5
        
        return min(score, 100)
    
    def generate_schema_markup(self):
        """Generate Schema.org structured data"""
        print("🏷️ Generating Schema.org markup...")
        
        # Organization schema
        organization_schema = {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": "MindPulse Daily",
            "url": self.base_url,
            "logo": f"{self.base_url}/favicon.svg",
            "description": "Daily knowledge drops about science, psychology, space, history, and nature",
            "foundingDate": "2025",
            "sameAs": [
                "https://twitter.com/mindpulsedaily",
                "https://facebook.com/mindpulsedaily"
            ],
            "contactPoint": {
                "@type": "ContactPoint",
                "contactType": "customer service",
                "availableLanguage": ["English", "Turkish"]
            }
        }
        
        # Website schema
        website_schema = {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": "MindPulse Daily",
            "url": self.base_url,
            "description": "Discover fascinating insights about science, psychology, space, history, and nature. Fresh knowledge delivered daily.",
            "inLanguage": ["en", "tr"],
            "potentialAction": {
                "@type": "SearchAction",
                "target": f"{self.base_url}/search?q={{search_term_string}}",
                "query-input": "required name=search_term_string"
            }
        }
        
        # Save schemas
        with open("public/schema-organization.json", "w") as f:
            json.dump(organization_schema, f, indent=2)
            
        with open("public/schema-website.json", "w") as f:
            json.dump(website_schema, f, indent=2)
        
        print("✅ Schema markup generated")
    
    def run_seo_optimization(self):
        """Run complete SEO optimization"""
        print("🚀 Starting SEO optimization...")
        
        self.generate_sitemap()
        self.generate_robots_txt()
        self.analyze_content_performance()
        self.generate_schema_markup()
        
        print("🎉 SEO optimization complete!")
        print(f"📊 Check seo_analytics.json for detailed performance data")

if __name__ == "__main__":
    optimizer = SEOOptimizer()
    optimizer.run_seo_optimization()
