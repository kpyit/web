"use strict";
 
function greeting(){  
  $(".alert").removeClass('fade'); 
  var user_name = document.getElementById("user_name").value;  
  console.info("Привествую пользователь:" +user_name);
  document.getElementById("user_congrat").textContent =  ("Привествую пользователь:" + user_name);
} 

function toggleAlert(){ 
  $(".alert").addClass('fade'); 
  return false; 
}
 
document.getElementById("congratulation_user").onclick = greeting; 
$('#bsalert').on('click', toggleAlert);