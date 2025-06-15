// Footer component - loads consistent footer across all pages
document.addEventListener('DOMContentLoaded', function() {
    const footerHTML = `
        <footer>
            <small>© 2025 Massimiliano Gargano</small>
        </footer>
    `;
    
    // Find existing footer and replace it, or add to body if none exists
    const existingFooter = document.querySelector('footer');
    if (existingFooter) {
        existingFooter.outerHTML = footerHTML;
    } else {
        // Insert before the closing body tag
        document.body.insertAdjacentHTML('beforeend', footerHTML);
    }
});