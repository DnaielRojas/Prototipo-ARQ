//Validaciones de formularios
$().ready(function(){
    $.validator.addMethod(
        "formatoRut",
        function isValidRUT(rut) {
            if (!rut | typeof rut !== 'string') return false;
            var regexp = /^\d{7,8}-[k|K|\d]{1}$/;
            return regexp.test(rut);
        }
    );
    $('#regUsuario').validate({
        rules:{
            username:{
                required: true,
                rangelength: [9, 10],
                formatoRut: true
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
                rangelength: "Deben ser entre 9 y 10 carácteres",
                formatoRut: "El Formato de rut debe ser '12345678-9'"
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
    $('#logUsuario').validate({
        rules:{
            logRut:{
                required: true,
                rangelength: [9, 10],
                formatoRut: true
            },
            logPass:{
                required: true,
                minlength: 8
            }
        },
        messages:{
            logRut:{
                required: "Campo Obligatorio",
                rangelength: "Deben ser entre 9 y 10 carácteres",
                formatoRut: "El Formato de rut debe ser '12345678-9'"
            },
            logPass:{
                required: "Campo Obligatorio",
                minlength: "8 carácteres mínimo"
            }
        }
    });
    $('#modUsuario').validate({
        rules:{
            nombre:{
                required: true,
                maxlength: 50
            },
            apellido_pat:{
                required: true,
                maxlength: 50
            },
            apellido_mat:{
                required: true,
                maxlength: 50
            },
            mail:{
                required: true,
                email: true
            }
        },
        messages:{
            nombre:{
                required: "Campo Obligatorio",
                maxlength: "Límite alcanzado"
            },
            apellido_pat:{
                required: "Campo Obligatorio",
                maxlength: "Límite alcanzado"
            },
            apellido_mat:{
                required: "Campo Obligatorio",
                maxlength: "Límite alcanzado"
            },
            mail:{
                required: "Campo Obligatorio",
                email: "Ingrese mail válido"
            }
        }
    });
});