jQuery(function() {
    const $enabledCheckbox = $(".form-check-input");

    $enabledCheckbox.on("click", function() {
        const url = $(this).data("url");

        fetch(url, {
            method: "POST",
            headers: {
                "X-CSRFToken": Cookies.get("csrftoken")
            }
        })
        .then(res => res.json())
        .then(data => console.log(data))
        .catch(console.error);
    });
});