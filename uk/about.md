---
layout: default
title: Про книгу
lang: uk
---

<div class="about-container">
    <header class="about-header">
        <div class="language-switcher">
            <a href="{{ '/uk/' | relative_url }}">УКР</a>
            <span class="separator">|</span>
            <a href="{{ '/ru/' | relative_url }}">РУС</a>
            <span class="separator">|</span>
            <a href="{{ '/uk/about' | relative_url }}" class="active">Про книгу</a>
        </div>
        <h1>Про книгу</h1>
    </header>

    <div class="about-content">
        <section class="about-section">
            <h2>Про проект</h2>
            <p>Ця книга є результатом спільної роботи авторів, які хочуть поділитися своїми думками та досвідом. Ми віримо, що знання повинні бути доступними для всіх, незалежно від мови чи географічного розташування.</p>
        </section>

        <section class="about-section">
            <h2>Мета</h2>
            <p>Нашою метою є створення простору, де кожен може знайти корисну інформацію та надихнутися новими ідеями. Ми прагнемо до того, щоб наш контент був зрозумілим, доступним та корисним для всіх читачів.</p>
        </section>

        <section class="about-section">
            <h2>Мультимовність</h2>
            <p>Книга доступна українською та російською мовами, що дозволяє нам охопити ширшу аудиторію та зробити контент доступним для більшої кількості читачів.</p>
        </section>

        <section class="about-section">
            <h2>Зворотній зв'язок</h2>
            <p>Ми завжди відкриті до ваших пропозицій та коментарів. Якщо у вас є ідеї щодо покращення нашого проекту, будь ласка, зв'яжіться з нами.</p>
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