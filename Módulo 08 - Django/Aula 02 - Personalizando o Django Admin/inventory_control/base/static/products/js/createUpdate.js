jQuery(function() {
    const $addButton = $("#addSupplierButton");
    const $suppliersContainer = $("#supplierFormset");
    const $totalSuppliers = $("#id_supplierproduct_set-TOTAL_FORMS");

    const $originalSupplier = $suppliersContainer.children(".row:first").clone(true);

    $addButton.on("click", function() {
        const $newRow = $originalSupplier.clone(true);
        const index = parseInt($totalSuppliers.val());

        $newRow.find(":input[name]").each(function() {
            const name = $(this).attr("name").replace("-0-", `-${index}-`);
            const id = "id_" + name;

            $(this).attr({ name, id }).val("");
        });

        $totalSuppliers.val(index + 1);
        $suppliersContainer.append($newRow);
    });

    $suppliersContainer.on("click", ".remove-btn", function() {
        const $button = $(this);

        $button.closest(".row").remove();
        $totalSuppliers.val(parseInt($totalSuppliers.val()) - 1);
    });
});