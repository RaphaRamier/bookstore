document.addEventListener('DOMContentLoaded', function() {
    const closeButton = document.getElementById('close-button');
    const saveAndCreateAnotherButton = document.getElementById('save-and-create-another');
    const assetForm = document.getElementById('asset-form');

    closeButton.addEventListener('click', function() {
        window.history.back();
    });

    saveAndCreateAnotherButton.addEventListener('click', function() {
        saveAndCreateAnother();
    });

    function saveAndCreateAnother() {
        const formData = new FormData(assetForm);

        fetch(assetForm.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Clear the form fields to allow entering a new item
                assetForm.reset();
                // Optionally, show a success message
                alert('Item saved! You can add another item.');
            } else {
                // Handle form validation errors here
                alert('Error saving item. Please check the form and try again.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        });
    }
});
