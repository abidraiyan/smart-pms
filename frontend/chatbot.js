const chatbotResponses={
 "hello":"Hello! How can I help you today?",
 "visiting hours":"Visiting hours are 9am to 5pm, Monday to Friday.",
 "contact":"You can contact us at (02) 1234 5678.",
 "book appointment":"You can book an appointment from the Booking page in the top menu.",
 "register":"Use the Register page to create your profile before booking.",
 "bye":"Goodbye! Have a great day."};
function chatbotGreet(){const chatBody=document.getElementById("chatBody"); if(chatBody){chatBody.innerHTML='<div class="msg bot">Hi, how can I help you today?</div>';}};
function sendMessage(){const inputEl=document.getElementById("chatInput"); const chatBody=document.getElementById("chatBody"); const input=(inputEl.value||"").trim(); if(!input) return;
 const key=input.toLowerCase(); const reply=chatbotResponses[key]||"Sorry, I don’t understand that yet.";
 chatBody.innerHTML+=`<div class="msg user">${input}</div>`; chatBody.innerHTML+=`<div class="msg bot">${reply}</div>`;
 inputEl.value=""; chatBody.scrollTop=chatBody.scrollHeight;}
window.addEventListener("load",chatbotGreet);