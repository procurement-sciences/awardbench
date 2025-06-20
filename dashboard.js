// Benchmark data
const benchmarkData = {
  timestamp: new Date().toISOString(),
  leaderboard: [
    {
      rank: 1,
      model: 'Awarded AI Platform',
      overall_score: 0.947,
      tier: 'Elite Performance',
      tier_badge: '99th Percentile',
      scores: {
        compliance_accuracy: 0.98,
        proposal_quality: 0.92,
        workflow_effectiveness: 0.94,
        retrieval_accuracy: 0.95,
        efficiency: 0.96,
        compliance_matrix: 0.97,
        raci_matrix: 0.95,
      },
      strengths: [
        'Exceptional compliance accuracy',
        'Superior domain knowledge',
        'Advanced compliance matrix generation',
        'Automated RACI matrix creation',
      ],
    },
    {
      rank: 2,
      model: 'Claude 3.7 Sonnet',
      overall_score: 0.883,
      tier: 'Advanced Capability',
      tier_badge: '90th Percentile',
      scores: {
        compliance_accuracy: 0.85,
        proposal_quality: 0.91,
        workflow_effectiveness: 0.88,
        retrieval_accuracy: 0.89,
        efficiency: 0.9,
        compliance_matrix: 0.87,
        raci_matrix: 0.84,
      },
      strengths: ['Strong proposal generation', 'Good efficiency'],
    },
    {
      rank: 3,
      model: 'GPT-4o',
      overall_score: 0.872,
      tier: 'Advanced Capability',
      tier_badge: '85th Percentile',
      scores: {
        compliance_accuracy: 0.83,
        proposal_quality: 0.89,
        workflow_effectiveness: 0.87,
        retrieval_accuracy: 0.88,
        efficiency: 0.89,
        compliance_matrix: 0.85,
        raci_matrix: 0.82,
      },
      strengths: ['Consistent performance', 'Fast response times'],
    },
    {
      rank: 4,
      model: 'Generic ChatGPT',
      overall_score: 0.724,
      tier: 'Professional Standard',
      tier_badge: '70th Percentile',
      scores: {
        compliance_accuracy: 0.65,
        proposal_quality: 0.78,
        workflow_effectiveness: 0.72,
        retrieval_accuracy: 0.75,
        efficiency: 0.73,
        compliance_matrix: 0.68,
        raci_matrix: 0.62,
      },
      strengths: ['General knowledge', 'User-friendly'],
    },
  ],
  metrics: {
    compliance_accuracy: {
      name: 'Compliance Accuracy',
      description:
        'FAR/DFARS interpretation and compliance requirement identification',
      best_model: 'Awarded AI Platform',
      best_score: 0.98,
    },
    proposal_quality: {
      name: 'Proposal Generation Quality',
      description: 'Win theme alignment and technical accuracy in proposals',
      best_model: 'Awarded AI Platform',
      best_score: 0.92,
    },
    workflow_effectiveness: {
      name: 'Workflow Automation',
      description: 'End-to-end process automation and time-to-value',
      best_model: 'Awarded AI Platform',
      best_score: 0.94,
    },
    retrieval_accuracy: {
      name: 'Retrieval & Context',
      description: 'Document retrieval precision and context utilization',
      best_model: 'Awarded AI Platform',
      best_score: 0.95,
    },
    efficiency: {
      name: 'Overall Efficiency',
      description: 'Speed, cost optimization, and resource utilization',
      best_model: 'Awarded AI Platform',
      best_score: 0.96,
    },
    compliance_matrix: {
      name: 'Compliance Matrix Generation',
      description:
        'Section L/M parsing, requirement traceability, and automated cross-referencing',
      best_model: 'Awarded AI Platform',
      best_score: 0.97,
    },
    raci_matrix: {
      name: 'RACI Matrix Creation',
      description:
        'Responsibility assignment, role identification, and task accountability mapping',
      best_model: 'Awarded AI Platform',
      best_score: 0.95,
    },
  },
};

// Static paper files path
const PAPERS_PATH = '/papers';

// Theme management
class ThemeManager {
  constructor() {
    this.theme = localStorage.getItem('theme') || 'dark';
    this.init();
  }

  init() {
    // Set initial theme
    document.documentElement.setAttribute('data-theme', this.theme);

    // Setup toggle button
    const toggle = document.getElementById('themeToggle');
    toggle.addEventListener('click', () => this.toggleTheme());

    // Update button state
    this.updateToggleButton();

    // Set initial hero image
    this.updateHeroImage();
  }

  toggleTheme() {
    this.theme = this.theme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', this.theme);
    localStorage.setItem('theme', this.theme);
    this.updateToggleButton();
    this.updateHeroImage();

    // Update charts for new theme
    updateChartsTheme();
  }

  updateToggleButton() {
    const sunIcon = document.querySelector('.sun-icon');
    const moonIcon = document.querySelector('.moon-icon');

    if (this.theme === 'dark') {
      sunIcon.classList.remove('active');
      moonIcon.classList.add('active');
    } else {
      sunIcon.classList.add('active');
      moonIcon.classList.remove('active');
    }
  }

  updateHeroImage() {
    const heroImage = document.getElementById('heroImage');
    if (heroImage) {
      heroImage.src =
        this.theme === 'dark' ? 'hero_image_dark.png' : 'hero_image_light.png';
    }
  }

  getCurrentTheme() {
    return this.theme;
  }
}

// Initialize theme manager
let themeManager;

// Chart instances
let radarChart;
let barChart;

// Initialize dashboard
document.addEventListener('DOMContentLoaded', function () {
  // Initialize theme
  themeManager = new ThemeManager();

  // Set up tabs
  initializeTabs();

  // Populate metrics
  updateMetrics();

  // Populate leaderboard
  updateLeaderboard();

  // Initialize charts
  initializeCharts();

  // Set up download links
  setupDownloadLinks();

  // Smooth scroll for metric discussions
  setupSmoothScroll();
});

// Tab functionality
function initializeTabs() {
  const tabButtons = document.querySelectorAll('.tab-button');
  const tabContents = document.querySelectorAll('.tab-content');

  tabButtons.forEach(button => {
    button.addEventListener('click', () => {
      const targetTab = button.getAttribute('data-tab');

      // Update active states
      tabButtons.forEach(btn => btn.classList.remove('active'));
      tabContents.forEach(content => content.classList.remove('active'));

      button.classList.add('active');
      document.getElementById(targetTab).classList.add('active');
    });
  });
}

// Update metrics
function updateMetrics() {
  const leader = benchmarkData.leaderboard[0];

  document.getElementById('overallScore').textContent =
    `${(leader.overall_score * 100).toFixed(1)}%`;
  document.getElementById('overallLeader').textContent = leader.model;

  document.getElementById('complianceScore').textContent =
    `${(leader.scores.compliance_accuracy * 100).toFixed(1)}%`;
  document.getElementById('bestCompliance').textContent = leader.model;

  document.getElementById('proposalScore').textContent =
    `${(leader.scores.proposal_quality * 100).toFixed(1)}%`;
  document.getElementById('bestProposal').textContent = leader.model;

  document.getElementById('efficiencyScore').textContent =
    `${(leader.scores.efficiency * 100).toFixed(1)}%`;
  document.getElementById('mostEfficient').textContent = leader.model;

  document.getElementById('complianceMatrixScore').textContent =
    `${(leader.scores.compliance_matrix * 100).toFixed(1)}%`;
  document.getElementById('bestComplianceMatrix').textContent = leader.model;

  document.getElementById('raciMatrixScore').textContent =
    `${(leader.scores.raci_matrix * 100).toFixed(1)}%`;
  document.getElementById('bestRaciMatrix').textContent = leader.model;
}

// Update leaderboard
function updateLeaderboard() {
  const tbody = document.getElementById('leaderboardBody');
  tbody.innerHTML = '';

  benchmarkData.leaderboard.forEach(model => {
    const row = document.createElement('tr');
    row.innerHTML = `
            <td class="rank">#${model.rank}</td>
            <td class="model-name">${model.model}</td>
            <td class="score">${(model.overall_score * 100).toFixed(1)}%</td>
            <td><span class="tier">${model.tier}</span><br><span class="tier-badge">${model.tier_badge}</span></td>
            <td>${model.strengths.join(', ')}</td>
        `;
    tbody.appendChild(row);
  });
}

// Get theme colors
function getThemeColors() {
  const isDark = themeManager.getCurrentTheme() === 'dark';
  return {
    text: isDark ? '#999999' : '#6B7280',
    border: isDark ? 'rgba(255, 255, 255, 0.08)' : 'rgba(0, 0, 0, 0.08)',
    grid: isDark ? 'rgba(255, 255, 255, 0.08)' : 'rgba(0, 0, 0, 0.08)',
    background: isDark ? '#101010' : '#FFFFFF',
  };
}

// Initialize charts with theme support
function initializeCharts() {
  const colors = getThemeColors();

  // Chart.js defaults
  Chart.defaults.color = colors.text;
  Chart.defaults.borderColor = colors.border;
  Chart.defaults.font.family =
    "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif";

  // Radar Chart
  const radarCtx = document.getElementById('radarChart').getContext('2d');
  radarChart = new Chart(radarCtx, {
    type: 'radar',
    data: {
      labels: [
        'Compliance',
        'Proposal Quality',
        'Workflow',
        'Retrieval',
        'Efficiency',
        'Compliance Matrix',
        'RACI Matrix',
      ],
      datasets: benchmarkData.leaderboard.slice(0, 3).map((model, index) => ({
        label: model.model,
        data: [
          model.scores.compliance_accuracy,
          model.scores.proposal_quality,
          model.scores.workflow_effectiveness,
          model.scores.retrieval_accuracy,
          model.scores.efficiency,
          model.scores.compliance_matrix,
          model.scores.raci_matrix,
        ],
        borderColor:
          index === 0 ? '#00A67E' : index === 1 ? '#3B82F6' : '#EF4444',
        backgroundColor:
          index === 0
            ? 'rgba(0, 166, 126, 0.1)'
            : index === 1
              ? 'rgba(59, 130, 246, 0.1)'
              : 'rgba(239, 68, 68, 0.1)',
        borderWidth: 2,
        pointBackgroundColor:
          index === 0 ? '#00A67E' : index === 1 ? '#3B82F6' : '#EF4444',
        pointBorderColor: colors.background,
        pointBorderWidth: 2,
      })),
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'bottom',
          labels: {
            padding: 20,
            usePointStyle: true,
            font: {
              size: 12,
            },
            color: colors.text,
          },
        },
      },
      scales: {
        r: {
          beginAtZero: true,
          max: 1,
          ticks: {
            stepSize: 0.2,
            callback: function (value) {
              return value * 100 + '%';
            },
            color: colors.text,
          },
          grid: {
            color: colors.grid,
          },
          pointLabels: {
            font: {
              size: 12,
            },
            color: colors.text,
          },
        },
      },
    },
  });

  // Bar Chart
  const barCtx = document.getElementById('barChart').getContext('2d');
  barChart = new Chart(barCtx, {
    type: 'bar',
    data: {
      labels: benchmarkData.leaderboard.map(m => m.model),
      datasets: [
        {
          label: 'Overall Score',
          data: benchmarkData.leaderboard.map(m => m.overall_score),
          backgroundColor: ['#00A67E', '#3B82F6', '#EF4444', '#F59E0B'],
          borderColor: ['#00A67E', '#3B82F6', '#EF4444', '#F59E0B'],
          borderWidth: 0,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false,
        },
      },
      scales: {
        y: {
          beginAtZero: true,
          max: 1,
          ticks: {
            stepSize: 0.2,
            callback: function (value) {
              return value * 100 + '%';
            },
            color: colors.text,
          },
          grid: {
            color: colors.grid,
          },
        },
        x: {
          grid: {
            display: false,
          },
          ticks: {
            color: colors.text,
          },
        },
      },
    },
  });
}

// Update charts when theme changes
function updateChartsTheme() {
  if (radarChart && barChart) {
    radarChart.destroy();
    barChart.destroy();
    initializeCharts();
  }
}

// Setup download links
function setupDownloadLinks() {
  // Download handlers
  document.getElementById('downloadTex').addEventListener('click', e => {
    e.preventDefault();
    downloadPaper('tex');
  });

  document.getElementById('downloadPdf').addEventListener('click', e => {
    e.preventDefault();
    downloadPaper('pdf');
  });

  document.getElementById('downloadBundle').addEventListener('click', e => {
    e.preventDefault();
    downloadPaper('bundle');
  });

  document.getElementById('technicalPaper').addEventListener('click', e => {
    e.preventDefault();
    downloadPaper('pdf');
  });
}

// Download paper in specified format
function downloadPaper(format) {
  const link = document.createElement('a');

  switch (format) {
    case 'tex':
      link.href = `${PAPERS_PATH}/awardbench_paper.tex`;
      link.download = 'awardbench_paper.tex';
      break;
    case 'pdf':
      link.href = `${PAPERS_PATH}/awardbench_paper.pdf`;
      link.download = 'awardbench_paper.pdf';
      break;
    case 'bundle':
      link.href = `${PAPERS_PATH}/awardbench_bundle.zip`;
      link.download = 'awardbench_bundle.zip';
      break;
  }

  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

// Setup smooth scroll
function setupSmoothScroll() {
  // Add smooth scroll behavior
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start',
        });
      }
    });
  });

  // Add intersection observer for metric discussion items
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px',
  };

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, observerOptions);

  // Observe metric discussion items
  document.querySelectorAll('.metric-discussion-item').forEach(item => {
    item.style.opacity = '0';
    item.style.transform = 'translateY(20px)';
    item.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(item);
  });
}

// Add hover effects to metric cards
document.querySelectorAll('.metric-card').forEach(card => {
  card.addEventListener('mouseenter', function () {
    this.style.transform = 'translateY(-4px)';
  });

  card.addEventListener('mouseleave', function () {
    this.style.transform = 'translateY(0)';
  });
});

// Add click-to-copy functionality for code blocks
document.querySelectorAll('.code-block, .metric-example').forEach(block => {
  block.style.cursor = 'pointer';
  block.title = 'Click to copy';

  block.addEventListener('click', function () {
    const text = this.textContent.trim();
    navigator.clipboard.writeText(text).then(() => {
      const originalBg = this.style.background;
      this.style.background = 'rgba(0, 166, 126, 0.1)';
      setTimeout(() => {
        this.style.background = originalBg;
      }, 300);
    });
  });
});
