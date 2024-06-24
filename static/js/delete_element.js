function deleteItem(id) {
    var element = document.getElementById(id);
    element.parentNode.removeChild(element);
    console.log('Deleted');
}