$.validator.setDefaults( {
    submitHandler: function () {
	   alert( "Perfil Modificado con exito!" );
	   ('#Modificar').attr('href','./cuenta.html');
    }
 });
 
 $(document).ready(function(){
	 $('#cuentaform').validate({
		rules: {
		   nombreC: {
			  required: true,

           },
           telefono: {
              required:true,
              minlength: 8,
                            
           },
		   contraseñaC: {
			  required: true,
			  minlength: 6,
		   },
		   agree: "required"
		},
		messages: {           
		   nombreC: {
			  required: "Por favor ingrese su nombre completo"
		   },
		   contraseñaC: {
			  required: "Por favor ingresa una contraseña",
			  minlength: "Tu contraseña debe ser de no menos de 5 caracteres de longitud"
           },
           telefono: {
               required: "debe ingresar su telefono",
               minlength: "debe tener minimo 8 numeros"

           },
		},
	 });
  });