//Validaciones de formularios
$().ready(function(){
    $('#regUsuario').validate({
        rules:{
            username:{
                required: true,
                rangelength: [9, 10]
            },
            password1:{
                required: true,
                minlength: 8
            },
            password2:{
                required: true,
                minlength: 8,
                equalTo: "#id_password1"
            },
            regNombre:{
                required: true,
                maxlength: 50
            },
            regAp_pat:{
                required: true,
                maxlength: 50
            },
            regAp_mat:{
                required: true,
                maxlength: 50
            },
            regMail:{
                required: true,
                email: true
            }
        },
        messages:{
            username:{
                required: "Campo Obligatorio",
                rangelength: "Deben ser entre 9 y 10 carácteres"
            },
            password1:{
                required: "Campo Obligatorio",
                minlength: "8 carácteres mínimo"
            },
            password2:{
                required: "Campo Obligatorio",
                minlength: "8 carácteres mínimo",
                equalTo: "Contraseña debe ser igual a la anterior"
            },
            regNombre:{
                required: "Campo Obligatorio",
                maxlength: "Límite alcanzado"
            },
            regAp_pat:{
                required: "Campo Obligatorio",
                maxlength: "Límite alcanzado"
            },
            regAp_mat:{
                required: "Campo Obligatorio",
                maxlength: "Límite alcanzado"
            },
            regMail:{
                required: "Campo Obligatorio",
                email: "Ingrese mail válido"
            }
        }
    });
});