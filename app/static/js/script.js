
$(document).ready(function() {
    $("#miFormulario").submit(function(event) {
      event.preventDefault();

      let primerNombre = $("#primerNombre").val();
      let segundoNombre = $("#segundoNombre").val();
      let email = $("#email").val();
      let telefono = $("#telefono").val();
      let contrasena = $("#contrasena").val();

      
      if (primerNombre === "" ) {
        alert("Por favor, ingrese su primer nombre.");
        return false;
      }

      if (segundoNombre === "" ) {
        alert("Por favor, ingrese su segundo nombre.");
        return false;
      }

      let emailRegEx = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegEx.test(email)) {
        alert("Por favor, introduce una dirección de correo electrónico válida.");
        return false;
      }

      
      let telefonoRegEx = /^\d{10}$/;
      if (!telefonoRegEx.test(telefono)) {
        alert("Por favor, introduce un número telefónico válido (10 dígitos).");
        return false;
      }

      
      if (contrasena.length < 8) {
        alert("Por favor, introduce una contraseña con al menos 8 caracteres.");
        return false;
      }

      $("#miFormulario").unbind("submit").submit();
    });
});

$(document).ready(function() {

    var loginForm = $('#login-form');
    var emailInput = $('#email');
    var passwordInput = $('#password');
  

    function validateEmail(email) {
      var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return re.test(email);
    }
  

    loginForm.submit(function(event) {

      if (!validateEmail(emailInput.val())) {
        alert('Por favor ingrese un correo electrónico válido');
        event.preventDefault();
        return;
      }
  

      if (passwordInput.val().length < 6) {
        alert('Por favor ingrese una contraseña válida (mínimo 6 caracteres)');
        event.preventDefault();
        return;
      }
    });
  });
  
  // Eventos
  //Llevar a cards de ofertas 
$(document).ready(function() {
  $("#oferta").click(function(){
      $("html, body").animate({ scrollTop: $("#oferta_titulo").offset().top }, "fast");
      
    });
  });
//Llevar pagina de doativos
$(document).ready(function() {
$('#donar').click('shown.bs.modal', function () {
  $("#modal1").modal('show');
});


$("#ir").click(function() {
  window.location.href = "error";
});
});

// Volver con ESC
$(document).ready(function() {
$("#volver").click(function(){

  window.location.href = "index";
});
$(document).keydown(function(event) {

  if (event.keyCode == 27) {
   
    window.location.href = "index";
  }
});
});

// Modal perro 
$(document).ready(function() {
  $(document).keydown(function(event) {
    if (event.key === "F6"){
      console.log("La tecla F6 fue presionada");
      $("#modal2").modal('show');
      
    }
    
  });
});

/* Filtro */ 

let producto_perro = ['perro_fitFormula', 'perro_dogChow', 'perro_cannesAdulto', 'perro_cachupinCarne' ];
let producto_gato = ['gato_felinesPremium','gato_whiskasCarne', 'gato_purinaPollo','gato_purinaChow'];
let id_ocultar;

$(document).ready(function() {
  $('input[name=ocultar]').change(function() {
    if ($(this).val() === 'ocultarGato' && $(this).is(':checked')) {
      for (let i = 0; i < producto_gato.length; i++) {
        
        let id_ocultar = producto_gato[i];
        var selector = '#' + id_ocultar;
        $(selector).hide(); // oculta el objeto seleccionado
      }
      
    } else {
       for (let i = 0; i < producto_gato.length; i++) {
        
        let id_ocultar = producto_gato[i];
        var selector = '#' + id_ocultar;
        $(selector).show(); // oculta el objeto seleccionado
      }

    }

    if ($(this).val() === 'ocultarPerro' && $(this).is(':checked')) {
      for (let i = 0; i < producto_perro.length; i++) {
        
        let id_ocultar = producto_perro[i];
        var selector = '#' + id_ocultar;
        $(selector).hide(); // oculta el objeto seleccionado
      }
    } else {
      for (let i = 0; i < producto_perro.length; i++) {
        
        let id_ocultar = producto_perro[i];
        var selector = '#' + id_ocultar;
        $(selector).show(); // oculta el objeto seleccionado
      }

    }
 });
});

// evento de carga

$(document).ready(function() {
  console.log("a");
  $('#content_anim').fadeIn(2000); 
  
  });


