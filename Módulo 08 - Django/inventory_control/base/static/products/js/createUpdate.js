jQuery(function () {
  const $addButton = $("#addSupplierButton");
  const $formsetContainer = $("#supplierFormset");
  const $totalForms = $("#id_supplierproduct_set-TOTAL_FORMS");
  const $originalForm = $formsetContainer.children(".row:first").clone(true);

  $addButton.on("click", function () {
    const $newRow = $originalForm.clone(true);
    const formIndex = parseInt($totalForms.val());

    $newRow.find(":input[name]").each(function () {
      const name = $(this).attr("name").replace("-0-", `-${formIndex}-`);
      const id = "id_" + name;
      $(this).attr({ name: name, id: id }).val("");
    });

    $totalForms.val(formIndex + 1);
    $formsetContainer.append($newRow);
  });

  $formsetContainer.on("click", ".remove-btn", function () {
    const $button = $(this);

    $button.closest(".row").remove();
    $totalForms.val(parseInt($totalForms.val()) - 1);

    const url = $button.data("url");

    if (url) {
      fetch(url, {
        method: "DELETE",
        headers: {
          "X-CSRFToken": Cookies.get("csrftoken"),
        },
      })
        .then((res) => res.json())
        .then((data) => console.log(data))
        .catch(console.error);
    }
  });
});
