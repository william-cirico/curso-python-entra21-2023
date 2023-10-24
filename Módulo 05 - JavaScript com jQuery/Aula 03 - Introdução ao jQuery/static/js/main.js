$(document).ready(() => {
    // Selecionando os elementos no dom
    const $clock = $(".clock");
    const $date = $(".date");
    const $toggleButton = $("#toggleButton");

    /**
     * Formata o mês de número para português
     * @param {number} month - número do mês 
     * @returns {string} dia do mês formatado
     */
    const formatMonth = (month) => {
        const monthNames = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];
        return monthNames[month];
    };

    /**
     * Formata o dia da semana de número para português
     * @param {number} day - dia da semana
     * @returns {string} dia da semana formatado
     */
    const formatDayOfWeek = (day) => {
        const dayOfWeekNames = ["Domingo", "Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado"];
        return dayOfWeekNames[day];
    };

    /**
     * Formata o dia do mês para que ele sempre possua duas casas
     * @param {number} day - dia do mês
     * @returns {string} dia do mês com duas casas
     */
    const formatDay = (day) => String(day).padStart(2, "0");

    const updateClock = () => {
        $clock.text(new Date().toLocaleTimeString());
    };

    // Função para atualizar a data
    const updateDate = () => {
        const today = new Date();
        const dayOfWeek = formatDayOfWeek(today.getDay());
        const day = formatDay(today.getDate());
        const month = formatMonth(today.getMonth());
        const year = today.getFullYear();
        $date.text(`${dayOfWeek}, ${day} de ${month} de ${year}`);
    };

    // Iniciar temporizadores para atualizar relógio e a data
    let clockTimer = setInterval(updateClock, 1000);
    let dateTimer = setInterval(updateDate, 60000);

    let isPaused = false;

    // Função para pausar ou retomar os temporizadores
    const toggleTimer = () => {
        isPaused = !isPaused;
        if (isPaused) {
            // Se pausado limpar os temporizadores
            clearInterval(clockTimer);
            clearInterval(dateTimer);
        } else {
            // Se retomado, atualizar o relógio e configurar novamente os temporizadores
            updateClock();
            clockTimer = setInterval(updateClock, 1000);
            dateTimer = setInterval(updateDate, 60000);
        }

        // Atualizar o texto e o estilo do botão com base no estado (pausado ou retomado)
        $toggleButton.text(isPaused ? "Resumir" : "Pausar");
        $toggleButton.css("background-color", isPaused ? "#ADE25D" : "rgb(6, 164, 236)");
    };

    // Vincular a função de alternância ao clique do botão
    $toggleButton.click(toggleTimer);

    // Inicialmente, atualizar o relógio e a data
    updateClock();
    updateDate();
});