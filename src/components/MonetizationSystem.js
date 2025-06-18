// Advanced Monetization System - Multiple Revenue Streams
class MonetizationSystem {
  constructor() {
    this.config = {
      adsense: {
        publisherId: 'ca-pub-XXXXXXXXXXXXXXXXX', // Replace with actual ID
        adUnits: {
          header: 'XXXXXXXXXX',
          sidebar: 'XXXXXXXXXX',
          inArticle: 'XXXXXXXXXX',
          footer: 'XXXXXXXXXX'
        },
        autoAds: true
      },
      affiliate: {
        programs: {
          amazon: 'mindpulse-20', // Replace with actual affiliate tag
          audible: 'mindpulse-audible',
          coursera: 'mindpulse-coursera',
          masterclass: 'mindpulse-mc'
        },
        disclosureText: 'This post contains affiliate links. We may earn a commission if you make a purchase.'
      },
      premium: {
        enabled: true,
        price: 4.99,
        currency: 'USD',
        features: [
          'Ad-free reading experience',
          'Early access to new content',
          'Exclusive deep-dive articles',
          'Weekly video explanations',
          'Direct access to researchers',
          'Downloadable fact sheets'
        ]
      },
      donations: {
        enabled: true,
        buyMeCoffeeUrl: 'https://www.buymeacoffee.com/mindpulsedaily',
        patreonUrl: 'https://www.patreon.com/mindpulsedaily',
        suggestedAmounts: [3, 5, 10, 25]
      }
    };

    this.analytics = {
      adRevenue: 0,
      affiliateRevenue: 0,
      premiumRevenue: 0,
      donationRevenue: 0,
      adClicks: 0,
      affiliateClicks: 0
    };

    this.init();
  }

  init() {
    this.loadAnalytics();
    this.setupAdSense();
    this.setupAffiliateTracking();
    this.setupPremiumFeatures();
    this.setupDonationButtons();
    this.setupRevenueTracking();
    this.createMonetizationWidgets();
  }

  loadAnalytics() {
    try {
      const saved = localStorage.getItem('mindpulse_monetization_analytics');
      if (saved) {
        this.analytics = { ...this.analytics, ...JSON.parse(saved) };
      }
    } catch (e) {
      console.warn('Failed to load monetization analytics:', e);
    }
  }

  saveAnalytics() {
    localStorage.setItem('mindpulse_monetization_analytics', JSON.stringify(this.analytics));
  }

  setupAdSense() {
    if (!this.config.adsense.publisherId.includes('XXXX')) {
      // Load Google AdSense
      const adsenseScript = document.createElement('script');
      adsenseScript.async = true;
      adsenseScript.src = `https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${this.config.adsense.publisherId}`;
      adsenseScript.crossOrigin = 'anonymous';
      document.head.appendChild(adsenseScript);

      // Initialize auto ads if enabled
      if (this.config.adsense.autoAds) {
        adsenseScript.onload = () => {
          (window.adsbygoogle = window.adsbygoogle || []).push({
            google_ad_client: this.config.adsense.publisherId,
            enable_page_level_ads: true
          });
        };
      }

      // Create ad placements
      this.createAdPlacements();
    }
  }

  createAdPlacements() {
    // Header Ad
    this.createAdUnit('header-ad', {
      slot: this.config.adsense.adUnits.header,
      size: [[728, 90], [970, 90]], // Leaderboard/Super Leaderboard
      position: 'afterbegin',
      parent: 'header'
    });

    // Sidebar Ad
    this.createAdUnit('sidebar-ad', {
      slot: this.config.adsense.adUnits.sidebar,
      size: [[300, 250], [336, 280]], // Medium Rectangle/Large Rectangle
      position: 'sticky',
      parent: 'aside'
    });

    // In-Article Ad
    this.createInArticleAd();

    // Footer Ad
    this.createAdUnit('footer-ad', {
      slot: this.config.adsense.adUnits.footer,
      size: [[728, 90], [970, 90]],
      position: 'beforeend',
      parent: 'footer'
    });
  }

  createAdUnit(id, config) {
    const adContainer = document.createElement('div');
    adContainer.className = 'ad-container';
    adContainer.style.cssText = `
      text-align: center;
      margin: 2rem 0;
      padding: 1rem;
      background: #f9fafb;
      border-radius: 0.5rem;
      border: 1px solid #e5e7eb;
    `;

    adContainer.innerHTML = `
      <div style="font-size: 0.75rem; color: #9ca3af; margin-bottom: 0.5rem;">Advertisement</div>
      <ins class="adsbygoogle"
           style="display:block"
           data-ad-client="${this.config.adsense.publisherId}"
           data-ad-slot="${config.slot}"
           data-ad-format="auto"
           data-full-width-responsive="true"></ins>
    `;

    // Insert ad based on position
    const parent = document.querySelector(config.parent) || document.body;
    if (config.position === 'afterbegin') {
      parent.insertAdjacentElement('afterbegin', adContainer);
    } else if (config.position === 'beforeend') {
      parent.insertAdjacentElement('beforeend', adContainer);
    } else {
      parent.appendChild(adContainer);
    }

    // Initialize AdSense ad
    if (window.adsbygoogle) {
      (window.adsbygoogle = window.adsbygoogle || []).push({});
    }

    this.trackAdView(id);
  }

  createInArticleAd() {
    const article = document.querySelector('article, .article-content, main');
    if (!article) return;

    const paragraphs = article.querySelectorAll('p');
    if (paragraphs.length < 3) return;

    // Insert ad after 3rd paragraph
    const targetParagraph = paragraphs[Math.min(2, paragraphs.length - 1)];

    const adContainer = document.createElement('div');
    adContainer.className = 'in-article-ad';
    adContainer.style.cssText = `
      margin: 3rem 0;
      padding: 2rem;
      background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
      border-radius: 1rem;
      border: 1px solid #e2e8f0;
      text-align: center;
    `;

    adContainer.innerHTML = `
      <div style="font-size: 0.875rem; color: #6b7280; margin-bottom: 1rem;">📢 Sponsored Content</div>
      <ins class="adsbygoogle"
           style="display:block; text-align:center;"
           data-ad-layout="in-article"
           data-ad-format="fluid"
           data-ad-client="${this.config.adsense.publisherId}"
           data-ad-slot="${this.config.adsense.adUnits.inArticle}"></ins>
    `;

    targetParagraph.insertAdjacentElement('afterend', adContainer);

    if (window.adsbygoogle) {
      (window.adsbygoogle = window.adsbygoogle || []).push({});
    }

    this.trackAdView('in-article');
  }

  setupAffiliateTracking() {
    // Create affiliate disclosure
    this.createAffiliateDisclosure();

    // Setup affiliate link tracking
    document.addEventListener('click', (e) => {
      if (e.target.matches('.affiliate-link, [data-affiliate]')) {
        this.trackAffiliateClick(e.target);
      }
    });

    // Auto-affiliate links
    this.autoAffiliateLinks();
  }

  createAffiliateDisclosure() {
    const disclosure = document.createElement('div');
    disclosure.className = 'affiliate-disclosure';
    disclosure.style.cssText = `
      background: #fef3c7;
      border: 1px solid #f59e0b;
      color: #92400e;
      padding: 1rem;
      border-radius: 0.5rem;
      margin: 2rem 0;
      font-size: 0.875rem;
      line-height: 1.5;
    `;

    disclosure.innerHTML = `
      <strong>💡 Affiliate Disclosure:</strong> ${this.config.affiliate.disclosureText}
    `;

    // Insert after first paragraph
    const article = document.querySelector('article, .article-content');
    if (article) {
      const firstParagraph = article.querySelector('p');
      if (firstParagraph) {
        firstParagraph.insertAdjacentElement('afterend', disclosure);
      }
    }
  }

  autoAffiliateLinks() {
    // Replace certain keywords with affiliate links
    const affiliateKeywords = {
      'audiobook': {
        text: 'audiobook',
        url: `https://www.amazon.com/gp/search?tag=${this.config.affiliate.programs.amazon}&keywords=audiobook`,
        program: 'amazon'
      },
      'online course': {
        text: 'online course',
        url: `https://www.coursera.org/?ranMID=40328&ranEAID=vedj0cWlu2Y&ranSiteID=vedj0cWlu2Y-${this.config.affiliate.programs.coursera}`,
        program: 'coursera'
      },
      'masterclass': {
        text: 'MasterClass',
        url: `https://www.masterclass.com/?utm_source=${this.config.affiliate.programs.masterclass}`,
        program: 'masterclass'
      }
    };

    // This would be implemented with more sophisticated text replacement
    // For now, we'll create contextual affiliate recommendations
    this.createContextualRecommendations();
  }

  createContextualRecommendations() {
    const article = document.querySelector('article, .article-content');
    if (!article) return;

    const recommendations = document.createElement('div');
    recommendations.className = 'affiliate-recommendations';
    recommendations.style.cssText = `
      margin: 3rem 0;
      padding: 2rem;
      background: white;
      border-radius: 1rem;
      border: 1px solid #e5e7eb;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    `;

    recommendations.innerHTML = `
      <h3 style="color: #1f2937; margin-bottom: 1.5rem; font-size: 1.25rem; font-weight: 700;">
        📚 Recommended Resources
      </h3>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
        <a href="https://www.amazon.com/gp/search?tag=${this.config.affiliate.programs.amazon}&keywords=science+books"
           class="affiliate-link" data-affiliate="amazon" data-product="science-books"
           style="display: block; padding: 1.5rem; background: #f8fafc; border-radius: 0.75rem; text-decoration: none; color: inherit; transition: all 0.3s ease; border: 1px solid #e2e8f0;">
          <div style="font-size: 1.5rem; margin-bottom: 0.75rem;">📖</div>
          <h4 style="color: #1f2937; font-weight: 600; margin-bottom: 0.5rem;">Science Books</h4>
          <p style="color: #6b7280; font-size: 0.875rem; margin: 0;">Explore fascinating science books on Amazon</p>
        </a>

        <a href="https://www.audible.com/search?tag=${this.config.affiliate.programs.audible}&keywords=science"
           class="affiliate-link" data-affiliate="audible" data-product="science-audiobooks"
           style="display: block; padding: 1.5rem; background: #f8fafc; border-radius: 0.75rem; text-decoration: none; color: inherit; transition: all 0.3s ease; border: 1px solid #e2e8f0;">
          <div style="font-size: 1.5rem; margin-bottom: 0.75rem;">🎧</div>
          <h4 style="color: #1f2937; font-weight: 600; margin-bottom: 0.5rem;">Science Audiobooks</h4>
          <p style="color: #6b7280; font-size: 0.875rem; margin: 0;">Listen to fascinating science stories</p>
        </a>

        <a href="https://www.coursera.org/browse/physical-science-and-engineering?ranMID=40328&ranEAID=${this.config.affiliate.programs.coursera}"
           class="affiliate-link" data-affiliate="coursera" data-product="science-courses"
           style="display: block; padding: 1.5rem; background: #f8fafc; border-radius: 0.75rem; text-decoration: none; color: inherit; transition: all 0.3s ease; border: 1px solid #e2e8f0;">
          <div style="font-size: 1.5rem; margin-bottom: 0.75rem;">🎓</div>
          <h4 style="color: #1f2937; font-weight: 600; margin-bottom: 0.5rem;">Online Courses</h4>
          <p style="color: #6b7280; font-size: 0.875rem; margin: 0;">Learn from top universities</p>
        </a>
      </div>

      <div style="margin-top: 1rem; font-size: 0.75rem; color: #9ca3af; text-align: center;">
        These are affiliate links. We may earn a commission if you make a purchase.
      </div>
    `;

    article.appendChild(recommendations);

    // Add hover effects
    const links = recommendations.querySelectorAll('.affiliate-link');
    links.forEach(link => {
      link.addEventListener('mouseenter', () => {
        link.style.transform = 'translateY(-2px)';
        link.style.boxShadow = '0 8px 25px rgba(0, 0, 0, 0.1)';
      });

      link.addEventListener('mouseleave', () => {
        link.style.transform = 'translateY(0)';
        link.style.boxShadow = 'none';
      });
    });
  }

  setupPremiumFeatures() {
    if (!this.config.premium.enabled) return;

    this.createPremiumUpgradeWidget();
    this.setupPremiumContentGating();
  }

  createPremiumUpgradeWidget() {
    const widget = document.createElement('div');
    widget.className = 'premium-upgrade-widget';
    widget.style.cssText = `
      position: fixed;
      bottom: 2rem;
      left: 2rem;
      background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
      color: white;
      padding: 1.5rem;
      border-radius: 1rem;
      box-shadow: 0 10px 25px rgba(251, 191, 36, 0.3);
      max-width: 300px;
      z-index: 1000;
      cursor: pointer;
      transition: all 0.3s ease;
    `;

    widget.innerHTML = `
      <div style="display: flex; align-items: center; gap: 1rem;">
        <div style="font-size: 2rem;">⭐</div>
        <div>
          <h4 style="margin: 0; font-size: 1rem; font-weight: 700;">Go Premium</h4>
          <p style="margin: 0.25rem 0 0 0; font-size: 0.875rem; opacity: 0.9;">
            Unlock exclusive content & remove ads
          </p>
        </div>
      </div>
      <div style="margin-top: 1rem; text-align: center;">
        <span style="font-size: 1.25rem; font-weight: 700;">$${this.config.premium.price}/month</span>
      </div>
    `;

    widget.addEventListener('click', () => {
      this.showPremiumModal();
    });

    widget.addEventListener('mouseenter', () => {
      widget.style.transform = 'translateY(-2px)';
      widget.style.boxShadow = '0 15px 35px rgba(251, 191, 36, 0.4)';
    });

    widget.addEventListener('mouseleave', () => {
      widget.style.transform = 'translateY(0)';
      widget.style.boxShadow = '0 10px 25px rgba(251, 191, 36, 0.3)';
    });

    document.body.appendChild(widget);

    // Show only after user has read for 30 seconds
    widget.style.display = 'none';
    setTimeout(() => {
      widget.style.display = 'block';
    }, 30000);
  }

  showPremiumModal() {
    const modal = document.createElement('div');
    modal.className = 'premium-modal';
    modal.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.8);
      z-index: 10000;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem;
    `;

    modal.innerHTML = `
      <div style="background: white; border-radius: 1rem; padding: 3rem; max-width: 500px; width: 100%; text-align: center; position: relative;">
        <button class="close-modal" style="position: absolute; top: 1rem; right: 1rem; background: none; border: none; font-size: 1.5rem; cursor: pointer;">✕</button>

        <div style="font-size: 3rem; margin-bottom: 1rem;">⭐</div>
        <h2 style="color: #1f2937; margin-bottom: 1rem;">Upgrade to Premium</h2>
        <p style="color: #6b7280; margin-bottom: 2rem;">
          Get the ultimate MindPulse Daily experience with exclusive features
        </p>

        <div style="text-align: left; margin-bottom: 2rem;">
          ${this.config.premium.features.map(feature => `
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.75rem;">
              <span style="color: #10b981; font-weight: bold;">✓</span>
              <span style="color: #374151;">${feature}</span>
            </div>
          `).join('')}
        </div>

        <div style="background: #f9fafb; padding: 1.5rem; border-radius: 0.75rem; margin-bottom: 2rem;">
          <div style="font-size: 2rem; font-weight: 700; color: #9333ea;">$${this.config.premium.price}</div>
          <div style="color: #6b7280;">per month</div>
        </div>

        <button class="upgrade-btn" style="background: linear-gradient(135deg, #9333ea 0%, #7c3aed 100%); color: white; border: none; padding: 1rem 2rem; border-radius: 0.75rem; font-weight: 700; font-size: 1.1rem; cursor: pointer; width: 100%; margin-bottom: 1rem;">
          Start Premium Trial
        </button>

        <p style="color: #9ca3af; font-size: 0.875rem;">Cancel anytime • 7-day free trial</p>
      </div>
    `;

    document.body.appendChild(modal);

    // Close modal handlers
    modal.querySelector('.close-modal').addEventListener('click', () => {
      document.body.removeChild(modal);
    });

    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        document.body.removeChild(modal);
      }
    });

    // Upgrade button handler
    modal.querySelector('.upgrade-btn').addEventListener('click', () => {
      this.handlePremiumUpgrade();
    });

    this.trackEvent('premium_modal_viewed');
  }

  handlePremiumUpgrade() {
    // In real implementation, integrate with payment providers:
    // - Stripe: https://stripe.com/
    // - PayPal: https://www.paypal.com/
    // - Paddle: https://paddle.com/

    alert('Premium upgrade coming soon! 🚀');
    this.trackEvent('premium_upgrade_attempted');
  }

  setupDonationButtons() {
    if (!this.config.donations.enabled) return;

    this.createDonationWidget();
  }

  createDonationWidget() {
    const widget = document.createElement('div');
    widget.className = 'donation-widget';
    widget.style.cssText = `
      margin: 3rem 0;
      padding: 2rem;
      background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
      border-radius: 1rem;
      border: 1px solid #f59e0b;
      text-align: center;
    `;

    widget.innerHTML = `
      <div style="font-size: 2rem; margin-bottom: 1rem;">☕</div>
      <h3 style="color: #92400e; margin-bottom: 1rem; font-size: 1.25rem;">
        Enjoying the content? Support us!
      </h3>
      <p style="color: #a16207; margin-bottom: 2rem; line-height: 1.6;">
        Your support helps us continue creating fascinating content and keep the site ad-light.
      </p>

      <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; margin-bottom: 1.5rem;">
        ${this.config.donations.suggestedAmounts.map(amount => `
          <button class="donation-btn" data-amount="${amount}"
                  style="background: #f59e0b; color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 0.5rem; font-weight: 600; cursor: pointer; transition: all 0.3s ease;">
            $${amount}
          </button>
        `).join('')}
      </div>

      <div style="display: flex; justify-content: center; gap: 1rem;">
        <a href="${this.config.donations.buyMeCoffeeUrl}" target="_blank" rel="noopener"
           class="donation-link" data-platform="buymeacoffee"
           style="background: #ff813f; color: white; padding: 0.75rem 1.5rem; text-decoration: none; border-radius: 0.5rem; font-weight: 600; transition: all 0.3s ease;">
          ☕ Buy Me a Coffee
        </a>
        <a href="${this.config.donations.patreonUrl}" target="_blank" rel="noopener"
           class="donation-link" data-platform="patreon"
           style="background: #ff424d; color: white; padding: 0.75rem 1.5rem; text-decoration: none; border-radius: 0.5rem; font-weight: 600; transition: all 0.3s ease;">
          💖 Patreon
        </a>
      </div>
    `;

    // Add to article
    const article = document.querySelector('article, .article-content');
    if (article) {
      article.appendChild(widget);
    }

    // Setup donation tracking
    widget.querySelectorAll('.donation-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const amount = btn.dataset.amount;
        this.handleDonation(amount);
      });
    });

    widget.querySelectorAll('.donation-link').forEach(link => {
      link.addEventListener('click', () => {
        this.trackEvent('donation_link_clicked', {
          platform: link.dataset.platform
        });
      });
    });
  }

  handleDonation(amount) {
    // In real implementation, integrate with payment processors
    // For now, redirect to Buy Me a Coffee with amount
    const url = `${this.config.donations.buyMeCoffeeUrl}?amount=${amount}`;
    window.open(url, '_blank');

    this.trackEvent('donation_initiated', {
      amount: amount,
      platform: 'buymeacoffee'
    });
  }

  trackAdView(adUnit) {
    this.analytics.adViews = (this.analytics.adViews || 0) + 1;
    this.trackEvent('ad_view', { adUnit: adUnit });
  }

  trackAffiliateClick(element) {
    this.analytics.affiliateClicks += 1;
    const program = element.dataset.affiliate;
    const product = element.dataset.product;

    this.trackEvent('affiliate_click', {
      program: program,
      product: product,
      url: element.href
    });

    this.saveAnalytics();
  }

  trackEvent(eventName, data = {}) {
    // Google Analytics
    if (typeof gtag !== 'undefined') {
      gtag('event', eventName, {
        'event_category': 'monetization',
        'event_label': eventName,
        ...data
      });
    }

    // Internal analytics
    const analytics = JSON.parse(localStorage.getItem('mindpulse_monetization_events') || '[]');
    analytics.push({
      event: eventName,
      data: data,
      timestamp: Date.now(),
      url: window.location.href
    });

    // Keep only last 1000 events
    if (analytics.length > 1000) {
      analytics.splice(0, analytics.length - 1000);
    }

    localStorage.setItem('mindpulse_monetization_events', JSON.stringify(analytics));
  }

  setupRevenueTracking() {
    // Track estimated revenue (in a real app, this would come from actual payment data)
    setInterval(() => {
      this.updateRevenueEstimates();
    }, 60000); // Update every minute
  }

  updateRevenueEstimates() {
    // Simulate revenue calculations based on engagement
    const pageViews = parseInt(localStorage.getItem('total_page_views') || '0');
    const adClicks = this.analytics.adClicks || 0;
    const affiliateClicks = this.analytics.affiliateClicks || 0;

    // Estimated ad revenue (typical rates)
    this.analytics.adRevenue = pageViews * 0.001; // $1 per 1000 views

    // Estimated affiliate revenue (conversion rate * commission)
    this.analytics.affiliateRevenue = affiliateClicks * 0.05 * 10; // 5% conversion, $10 avg commission

    this.saveAnalytics();
  }

  getRevenueReport() {
    return {
      totalRevenue: this.analytics.adRevenue + this.analytics.affiliateRevenue + this.analytics.premiumRevenue + this.analytics.donationRevenue,
      breakdown: {
        ads: this.analytics.adRevenue,
        affiliate: this.analytics.affiliateRevenue,
        premium: this.analytics.premiumRevenue,
        donations: this.analytics.donationRevenue
      },
      performance: {
        adClicks: this.analytics.adClicks,
        affiliateClicks: this.analytics.affiliateClicks,
        premiumConversions: this.analytics.premiumConversions || 0
      }
    };
  }

  createMonetizationWidgets() {
    // Create floating support widget
    this.createFloatingSupportWidget();
  }

  createFloatingSupportWidget() {
    const widget = document.createElement('div');
    widget.style.cssText = `
      position: fixed;
      top: 50%;
      right: 2rem;
      transform: translateY(-50%);
      background: white;
      border-radius: 1rem;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
      padding: 1rem;
      z-index: 1000;
      transition: all 0.3s ease;
      cursor: pointer;
      border: 2px solid #9333ea;
    `;

    widget.innerHTML = `
      <div style="text-align: center;">
        <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">💜</div>
        <div style="font-size: 0.875rem; font-weight: 600; color: #9333ea;">Support Us</div>
      </div>
    `;

    widget.addEventListener('click', () => {
      this.showSupportModal();
    });

    document.body.appendChild(widget);

    // Show after 45 seconds
    widget.style.display = 'none';
    setTimeout(() => {
      widget.style.display = 'block';
    }, 45000);
  }

  showSupportModal() {
    // Similar to premium modal but for general support options
    const modal = document.createElement('div');
    modal.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.8);
      z-index: 10000;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem;
    `;

    modal.innerHTML = `
      <div style="background: white; border-radius: 1rem; padding: 2rem; max-width: 400px; width: 100%; text-align: center;">
        <div style="font-size: 3rem; margin-bottom: 1rem;">💜</div>
        <h2 style="margin-bottom: 1rem;">Support MindPulse Daily</h2>
        <p style="color: #6b7280; margin-bottom: 2rem;">
          Help us continue creating fascinating content for curious minds like you!
        </p>

        <div style="display: grid; gap: 1rem;">
          <button onclick="window.open('${this.config.donations.buyMeCoffeeUrl}', '_blank')"
                  style="background: #ff813f; color: white; border: none; padding: 1rem; border-radius: 0.5rem; font-weight: 600; cursor: pointer;">
            ☕ Buy Me a Coffee
          </button>
          <button onclick="window.open('${this.config.donations.patreonUrl}', '_blank')"
                  style="background: #ff424d; color: white; border: none; padding: 1rem; border-radius: 0.5rem; font-weight: 600; cursor: pointer;">
            💖 Become a Patron
          </button>
          <button onclick="document.body.removeChild(this.closest('.support-modal'))"
                  style="background: #f3f4f6; color: #374151; border: none; padding: 1rem; border-radius: 0.5rem; font-weight: 600; cursor: pointer;">
            Maybe Later
          </button>
        </div>
      </div>
    `;

    modal.className = 'support-modal';
    document.body.appendChild(modal);

    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        document.body.removeChild(modal);
      }
    });

    this.trackEvent('support_modal_viewed');
  }
}

// Initialize monetization system
const monetization = new MonetizationSystem();

// Export for global use
window.MindPulseMonetization = monetization;

export default monetization;
