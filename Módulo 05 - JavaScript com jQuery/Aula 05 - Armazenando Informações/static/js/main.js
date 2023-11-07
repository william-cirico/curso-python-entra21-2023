$(document).ready(() => {
    // Referências de elementos do DOM
    const $taskForm = $("#taskForm");
    const $descriptionInput = $("#descriptionInput");
    const $expirationDateInput = $("#expirationDateInput");
    const $successToast = $("#successToast");
    const $taskList = $(".list-group");
    const $toggleCompletedButton = $("#toggleCompletedButton");
    const $emptyMessage = $("#emptyMessage");
    const $searchInput = $("#searchInput");

    // Instância do componente Toast do bootstrap
    const successToast = bootstrap.Toast.getOrCreateInstance($successToast);

    // 6º Passo:
    /** Filtra as tarefas de acordo com texto digitado no input de pesquisa */
    const filterTasks = () => {
        const searchTerm = $searchInput.val().toLowerCase(); // Obtém o valor do input de pesquisa e converte ele para minúsculo

        const $tasks = $(".list-group-item:not(.active):not(#emptyMessage)");
        $.each($tasks, (_, task) => {
            const $task = $(task); //Transforma o elemento do DOM para elemento do jQuery (habilita o .find())
            const description = $task.find("p").text().toLowerCase(); // Obtém o valor da descrição da tarefa

            if (!description.includes(searchTerm)) {
                $task.removeClass("d-flex").hide(); // Remove a classe d-flex e esconde a tarefa
            } else {
                $task.addClass("d-flex").show(); // Adiciona a classe d-flex e exibe a tarefa
            }
        });
    };

    /** Função responsável por realizar o toggle da mensagem de lista vazia */
    const checkEmptyList = () => {
        // Verifique se a quantidade de tarefas é 0
        if ($(".list-group-item:not(.active):not(#emptyMessage)").length === 0) {
            $emptyMessage.show(); // Mostra a mensagem: "Não há tarefas cadastradas"
        } else {
            $emptyMessage.hide(); // Esconde a mensagem
        }
    };

    // 7º Passo
    /** Salva as tarefas no localStorage */
    const saveTasksToLocalStorage = () => {
        const tasks = [];
        // Obtendo todas as tarefas na tela (<li>)
        const $tasks = $(".list-group-item:not(.active):not(#emptyMessage)");

        // Percorrendo cada tarefa para gerar um objeto da tarefa ({ description, expirationDate, isCompleted })
        $.each($tasks, (_, task) => {
            const $task = $(task);
            // Obtendo os elementos da tarefa (descrição, data de expiração, status)
            const description = $task.find("p").text(); // Obtém o texto do parágrafo de descrição
            const expirationDate = $task.find("span").text().replace("Expira em: ", ""); //Obtém o texto da <span> e substitui o texto Expira em por "".
            const isCompleted = $task.find("input[type='checkbox']").is(":checked"); // Obtém o status da tarefa (true ou false)

            // Adiciona a tarefa no vetor de tarefas
            tasks.push({
                description,
                expirationDate,
                isCompleted
            });
        });

        // Adicionando as tarefas no localStorage
        localStorage.setItem("tasks", JSON.stringify(tasks));
    };

    /** Carrega as tarefas do localStorage e as adiciona à lista de tarefas */
    const loadTasksFromLocalStorage = () => {
        const tasks = JSON.parse(localStorage.getItem("tasks")) || [];

        // Adicionando cada tarefa salva à lista de tarefas
        tasks.forEach(task => {
            const $task = createTask(task.description, task.expirationDate, task.completed); // Criando a tarefa
            $taskList.append($task); // Adicionando a tarefa na lista
        });
    };

    /** Define a data mínima de expiração para o input de data de expiração */
    const setMinExpirationDate = () => {
        const today = dayjs().format("YYYY-MM-DD"); // Obtém a data atual e formata ela para "ano-mes-dia" (O input type="date" só aceita datas nesse formato)
        $expirationDateInput.attr("min", today); //Definindo o valor mínimo para a data
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
        const $button = $("<button></button>").addClass(btnClasses); // Criando o elemento <button> e adicionando as classes
        const $icon = $("<i></i>").addClass(iconClasses); // Criando o elemento do ícone e adicionando as classes
        $button.append($icon); // Adicionando dentro do botão
        $button.on("click", clickHandler); // Adicionando o eveto de click do button

        return $button; // Retornando o botão criado
    };

    /**
     * Evento de remoção de uma tarefa
     * @param {jQuery} $task - O elemento jQuery da tarefa que será removida 
     */
    const onRemoveTask = ($task) => {
        $task.remove(); // Removendo a tarefa do DOM
        checkEmptyList(); // Verificando se a lista está vazia para exibir a mensagem
    };

    /**
     * Encerra a edição de uma tarefa
     * @param {jQuery} $task - O elemento jQuery da tarefa que está sendo editada
     */
    const endEditTask = ($task) => {
        // Obtendo os inputs da tarefa no DOM
        const $descriptionInput = $task.find("input.form-control[type='text']");
        const $expirationDateInput = $task.find("input.form-control[type='date']");
        const $completedCheckbox = $task.find("input[type='checkbox']");

        // Obtendo os valores digitados nos inputs
        const description = $descriptionInput.val();
        const expirationDate = dayjs($expirationDateInput.val()).format("DD/MM/YYYY");
        const completed = $completedCheckbox.prop("checked");

        // Criando uma nova tarefa com os valores atualizados
        const $updatedTask = createTask(description, expirationDate, completed);

        // Substituindo a tarefa antiga pela tarefa atualiza
        $task.replaceWith($updatedTask);
    };

    /**
     * Inicia a edição de uma tarefa, substituindo parágrafos e spans por inputs
     * @param {jQuery} $task - O elmento jQuery da tarefa que vai entrar em modo de edição
     */
    const startEditTask = ($task) => {
        // Obtendo os elementos de descrição e data de expiração do DOM
        const $description = $task.find("p");
        const $expirationDate = $task.find("span");

        // Obtendo os valores desses elementos
        const currentDescription = $description.text();
        const currentExpiration = dayjs($expirationDate.text().replace("Expira em: ", ""), "DD/MM/YYYY").format("YYYY-MM-DD"); // Formatando a data que vem em: "Expira em: dia/mês/ano" para "ano-mes-dia"

        // Criando os inputs para edição
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

        // Criando os botões de salvar e cancelar
        const $saveButton = $("<button class='btn btn-success btn-sm'>Salvar</button>");
        const $cancelButton = $("<button class='btn btn-secondary btn-sm'>Cancelar</button>");

        // Adicionando o evento no botão de salvar
        $saveButton.on("click", () => {
            $description.text($descriptionInput.val());
            const formattedDate = dayjs($expirationDateInput.val()).format("DD/MM/YYYY");
            $expirationDate.text(`Expira em: ${formattedDate}`);
            endEditTask($task);
        });

        // Adicionando o evento no botão de cancelar
        $cancelButton.on("click", () => endEditTask($task));

        // Substituindo o <p> e o <span> da tarefa pelos inputs
        $description.replaceWith($descriptionInput);
        $expirationDate.replaceWith($expirationDateInput);

        // Substituindo os botões
        const $buttonDiv = $task.find("div:nth-of-type(2)");
        $buttonDiv.empty().append($saveButton, $cancelButton);
    };

    /**
     * Cria a representação DOM de uma tarefa e retorna o elemento jQuery
     * @param {string} description - Descrição da tarefa
     * @param {string} expirationDate - Data de expiração da tarefa
     * @param {boolean} completed - Estado da tarefa
     * @returns {jQuery} O elemento jQuery da nova tarefa
     */
    const createTask = (description, expirationDate, completed = false) => {
        const $li = $('<li class="list-group-item d-flex justify-content-between align-items-center"></li>');

        // Criando os elementos do checkbox
        const $checkboxDiv = $("<div>", {
            "class": "form-check d-flex align-items-center column-gap-2 checkbox-xl"
        });

        // Gerando um ID único para a checkbox (Para que ao clicar na label marque o checkbox :D)
        const checkboxId = generateRandomId("checkbox_");
        const $checkbox = $("<input>", {
            "class": "form-check-input",
            type: "checkbox",
            id: checkboxId,
            checked: completed
        });

        const $label = $("<label class='form-check-label'></label>").attr("for", checkboxId);
        const $description = $("<p class='fs-6 mb-0'></p>").text(description);
        const $expirationDate = $("<span class='text-secondary'></span>").text(`Expira em: ${expirationDate}`);
        
        // Adicionando a descrição e a data de expiração na label
        $label.append($description, $expirationDate);

        // Adicionando o checkbox e a label na DIV
        $checkboxDiv.append($checkbox, $label);

        // Criando os botões de editar e excluir
        const $buttonDiv = $("<div class='d-flex column-gap-2'></div>");
        const $editButton = createIconButton("bi bi-pencil", "btn btn-warning btn-sm", () => startEditTask($li)); // 4º Passo: criar a função de edição
        const $removeButton = createIconButton("bi bi-x-lg", "btn btn-danger btn-sm", () => onRemoveTask($li)); // 3º Passo: criar a função de remoção
        $buttonDiv.append($editButton, $removeButton);

        // Adicionando a div do checkbox e a div dos botões na tarefa
        $li.append($checkboxDiv, $buttonDiv);

        return $li;
    };

    // 1º Passo:
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
        const $task = createTask(description, expirationDate); // 2º Passo: criar a função.

        // Inserindo a tarefa na lista
        $taskList.append($task);

        // Mostrando o toast de sucesso
        successToast.show();

        // Removendo a classe de expiração
        $taskForm.removeClass("was-validated");

        // Resetando o formulário
        $taskForm[0].reset();

        checkEmptyList();
    });

    // 5º Passo:
    // Alternância da exibição de tarefas concluídas
    $toggleCompletedButton.on("click", () => {
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

    // 8º Passo:
    // Salvando as tarefas antes de sair da página
    $(window).on("beforeunload", () => {
        saveTasksToLocalStorage();
    });

    // Evento de entrada de teclado para filtrar conforme o usuário digita
    $searchInput.on("keyup", filterTasks);

    setMinExpirationDate();

    // 9º Passo
    loadTasksFromLocalStorage();
    checkEmptyList();
});