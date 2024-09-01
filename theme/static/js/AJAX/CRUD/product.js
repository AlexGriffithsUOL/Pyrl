function display_product_form(product_id) {
    if (document.getElementById(`bottom-contents-${product_id}`)) {
        //toggle_display_card(product_id);
        display_by_id(`bottom-contents-${product_id}`, 'hidden');
    } else {
        $.ajax({
            type: 'GET',
            url: `{% url 'main_app:products:product_info'%}`,
            headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},
            mode: 'same-origin', // Do not send CSRF token to another domain.
            data: {
                product_id: product_id,
            },
            success: function (data) {
                $(`#contents-${product_id}`).html(data);
            }
        })
    }
}

function delete_product(product_id) {
    console.log(product_id);
    if (document.getElementById(`bottom-contents-${product_id}`)) {
        $.ajax({
            type: 'POST',
            headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},
            url: "{% url 'main_app:products:delete' %}",
            mode: 'same-origin', // Do not send CSRF token to another domain.
            data: {
                product_id: product_id,
                action: 'post'
            },
        })
    }
    var element = document.getElementById(`product-card-${product_id}`);
    console.log(`product-card-${product_id}`);
    element.remove();
}


function save_product(product_id) {
    var form = document.getElementById(`product-form-${product_id}`);
    console.log(form);
    $.ajax({
        type: 'POST',
        headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()},
        url: "{% url 'main_app:products:create' %}",
        mode: 'same-origin', // Do not send CSRF token to another domain.
        data: {
            product_name: $(`#name-${product_id}`).val(),
            product_description: $(`#description-${product_id}`).val(),
            product_price: $(`#price-${product_id}`).val(),
            product_category: $(`#category-${product_id}`).val(),
            action: 'post'
        },
    })
    window.location.reload();
}
