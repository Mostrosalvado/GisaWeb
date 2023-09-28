document.addEventListener("DOMContentLoaded", function() {
  // Obtén el botón por su ID
  var myButton = document.getElementById("contactButton");

  // Agrega un evento de clic al botón
  myButton.addEventListener("click", function() {
      // Redirige a la página de contacto
      window.location.href = "/contacto";
  });
});

