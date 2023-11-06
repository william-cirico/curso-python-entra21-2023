$(document).ready(() => {
    // Referências de elementos do DOM
    const $taskForm = $("#taskForm");
    const $descriptionInput = $("#descriptionInput");
    const $expirationDateInput = $("#expirationDateInput");
    const $successToast = $("#successToast");
    const $taskList = $(".list-group");
    const $toggleCompletedButton = $("#toggleCompletedButton");

    // Instância do componente Toast do bootstrap
    const successToast = bootstrap.Toast.getOrCreateInstance($successToast);

    /** Salva as tarefas no localStorage */
    const saveTasksToLocalStorage = () => {
        const tasks = [];
        const $tasks = $(".list-group-item:not(.active)");

        $.each($tasks, (_, task) => {
            const $task = $(task);
            const description = $task.find("p").text();
            const expirationDate = $task.find("span").text().replace("Expira em: ", "");
            const isCompleted = $task.find("input[type='checkbox']").is(":checked");

            tasks.push({
                description,
                expirationDate,
                isCompleted
            });
        });

        localStorage.setItem("tasks", JSON.stringify(tasks));
    };

    /** Carrega as tarefas do localStorage e as adiciona à lista de tarefas */
    const loadTasksFromLocalStorage = () => {
        const tasks = JSON.parse(localStorage.getItem("tasks")) || [];

        // Adicionando cada tarefa salva à lista de tarefas
        tasks.forEach(task => {
            const $task = createTask(task.description, task.expirationDate);

            if (task.isCompleted) {
                $task.find("input[type='checkbox']").prop("checked", true);
            }

            $taskList.append($task);
        });
    };

    /** Define a data mínima de expiração para o input de data de expiração */
    const setMinExpirationDate = () => {
        const today = dayjs().format("YYYY-MM-DD");
        $expirationDateInput.attr("min", today);
    };

    /**
     * Gera um identificador aleatório para o uso em IDs de elementos HTML
     * @param {string} prefix - Prefixo opcional para o identificador
     * @returns {string} Um identificador único
     */
    const generateRandomId = (prefix = "") => prefix + Math.random().toString(36).substring(2, 9);

    /**
     * Cria um botão de ícone com manipulador de clique associado
     * @param {string} iconClasses - Classes para o ícone do botão
     * @param {string} btnClasses - Classes para o botão
     * @param {Function} clickHandler - Função a ser chamada no evento de clique
     * @returns {jQuery} O botão jQuery criado
     */
    const createIconButton = (iconClasses, btnClasses, clickHandler) => {
        const $button = $("<button></button>").addClass(btnClasses);
        const $icon = $("<i></i>").addClass(iconClasses);
        $button.append($icon);
        $button.on("click", clickHandler);

        return $button;
    };

    /**
     * Encerra a edição de uma tarefa e atualiza o localStorage
     * @param {jQuery} $task - O elemento jQuery da tarefa que está sendo editada.
     */
    const endEditTask = ($task) => {
        const $descriptionInput = $task.find("input.form-control[type='text']");
        const $expirationDateInput = $task.find("input.form-control[type='date']");

        const $description = $("<p class='fs-6 mb-0'></p>").text($descriptionInput.val());
        const $expirationDate = $("<span class='text-secondary'></span>").text(`Expira em: ${dayjs($expirationDateInput.val()).format("DD/MM/YYYY")}`);

        $descriptionInput.replaceWith($description);
        $expirationDateInput.replaceWith($expirationDate);

        const $editButton = createIconButton("bi bi-pencil", "btn btn-warning btn-sm", () => startEditTask($task));
        const $removeButton = createIconButton("bi bi-x-lg", "btn btn-danger btn-sm", () => $task.remove());

        const $buttonDiv = $task.find("div:nth-of-type(2)");
        $buttonDiv.empty().append($editButton, $removeButton);
    };

    /**
     * Inicia a edição de uma tarefa, substituindo parágrafos e spans por inputs
     * @param {jQuery} $task - O elmento jQuery da tarefa que vai entrar em modo de edição
     */
    const startEditTask = ($task) => {
        const $description = $task.find("p");
        const $expirationDate = $task.find("span");

        const currentDescription = $description.text();
        const currentExpiration = dayjs($expirationDate.text().replace("Expira em: ", ""), "DD/MM/YYYY").format("YYYY-MM-DD");

        const $descriptionInput = $("<input>", {
            "class": "form-control mb-2",
            type: "text",
            value: currentDescription
        });
        const $expirationDateInput = $("<input>", {
            "class": "form-control",
            type: "date",
            value: currentExpiration
        });

        const $saveButton = $("<button class='btn btn-success btn-sm'>Salvar</button>");
        const $cancelButton = $("<button class='btn btn-secondary btn-sm'>Cancelar</button>");

        $saveButton.on("click", () => {
            $description.text($descriptionInput.val());
            const formattedDate = dayjs($expirationDateInput.val()).format("DD/MM/YYYY");
            $expirationDate.text(`Expira em: ${formattedDate}`);
            endEditTask($task);
        });

        $cancelButton.on("click", () => endEditTask($task));

        $description.replaceWith($descriptionInput);
        $expirationDate.replaceWith($expirationDateInput);

        const $buttonDiv = $task.find("div:nth-of-type(2)");
        $buttonDiv.empty().append($saveButton, $cancelButton);
    };

    /**
     * Cria a representação DOM de uma tarefa e retorna o elemento jQuery
     * @param {string} description - Descrição da tarefa
     * @param {string} expirationDate - Data de expiração da tarefa
     * @returns {jQuery} O elemento jQuery da nova tarefa
     */
    const createTask = (description, expirationDate) => {
        const $li = $('<li class="list-group-item d-flex justify-content-between align-items-center"></li>');

        // Criando os elementos do checkbox
        const $checkboxDiv = $("<div>", {
            "class": "form-check d-flex align-items-center column-gap-2 checkbox-xl"
        });
        const checkboxId = generateRandomId("checkbox_");
        const $checkbox = $("<input>", {
            "class": "form-check-input",
            type: "checkbox",
            id: checkboxId
        });

        const $label = $("<label class='form-check-label'></label>").attr("for", checkboxId);
        const $description = $("<p class='fs-6 mb-0'></p>").text(description);
        const $expirationDate = $("<span class='text-secondary'></span>").text(`Expira em: ${expirationDate}`);
        $label.append($description, ' ', $expirationDate);
        $checkboxDiv.append($checkbox, $label);

        // Criando os botões de editar e excluir
        const $buttonDiv = $("<div class='d-flex column-gap-2'></div>");
        const $editButton = createIconButton("bi bi-pencil", "btn btn-warning btn-sm", () => startEditTask($li));
        const $removeButton = createIconButton("bi bi-x-lg", "btn btn-danger btn-sm", () => $li.remove());
        $buttonDiv.append($editButton, $removeButton);

        // Adicionando o checkbox e o botão na div
        $li.append($checkboxDiv, $buttonDiv);

        return $li;
    };

    // Configuração do evento de envio do formulário de tarefa
    $taskForm.on("submit", event => {
        event.preventDefault();

        if (!$taskForm[0].checkValidity()) {
            $taskForm.addClass("was-validated");
            return;
        }

        // Obtendo os valores do formulário
        const description = $descriptionInput.val();
        const expirationDate = dayjs($expirationDateInput.val()).format("DD/MM/YYYY");

        // Criando a tarefa
        const $task = createTask(description, expirationDate);

        // Inserindo a tarefa na lista
        $taskList.append($task);

        // Mostrando o toast de sucesso
        successToast.show();

        // Removendo a classe de expiração
        $taskForm.removeClass("was-validated");
        $taskForm[0].reset();
    });

    // Alternância da exibição de tarefas concluídas
    $toggleCompletedButton.on("click", function () {
        const isShowingCompleted = $(this).data("showing-completed");

        if (isShowingCompleted) {
            // Se estamos atualmente mostrando tarefas concluídas, escondê-las
            $("input[type='checkbox']:checked").closest("li").removeClass("d-flex").hide();
            $(this).html('<i class="bi bi-eye"></i> Mostrar tarefas concluídas');
        } else {
            // Se estamos escondendo tarefas concluídas, mostrá-las
            $("input[type='checkbox']:checked").closest("li").addClass("d-flex").show();
            $(this).html('<i class="bi bi-eye-slash"></i> Esconder tarefas concluídas');
        }

        // Alternar o estado
        $(this).data("showing-completed", !isShowingCompleted);
    });

    // Salvando as tarefas antes de sair da página
    $(window).on("beforeunload", () => {
        saveTasksToLocalStorage();
    });

    setMinExpirationDate();
    loadTasksFromLocalStorage();
});