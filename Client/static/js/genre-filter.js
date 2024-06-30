document.addEventListener('DOMContentLoaded', function () {
    const genreButtons = document.querySelectorAll('.genre-filter');
    const bookItems = document.querySelectorAll('.book-item');

    genreButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            e.preventDefault();
            const genreId = this.getAttribute('data-genre');

            bookItems.forEach(book => {
                if (genreId === 'all') {
                    book.style.display = 'block';
                } else {
                    const bookGenreIds = book.getAttribute('data-genre-ids').split(',');
                    if (bookGenreIds.includes(genreId)) {
                        book.style.display = 'block';
                    } else {
                        book.style.display = 'none';
                    }
                }
            });

            // Update active class for buttons
            genreButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
        });
    });
});
