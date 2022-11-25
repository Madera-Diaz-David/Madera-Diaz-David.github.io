

function validacampos (){
    var formulario;
    formulario=document.formUser;
    //valida el campo usuario
    if (formulario.user.value=="") {
        //valida si el campo esta vacio
        document.getElementById("validaUser").innerHTML="Favor escribir el usuario"
        //se posiciona en el campo user
        formulario.user.focus();
        return false
    }else{
        document.getElementById("validaUser").innerHTML=""; 

    }

    if (formulario.email.value=="") {
        //valida si el campo esta vacio
        document.getElementById("validaEmail").innerHTML="Favor escribir el Email"
        //se posiciona en el campo user
        formulario.Email.focus();
        return false
    }else{
        document.getElementById("validaEmail").innerHTML=""; 
        
    }

    if (formulario.password.value=="") {
        //valida si el campo esta vacio
        document.getElementById("valida_password").innerHTML="Favor escribir password"
        //se posiciona en el campo user
        formulario.passwpord.focus();
        return false
    }else{
        document.getElementById("valida_password").innerHTML=""; 
        
    }

    if (formulario.passwordC.value=="") {
        //valida si el campo esta vacio
        document.getElementById("valida_passwordC").innerHTML="Favor confirmar password"
        //se posiciona en el campo user
        formulario.passwordC.focus();
        return false
    }else{
        document.getElementById("valida_passwordC").innerHTML=""; 
    
}

formulario.submit()

}