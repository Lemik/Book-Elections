// Mobile Menu
const mobileMenuToggle = document.getElementById('mobileMenuToggle');
const mobileMenuOverlay = document.getElementById('mobileMenuOverlay');
const navLinks = document.querySelector('.nav-links');

function toggleMobileMenu() {
    mobileMenuToggle.classList.toggle('active');
    mobileMenuOverlay.classList.toggle('active');
    navLinks.classList.toggle('active');
}

mobileMenuToggle.addEventListener('click', toggleMobileMenu);
mobileMenuOverlay.addEventListener('click', toggleMobileMenu);

// Scroll Animations
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe elements with animation classes
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    animatedElements.forEach(element => {
        observer.observe(element);
    });
});

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Newsletter Form Validation
const newsletterForm = document.querySelector('.newsletter-form');
if (newsletterForm) {
    newsletterForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const emailInput = this.querySelector('input[type="email"]');
        const email = emailInput.value.trim();
        
        if (!email) {
            showFormError(emailInput, 'Please enter your email address');
            return;
        }
        
        if (!isValidEmail(email)) {
            showFormError(emailInput, 'Please enter a valid email address');
            return;
        }
        
        // Submit form
        this.submit();
    });
}

function showFormError(input, message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'form-error';
    errorDiv.textContent = message;
    
    const existingError = input.parentNode.querySelector('.form-error');
    if (existingError) {
        existingError.remove();
    }
    
    input.parentNode.appendChild(errorDiv);
    input.classList.add('error');
    
    setTimeout(() => {
        errorDiv.remove();
        input.classList.remove('error');
    }, 3000);
}

function isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Feedback Button
const feedbackButton = document.querySelector('.feedback-button');
if (feedbackButton) {
    feedbackButton.addEventListener('click', function() {
        const feedbackModal = document.createElement('div');
        feedbackModal.className = 'feedback-modal';
        feedbackModal.innerHTML = `
            <div class="feedback-content">
                <h3>Did you enjoy the book?</h3>
                <div class="feedback-buttons">
                    <button class="feedback-yes">Yes</button>
                    <button class="feedback-no">No</button>
                </div>
                <button class="close-modal">&times;</button>
            </div>
        `;
        
        document.body.appendChild(feedbackModal);
        
        // Handle feedback
        feedbackModal.querySelector('.feedback-yes').addEventListener('click', () => {
            submitFeedback(true);
            feedbackModal.remove();
        });
        
        feedbackModal.querySelector('.feedback-no').addEventListener('click', () => {
            submitFeedback(false);
            feedbackModal.remove();
        });
        
        feedbackModal.querySelector('.close-modal').addEventListener('click', () => {
            feedbackModal.remove();
        });
    });
}

function submitFeedback(isPositive) {
    // Here you would typically send the feedback to your backend
    console.log('Feedback submitted:', isPositive ? 'Positive' : 'Negative');
    // Show thank you message
    const thankYouMessage = document.createElement('div');
    thankYouMessage.className = 'thank-you-message';
    thankYouMessage.textContent = 'Thank you for your feedback!';
    document.body.appendChild(thankYouMessage);
    
    setTimeout(() => {
        thankYouMessage.remove();
    }, 3000);
} 