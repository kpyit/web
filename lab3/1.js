"use strict"; 

function calc_fahrenheit(){     
  var temperature_C = parseFloat(document.getElementById("temp_C").value);
  var temperature_F = (9 / 5) * temperature_C + 32;
  console.info("temperature_F="+temperature_F);
  document.getElementById("temp_F").value = temperature_F.toFixed(2);  
}

document.getElementById("calc_fahrenheit").onclick = calc_fahrenheit;
 