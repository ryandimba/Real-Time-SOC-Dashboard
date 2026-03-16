var logs=[

"Firewall blocked suspicious IP",
"Failed login attempt detected",
"Malware signature detected",
"Phishing email reported",
"Unusual outbound traffic"

]

setInterval(()=>{

var log=logs[Math.floor(Math.random()*logs.length)]

var container=document.getElementById("logs")

container.innerHTML += "<div class='text-green-400'>"+log+"</div>"

container.scrollTop = container.scrollHeight

},2000)