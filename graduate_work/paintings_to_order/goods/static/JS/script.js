var prices = {
    "40x30": ["1800₽"],
    "40x60": ["2500₽"],
    "70x70": ["3100₽"],
    "80x60": ["3500₽"],
    "100x80": ["4000₽"],
    "120x100": ["4800₽"],
    "myself_size": ["Договорная"]
};
var country = document.getElementById("size");
var city = document.querySelector("#price");
window.onload = selectSize;
country.onchange = selectSize;

function selectSize(ev){
    price.innerHTML = "";
    var c = this.value || "40x30", o;
    for(let i = 0; i < prices[c].length; i++){
      o = new Option(prices[c][i],i,false,false);
      price.add(o);
    };
  }