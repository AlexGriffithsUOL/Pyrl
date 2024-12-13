function clear_element_by_id(id, password) {
    if (password === 'password' | password === 'confirm_password') {
        document.getElementById(`${id}`).type = 'password';
    }
    document.getElementById(`${id}`).value = '';
}

function refill(id, text) {
    element = document.getElementById(`${id}`);
    if ((element.type === 'password') && (element.value === '')) {
        document.getElementById(`${id}`).value = 'password';
    } else if (element.value === '') {
        document.getElementById(`${id}`).value = text;
    }
}