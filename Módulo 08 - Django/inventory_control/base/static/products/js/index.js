jQuery(function() {
    const $enabledCheckbox = $(".form-check-input");
    const $modal = $("#suppliersModal");

    $enabledCheckbox.on("click", function() {
        const url = $(this).data("url");

        fetch(url, {
            method: "PUT",
            headers: {
                "X-CSRFToken": Cookies.get("csrftoken")
            }
        })
        .catch(err => alert("Não foi possível atualizar o status do produto: " + err.message));
    });

    $modal.on("show.bs.modal", function (event) {
        const $button = $(event.relatedTarget); // Botão que acionou o modal
        const url = $button.data("url"); // Extrai o ID do produto do atributo data
      
        fetch(url)
        .then(res => res.json())
        .then(suppliers => {
            // Implemente a criação de uma tabela com nome e preço de custo de cada fornecedor
            const $suppliersTable = $("#suppliersTable");
            $suppliersTable.empty(); // Limpa a tabela existente

            suppliers.forEach(record => {
                // Cria uma nova linha para cada fornecedor
                const $row = $("<tr>");
                $row.append($("<td>").text(record.supplier));
                $row.append($("<td>").text(record.price));

                // Adiciona a linha à tabela
                $suppliersTable.append($row);
            });
        })
        .catch(console.error);
    });
});