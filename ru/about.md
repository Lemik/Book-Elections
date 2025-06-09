---
layout: default
title: О книге
lang: ru
---

<div class="about-container">
    <header class="about-header">
        <div class="language-switcher">
            <a href="{{ '/uk/' | relative_url }}">УКР</a>
            <span class="separator">|</span>
            <a href="{{ '/ru/' | relative_url }}">РУС</a>
            <span class="separator">|</span>
            <a href="{{ '/ru/about' | relative_url }}" class="active">О книге</a>
        </div>
        <h1>О книге</h1>
    </header>

    <div class="about-content">
        <section class="about-section">
            <h2>О проекте</h2>
            <p>Эта книга является результатом совместной работы авторов, которые хотят поделиться своими мыслями и опытом. Мы верим, что знания должны быть доступны всем, независимо от языка или географического расположения.</p>
        </section>

        <section class="about-section">
            <h2>Цель</h2>
            <p>Нашей целью является создание пространства, где каждый может найти полезную информацию и вдохновиться новыми идеями. Мы стремимся к тому, чтобы наш контент был понятным, доступным и полезным для всех читателей.</p>
        </section>

        <section class="about-section">
            <h2>Многоязычность</h2>
            <p>Книга доступна на украинском и русском языках, что позволяет нам охватить более широкую аудиторию и сделать контент доступным для большего количества читателей.</p>
        </section>

        <section class="about-section">
            <h2>Обратная связь</h2>
            <p>Мы всегда открыты к вашим предложениям и комментариям. Если у вас есть идеи по улучшению нашего проекта, пожалуйста, свяжитесь с нами.</p>
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