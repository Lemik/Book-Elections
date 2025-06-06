# Book Website

A modern, responsive Jekyll website for showcasing and distributing a book, with features for collecting reader feedback and support.

## Features

- 📱 Responsive, mobile-first design
- 📚 Multiple reading formats (online, PDF, EPUB)
- 💬 Reader feedback system
- 📧 Newsletter integration
- 💰 Multiple payment options for support
- 🌙 Dark mode support
- 📊 SEO optimized
- 🎨 Modern, clean design

## Setup

1. Install Ruby and Jekyll:
   ```bash
   gem install jekyll bundler
   ```

2. Clone this repository:
   ```bash
   git clone [repository-url]
   cd [repository-name]
   ```

3. Install dependencies:
   ```bash
   bundle install
   ```

4. Start the development server:
   ```bash
   bundle exec jekyll serve
   ```

5. Visit `http://localhost:4000` in your browser

## Customization

### Configuration

Edit `_config.yml` to customize:
- Site title and description
- Feature flags
- Social media links
- Payment integration settings

### Content

1. Book Content:
   - Place your book content in `_book/` directory
   - Each chapter should be a separate Markdown file
   - Update `book.html` to include your content

2. Images:
   - Place all images in `assets/images/`
   - Update image paths in templates

3. Testimonials:
   - Add testimonials in `_testimonials/` directory
   - Each testimonial should be a Markdown file with front matter

### Styling

- Main styles are in `assets/css/main.scss`
- Customize colors, fonts, and layout in the SCSS variables
- Add custom styles in the same file

### Features

Enable/disable features in `_config.yml`:
```yaml
features:
  testimonials: true
  newsletter: true
  blog: true
  feedback: true
```

## Deployment

### GitHub Pages

1. Push your repository to GitHub
2. Enable GitHub Pages in repository settings
3. Select the main branch as source

### Netlify

1. Connect your GitHub repository to Netlify
2. Set build command: `bundle exec jekyll build`
3. Set publish directory: `_site`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact [your-email@example.com]. 