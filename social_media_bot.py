#!/usr/bin/env python3
"""
🚀 MindPulse Daily - Social Media Automation Bot
Auto-posts new content to Twitter, LinkedIn, and other platforms
"""

import os
import json
import requests
from datetime import datetime
from pathlib import Path
import tweepy
import hashlib

class SocialMediaBot:
    def __init__(self):
        self.twitter_api = self.setup_twitter()
        self.webhook_urls = {
            'discord': os.getenv('DISCORD_WEBHOOK_URL'),
            'slack': os.getenv('SLACK_WEBHOOK_URL'),
        }

    def setup_twitter(self):
        """Setup Twitter API v2 client"""
        try:
            api_key = os.getenv('TWITTER_API_KEY')
            api_secret = os.getenv('TWITTER_API_SECRET')
            access_token = os.getenv('TWITTER_ACCESS_TOKEN')
            access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
            bearer_token = os.getenv('TWITTER_BEARER_TOKEN')

            if all([api_key, api_secret, access_token, access_token_secret]):
                client = tweepy.Client(
                    bearer_token=bearer_token,
                    consumer_key=api_key,
                    consumer_secret=api_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret,
                    wait_on_rate_limit=True
                )
                return client
        except Exception as e:
            print(f"⚠️ Twitter API setup failed: {e}")
        return None

    def get_latest_posts(self):
        """Get the latest generated posts"""
        posts = []

        # Check English posts
        en_dir = Path("src/content/posts/en")
        tr_dir = Path("src/content/posts/tr")

        today = datetime.now().strftime("%Y-%m-%d")

        for post_dir, lang in [(en_dir, "en"), (tr_dir, "tr")]:
            if post_dir.exists():
                for post_file in post_dir.glob(f"viral-{today}-*.md"):
                    content = post_file.read_text(encoding='utf-8')
                    # Extract frontmatter
                    if content.startswith('---'):
                        parts = content.split('---', 2)
                        if len(parts) >= 3:
                            frontmatter = parts[1].strip()
                            title = ""
                            description = ""
                            for line in frontmatter.split('\n'):
                                if line.startswith('title:'):
                                    title = line.split('title:', 1)[1].strip().strip('"')
                                elif line.startswith('description:'):
                                    description = line.split('description:', 1)[1].strip().strip('"')

                            if title and description:
                                posts.append({
                                    'title': title,
                                    'description': description,
                                    'file': post_file.name,
                                    'language': lang,
                                    'url': f"https://mindpulse-daily.vercel.app/{'tr/' if lang == 'tr' else ''}posts/{post_file.stem}"
                                })

        return posts

    def create_social_media_posts(self, post_data):
        """Create optimized social media content"""
        title = post_data['title']
        description = post_data['description']
        url = post_data['url']
        lang = post_data['language']

        # Viral templates based on language
        if lang == 'en':
            templates = [
                f"🧠 MIND-BLOWN: {title}\n\n{description}\n\nThis will change how you think! 🤯\n\n{url}\n\n#MindPulse #Science #Psychology #Learning",
                f"🔥 VIRAL DISCOVERY: {title}\n\n{description}\n\nYou won't believe what scientists found! 🚀\n\n{url}\n\n#Viral #Knowledge #MindBlown #Facts",
                f"💡 SHOCKING TRUTH: {title}\n\n{description}\n\nEveryone needs to know this! 📚\n\n{url}\n\n#Education #ScienceFacts #TrendingNow",
            ]
        else:  # Turkish
            templates = [
                f"🧠 AKLIN DURACAK: {title}\n\n{description}\n\nBu düşüncelerinizi değiştirecek! 🤯\n\n{url}\n\n#MindPulse #Bilim #Psikoloji #Öğrenme",
                f"🔥 VİRAL KEŞİF: {title}\n\n{description}\n\nBilim insanlarının bulduklarına inanamayacaksınız! 🚀\n\n{url}\n\n#Viral #Bilgi #AklınDursun #Gerçekler",
                f"💡 ŞAŞIRTICI GERÇEK: {title}\n\n{description}\n\nHerkesin bilmesi gereken! 📚\n\n{url}\n\n#Eğitim #BilimGerçekleri #Trend",
            ]

        # Select template based on content hash for consistency
        template_index = int(hashlib.md5(title.encode()).hexdigest(), 16) % len(templates)
        return templates[template_index]

    def post_to_twitter(self, content):
        """Post content to Twitter"""
        if not self.twitter_api:
            print("⚠️ Twitter API not configured")
            return False

        try:
            # Split content if too long for Twitter
            if len(content) > 280:
                content = content[:277] + "..."

            response = self.twitter_api.create_tweet(text=content)
            print(f"✅ Posted to Twitter: {response.data['id']}")
            return True
        except Exception as e:
            print(f"❌ Twitter post failed: {e}")
            return False

    def post_to_discord(self, content, url):
        """Post content to Discord via webhook"""
        webhook_url = self.webhook_urls.get('discord')
        if not webhook_url:
            print("⚠️ Discord webhook not configured")
            return False

        try:
            data = {
                "content": content,
                "embeds": [{
                    "title": "🧠 New MindPulse Daily Article",
                    "description": content[:500] + ("..." if len(content) > 500 else ""),
                    "url": url,
                    "color": 0x9333ea,
                    "footer": {"text": "MindPulse Daily - Daily Knowledge Drops"}
                }]
            }

            response = requests.post(webhook_url, json=data)
            if response.status_code == 204:
                print("✅ Posted to Discord")
                return True
        except Exception as e:
            print(f"❌ Discord post failed: {e}")
        return False

    def post_to_slack(self, content, url):
        """Post content to Slack via webhook"""
        webhook_url = self.webhook_urls.get('slack')
        if not webhook_url:
            print("⚠️ Slack webhook not configured")
            return False

        try:
            data = {
                "text": f"🧠 New MindPulse Daily Article",
                "attachments": [{
                    "color": "#9333ea",
                    "title": "Check out our latest viral content!",
                    "text": content[:500] + ("..." if len(content) > 500 else ""),
                    "title_link": url,
                    "footer": "MindPulse Daily",
                    "footer_icon": "https://mindpulse-daily.vercel.app/favicon.svg"
                }]
            }

            response = requests.post(webhook_url, json=data)
            if response.status_code == 200:
                print("✅ Posted to Slack")
                return True
        except Exception as e:
            print(f"❌ Slack post failed: {e}")
        return False

    def run_automation(self):
        """Main automation function"""
        print("🚀 Starting social media automation...")

        # Get latest posts
        posts = self.get_latest_posts()

        if not posts:
            print("📝 No new posts found for today")
            return

        print(f"📚 Found {len(posts)} new posts to promote")

        success_count = 0
        for post in posts:
            print(f"\n📢 Promoting: {post['title']} ({post['language'].upper()})")

            # Create social media content
            social_content = self.create_social_media_posts(post)

            # Post to platforms
            platforms_posted = 0

            # Twitter
            if self.post_to_twitter(social_content):
                platforms_posted += 1

            # Discord
            if self.post_to_discord(social_content, post['url']):
                platforms_posted += 1

            # Slack
            if self.post_to_slack(social_content, post['url']):
                platforms_posted += 1

            if platforms_posted > 0:
                success_count += 1
                print(f"✅ Successfully promoted to {platforms_posted} platforms")
            else:
                print("❌ Failed to promote on any platform")

        print(f"\n🎉 Automation complete! Successfully promoted {success_count}/{len(posts)} posts")

if __name__ == "__main__":
    bot = SocialMediaBot()
    bot.run_automation()
