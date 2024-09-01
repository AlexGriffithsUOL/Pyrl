function display_by_id(id, string) {
    var x = document.getElementById(id);
    if (x.classList.contains(string)) {
        x.classList.remove(string);
    } else {
        x.classList.add(string);
    }
}

function pivot_by_id(id, string1, string2) {
    var x = document.getElementById(id);
    if (x.classList.contains(string1)) {
        x.classList.remove(string1);
        x.classList.add(string2);
    } else if (x.classList.contains(string2)) {
        x.classList.remove(string2);
        x.classList.add(string1);
    }
}