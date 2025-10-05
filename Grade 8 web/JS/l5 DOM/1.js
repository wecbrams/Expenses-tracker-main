function validate(e){
    e.preventDefault();

    const email = document.getElementById('email').value;
    const pass = document.getElementById('password').value;
    const age = document.getElementById('age').value;
    const msgBox = document.getElementById('message');

    let message = ""

    if (email==''){
        message="Please enter a valid Email"
        msgBox.style.color='red'
    }
    else if(pass==""){
        message ="Password must be atleast 8 characters"
        msgBox.style.color='red'

    }
    else if (age==''){
        message='Age nust be between 18 to 55'
        msgBox.style.color='red'
    }
    else{
        message="Login Successfully"
        msgBox.style.color='green'
    }
    msgBox.innerHTML=message
}