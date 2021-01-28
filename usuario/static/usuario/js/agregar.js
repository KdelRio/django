$.validator.setDefaults( {
    submitHandler: function () {
		alert( "Usuario Agregado Exitosamente!" );
		('#ingresar').attr('href','./agregar2.html');
	  }
    }
 );
 
 $(document).ready(function(){
	$('#addform').validate({
	   rules: {
		  nombre: {
			 required: true,
			 minlength: 4,
		  },
		  telefono: {
			 required: true,
			 number: true,
			 minlength: 8
		  },
		  direccion: {
			required: true,
			minlength: 6
		 },
		 sueldobruto: {
			required: true,
			number: true,
			minlength: 4
		 },
		 prevision: {
			required: true,
			number: true,
			minlength: 4
		 },
		 imposiciones: {
			required: true,
			number: true,
			minlength: 4
		 },
		 bonotransporte: {
			required: true,
			number: true,
			minlength: 4
		 },
		 bonoadc: {
			required: true,
			number: true,
			minlength: 4
		 },
		  agree: "required"
	   },
	   messages: {           
		nombre: {
			required: "Obligatorio",
			minlength: "Debe contener almenos 4 caracteres"
		 },
		 telefono: {
			required: "Obligatorio",
			minlength: "Debe contener almenos 8 caracteres"
		 },
		 direccion: {
		   required: "Obligatorio",
		   minlength: "Debe contener almenos 6 caracteres"
		},
		sueldobruto: {
		   required: "Obligatorio",
		   minlength: "Debe contener almenos 4 caracteres"
		},
		prevision: {
			required: "Obligatorio",
			minlength: "Debe contener almenos 4 caracteres"
		},
		imposiciones: {
			required: "Obligatorio",
			minlength: "Debe contener almenos 4 caracteres"
		},
		bonotransporte: {
			required: "Obligatorio",
			minlength: "Debe contener almenos 4 caracteres"
		},
		bonoadc: {
			required: "Obligatorio",
			minlength: "Debe contener almenos 4 caracteres"
		},
	   },
	});
 });