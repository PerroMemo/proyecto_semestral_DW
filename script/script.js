let mostrador = document.getElementById("mostrador");
let seleccion = document.getElementById("seleccion");
let imgSeleccionada = document.getElementById("img");
let modeloSeleccionado = document.getElementById("modelo");
let descripSeleccionada = document.getElementById("descripcion");
let precioSeleccionado = document.getElementById("precio");

function cargar(item){
    quitarBordes();
    mostrador.style.width = "60%";
    seleccion.style.width = "40%";
    seleccion.style.opacity = "1";
    item.style.border = "2px solid red";

    imgSeleccionada.src = item.getElementsByTagName("img")[0].src;

    modeloSeleccionado.innerHTML =  item.getElementsByTagName("p")[0].innerHTML;

    descripSeleccionada.innerHTML = "Descripción del modelo ";

    precioSeleccionado.innerHTML =  item.getElementsByTagName("span")[0].innerHTML;


}
function cerrar(){
    mostrador.style.width = "100%";
    seleccion.style.width = "0%";
    seleccion.style.opacity = "0";
    quitarBordes();
}
function quitarBordes(){
    var items = document.getElementsByClassName("item");
    for(i=0;i <items.length; i++){
        items[i].style.border = "none";
    };
};

$(document).ready(function() {
    $("#miFormulario").submit(function(event) {
      event.preventDefault();

      let primerNombre = $("#primerNombre").val();
      let segundoNombre = $("#segundoNombre").val();
      let email = $("#email").val();
      let telefono = $("#telefono").val();
      let contrasena = $("#contrasena").val();

      


      if (primerNombre === "" || email === "" || telefono === "" || contrasena === "") {
        alert("Por favor, rellena todos los campos.");
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
      
      console.log("a"); 
    });
  });
//Llevar pagina de doativos
$(document).ready(function() {
$('#donar').click('shown.bs.modal', function () {
  $("#modal1").modal('show');
});


$("#ir").click(function() {
  window.location.href = "error.html";
});
});

// Volver con ESC
$(document).ready(function() {
$("#volver").click(function(){

  window.location.href = "main.html";
});
$(document).keydown(function(event) {

  if (event.keyCode == 27) {
   
    window.location.href = "main.html";
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


