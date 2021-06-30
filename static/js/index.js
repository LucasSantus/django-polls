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
    