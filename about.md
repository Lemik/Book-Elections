---
layout: default
title: About
---

<div class="about-landing-container">
    <header class="about-landing-header">
        <h1>About the Book</h1>
        <p class="subtitle">Choose your preferred language to learn more</p>
    </header>

    <div class="language-options">
        <a href="{{ '/uk/about' | relative_url }}" class="language-card">
            <div class="language-content">
                <h2>Українська</h2>
                <p>Прочитати українською мовою</p>
                <span class="arrow">→</span>
            </div>
        </a>

        <a href="{{ '/ru/about' | relative_url }}" class="language-card">
            <div class="language-content">
                <h2>Русский</h2>
                <p>Читать на русском языке</p>
                <span class="arrow">→</span>
            </div>
        </a>
    </div>

    <div class="quick-links">
        <a href="{{ '/' | relative_url }}" class="back-link">← Back to Home</a>
    </div>
</div>

<style>
.about-landing-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
    min-height: 80vh;
    display: flex;
    flex-direction: column;
}

.about-landing-header {
    text-align: center;
    margin-bottom: 4rem;
}

.about-landing-header h1 {
    font-size: 2.5rem;
    color: #333;
    margin-bottom: 1rem;
}

.subtitle {
    color: #666;
    font-size: 1.2rem;
}

.language-options {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    margin-bottom: 3rem;
}

.language-card {
    text-decoration: none;
    color: inherit;
    background: #f9f9f9;
    border-radius: 12px;
    padding: 2rem;
    transition: all 0.3s ease;
}

.language-card:hover {
    transform: translateX(10px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    background: #fff;
}

.language-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.language-content h2 {
    font-size: 1.8rem;
    color: #333;
    margin: 0;
}

.language-content p {
    color: #666;
    margin: 0.5rem 0 0 0;
}

.arrow {
    font-size: 1.5rem;
    color: #666;
    transition: transform 0.3s ease;
}

.language-card:hover .arrow {
    transform: translateX(5px);
}

.quick-links {
    margin-top: auto;
    padding-top: 2rem;
}

.back-link {
    color: #666;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    transition: color 0.3s ease;
}

.back-link:hover {
    color: #333;
}

@media (max-width: 600px) {
    .about-landing-container {
        padding: 1rem;
    }

    .about-landing-header h1 {
        font-size: 2rem;
    }

    .language-content {
        flex-direction: column;
        text-align: center;
        gap: 1rem;
    }

    .arrow {
        display: none;
    }
}
</style> 