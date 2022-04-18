
<style>
  h1 {
    font-family: sans-serif;
    font-size: 64px;
    color: #CCC;
    padding: 5px;
    margin: 5px;
  }
  ul {
    padding: 0;
    margin: 10px;
  }
  li {
    font-family: sans-serif;
    background-color:gold;
    float: left;
    clear: both;
    padding: 5px;
    list-style-type: none;
    margin: 10px;
    border-radius: 5px;
  }
</style>

 
<body>
  <h1>Toppings</h1>
  <ul>
 
  </ul>
 
  <script>
  var toppings = ["Tomato", "Cheese", "Pepperoni", 
                  "Olives", "Jalapenos", "Pineapple", "Ham"];

  var ul = document.querySelector("ul");

  for (var i = 0; i < toppings.length; i++) {
    var topping = toppings[i];

    var listItem = document.createElement("li");
    listItem.textContent = topping;

    ul.appendChild(listItem);
  }
  </script>
</body>
 
