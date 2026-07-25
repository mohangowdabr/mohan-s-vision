// Main app logic

document.addEventListener("DOMContentLoaded", () => {
  // Tabs logic
  const tabContainers = document.querySelectorAll(".tabs");
  tabContainers.forEach(container => {
    const tabs = container.querySelectorAll(".tab");
    tabs.forEach(tab => {
      tab.addEventListener("click", () => {
        // Remove active from all
        tabs.forEach(t => t.classList.remove("tab--active"));
        // Add active to clicked
        tab.classList.add("tab--active");
        
        // Find associated content and show it
        const targetId = tab.dataset.target;
        if (targetId) {
          const contentSections = document.querySelectorAll(".tab-content");
          contentSections.forEach(c => c.style.display = "none");
          const targetSection = document.getElementById(targetId);
          if (targetSection) {
            targetSection.style.display = "block";
          }
        }
      });
    });
  });

  // Score Ring Animation
  const scoreRing = document.getElementById("scoreRingProgress");
  const scoreRingValue = document.getElementById("scoreRingValue");
  if (scoreRing && scoreRingValue) {
    const targetScore = parseInt(scoreRing.dataset.score, 10);
    const size = 180; // Default size
    const radius = (size - 20) / 2;
    const circumference = 2 * Math.PI * radius;
    
    scoreRing.style.strokeDasharray = circumference;
    scoreRing.style.strokeDashoffset = circumference;

    let startTime = null;
    const duration = 1500;

    const animate = (currentTime) => {
      if (!startTime) startTime = currentTime;
      const elapsed = currentTime - startTime;
      const fraction = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - fraction, 3);
      
      const currentScore = Math.round(eased * targetScore);
      scoreRingValue.textContent = currentScore;
      
      const progress = (currentScore / 900) * circumference;
      scoreRing.style.strokeDashoffset = circumference - progress;
      
      if (fraction < 1) requestAnimationFrame(animate);
    };
    
    requestAnimationFrame(animate);
  }

  // Asset Allocation Donut Chart (Chart.js)
  const donutCanvas = document.getElementById("allocationChart");
  if (donutCanvas && window.Chart) {
    const dataElement = document.getElementById("allocationData");
    if (dataElement) {
      const data = JSON.parse(dataElement.textContent);
      
      new Chart(donutCanvas, {
        type: 'doughnut',
        data: {
          labels: data.labels,
          datasets: [{
            data: data.values,
            backgroundColor: data.colors,
            borderWidth: 0,
            hoverOffset: 4
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          cutout: '70%',
          plugins: {
            legend: {
              display: false
            },
            tooltip: {
              callbacks: {
                label: function(context) {
                  return ' ' + context.label + ': ' + context.parsed + '%';
                }
              },
              backgroundColor: 'rgba(25, 30, 60, 0.9)',
              titleFont: { size: 14, family: 'Inter' },
              bodyFont: { size: 13, family: 'Inter' },
              padding: 10,
              cornerRadius: 6,
              borderColor: 'rgba(255, 255, 255, 0.1)',
              borderWidth: 1
            }
          },
          animation: {
            animateScale: true,
            animateRotate: true,
            duration: 1200
          }
        }
      });
    }
  }

  // Fraud Shield Search
  const searchBtn = document.getElementById("searchBtn");
  const searchInput = document.getElementById("searchInput");
  const clearSearchBtn = document.getElementById("clearSearchBtn");
  const suggestionsBox = document.getElementById("suggestionsBox");
  const resultContainer = document.getElementById("resultContainer");
  const defaultChips = document.getElementById("defaultChips");

  if (searchBtn && searchInput) {
    const handleSearch = (query) => {
      const q = query || searchInput.value;
      if (q.trim().length < 2) return;
      
      // Hide suggestions
      if (suggestionsBox) suggestionsBox.style.display = 'none';
      
      fetch('/api/fraud-check', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: q })
      })
      .then(res => res.json())
      .then(data => {
        if (defaultChips) defaultChips.style.display = 'none';
        
        let html = '';
        if (data.status === 'empty') return;
        
        const configs = {
          verified: { className: 'fraud-result--verified', icon: '✅', title: 'SEBI Verified', color: 'var(--color-success)' },
          suspended: { className: 'fraud-result--warning', icon: '⚠️', title: 'Registration Suspended', color: 'var(--color-warning)' },
          scam_alert: { className: 'fraud-result--scam', icon: '🚨', title: 'SCAM ALERT', color: 'var(--color-danger)' },
          finfluencer: { className: 'fraud-result--warning', icon: '⚠️', title: 'Unregistered Influencer', color: 'var(--color-warning)' },
          not_found: { className: 'fraud-result--unknown', icon: '❓', title: 'Not Found in Registry', color: 'var(--color-info)' },
        };
        const config = configs[data.status] || configs.not_found;
        
        html += `<div class="fraud-result ${config.className}">
          <div class="fraud-result__icon">${config.icon}</div>
          <div class="fraud-result__title" style="color: ${config.color}">${config.title}</div>
          <div class="fraud-result__message">${data.message}</div>`;
          
        if (data.registered_matches && data.registered_matches.length > 0 && data.status === 'verified') {
          const m = data.registered_matches[0];
          html += `<div class="fraud-result__details">
            <div class="fraud-result__detail-row"><span class="fraud-result__detail-label">Name</span><span>${m.name}</span></div>
            <div class="fraud-result__detail-row"><span class="fraud-result__detail-label">Registration</span><span style="font-family: var(--font-mono, monospace); font-size: var(--text-sm)">${m.reg_number}</span></div>
            <div class="fraud-result__detail-row"><span class="fraud-result__detail-label">Category</span><span>${m.category}</span></div>
            <div class="fraud-result__detail-row"><span class="fraud-result__detail-label">Status</span><span class="badge ${m.status === 'Active' ? 'badge--success' : 'badge--warning'}">${m.status}</span></div>
            <div class="fraud-result__detail-row"><span class="fraud-result__detail-label">City</span><span>${m.city}</span></div>
            <div class="fraud-result__detail-row" style="border-bottom: none"><span class="fraud-result__detail-label">Registered Since</span><span>${m.reg_date}</span></div>
          </div>`;
        }
        
        if (data.scam_matches && data.scam_matches.length > 0) {
          const s = data.scam_matches[0];
          html += `<div class="fraud-result__details">
            <div class="fraud-result__detail-row"><span class="fraud-result__detail-label">Scheme</span><span style="color: var(--color-danger); font-weight: 600">${s.scheme_name}</span></div>
            <div class="fraud-result__detail-row"><span class="fraud-result__detail-label">Type</span><span>${s.type}</span></div>
            <div class="fraud-result__detail-row"><span class="fraud-result__detail-label">SEBI Order</span><span style="font-family: var(--font-mono, monospace); font-size: var(--text-xs)">${s.sebi_order_ref}</span></div>
            <div class="fraud-result__detail-row" style="border-bottom: none"><span class="fraud-result__detail-label">Description</span><span style="font-size: var(--text-xs); line-height: 1.5">${s.description}</span></div>
          </div>`;
        }
        
        html += `</div>`;
        
        if (resultContainer) resultContainer.innerHTML = html;
      });
    };

    searchBtn.addEventListener("click", () => handleSearch());
    searchInput.addEventListener("keypress", (e) => {
      if (e.key === "Enter") handleSearch();
    });
    
    if (clearSearchBtn) {
      clearSearchBtn.addEventListener("click", () => {
        searchInput.value = '';
        if (resultContainer) resultContainer.innerHTML = '';
        if (defaultChips) defaultChips.style.display = 'block';
        clearSearchBtn.style.display = 'none';
        if (suggestionsBox) suggestionsBox.style.display = 'none';
      });
      
      searchInput.addEventListener("input", () => {
        clearSearchBtn.style.display = searchInput.value.length > 0 ? 'block' : 'none';
        
        if (searchInput.value.length >= 2) {
          fetch(`/api/suggestions?q=${encodeURIComponent(searchInput.value)}`)
          .then(res => res.json())
          .then(data => {
            if (data.length > 0 && suggestionsBox) {
              const typeColors = { registered: 'badge--success', scam: 'badge--danger', finfluencer: 'badge--warning' };
              const typeLabels = { registered: 'Registered', scam: 'Scam Alert', finfluencer: 'Finfluencer' };
              
              let html = '';
              data.forEach(sug => {
                html += `<div class="suggestions__item" data-label="${sug.label}">
                  <span class="suggestions__item-label">${sug.label}</span>
                  <span class="suggestions__item-type badge ${typeColors[sug.type] || 'badge--neutral'}">
                    ${typeLabels[sug.type] || sug.category}
                  </span>
                </div>`;
              });
              suggestionsBox.innerHTML = html;
              suggestionsBox.style.display = 'block';
              
              document.querySelectorAll('.suggestions__item').forEach(item => {
                item.addEventListener('click', () => {
                  searchInput.value = item.dataset.label;
                  handleSearch(item.dataset.label);
                });
              });
            } else if (suggestionsBox) {
              suggestionsBox.style.display = 'none';
            }
          });
        } else if (suggestionsBox) {
          suggestionsBox.style.display = 'none';
        }
      });
    }

    // Handle chips
    document.querySelectorAll(".chip-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        searchInput.value = btn.textContent.trim();
        if (clearSearchBtn) clearSearchBtn.style.display = 'block';
        handleSearch(searchInput.value);
      });
    });
  }
});
