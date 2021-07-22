
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

    // Menu flutuante 
    $('.fixed-action-btn').floatingActionButton({
        direction: 'left'
    }); 
    
    //Collapsible
    $('.collapsible').collapsible();
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