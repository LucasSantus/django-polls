
$(document).ready(function(){
    /* Inicialização do modal */
    $('.modal').modal();

    /* Inicialização do tooltipped */
    $('.tooltipped').tooltip({delay: 50});

    /* Inicialização do chip */
    $('.chips').material_chip();

    /* Inicialização do sidenav */
    $('.sidenav').sidenav();

    /* Inicialização do select */
    $('select').formSelect();

    /* Inicialização do dropdown */
    $('.dropdown-trigger').dropdown({
        coverTrigger: false,
        hover: true,
    });

    /* Inicialização do datepicker */
    $('.datepickera').datepicker({
        i18n: {
            months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
            monthsShort: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
            weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo'],
            weekdaysShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'],
            weekdaysAbbrev: ['D', 'S', 'T', 'Q', 'Q', 'S', 'S'],
            today: 'Hoje',
            clear: 'Limpar',
            cancel: 'Sair',
            done: 'Confirmar',
            labelMonthNext: 'Próximo mês',
            labelMonthPrev: 'Mês anterior',
            labelMonthSelect: 'Selecione um mês',
            labelYearSelect: 'Selecione um ano',
            selectMonths: true,
            selectYears: 15,
        },
        format: 'yyyy-mm-dd',
        container: 'body',
        yearRange: 80,
        maxDate: new Date(),
    }); 
});

function validacao_data(){
    var data_inicial = new Date($("input[name='data_inicio']").val());
    var data_final = new Date($("input[name='data_fim']").val());
    if (!data_inicial || !data_final) return false;
    if(data_inicial >= data_final){
        var toastHTML = '<span>Insira datas corretamente!</span>';
        M.toast({html: toastHTML});
        return false;
    }else{
        return true;
    }
}