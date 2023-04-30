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
    }
}

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
  