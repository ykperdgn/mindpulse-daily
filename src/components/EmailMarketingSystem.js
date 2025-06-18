// Advanced Email Marketing & Newsletter System
class EmailMarketingSystem {
  constructor() {
    this.subscribers = this.loadSubscribers();
    this.emailTemplates = this.loadEmailTemplates();
    this.automationRules = this.loadAutomationRules();
    this.analyticsData = {
      openRates: [],
      clickRates: [],
      subscriptions: [],
      unsubscribes: []
    };

    this.init();
  }

  init() {
    this.setupNewsletterForms();
    this.setupEmailCapture();
    this.setupAutomationTriggers();
    this.loadAnalyticsData();
  }

  loadSubscribers() {
    try {
      return JSON.parse(localStorage.getItem('newsletter_subscribers') || '[]');
    } catch {
      return [];
    }
  }

  saveSubscribers() {
    localStorage.setItem('newsletter_subscribers', JSON.stringify(this.subscribers));
  }

  loadEmailTemplates() {
    return {
      welcome: {
        subject: "🧠 Welcome to MindPulse Daily - Your Mind Will Thank You!",
        content: `
          <div style="max-width: 600px; margin: 0 auto; font-family: Arial, sans-serif; color: #333;">
            <div style="background: linear-gradient(135deg, #9333ea 0%, #7c3aed 100%); padding: 2rem; text-align: center; color: white;">
              <h1 style="margin: 0; font-size: 2rem;">🧠 Welcome to MindPulse Daily!</h1>
              <p style="margin: 1rem 0 0 0; font-size: 1.1rem; opacity: 0.9;">Get ready for daily doses of fascinating knowledge</p>
            </div>

            <div style="padding: 2rem;">
              <h2 style="color: #9333ea;">Hi there, curious mind! 👋</h2>

              <p>You've just joined thousands of knowledge seekers who start their day with mind-blowing insights about:</p>

              <ul style="line-height: 1.8;">
                <li>🚀 <strong>Space discoveries</strong> that challenge our understanding</li>
                <li>🧠 <strong>Psychology insights</strong> that explain human behavior</li>
                <li>🔬 <strong>Science breakthroughs</strong> happening right now</li>
                <li>🌟 <strong>Nature phenomena</strong> that will amaze you</li>
                <li>📚 <strong>History mysteries</strong> finally solved</li>
              </ul>

              <div style="background: #f8fafc; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0; border-left: 4px solid #9333ea;">
                <h3 style="margin: 0 0 1rem 0; color: #9333ea;">🎁 Your Welcome Gift</h3>
                <p style="margin: 0;">Here's our most viral article to get you started:</p>
                <a href="https://mindpulse-daily.vercel.app/posts/why-do-we-dream"
                   style="display: inline-block; margin-top: 1rem; background: #9333ea; color: white; padding: 0.75rem 1.5rem; text-decoration: none; border-radius: 0.5rem; font-weight: bold;">
                  🌙 Why Do We Dream? Scientists Finally Have Answers
                </a>
              </div>

              <p>Every day, you'll receive one carefully curated insight that will:</p>
              <ul style="line-height: 1.8;">
                <li>✨ Spark fascinating conversations</li>
                <li>🎯 Expand your perspective</li>
                <li>🤓 Make you the smartest person in the room</li>
                <li>🚀 Feed your curiosity for learning</li>
              </ul>

              <div style="text-align: center; margin: 2rem 0;">
                <a href="https://mindpulse-daily.vercel.app"
                   style="background: linear-gradient(135deg, #9333ea 0%, #7c3aed 100%); color: white; padding: 1rem 2rem; text-decoration: none; border-radius: 0.5rem; font-weight: bold; font-size: 1.1rem;">
                  🌐 Explore More Mind-Blowing Content
                </a>
              </div>

              <p style="color: #6b7280; font-size: 0.9rem; margin-top: 2rem;">
                P.S. Follow us on social media for instant knowledge drops throughout the day!
              </p>

              <div style="text-align: center; margin-top: 1.5rem;">
                <a href="#" style="margin: 0 0.5rem; color: #9333ea; text-decoration: none;">🐦 Twitter</a>
                <a href="#" style="margin: 0 0.5rem; color: #9333ea; text-decoration: none;">📘 Facebook</a>
                <a href="#" style="margin: 0 0.5rem; color: #9333ea; text-decoration: none;">💼 LinkedIn</a>
              </div>
            </div>

            <div style="background: #f9fafb; padding: 1rem 2rem; text-align: center; color: #6b7280; font-size: 0.8rem;">
              <p>You're receiving this because you subscribed to MindPulse Daily.</p>
              <p><a href="#" style="color: #9333ea;">Unsubscribe</a> | <a href="#" style="color: #9333ea;">Update preferences</a></p>
            </div>
          </div>
        `
      },

      daily: {
        subject: "🤯 Today's Mind-Blowing Fact Will Change How You See {{topic}}",
        content: `
          <div style="max-width: 600px; margin: 0 auto; font-family: Arial, sans-serif; color: #333;">
            <div style="background: linear-gradient(135deg, #9333ea 0%, #7c3aed 100%); padding: 1.5rem; text-align: center; color: white;">
              <h1 style="margin: 0; font-size: 1.5rem;">{{emoji}} MindPulse Daily</h1>
              <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">{{date}}</p>
            </div>

            <div style="padding: 2rem;">
              <h2 style="color: #9333ea; line-height: 1.3;">{{title}}</h2>

              <div style="background: #f8fafc; padding: 1.5rem; border-radius: 0.5rem; margin: 1.5rem 0; border-left: 4px solid #9333ea;">
                <p style="margin: 0; font-size: 1.1rem; line-height: 1.6; color: #374151;">
                  {{fact}}
                </p>
              </div>

              <p>{{explanation}}</p>

              <div style="text-align: center; margin: 2rem 0;">
                <a href="{{articleUrl}}"
                   style="background: linear-gradient(135deg, #9333ea 0%, #7c3aed 100%); color: white; padding: 1rem 2rem; text-decoration: none; border-radius: 0.5rem; font-weight: bold;">
                  🔍 Read the Full Story
                </a>
              </div>

              <div style="background: #f1f5f9; padding: 1.5rem; border-radius: 0.5rem; margin: 2rem 0;">
                <h3 style="margin: 0 0 1rem 0; color: #374151;">💡 Did You Know?</h3>
                <p style="margin: 0; color: #6b7280;">{{bonus_fact}}</p>
              </div>

              <p style="color: #6b7280; font-size: 0.9rem;">
                Share this fascinating fact with someone who would find it interesting!
              </p>

              <div style="text-align: center; margin-top: 1.5rem;">
                <a href="{{shareTwitter}}" style="margin: 0 0.5rem; background: #1da1f2; color: white; padding: 0.5rem 1rem; text-decoration: none; border-radius: 0.25rem; font-size: 0.9rem;">🐦 Tweet</a>
                <a href="{{shareFacebook}}" style="margin: 0 0.5rem; background: #4267b2; color: white; padding: 0.5rem 1rem; text-decoration: none; border-radius: 0.25rem; font-size: 0.9rem;">📘 Share</a>
                <a href="{{shareLinkedIn}}" style="margin: 0 0.5rem; background: #0077b5; color: white; padding: 0.5rem 1rem; text-decoration: none; border-radius: 0.25rem; font-size: 0.9rem;">💼 Post</a>
              </div>
            </div>

            <div style="background: #f9fafb; padding: 1rem 2rem; text-align: center; color: #6b7280; font-size: 0.8rem;">
              <p>You're receiving this because you subscribed to MindPulse Daily.</p>
              <p><a href="#" style="color: #9333ea;">Unsubscribe</a> | <a href="#" style="color: #9333ea;">Update preferences</a></p>
            </div>
          </div>
        `
      },

      reengagement: {
        subject: "🤔 We Miss Your Curious Mind - Come Back for This Amazing Discovery!",
        content: `
          <div style="max-width: 600px; margin: 0 auto; font-family: Arial, sans-serif; color: #333;">
            <div style="background: linear-gradient(135deg, #9333ea 0%, #7c3aed 100%); padding: 2rem; text-align: center; color: white;">
              <h1 style="margin: 0; font-size: 2rem;">🤔 We Miss You!</h1>
              <p style="margin: 1rem 0 0 0; font-size: 1.1rem; opacity: 0.9;">Your curious mind has been missed at MindPulse Daily</p>
            </div>

            <div style="padding: 2rem;">
              <p>Hi there,</p>

              <p>We noticed you haven't opened our emails in a while, and we're wondering if we did something wrong? 🥺</p>

              <p>While you were away, we discovered some absolutely mind-blowing facts that we think you'd love:</p>

              <div style="background: #f8fafc; padding: 1.5rem; border-radius: 0.5rem; margin: 1.5rem 0; border-left: 4px solid #9333ea;">
                <h3 style="margin: 0 0 1rem 0; color: #9333ea;">🚀 What You Missed:</h3>
                <ul style="margin: 0; padding-left: 1.5rem; line-height: 1.8;">
                  <li>Why your brain literally shrinks when you sleep (and why that's amazing)</li>
                  <li>The surprising reason why we forget dreams within seconds</li>
                  <li>How NASA's new telescope found something that shouldn't exist</li>
                  <li>The psychology trick that makes people 40% more creative</li>
                </ul>
              </div>

              <p><strong>Here's what we promise:</strong></p>
              <ul style="line-height: 1.8;">
                <li>📧 Only valuable, mind-expanding content (no spam, ever)</li>
                <li>⏱️ Quick 2-3 minute reads that fit your busy schedule</li>
                <li>🧠 Facts so interesting you'll want to share them immediately</li>
                <li>🎯 Content carefully curated to spark your curiosity</li>
              </ul>

              <div style="text-align: center; margin: 2rem 0;">
                <a href="https://mindpulse-daily.vercel.app"
                   style="background: linear-gradient(135deg, #9333ea 0%, #7c3aed 100%); color: white; padding: 1rem 2rem; text-decoration: none; border-radius: 0.5rem; font-weight: bold; font-size: 1.1rem;">
                  🌟 Give Us Another Chance
                </a>
              </div>

              <p style="color: #6b7280; font-size: 0.9rem;">
                If you're still not interested, no hard feelings. You can <a href="#" style="color: #9333ea;">unsubscribe here</a> and we won't bother you again.
              </p>

              <p>Thanks for considering us,<br>
              The MindPulse Daily Team 💜</p>
            </div>
          </div>
        `
      }
    };
  }

  loadAutomationRules() {
    return {
      welcome: {
        trigger: 'subscription',
        delay: 0, // Send immediately
        template: 'welcome'
      },
      reengagement: {
        trigger: 'inactivity',
        delay: 7 * 24 * 60 * 60 * 1000, // 7 days
        template: 'reengagement'
      }
    };
  }

  setupNewsletterForms() {
    document.addEventListener('submit', (e) => {
      if (e.target.matches('.newsletter-form, [data-newsletter]')) {
        e.preventDefault();
        this.handleNewsletterSignup(e.target);
      }
    });
  }

  async handleNewsletterSignup(form) {
    const emailInput = form.querySelector('input[type="email"]');
    const submitBtn = form.querySelector('button[type="submit"]');

    if (!emailInput || !emailInput.value) return;

    const email = emailInput.value.trim().toLowerCase();
    const formLocation = form.dataset.location || 'unknown';

    // Validate email
    if (!this.validateEmail(email)) {
      this.showMessage(form, '❌ Please enter a valid email address', 'error');
      return;
    }

    // Check if already subscribed
    if (this.subscribers.find(sub => sub.email === email)) {
      this.showMessage(form, '✅ You\'re already subscribed! Check your inbox.', 'info');
      return;
    }

    // Disable button and show loading
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Subscribing...';
    submitBtn.disabled = true;

    try {
      // Add subscriber
      const subscriber = {
        email: email,
        subscriptionDate: new Date().toISOString(),
        source: formLocation,
        confirmed: false,
        preferences: {
          frequency: 'daily',
          topics: ['all']
        },
        engagement: {
          opens: 0,
          clicks: 0,
          lastActivity: new Date().toISOString()
        }
      };

      this.subscribers.push(subscriber);
      this.saveSubscribers();

      // Track subscription event
      this.trackEvent('newsletter_signup', {
        source: formLocation,
        email_domain: email.split('@')[1]
      });

      // Send welcome email (simulated)
      await this.sendEmail(subscriber, 'welcome');

      // Show success message
      this.showMessage(form, '🎉 Success! Check your email for a welcome gift.', 'success');

      // Reset form
      emailInput.value = '';

      // Track in analytics
      if (typeof gtag !== 'undefined') {
        gtag('event', 'newsletter_signup', {
          'event_category': 'engagement',
          'event_label': formLocation
        });
      }

    } catch (error) {
      console.error('Newsletter signup error:', error);
      this.showMessage(form, '❌ Something went wrong. Please try again.', 'error');
    } finally {
      // Restore button
      submitBtn.textContent = originalText;
      submitBtn.disabled = false;
    }
  }

  validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  showMessage(form, message, type = 'info') {
    // Remove existing message
    const existingMessage = form.querySelector('.signup-message');
    if (existingMessage) {
      existingMessage.remove();
    }

    // Create new message
    const messageDiv = document.createElement('div');
    messageDiv.className = 'signup-message';
    messageDiv.style.cssText = `
      margin-top: 1rem;
      padding: 0.75rem;
      border-radius: 0.5rem;
      font-size: 0.875rem;
      font-weight: 500;
      text-align: center;
      ${type === 'success' ? 'background: #d1fae5; color: #065f46;' : ''}
      ${type === 'error' ? 'background: #fee2e2; color: #991b1b;' : ''}
      ${type === 'info' ? 'background: #dbeafe; color: #1e40af;' : ''}
    `;
    messageDiv.textContent = message;

    form.appendChild(messageDiv);

    // Remove message after 5 seconds
    setTimeout(() => {
      if (messageDiv.parentNode) {
        messageDiv.remove();
      }
    }, 5000);
  }

  async sendEmail(subscriber, templateName, variables = {}) {
    const template = this.emailTemplates[templateName];
    if (!template) return;

    // Prepare email content with variables
    let content = template.content;
    let subject = template.subject;

    // Replace template variables
    Object.keys(variables).forEach(key => {
      const regex = new RegExp(`{{${key}}}`, 'g');
      content = content.replace(regex, variables[key]);
      subject = subject.replace(regex, variables[key]);
    });

    // Simulate email sending (in real implementation, use SendGrid, Mailchimp, etc.)
    console.log('📧 Sending email:', {
      to: subscriber.email,
      subject: subject,
      template: templateName
    });

    // Track email sent
    this.trackEvent('email_sent', {
      template: templateName,
      recipient: subscriber.email
    });

    // In real implementation, you would integrate with email service providers:
    // - SendGrid: https://sendgrid.com/
    // - Mailchimp: https://mailchimp.com/
    // - ConvertKit: https://convertkit.com/
    // - Substack: https://substack.com/

    // Example SendGrid integration:
    /*
    const sgMail = require('@sendgrid/mail');
    sgMail.setApiKey(process.env.SENDGRID_API_KEY);

    await sgMail.send({
      to: subscriber.email,
      from: 'noreply@mindpulse-daily.com',
      subject: subject,
      html: content
    });
    */

    return true;
  }

  setupEmailCapture() {
    // Exit-intent popup
    this.setupExitIntentPopup();

    // Scroll-based popup
    this.setupScrollBasedCapture();

    // Time-based popup
    this.setupTimeBasedCapture();
  }

  setupExitIntentPopup() {
    let exitIntentShown = false;

    document.addEventListener('mouseleave', (e) => {
      if (e.clientY <= 0 && !exitIntentShown && !this.hasSubscribed()) {
        exitIntentShown = true;
        this.showEmailCapturePopup('exit_intent');
      }
    });
  }

  setupScrollBasedCapture() {
    let scrollCaptureShown = false;

    window.addEventListener('scroll', () => {
      const scrollPercent = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;

      if (scrollPercent > 70 && !scrollCaptureShown && !this.hasSubscribed()) {
        scrollCaptureShown = true;
        this.showEmailCapturePopup('scroll_70');
      }
    });
  }

  setupTimeBasedCapture() {
    setTimeout(() => {
      if (!this.hasSubscribed()) {
        this.showEmailCapturePopup('time_30s');
      }
    }, 30000); // 30 seconds
  }

  hasSubscribed() {
    return localStorage.getItem('newsletter_subscribed') === 'true';
  }

  showEmailCapturePopup(trigger) {
    // Check for persistent dismissal
    if (localStorage.getItem('newsletter_popup_dismissed') === 'true' || this.hasSubscribed()) {
      return;
    }
    // Create popup overlay
    const overlay = document.createElement('div');
    overlay.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.7);
      z-index: 10000;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem;
    `;

    // Create popup content
    const popup = document.createElement('div');
    popup.style.cssText = `
      background: white;
      border-radius: 1rem;
      padding: 2rem;
      max-width: 500px;
      width: 100%;
      text-align: center;
      position: relative;
      animation: popupSlideIn 0.3s ease-out;
    `;

    popup.innerHTML = `
      <style>
        @keyframes popupSlideIn {
          from { opacity: 0; transform: scale(0.9) translateY(-20px); }
          to { opacity: 1; transform: scale(1) translateY(0); }
        }
      </style>

      <button class="close-popup" style="position: absolute; top: 1rem; right: 1rem; background: none; border: none; font-size: 1.5rem; cursor: pointer; color: #6b7280;">✕</button>

      <div style="font-size: 3rem; margin-bottom: 1rem;">🧠</div>
      <h2 style="color: #1f2937; margin-bottom: 1rem; font-size: 1.5rem;">Don't Miss Out on Mind-Blowing Facts!</h2>
      <p style="color: #6b7280; margin-bottom: 2rem; line-height: 1.6;">
        Join thousands of curious minds who get daily doses of fascinating insights delivered to their inbox.
      </p>

      <form class="newsletter-form popup-form" data-location="${trigger}" style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="email" placeholder="Enter your email" required
               style="flex: 1; padding: 0.75rem; border: 1px solid #d1d5db; border-radius: 0.5rem; font-size: 1rem;">
        <button type="submit"
                style="background: linear-gradient(135deg, #9333ea 0%, #7c3aed 100%); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 0.5rem; font-weight: 600; cursor: pointer; white-space: nowrap;">
          Subscribe
        </button>
      </form>

      <p style="color: #9ca3af; font-size: 0.875rem;">
        ✨ No spam, unsubscribe anytime. Your email stays private.
      </p>
    `;

    overlay.appendChild(popup);
    document.body.appendChild(overlay);

    // Close popup handlers
    const closeBtn = popup.querySelector('.close-popup');
    closeBtn.addEventListener('click', () => {
      localStorage.setItem('newsletter_popup_dismissed', 'true');
      document.body.removeChild(overlay);
    });

    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) {
        localStorage.setItem('newsletter_popup_dismissed', 'true');
        document.body.removeChild(overlay);
      }
    });

    // Track popup view
    this.trackEvent('email_popup_shown', {
      trigger: trigger
    });
  }

  trackEvent(eventName, data) {
    // Track analytics
    if (typeof gtag !== 'undefined') {
      gtag('event', eventName, {
        'event_category': 'email_marketing',
        'event_label': eventName,
        ...data
      });
    }

    // Store for internal analytics
    const analytics = JSON.parse(localStorage.getItem('mindpulse_email_analytics') || '{}');
    analytics[eventName] = (analytics[eventName] || 0) + 1;
    analytics.lastEvent = {
      name: eventName,
      data: data,
      timestamp: Date.now()
    };
    localStorage.setItem('mindpulse_email_analytics', JSON.stringify(analytics));
  }

  loadAnalyticsData() {
    // Load email marketing analytics
    this.analyticsData = JSON.parse(localStorage.getItem('mindpulse_email_analytics') || '{}');
  }

  getSubscriberCount() {
    return this.subscribers.length;
  }

  getEngagementStats() {
    const totalOpens = this.subscribers.reduce((sum, sub) => sum + sub.engagement.opens, 0);
    const totalClicks = this.subscribers.reduce((sum, sub) => sum + sub.engagement.clicks, 0);

    return {
      totalSubscribers: this.subscribers.length,
      averageOpenRate: this.subscribers.length > 0 ? (totalOpens / this.subscribers.length) : 0,
      averageClickRate: this.subscribers.length > 0 ? (totalClicks / this.subscribers.length) : 0,
      recentSubscriptions: this.subscribers.filter(sub => {
        const subDate = new Date(sub.subscriptionDate);
        const daysDiff = (Date.now() - subDate.getTime()) / (1000 * 60 * 60 * 24);
        return daysDiff <= 7;
      }).length
    };
  }
}

// Initialize email marketing system
const emailMarketing = new EmailMarketingSystem();

// Export for global use
window.MindPulseEmailMarketing = emailMarketing;

export default emailMarketing;
