/**
 * Mohan's Vision "Any Help" Chatbot — Rule-based FAQ assistant
 */
(function () {
  "use strict";

  // ── FAQ Knowledge Base ──
  const FAQ = [
    {
      keywords: ["health score", "financial score", "my score", "score meaning"],
      answer:
        "Your **Financial Health Score** ranges from 0–900 and is calculated based on 5 signals:\n\n• **Diversification** — Are your assets well-spread?\n• **Concentration Risk** — Is too much in one stock/sector?\n• **Advisor Trust** — Are your advisors SEBI-registered?\n• **Behavioural Bias** — Do you panic-sell or FOMO-buy?\n• **Goal Alignment** — Are your goals on track?\n\nVisit the **Score** tab to see your detailed breakdown!",
    },
    {
      keywords: ["connect account", "link account", "add account", "connect bank", "how to connect"],
      answer:
        "To connect your accounts:\n\n1. Go to **Connect Accounts** from the dashboard\n2. Link your **Demat** (CDSL/NSDL), **Bank**, **Mutual Funds**, and **NPS** accounts\n3. Each step is optional — skip what you don't have\n4. Your data is securely transmitted via the Account Aggregator framework\n\nYou can also access it from the onboarding flow!",
    },
    {
      keywords: ["sip", "systematic investment", "sip meaning"],
      answer:
        "**SIP (Systematic Investment Plan)** lets you invest a fixed amount regularly (monthly/weekly) in mutual funds.\n\n✅ Benefits:\n• Rupee cost averaging — buy more units when prices are low\n• Disciplined investing — no need to time the market\n• Start small — as low as ₹500/month\n• Power of compounding over time\n\nCheck your active SIPs in the **Portfolio** tab!",
    },
    {
      keywords: ["mutual fund", "mf", "what are mutual funds"],
      answer:
        "**Mutual Funds** pool money from many investors to invest in stocks, bonds, or other securities.\n\n📊 Types you might see:\n• **Equity Funds** — Invest in stocks (higher risk, higher returns)\n• **Debt Funds** — Invest in bonds (lower risk, stable returns)\n• **Hybrid Funds** — Mix of both\n• **ELSS** — Tax-saving equity funds (80C deduction)\n• **Index Funds** — Track an index like Nifty 50\n\nView your MF holdings in the **Portfolio** tab!",
    },
    {
      keywords: ["nps", "national pension", "pension", "pran"],
      answer:
        "**NPS (National Pension System)** is a government-backed retirement savings scheme.\n\n🏛️ Key points:\n• **Tier I** — Retirement account (locked until 60)\n• **Tier II** — Flexible savings (withdraw anytime)\n• Tax benefits under 80C and 80CCD(1B) — extra ₹50,000\n• Choose your Pension Fund Manager (SBI, LIC, etc.)\n• Invest in Equity (E), Corp Bonds (C), Govt Securities (G)\n\nYour NPS details are in the **Portfolio** tab!",
    },
    {
      keywords: ["risk", "risk calculate", "risk profile", "how is risk"],
      answer:
        "Your **Risk Profile** is based on several factors:\n\n📋 Assessment includes:\n• Investment horizon (short/medium/long term)\n• Income stability and emergency fund\n• Past investing experience\n• Comfort with market volatility\n• Financial goals and timelines\n\n🎯 Profiles:\n• **Conservative** — Prefers stability, lower risk\n• **Moderate** — Balanced approach\n• **Aggressive** — Comfortable with high volatility\n\nYour profile was set during onboarding and affects your health score!",
    },
    {
      keywords: ["fraud", "scam", "shield", "verify", "sebi check"],
      answer:
        "The **Fraud Shield** protects you by checking entities against SEBI's registry.\n\n🛡️ What it checks:\n• Is the advisor/entity SEBI-registered?\n• Are there any scam alerts or suspensions?\n• Is a finfluencer giving unregistered advice?\n\nGo to the **Shield** tab and search any name, registration number, or scheme to verify!",
    },
    {
      keywords: ["goal", "financial goal", "target", "planning"],
      answer:
        "**Goal-Based Tracking** helps you plan for major life events:\n\n🎯 How it works:\n• Set goals like Emergency Fund, Retirement, Child Education\n• Track progress with monthly SIP contributions\n• Get nudges when you're falling behind\n• See if you're on track based on expected returns\n\nVisit the **Goals** tab to see your progress!",
    },
    {
      keywords: ["portfolio", "holdings", "my investments", "net worth"],
      answer:
        "Your **Portfolio** shows all your investments in one place:\n\n📊 Asset classes tracked:\n• Equities (stocks)\n• Mutual Funds\n• Bonds & Government Securities\n• Gold (Digital + SGB)\n• NPS\n• REITs / InvITs\n\nTotal net worth, P&L, and allocation breakdowns are all on the **Portfolio** tab!",
    },
    {
      keywords: ["support", "contact", "help", "customer care", "reach"],
      answer:
        "📞 **Contact Support:**\n\n• **Email:** support@risklens.in\n• **Phone:** 1800-XXX-XXXX (Toll Free)\n• **Hours:** Mon–Sat, 9 AM – 6 PM IST\n• **Response time:** Usually within 2 hours\n\nYou can also report issues directly through this chat!",
    },
    {
      keywords: ["hello", "hi", "hey", "good morning", "good evening"],
      answer:
        "Hello! 👋 I'm **Any Help**, your Mohan's Vision assistant.\n\nI can help you with:\n• Understanding your health score\n• Connecting accounts\n• Learning about SIPs, mutual funds, NPS\n• Checking fraud/scam alerts\n• Tracking your goals\n\nJust type your question or tap a quick reply below! 😊",
    },
    {
      keywords: ["thank", "thanks", "thank you", "thx"],
      answer: "You're welcome! 😊 Happy to help. Let me know if you have any other questions!",
    },
  ];

  const FALLBACK_RESPONSE =
    "I'm not sure about that yet. 🤔\n\nTry asking me about:\n• Your **health score**\n• **Connecting accounts**\n• **SIP**, **mutual funds**, or **NPS**\n• **Fraud shield** verification\n• **Goal tracking**\n• **Contact support**\n\nOr tap one of the quick reply buttons below!";

  // ── State ──
  let isOpen = false;
  let chatHistory = [];

  // ── DOM Elements ──
  const fab = document.getElementById("chatbotFab");
  const panel = document.getElementById("chatbotPanel");
  const fabIcon = document.getElementById("fabIcon");
  const fabClose = document.getElementById("fabClose");
  const closeBtn = document.getElementById("chatbotClose");
  const messagesEl = document.getElementById("chatMessages");
  const inputEl = document.getElementById("chatInput");
  const sendBtn = document.getElementById("chatSendBtn");
  const quickRepliesEl = document.getElementById("quickReplies");

  if (!fab || !panel) return;

  // ── Initialize ──
  addBotMessage(
    "Hello! 👋 I'm **Any Help**, your Mohan's Vision assistant.\n\nHow can I help you today?"
  );

  // ── Toggle Chat ──
  function toggleChat() {
    isOpen = !isOpen;
    panel.classList.toggle("chatbot-panel--open", isOpen);
    fab.classList.toggle("chatbot-fab--active", isOpen);
    fabIcon.style.display = isOpen ? "none" : "flex";
    fabClose.style.display = isOpen ? "flex" : "none";

    if (isOpen) {
      setTimeout(() => inputEl && inputEl.focus(), 300);
    }

    if (window.lucide) lucide.createIcons();
  }

  fab.addEventListener("click", toggleChat);
  if (closeBtn) closeBtn.addEventListener("click", toggleChat);

  // ── Send Message ──
  function sendMessage(text) {
    if (!text || !text.trim()) return;
    const message = text.trim();

    addUserMessage(message);
    inputEl.value = "";

    // Show typing indicator
    showTyping();

    // Simulate thinking delay
    setTimeout(() => {
      hideTyping();
      const response = findAnswer(message);
      addBotMessage(response);
    }, 600 + Math.random() * 800);
  }

  if (sendBtn) {
    sendBtn.addEventListener("click", () => sendMessage(inputEl.value));
  }
  if (inputEl) {
    inputEl.addEventListener("keypress", (e) => {
      if (e.key === "Enter") sendMessage(inputEl.value);
    });
  }

  // Quick reply chips
  if (quickRepliesEl) {
    quickRepliesEl.querySelectorAll(".quick-reply-chip").forEach((chip) => {
      chip.addEventListener("click", () => {
        const query = chip.dataset.query;
        sendMessage(query);
      });
    });
  }

  // ── Find Answer ──
  function findAnswer(query) {
    const lower = query.toLowerCase();

    for (const faq of FAQ) {
      for (const kw of faq.keywords) {
        if (lower.includes(kw)) {
          return faq.answer;
        }
      }
    }

    return FALLBACK_RESPONSE;
  }

  // ── Add Messages to DOM ──
  function addUserMessage(text) {
    chatHistory.push({ role: "user", text: text });
    const msgEl = document.createElement("div");
    msgEl.className = "chat-message chat-message--user animate-fade-in-up";
    msgEl.innerHTML = `<div class="chat-message__bubble">${escapeHtml(text)}</div>`;
    messagesEl.appendChild(msgEl);
    scrollToBottom();
  }

  function addBotMessage(text) {
    chatHistory.push({ role: "bot", text: text });
    const msgEl = document.createElement("div");
    msgEl.className = "chat-message chat-message--bot animate-fade-in-up";
    msgEl.innerHTML = `
      <div class="chat-message__avatar">
        <i data-lucide="bot" style="width: 14px; height: 14px;"></i>
      </div>
      <div class="chat-message__bubble">${formatMarkdown(text)}</div>
    `;
    messagesEl.appendChild(msgEl);
    scrollToBottom();
    if (window.lucide) lucide.createIcons();
  }

  function showTyping() {
    const typingEl = document.createElement("div");
    typingEl.id = "typingIndicator";
    typingEl.className = "chat-message chat-message--bot animate-fade-in";
    typingEl.innerHTML = `
      <div class="chat-message__avatar">
        <i data-lucide="bot" style="width: 14px; height: 14px;"></i>
      </div>
      <div class="chat-message__bubble typing-indicator">
        <span></span><span></span><span></span>
      </div>
    `;
    messagesEl.appendChild(typingEl);
    scrollToBottom();
    if (window.lucide) lucide.createIcons();
  }

  function hideTyping() {
    const el = document.getElementById("typingIndicator");
    if (el) el.remove();
  }

  function scrollToBottom() {
    setTimeout(() => {
      messagesEl.scrollTop = messagesEl.scrollHeight;
    }, 50);
  }

  // ── Helpers ──
  function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
  }

  function formatMarkdown(text) {
    // Simple markdown: **bold**, \n→<br>, •→bullet
    return text
      .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
      .replace(/\n/g, "<br>");
  }
})();
