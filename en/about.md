---
layout: default
title: About the book
lang: en
---

<div class="about-container">
    <header class="about-header">
        <div class="language-switcher">
            <a href="{{ '/uk/' | relative_url }}">УКР</a>
            <span class="separator">|</span>
            <a href="{{ '/en/' | relative_url }}">ENG</a>
            <span class="separator">|</span>
            <a href="{{ '/ru/' | relative_url }}">РУС</a>
            <span class="separator">|</span>
            <a href="{{ '/en/about' | relative_url }}" class="active">About</a>
        </div>
        <h1>About the book</h1>
    </header>

    <div class="about-content">
        <section class="about-section">
            <h2>Authors</h2>
            <ul class="authors-list">
                {% for author in site.authors %}
                <li>{{ author }}</li>
                {% endfor %}
            </ul>
        </section>

        <section class="about-section">
            <h2>About the project</h2>
            <p>This site publishes <em>Elections: Technologies of election campaigns</em> — a structured handbook on running election campaigns. The complete book text is available in Ukrainian and Russian; English pages currently offer navigation and pointers to those editions.</p>
        </section>

        <section class="about-section">
            <h2>Languages</h2>
            <p>Use the header or the links on this page to switch between <a href="{{ '/en/' | relative_url }}">English</a>, <a href="{{ '/uk/' | relative_url }}">Ukrainian</a>, and <a href="{{ '/ru/' | relative_url }}">Russian</a> table of contents.</p>
        </section>

        <section class="about-section">
            <h2>Contact</h2>
            <p>We welcome suggestions and corrections. Contact: <a href="mailto:ElectionsBook@dushyn.com">ElectionsBook@dushyn.com</a>.</p>
        </section>
    </div>
</div>

<style>
.about-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
}

.about-header {
    text-align: center;
    margin-bottom: 3rem;
}

.language-switcher {
    margin-bottom: 2rem;
}

.language-switcher a {
    text-decoration: none;
    color: #666;
    padding: 5px 10px;
}

.language-switcher a.active {
    color: #000;
    font-weight: bold;
}

.language-switcher .separator {
    color: #ccc;
    margin: 0 5px;
}

.about-content {
    line-height: 1.6;
}

.about-section {
    margin-bottom: 2.5rem;
    padding: 1.5rem;
    background: #f9f9f9;
    border-radius: 8px;
    transition: transform 0.3s ease;
}

.about-section:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.about-section h2 {
    color: #333;
    margin-bottom: 1rem;
    font-size: 1.5rem;
}

.about-section p {
    color: #555;
    margin: 0;
}
</style>
