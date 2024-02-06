jQuery(function() {
    const $enabledCheckbox = $(".form-check-input");

    $enabledCheckbox.on("click", function() {
        const url = $(this).data("url");

        fetch(url, {
            method: "PUT",
            headers: {
                "X-CSRFToken": Cookies.get("csrftoken")
            }
        })
        .catch(err => alert(`Falha ao atualizar o status do fornecedor: ${err.message}`));
    });
});