$(document).on('submit', '#create-form', function(e) {
        e.preventDefault();
        $.ajax({
            type: 'post',
            headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},
            url: "{% url 'products:create' %}",
            mode: 'same-origin', // Do not send CSRF token to another domain.
            data: {
                product_name: $('#name').val(),
                product_brand: $('#brand').val(),
                product_description: $('#description').val(),
                product_price: $('#price').val(),
                product_image: $('#image').val(),
                product_category: $('#category').val(),
            },
            success: function (data) {
                console.log(data);
            }
        })
})