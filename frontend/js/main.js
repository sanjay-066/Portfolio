/* =============================================
   PORTFOLIO JS — main.js
   Sanjay N | Full Stack Developer Portfolio
   ============================================= */

// ===== CONFIGURATION =====
// Change this to your deployed Django backend URL when going live
const API_BASE = 'http://localhost:8000/api';

// ===== DOM READY =====
document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initTypingEffect();
  initScrollReveal();
  initContactForm();
  loadPortfolioData();
});

// ===== NAVBAR =====
function initNavbar() {
  const navbar = document.getElementById('navbar');
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');
  const links = document.querySelectorAll('.nav-link');

  // Scroll shadow
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 20);
    updateActiveLink();
  }, { passive: true });

  // Mobile toggle
  navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
  });

  // Close mobile nav on link click
  links.forEach(link => {
    link.addEventListener('click', () => navLinks.classList.remove('open'));
  });
}

function updateActiveLink() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');
  let current = '';

  sections.forEach(section => {
    const top = section.offsetTop - 100;
    if (window.scrollY >= top) current = section.id;
  });

  navLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === `#${current}`) {
      link.classList.add('active');
    }
  });
}

// ===== TYPING EFFECT =====
function initTypingEffect() {
  const el = document.getElementById('typedText');
  if (!el) return;

  const texts = [
    'Full Stack Developer',
    'Python Developer',
    'AI Enthusiast',
    'Problem Solver',
  ];

  let textIndex = 0;
  let charIndex = 0;
  let isDeleting = false;
  let delay = 120;

  function type() {
    const current = texts[textIndex];
    if (isDeleting) {
      el.textContent = current.substring(0, charIndex - 1);
      charIndex--;
      delay = 60;
    } else {
      el.textContent = current.substring(0, charIndex + 1);
      charIndex++;
      delay = 120;
    }

    if (!isDeleting && charIndex === current.length) {
      delay = 2000;
      isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      textIndex = (textIndex + 1) % texts.length;
      delay = 400;
    }

    setTimeout(type, delay);
  }

  type();
}

// ===== SCROLL REVEAL =====
function initScrollReveal() {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
          // Stagger child reveals
          entry.target.style.transitionDelay = `${i * 0.05}s`;
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
  );

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
}

// ===== CONTACT FORM =====
function initContactForm() {
  const form = document.getElementById('contactForm');
  const msgEl = document.getElementById('formMessage');
  const submitBtn = document.getElementById('submitBtn');

  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';

    try {
      const response = await fetch(`${API_BASE}/contact/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        showFormMessage(msgEl, '✅ Your message has been sent! I\'ll get back to you soon.', 'success');
        form.reset();
      } else {
        const err = await response.json();
        showFormMessage(msgEl, `❌ Error: ${JSON.stringify(err)}`, 'error');
      }
    } catch (error) {
      // If backend isn't running, show a friendly message
      showFormMessage(
        msgEl,
        '⚠️ Backend server not reachable. To test locally, start the Django server. Your message was not sent.',
        'error'
      );
    } finally {
      submitBtn.disabled = false;
      submitBtn.innerHTML = '<i class="fas fa-paper-plane"></i> Send Message';
    }
  });
}

function showFormMessage(el, message, type) {
  el.textContent = message;
  el.className = `form-message ${type}`;
  el.classList.remove('hidden');
  setTimeout(() => el.classList.add('hidden'), 6000);
}

// ===== LOAD PORTFOLIO DATA FROM API =====
async function loadPortfolioData() {
  // Try to load from API; silently fall back to static HTML if unavailable
  try {
    await Promise.allSettled([
      loadProjects(),
      loadSkills(),
      loadExperience(),
      loadEducation(),
    ]);
  } catch (e) {
    console.info('Portfolio: Using static fallback data (backend not connected).');
  }
}

// ===== PROJECTS =====
async function loadProjects() {
  const grid = document.getElementById('projectsGrid');
  if (!grid) return;

  const res = await fetch(`${API_BASE}/projects/`);
  if (!res.ok) return;

  const projects = await res.json();
  if (!projects.length) return;

  grid.innerHTML = '';
  projects.forEach((p, i) => {
    const techTags = (p.tech_stack || '').split(',').map(t =>
      `<span class="tech-tag">${t.trim()}</span>`
    ).join('');

    const card = document.createElement('div');
    card.className = 'project-card reveal';
    card.style.transitionDelay = `${i * 0.1}s`;
    card.innerHTML = `
      <div class="project-card-header">
        <i class="fas fa-folder-open project-icon"></i>
        <div class="project-links">
          ${p.github_url ? `<a href="${p.github_url}" target="_blank" title="GitHub"><i class="fab fa-github"></i></a>` : ''}
          ${p.live_url ? `<a href="${p.live_url}" target="_blank" title="Live Demo"><i class="fas fa-external-link-alt"></i></a>` : ''}
        </div>
      </div>
      <h3 class="project-title">${escHtml(p.title)}</h3>
      <p class="project-desc">${escHtml(p.description)}</p>
      <div class="project-tech">${techTags}</div>
    `;
    grid.appendChild(card);
  });

  // Trigger reveal for dynamically added elements
  grid.querySelectorAll('.reveal').forEach(el => {
    setTimeout(() => el.classList.add('visible'), 100);
  });

  // Update stat count
  const countEl = document.getElementById('projectCount');
  if (countEl) countEl.textContent = `${projects.length}+`;
}

// ===== SKILLS =====
async function loadSkills() {
  const container = document.getElementById('skillsContainer');
  if (!container) return;

  const res = await fetch(`${API_BASE}/skills/`);
  if (!res.ok) return;

  const skills = await res.json();
  if (!skills.length) return;

  // Group by category
  const grouped = skills.reduce((acc, skill) => {
    const cat = skill.category || 'General';
    if (!acc[cat]) acc[cat] = [];
    acc[cat].push(skill.name);
    return acc;
  }, {});

  const catIcons = {
    'Languages': 'fas fa-code',
    'Web Development': 'fas fa-layer-group',
    'Databases': 'fas fa-database',
    'Tools': 'fas fa-tools',
    'AI / ML': 'fas fa-robot',
    'General': 'fas fa-star',
  };

  container.innerHTML = '';
  Object.entries(grouped).forEach(([cat, skillNames], i) => {
    const icon = catIcons[cat] || 'fas fa-circle';
    const pills = skillNames.map(n => `<span class="skill-pill">${escHtml(n)}</span>`).join('');
    const div = document.createElement('div');
    div.className = 'skill-category reveal';
    div.style.transitionDelay = `${i * 0.1}s`;
    div.innerHTML = `
      <h3 class="skill-cat-title"><i class="${icon}"></i> ${escHtml(cat)}</h3>
      <div class="skill-pills">${pills}</div>
    `;
    container.appendChild(div);
  });

  container.querySelectorAll('.reveal').forEach(el => {
    setTimeout(() => el.classList.add('visible'), 100);
  });
}

// ===== EXPERIENCE =====
async function loadExperience() {
  const timeline = document.getElementById('experienceTimeline');
  if (!timeline) return;

  const res = await fetch(`${API_BASE}/experience/`);
  if (!res.ok) return;

  const experiences = await res.json();
  if (!experiences.length) return;

  timeline.innerHTML = '';
  experiences.forEach((exp, i) => {
    const tags = (exp.tech_stack || '').split(',').filter(Boolean).map(t =>
      `<span class="tech-tag">${t.trim()}</span>`
    ).join('');

    const item = document.createElement('div');
    item.className = 'timeline-item reveal';
    item.style.transitionDelay = `${i * 0.15}s`;
    item.innerHTML = `
      <div class="timeline-dot"></div>
      <div class="timeline-content">
        <div class="timeline-header">
          <h3 class="timeline-role">${escHtml(exp.role)}</h3>
          <span class="timeline-period">${escHtml(exp.duration)}</span>
        </div>
        <p class="timeline-company"><i class="fas fa-building"></i> ${escHtml(exp.company)}</p>
        <p class="timeline-desc">${escHtml(exp.description)}</p>
        ${tags ? `<div class="timeline-tags">${tags}</div>` : ''}
      </div>
    `;
    timeline.appendChild(item);
  });

  timeline.querySelectorAll('.reveal').forEach(el => {
    setTimeout(() => el.classList.add('visible'), 100);
  });
}

// ===== EDUCATION =====
async function loadEducation() {
  const grid = document.getElementById('educationGrid');
  if (!grid) return;

  const res = await fetch(`${API_BASE}/education/`);
  if (!res.ok) return;

  const education = await res.json();
  if (!education.length) return;

  const icons = ['fas fa-university', 'fas fa-school', 'fas fa-certificate'];

  grid.innerHTML = '';
  education.forEach((edu, i) => {
    const card = document.createElement('div');
    card.className = 'edu-card reveal';
    card.style.transitionDelay = `${i * 0.1}s`;
    card.innerHTML = `
      <div class="edu-icon"><i class="${icons[i % icons.length]}"></i></div>
      <div class="edu-content">
        <h3 class="edu-degree">${escHtml(edu.degree)}</h3>
        <p class="edu-institution">${escHtml(edu.institution)}</p>
        <p class="edu-year">${escHtml(edu.year)}</p>
        <p class="edu-desc">${escHtml(edu.description || '')}</p>
      </div>
    `;
    grid.appendChild(card);
  });

  grid.querySelectorAll('.reveal').forEach(el => {
    setTimeout(() => el.classList.add('visible'), 100);
  });
}

// ===== UTILITY =====
function escHtml(str) {
  if (!str) return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}
