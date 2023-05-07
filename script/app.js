$(document).ready(function() {
  $(".add-to-cart").click(function() {
    
    var productId = $(this).data("product-id");
    var productTitle = $("#modelo").text();
    var productPrice = parseFloat($("#precio").text().replace("$", ""));
    var productQuantity = parseInt($(this).siblings(".size").children("select").val());

    
    var newRow = $("<tr></tr>");

    
    var titleCell = $("<td></td>").text(productTitle);
    var priceCell = $("<td></td>").text("$" + productPrice.toFixed(2));
    var quantityCell = $("<td></td>").text(productQuantity);
    var totalCell = $("<td></td>").text("$" + (productPrice * productQuantity).toFixed(2));
    var removeCell = $("<td></td>").html('<button class="remove-from-cart" data-product-id="' + productId + '">Eliminar</button>');

    
    newRow.append(titleCell);
    newRow.append(priceCell);
    newRow.append(quantityCell);
    newRow.append(totalCell);
    newRow.append(removeCell);

    
    $("#carrito tbody").append(newRow);

    
    actualizarTotal();
  });

  
  $("#carrito").on("click", ".remove-from-cart", function() {
    var productId = $(this).data("product-id");
    $(this).parents("tr").remove();
    actualizarTotal();
  });

  
  function actualizarTotal() {
    var total = 0;

    
    $("#carrito tbody tr").each(function() {
      var rowTotal = parseFloat($(this).find("td:nth-child(4)").text().replace("$", ""));
      total += rowTotal;
    });

    
    $("#total").text("$" + total.toFixed(2));
  }
});






