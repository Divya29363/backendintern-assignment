function register(){

fetch("http://127.0.0.1:8000/register",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
username:username.value,
email:email.value,
password:password.value
})
})
.then(res=>res.json())
.then(data=>alert("Registered"))

}

function login(){

fetch("http://127.0.0.1:8000/login",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
email:loginEmail.value,
password:loginPassword.value
})
})
.then(res=>res.json())
.then(data=>alert("Login Success"))

}