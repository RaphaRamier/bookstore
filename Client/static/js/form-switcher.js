document.addEventListener('DOMContentLoaded', function() {
    const itemTypes = document.querySelectorAll('input[name="item-type"]');
    const formTypes = document.querySelectorAll('.form-type');

    itemTypes.forEach(itemType => {
        itemType.addEventListener('change', function() {
            formTypes.forEach(formType => {
                if (formType.id.includes(this.value)) {
                    formType.style.display = 'block';
                } else {
                    formType.style.display = 'none';
                }
            });
        });
    });

    // Trigger the change event to display the initial form
    document.querySelector('input[name="item-type"]:checked').dispatchEvent(new Event('change'));
});
