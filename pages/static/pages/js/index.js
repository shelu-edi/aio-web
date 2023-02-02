let faq1_info = document.getElementById('faq-info-1');
let faq2_info = document.getElementById('faq-info-2');

function Faq1() {
    if (faq1_info.style.display === 'none') {
        faq1_info.style.display = 'block';
    } else {
        faq1_info.style.display = 'none';
    }
}

function Faq2() {
    if (faq2_info.style.display === 'none') {
        faq2_info.style.display = 'block';
    } else {
        faq2_info.style.display = 'none';
    }
}