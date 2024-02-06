jQuery(function() {
    const $modal = $("#suppliersModal");

    $modal.on("show.bs.modal", function(e) {
        const $button = $(e.relatedTarget);

        const url = $button.data("url");

        fetch(url)
            .then(response => response.json())
            .then(suppliers => {
                const $suppliersTableBody = $("#suppliersTableBody");
                $suppliersTableBody.empty();

                suppliers.forEach(supplier => {
                    const $row = $("<tr></tr>");
                    $row.append($("<td>").text(supplier.name));
                    $row.append($("<td>").text(supplier.cost_price));

                    $suppliersTableBody.append($row);
                })
            })
            .catch(console.error)
    });
});