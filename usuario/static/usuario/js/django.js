$.validator.setDefaults( {
    submitHandler: function () {
        alert( "Datos Correctos, Ingresando!" );
        ('#ingresar').attr('href','./cuenta.html');
      }
    }
 );

$(document).ready(function(){
	 $('#loginform').validate({
		rules: {
		   correo: {
			  required: true,
			  email: true
		    },
		   contraseña: {
			  required: true,
			  minlength: 6
		    },
		   agree: "required"
		},
		messages: {           
		 correo: {
			  required: "Por favor ingresa un correo valido",
			  email: "Debe contener @; ejemplo@gmail.com"
		    },
		   contraseña: {
			  required: "Por favor ingresa una contraseña",
			  minlength: "Tu contraseña debe ser de no menos de 6 caracteres de longitud"
		    },
		},
	});
});

$.validator.submitHandler( {
    submitHandler: function () {
	   alert( "Usuario creado con exito!" );
	   ('#crearusuario').attr('href','./crearusuario2.html');
    }
 });
 
 $(document).ready(function(){
	 $('#creationform').validate({
		rules: {
		   nombre: {
              required: true,
              minlength: 4
           },
           contraseña: {
            required: true,
            minlength: 6
           },
           correo: {
            required: true,
            email: true
           },
           telefono: {
              number: true,  
              required:true,
              minlength: 8,           
           },
		   tipocuenta: {
            required: true,
            minlength: 6,
           },
		   agree: "required"
		},
		messages: {           
            nombre: {
                required: 'Debe ingresar nombre',
                minlength: 'Debe tener minimo 4 caracteres'
             },
             contraseña: {
              required: 'Debe ingresar su contraseña',
              minlength: 'Debe tener minimo 6 caracteres'
           },
           correo: {
              required: 'Debe ingresar un correo',
              email: 'Debe tener @; ejemplo@gmail.com'
           },
             telefono: {
                required: 'Debe ingresar un telefono',
                minlength: 'Debe tener minimo 8 numeros'
                              
             },
             tipocuenta: {
              required: 'Debe ingresar tipo cuenta',
              minlength: 'Debe tener minimo 4 caracteres'
           },
		},
	 });
  });
 
 