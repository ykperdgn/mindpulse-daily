// Advanced Analytics & User Engagement Tracker
class AdvancedAnalytics {
  constructor() {
    this.sessionId = this.generateSessionId();
    this.startTime = Date.now();
    this.events = [];
    this.userPreferences = this.loadUserPreferences();
    this.scrollDepth = 0;
    this.timeOnPage = 0;
    this.interactions = 0;
    
    this.init();
  }

  init() {
    // Track page view
    this.trackEvent('page_view', {
      url: window.location.href,
      title: document.title,
      timestamp: Date.now(),
      userAgent: navigator.userAgent,
      language: navigator.language,
      referrer: document.referrer
    });

    // Setup event listeners
    this.setupScrollTracking();
    this.setupTimeTracking();
    this.setupInteractionTracking();
    this.setupReadingProgress();
    this.setupSocialShares();
    this.setupNewsletterTracking();
    
    // Track user preferences
    this.detectUserPreferences();
    
    // Send data periodically
    setInterval(() => this.sendAnalytics(), 30000); // Every 30 seconds
    
    // Send data on page unload
    window.addEventListener('beforeunload', () => this.sendAnalytics());
  }

  generateSessionId() {
    return 'session_' + Math.random().toString(36).substr(2, 9) + '_' + Date.now();
  }

  trackEvent(eventType, data = {}) {
    const event = {
      id: this.generateEventId(),
      sessionId: this.sessionId,
      type: eventType,
      timestamp: Date.now(),
      url: window.location.href,
      ...data
    };
    
    this.events.push(event);
    
    // Store in localStorage for persistence
    this.saveToLocalStorage();
    
    // Send to Google Analytics if available
    this.sendToGA(eventType, data);
    
    console.log('📊 Analytics Event:', eventType, data);
  }

  generateEventId() {
    return 'evt_' + Math.random().toString(36).substr(2, 9);
  }

  setupScrollTracking() {
    let maxScroll = 0;
    
    window.addEventListener('scroll', () => {
      const scrollPercent = Math.round(
        (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100
      );
      
      if (scrollPercent > maxScroll) {
        maxScroll = scrollPercent;
        this.scrollDepth = maxScroll;
        
        // Track milestone scrolls
        if (maxScroll >= 25 && maxScroll < 50) {
          this.trackEvent('scroll_depth', { depth: '25%' });
        } else if (maxScroll >= 50 && maxScroll < 75) {
          this.trackEvent('scroll_depth', { depth: '50%' });
        } else if (maxScroll >= 75 && maxScroll < 90) {
          this.trackEvent('scroll_depth', { depth: '75%' });
        } else if (maxScroll >= 90) {
          this.trackEvent('scroll_depth', { depth: '90%' });
        }
      }
    });
  }

  setupTimeTracking() {
    setInterval(() => {
      this.timeOnPage = Date.now() - this.startTime;
      
      // Track time milestones
      const minutes = Math.floor(this.timeOnPage / 60000);
      if (minutes > 0 && minutes % 1 === 0) { // Every minute
        this.trackEvent('time_on_page', { 
          minutes: minutes,
          engaged: this.interactions > 0
        });
      }
    }, 10000); // Check every 10 seconds
  }

  setupInteractionTracking() {
    // Track clicks
    document.addEventListener('click', (e) => {
      this.interactions++;
      
      const element = e.target;
      const elementInfo = {
        tag: element.tagName,
        className: element.className,
        id: element.id,
        text: element.textContent?.slice(0, 50) || ''
      };

      // Track specific interactions
      if (element.matches('a[href^="mailto:"]')) {
        this.trackEvent('email_click', elementInfo);
      } else if (element.matches('a[href*="social"], .social-share')) {
        this.trackEvent('social_click', elementInfo);
      } else if (element.matches('.reaction-btn')) {
        this.trackEvent('reaction_click', { 
          reaction: element.dataset.reaction,
          ...elementInfo 
        });
      } else if (element.matches('a')) {
        this.trackEvent('link_click', { 
          href: element.href,
          ...elementInfo 
        });
      }
    });

    // Track form submissions
    document.addEventListener('submit', (e) => {
      const form = e.target;
      this.trackEvent('form_submit', {
        formId: form.id,
        formClass: form.className,
        action: form.action
      });
    });
  }

  setupReadingProgress() {
    const article = document.querySelector('article, .article-content, main');
    if (!article) return;

    let readingStarted = false;
    let readingCompleted = false;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !readingStarted) {
          readingStarted = true;
          this.trackEvent('reading_started', {
            articleTitle: document.title,
            articleUrl: window.location.href
          });
        }
      });
    }, { threshold: 0.5 });

    observer.observe(article);

    // Track reading completion based on scroll + time
    setInterval(() => {
      if (!readingCompleted && readingStarted && 
          this.scrollDepth > 80 && this.timeOnPage > 60000) {
        readingCompleted = true;
        this.trackEvent('reading_completed', {
          timeSpent: this.timeOnPage,
          scrollDepth: this.scrollDepth
        });
      }
    }, 5000);
  }

  setupSocialShares() {
    document.addEventListener('click', (e) => {
      if (e.target.matches('.social-share, [data-social-share]')) {
        const platform = e.target.dataset.platform || 
                        e.target.className.match(/twitter|facebook|linkedin|whatsapp/)?.[0] || 
                        'unknown';
        
        this.trackEvent('social_share', {
          platform: platform,
          url: window.location.href,
          title: document.title
        });
      }
    });
  }

  setupNewsletterTracking() {
    // Track newsletter form interactions
    const newsletterForms = document.querySelectorAll('[data-newsletter], .newsletter-form');
    
    newsletterForms.forEach(form => {
      const emailInput = form.querySelector('input[type="email"]');
      
      if (emailInput) {
        // Track when user starts typing
        emailInput.addEventListener('focus', () => {
          this.trackEvent('newsletter_focus', {
            formLocation: form.dataset.location || 'unknown'
          });
        });

        // Track form submission
        form.addEventListener('submit', (e) => {
          this.trackEvent('newsletter_signup', {
            email: emailInput.value,
            formLocation: form.dataset.location || 'unknown'
          });
        });
      }
    });
  }

  detectUserPreferences() {
    // Detect language preference
    const userLang = navigator.language.split('-')[0];
    
    // Detect device type
    const isMobile = /Android|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
    
    // Detect reading patterns
    const timeOfDay = new Date().getHours();
    let readingTime = 'morning';
    if (timeOfDay >= 12 && timeOfDay < 17) readingTime = 'afternoon';
    else if (timeOfDay >= 17) readingTime = 'evening';
    
    const preferences = {
      language: userLang,
      deviceType: isMobile ? 'mobile' : 'desktop',
      preferredReadingTime: readingTime,
      timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
      ...this.userPreferences
    };

    this.userPreferences = preferences;
    this.saveUserPreferences();
    
    this.trackEvent('user_preferences', preferences);
  }

  loadUserPreferences() {
    try {
      return JSON.parse(localStorage.getItem('mindpulse_user_preferences') || '{}');
    } catch {
      return {};
    }
  }

  saveUserPreferences() {
    localStorage.setItem('mindpulse_user_preferences', JSON.stringify(this.userPreferences));
  }

  saveToLocalStorage() {
    const data = {
      sessionId: this.sessionId,
      events: this.events,
      timeOnPage: this.timeOnPage,
      scrollDepth: this.scrollDepth,
      interactions: this.interactions,
      lastUpdate: Date.now()
    };
    
    localStorage.setItem('mindpulse_analytics_session', JSON.stringify(data));
  }

  sendToGA(eventType, data) {
    if (typeof gtag !== 'undefined') {
      gtag('event', eventType, {
        event_category: 'user_engagement',
        event_label: eventType,
        custom_parameter: JSON.stringify(data),
        ...data
      });
    }
  }

  async sendAnalytics() {
    if (this.events.length === 0) return;

    const analyticsData = {
      sessionId: this.sessionId,
      events: this.events,
      summary: {
        timeOnPage: this.timeOnPage,
        scrollDepth: this.scrollDepth,
        interactions: this.interactions,
        userPreferences: this.userPreferences
      },
      metadata: {
        url: window.location.href,
        title: document.title,
        userAgent: navigator.userAgent,
        timestamp: Date.now()
      }
    };

    try {
      // In a real implementation, send to your analytics endpoint
      console.log('📊 Sending Analytics Data:', analyticsData);
      
      // Simulate API call
      await fetch('/api/analytics', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(analyticsData)
      }).catch(() => {
        // Fallback: store in localStorage if API fails
        const storedData = JSON.parse(localStorage.getItem('mindpulse_analytics_queue') || '[]');
        storedData.push(analyticsData);
        localStorage.setItem('mindpulse_analytics_queue', JSON.stringify(storedData));
      });

      // Clear sent events
      this.events = [];
      
    } catch (error) {
      console.warn('Analytics send failed:', error);
    }
  }

  // Public API for tracking custom events
  track(eventType, data) {
    this.trackEvent(eventType, data);
  }

  // Get analytics summary for dashboard
  getSummary() {
    return {
      sessionId: this.sessionId,
      timeOnPage: this.timeOnPage,
      scrollDepth: this.scrollDepth,
      interactions: this.interactions,
      eventsCount: this.events.length,
      userPreferences: this.userPreferences
    };
  }
}

// Initialize analytics
const analytics = new AdvancedAnalytics();

// Export for global use
window.MindPulseAnalytics = analytics;

// Track page performance
window.addEventListener('load', () => {
  const loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
  analytics.track('page_performance', {
    loadTime: loadTime,
    domContentLoaded: performance.timing.domContentLoadedEventEnd - performance.timing.navigationStart
  });
});

export default analytics;
