function clear_element_by_id(id, password) {
    if (password == 'password') {
        document.getElementById(`${id}`).type = password;
    } else {
        console.log('Not password');
    }
    document.getElementById(`${id}`).value = '';
}