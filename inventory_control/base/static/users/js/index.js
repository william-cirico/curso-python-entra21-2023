jQuery(function() {
    $(".form-check-input").on("click", function() {
        const url = $(this).data("url");

        fetch(url, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": Cookies.get("csrftoken")
            }
        })
        .catch(err => alert(`Falha ao habilitar/desabilitar usuário: ${err.message}`));
    });
});