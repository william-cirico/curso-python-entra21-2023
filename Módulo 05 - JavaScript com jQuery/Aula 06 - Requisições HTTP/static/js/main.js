/**
 * Verifica se um nome tem ao menos 4 caracteres e se ele está completo
 * @param {string} name - Nome que será verificado
 * @returns {boolean}
 */
const isFullNameValid = (name) => name.trim().split(" ").length > 1;

/**
 * Verifica se o CPF é válido
 * @param {string} cpf - CPF a ser verificado
 * @returns {boolean} verdadeiro caso o CPF seja válido; falso em caso contrário
 */
const isCPFValid = (cpf) => {
    cpf = cpf.replace(/[^\d]+/g, ''); // Remove caracteres não numéricos
    if (cpf.length !== 11 || !!cpf.match(/(\d)\1{10}/)) {
        return false; // Verifica se tem tamanho 11 ou se é uma sequência de dígitos iguais
    }

    let soma;
    let resto;
    soma = 0;

    // Validação do primeiro dígito verificador
    for (let i = 1; i <= 9; i++) {
        soma += parseInt(cpf.substring(i - 1, i)) * (11 - i);
    }

    resto = (soma * 10) % 11;

    if ((resto === 10) || (resto === 11)) {
        resto = 0;
    }
    if (resto !== parseInt(cpf.substring(9, 10))) {
        return false;
    }

    soma = 0;

    // Validação do segundo dígito verificador
    for (let j = 1; j <= 10; j++) {
        soma += parseInt(cpf.substring(j - 1, j)) * (12 - j);
    }

    resto = (soma * 10) % 11;

    if ((resto === 10) || (resto === 11)) {
        resto = 0;
    }
    if (resto !== parseInt(cpf.substring(10, 11))) {
        return false;
    }

    return true;
}

$(document).ready(() => {
    // Referências para os elementos do DOM
    const $zipcodeInput = $("#zipcodeInput");
    const $streetInput = $("#streetInput");
    const $numberInput = $("#numberInput");
    const $cityInput = $("#cityInput");
    const $stateInput = $("#stateInput");
    const $complementInput = $("#complementInput");
    const $cpfInput = $("#cpfInput");
    const $zipcodeIcon = $("#zipcodeIcon");
    const $form = $("form");

    const $successToast = bootstrap.Toast.getOrCreateInstance($("#successToast"));

    // Adicionando as máscaras nos inputs
    $zipcodeInput.mask("00000-000");
    $cpfInput.mask("000.000.000-00");

    // Adicionando o manipulador do evento "input" (Quando algo é digitado) para o CPF
    $cpfInput.on("input", function () {
        const cpf = $(this).val();

        // Se o CPF for inválido adicionar a classe "is-invalid"
        if (!isCPFValid(cpf)) {
            $cpfInput.addClass("is-invalid");
        } else {
            $cpfInput.removeClass("is-invalid");
        }
    });

    // Adicionando o manipulador do evento "blur" para o input de CEP
    $zipcodeInput.on("blur", function () {
        // Valor do CEP digitado
        const zipcode = $(this).val();

        // Se nenhum CEP tiver sido digitado não realizar a requisição
        if (zipcode.length !== 8) return;

        // Mudando o ícone do CEP
        $zipcodeIcon.attr("class", "spinner-border spinner-border-sm");

        // Realiza uma solicitação GET para a API viacep.com.br usando o CEP informado
        fetch(`https://viacep.com.br/ws/${zipcode}/json/`)
            .then(res => res.json()) // Obtendo somento os dados da requisição
            .then(data => {
                if (!data.erro) { // Verificando se o site existe
                    // Preenchendo os inputs com os valores da API
                    $streetInput.val(data.logradouro);
                    $cityInput.val(data.localidade);
                    $stateInput.val(data.uf);
                    $complementInput.val(data.complemento);

                    // Focando o input de número
                    $numberInput.focus();
                }
            })
            .catch(() => console.error("Falha ao realizar a requisição para a API do VIACEP"))
            .finally(() => $zipcodeIcon.attr("class", "bi bi-geo-alt"));
    });

    // Acrescentando as validações para o formulário: https://jqueryvalidation.org/validate/
    $form.validate({
        errorElement: "div", // Elemento que será criado
        errorClass: "invalid-feedback", // Classe que será aplicada
        // Como os campos com erro irão se comportar
        highlight: (element, _, validClass) => {
            $(element).addClass("is-invalid");
        },
        // Como os campos sem erro irão se comportar
        unhighlight: (element) => {
            $(element).removeClass("is-invalid");
        },
        // Onde a mensagem de erro será adicionada
        errorPlacement: (error, element) => {
            error.addClass("invalid-feedback");
            if (element.prop("id") === "zipcodeInput") { // Caso seja o campo do CEP
                error.insertAfter(element.next()); // Inserir depois do ícone
            } else {
                error.insertAfter(element);
            }
        },
        // Validações que serão aplicadas
        rules: {
            name: {
                required: true,
                fullNameValidator: true, // Validação customizada (linha 138)
                minlength: 3,
            },
            birthDate: {
                required: true,
                min: "1900-01-01",
            },
            cpf: {
                required: true,
                cpfValidator: true, // Validação customizada (linha 145)
            },
            email: {
                required: true,
                email: true,
            },
            zipcode: {
                required: true,
            },
            street: {
                required: true,
            },
            number: {
                required: true,
            },
            city: {
                required: true,
            },
            state: {
                required: true,
            },
        },
        // Mensagens que serão exibidas de acordo com os erros
        messages: {
            name: {
                required: "Por favor, insira seu nome",
                minlength: "Seu nome deve ter pelo menos 3 caracteres",
                fullNameValidator: "Por favor, insira o seu nome completo"
            },
            birthDate: "Por favor, insira uma data de nascimento válida",
            cpf: {
                required: "Por favor, insira um CPF",
                cpfValidator: "Por favor, insira um CPF válido",
            },
            email: "Por favor, insira um endereço de e-mail válido",
            zipcode: "Por favor, insira um CEP válido",
            street: "Por favor, insira um endereço válido",
            number: "Por favor, insira um número válido",
            city: "Por favor, insira uma cidade",
            state: "Por favor, insira um estado"
        },
        // Evento de submissão do formulário
        submitHandler: (form, event) => {
            event.preventDefault();
            form.reset();
            $successToast.show();
        }
    });

    // Adicionando os validadores customizados: https://jqueryvalidation.org/jQuery.validator.addMethod/
    jQuery.validator.addMethod("cpfValidator", value => isCPFValid(value));
    jQuery.validator.addMethod("fullNameValidator", value => isFullNameValid(value));
});