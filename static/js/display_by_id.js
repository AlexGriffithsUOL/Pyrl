function display_by_id(id, string) {
    var x = document.getElementById(id);
    if (x.classList.contains(string)) {
        x.classList.remove(string);
    } else {
        x.classList.add(string);
    }
}