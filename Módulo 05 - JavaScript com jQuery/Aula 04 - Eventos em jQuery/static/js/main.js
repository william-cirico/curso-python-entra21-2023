$(document).ready(() => {
    const $form = $("#addTaskForm");
    const $modal = new bootstrap.Modal("#addTaskModal");
    const $descriptionInput = $("#descriptionInput");
    const $boardSelect = $("#boardSelect");

    /**
     * Cria um novo botão com um ícone e um manipulador de clique associado
     * @param {string} iconClass - classe do ícone
     * @param {string} btnClasses - classes do botão
     * @param {Function} clickHandler 
     * @returns {JQuery} retorna um elemento de botão jQuery
     */
    const createIconButton = (iconClass, btnClasses, clickHandler) => {
        const $button = $("<button></button>").addClass(btnClasses);
        const $icon = $("<i></i>").addClass(iconClass);
        $button.append($icon);
        $button.click(clickHandler);

        return $button;
    };

    /**
     * Função para adicionar uma tarefa a um quadro Kanban
     * @param {string} description - descrição da tarefa 
     * @param {string} board - ID do quadro onde a tarefa deve ser adicionada
     */
    const addTaskToBoard = (description, board) => {
        const $newTask = $("<div></div>").addClass("kanban-item");
        const $taskText = $("<span></span>").text(description);

        const $editButton = createIconButton("bi bi-pencil", "btn btn-warning btn-sm", () => {
            const editedText = prompt("Nova descrição", description);
            if (editedText !== null) {
                $taskText.text(editedText);
            }
        });

        const $deleteButton = createIconButton("bi bi-x", "btn btn-danger btn-sm", () => $newTask.remove());

        const $buttonsContainer = $("<div></div>").addClass("d-flex column-gap-2");
        $buttonsContainer.append($editButton, $deleteButton);

        $newTask.append($taskText, $buttonsContainer);
        $(`#${board}`).append($newTask);
    }

    // Evento para submissão do formulário
    $form.submit(event => {
        event.preventDefault();

        // Verifica se o formulário é válido
        if ($form[0].checkValidity()) {
            addTaskToBoard($descriptionInput.val(), $boardSelect.val());
            $form[0].reset(); // Reseta o formulário
            $modal.hide(); // Fecha o modal
            $form.removeClass("was-validated"); // Remove a classe de validação
        } else {
            $form.addClass("was-validated"); // Se o formulário não é válido, adiciona a classe de validação
        }
    });

    // Permite que as tarefas sejam arrastadas e soltas entre os quadros Kanban
    $(".kanban-column").sortable({
        connectWith: ".kanban-column",
        cursor: "grab"
    }).disableSelection();
});