function icpf(v){
    v=v.replace(/\D/g,"")                    //Remove tudo o que nao e digito
    v=v.replace(/(\d{3})(\d)/,"$1.$2")       //Coloca um ponto entre o terceiro e o quarto digitos
    v=v.replace(/(\d{3})(\d)/,"$1.$2")       //Coloca um ponto entre o terceiro e o quarto digitos
                                            //de novo (para o segundo bloco de numeros)
    v=v.replace(/(\d{3})(\d{1,2})$/,"$1-$2") //Coloca um hifen entre o terceiro e o quarto digitos
    return v
}
function itel(v){
    v=v.replace(/\D/g,"")                 //Remove tudo o que nao e digito
    v=v.replace(/^(\d\d)(\d)/g,"($1) $2") //Coloca parenteses em volta dos dois primeiros digitos
    console.log(v.length)
    if (v.length<14){
      v=v.replace(/(\d{4})(\d)/,"$1-$2")    //Coloca hifen entre o quarto e o quinto digitos
    }else{
      v=v.replace(/(\d{4,5})(\d)/,"$1-$2")    //Coloca hifen entre o quarto e o quinto digitos
    }
}
function icep(input) {
    input.value = input.value.replace(/\D/g, '');
    // Verifica se o valor tem pelo menos 5 dígitos
    if (input.value.length > 5) {
    // Insere o traço após o quinto dígito
    input.value = input.value.substring(0, 5) + '-' + input.value.substring(5);
    }
}
function mascara(o,f){
    v_obj=o
    v_fun=f
    setTimeout("execmascara()",1)
}    
function execmascara(){
    v_obj.value=v_fun(v_obj.value)
}