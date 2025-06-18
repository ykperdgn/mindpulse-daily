# 🧠 MindPulse Daily

**Daily Knowledge Drops**

MindPulse Daily is an automated blog platform that delivers fascinating insights about science, psychology, space exploration, history, and nature every day. Built with Astro and featuring automated content generation.

## ✨ Features

- 📚 **Automated Content Generation** - Daily articles covering diverse fascinating topics
- 🌍 **Multilingual Support** - English and Turkish content
- ⚡ **Fast & SEO-friendly** - Built with Astro for optimal performance
- 🎨 **Modern Design** - Beautiful, responsive UI with TailwindCSS
- 📱 **Mobile-first** - Optimized for all devices
- 🔄 **GitHub Actions** - Automated daily content generation and deployment

## 🎯 Content Topics

Our daily knowledge drops cover:
- 🚀 Space exploration and astronomy
- 🌊 Ocean mysteries and marine life
- 🧠 Human psychology and brain science
- 🏛️ Ancient civilizations and history
- 🦋 Wildlife behavior and nature
- 🔬 Scientific discoveries
- ❓ Unusual phenomena and mysteries

## 🚀 Project Structure

```
mindpulse-daily/
├── src/
│   ├── content/
│   │   ├── config.ts
│   │   └── posts/
│   │       ├── en/          # English articles
│   │       └── tr/          # Turkish articles
│   ├── layouts/
│   │   └── Layout.astro     # Main layout
│   ├── pages/
│   │   ├── index.astro      # English homepage
│   │   ├── tr.astro         # Turkish homepage
│   │   ├── posts/[slug].astro    # English article pages
│   │   └── tr/posts/[slug].astro # Turkish article pages
│   └── styles/
│       └── global.css       # Global styles with TailwindCSS
├── .github/workflows/
│   └── generate-and-deploy.yml  # Automated content generation
├── generate_content.py      # Content generation script
└── test_content.py         # Manual content testing script
```

## 🛠️ Getting Started

### Prerequisites

- Node.js 18+
- npm or yarn
- OpenAI API key (for content generation)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ykperdgn/mindpulse-daily.git
cd mindpulse-daily
```

2. Install dependencies:
```bash
npm install
```

3. Set up environment variables:
```bash
# For Windows PowerShell
$env:OPENAI_API_KEY="your-openai-api-key-here"

# For Linux/Mac
export OPENAI_API_KEY="your-openai-api-key-here"
```

4. Start development server:
```bash
npm run dev
```

5. Build for production:
```bash
npm run build
```

## 🤖 Content Generation

### Manual Content Generation

To manually generate test content:

```bash
python test_content.py
```

### Automated Content Generation

The project includes GitHub Actions that automatically:
- Generate 3 new articles daily at 7:00 AM UTC
- Commit and push changes to the repository
- Deploy to your hosting platform

To set up automation:
1. Add `OPENAI_API_KEY` to your GitHub repository secrets
2. The workflow will run automatically on schedule

## 🌐 Deployment

### Vercel (Recommended)

1. Connect your GitHub repository to Vercel
2. Set build command: `npm run build`
3. Set output directory: `dist`
4. Deploy!

### Netlify

1. Connect your GitHub repository to Netlify
2. Set build command: `npm run build`
3. Set publish directory: `dist`
4. Deploy!

### GitHub Pages

1. Enable GitHub Pages in repository settings
2. The included GitHub Action will build and deploy automatically

## 📈 Monetization Ready

The site is optimized for:
- **Google AdSense** - Clean, ad-friendly layout
- **Affiliate Marketing** - Easy link integration
- **Newsletter Signups** - Built-in subscription CTAs
- **SEO** - Optimized meta tags and structure

## 🔧 Customization

### Adding New Languages

1. Create new folder in `src/content/posts/` (e.g., `fr/` for French)
2. Update `src/content/config.ts` to include new language
3. Create new homepage in `src/pages/` (e.g., `fr.astro`)
4. Add new dynamic route in `src/pages/fr/posts/[slug].astro`

### Modifying Content Generation

Edit `generate_content.py` to:
- Change content topics
- Adjust article length
- Modify publishing frequency
- Add custom prompts

## 📊 Analytics & SEO

- **Built-in SEO** - Meta tags, OpenGraph, structured data
- **Fast Loading** - Astro's static site generation
- **Mobile Optimized** - Responsive design
- **Analytics Ready** - Easy Google Analytics integration

## 🎨 Design Features

- **Modern UI** - Clean, professional design
- **Dark/Light Themes** - Customizable color schemes
- **Typography** - Optimized reading experience
- **Responsive Grid** - Works on all screen sizes
- **Smooth Animations** - Subtle hover effects and transitions

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you have any questions or need help setting up the project, please open an issue or contact the maintainer.

---

**Happy Learning! 🧠✨**

## 🚀 Project Structure

```text
mindpulse-daily/
├── src/
│   ├── content/
│   │   ├── config.ts
│   │   └── posts/
│   │       ├── en/          # English articles
│   │       └── tr/          # Turkish articles
│   ├── layouts/
│   │   └── Layout.astro     # Main layout
│   ├── pages/
│   │   ├── index.astro      # English homepage
│   │   ├── tr.astro         # Turkish homepage
│   │   ├── posts/[slug].astro    # English article pages
│   │   └── tr/posts/[slug].astro # Turkish article pages
│   └── styles/
│       └── global.css       # TailwindCSS + custom styles
├── generate_content.py      # AI content generation script
└── .github/workflows/       # GitHub Actions automation
```

## 🧞 Commands

| Command | Action |
|:--------|:-------|
| `npm install` | Install dependencies |
| `npm run dev` | Start local dev server at `localhost:4321` |
| `npm run build` | Build production site to `./dist/` |
| `npm run preview` | Preview build locally |
| `python generate_content.py` | Generate new AI content (requires OPENAI_API_KEY) |

## 🔧 Setup & Deployment

### 1. Local Development
```bash
npm install
npm run dev
```

### 2. Environment Variables
Set your OpenAI API key:
```bash
export OPENAI_API_KEY=your_api_key_here
```

### 3. Deploy to Vercel
1. Push to GitHub
2. Connect repository to Vercel
3. Add `OPENAI_API_KEY` to Vercel environment variables
4. Deploy automatically

### 4. Automated Content Generation
The GitHub Action runs daily at 7:00 AM UTC to generate new content automatically.

## 💰 Monetization Ready

- Google AdSense compatible structure
- SEO optimized for organic traffic
- Newsletter signup integration ready
- Social media sharing features

## 📈 Live Site

Visit: [Your Vercel URL]

---

Built with ❤️ using Astro, TailwindCSS, and OpenAI
