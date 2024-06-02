document.addEventListener('DOMContentLoaded', function() {
    const dropdown = document.querySelector('.dropdown');
    const select = dropdown.querySelector('.select');
    const caret = dropdown.querySelector('.caret');
    const menu = dropdown.querySelector('.menu');
    const options = dropdown.querySelectorAll('.menu li');
    const selected = dropdown.querySelector('.selected');
    const submitBtn = document.getElementById('submitBtn');

    // Set default text
    selected.innerText = 'Select';

    select.addEventListener('click', () => {
        select.classList.toggle('select-clicked');
        caret.classList.toggle('caret-rotate');
        menu.classList.toggle('menu-open');
    });

    options.forEach(option => {
        option.addEventListener('click', () => {
            selected.innerText = option.innerText;
            select.classList.remove('select-clicked');
            caret.classList.remove('caret-rotate');
            menu.classList.remove('menu-open');
            options.forEach(option => {
                option.classList.remove('active');
            });
            option.classList.add('active');
        });
    });

    submitBtn.addEventListener('click', () => {
        const selectedCompany = selected.innerText.toLowerCase().replace(/ /g, '-');
        if (selectedCompany !== 'select') {
            window.location.href = /${selectedCompany}/; // Adjust URL as needed
        } else {
            alert('Please select a company');
        }
    });
});