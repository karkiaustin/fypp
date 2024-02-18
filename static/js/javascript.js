function abc() {
    document.querySelector(".logbo").style.display = "none";
    document.querySelector(".over").style.opacity = "1";

}
function bc() {
    document.querySelector(".logbo").style.display = "block";
    document.querySelector(".over").style.opacity = "0";
}
function aabc() {
     document.querySelector(".logbop").style.display = "none";
    document.querySelector(".overr").style.opacity = "1"; 
}
function bbc() {
    document.querySelector(".logbop").style.display = "block";
    document.querySelector(".overr").style.opacity = "0";
}
function togglePasswordVisibility(targetClass) {
    var passwordInput = document.querySelector("." + targetClass + " #b");       
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        document.querySelector("." + targetClass + " .a").innerHTML = 'HIDE';
        } 
    else {
            passwordInput.type = "password";
            document.querySelector("." + targetClass + " .a").innerHTML = 'SHOW';
        }
}
function vd(){
    document.querySelector(".mii").style.opacity = "1";
    document.querySelector(".middd").style.display = "none";       
}
function vid(){
    document.querySelector(".mii").style.opacity = "0";
    document.querySelector(".middd").style.display = "block";     
}

function iop() {
    var orderElement = document.querySelector('.order');
    var ipoElement = document.querySelector('.ipo');

    if (ipoElement.innerHTML === 'Show Order Detail <i class="fa-solid fa-arrow-down"></i>') {
        orderElement.style.display = 'block';
        ipoElement.innerHTML = 'Hide Order Detail <i class="fa-solid fa-arrow-up"></i>';
    } else {
        orderElement.style.display = 'none';
        ipoElement.innerHTML = 'Show Order Detail <i class="fa-solid fa-arrow-down"></i>';
    }
}
function asd(){
    document.querySelector(".mm").style.display = "none"; 
    document.querySelector(".backkkk").style.opacity = "1"; 
}
function ty(){
    document.querySelector(".mm").style.display = "block"; 
    document.querySelector(".backkkk").style.opacity = "0.4"; 
    
}

function PasswordVisibility() {
    var passwordInput = document.querySelector(".op");
    var showHideButton = document.querySelector(".aaa");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        showHideButton.innerHTML = "HIDE";
    } else {
        passwordInput.type = "password";
        showHideButton.innerHTML = "SHOW";
    }
}

function Visibility() {
    var passwordInput = document.querySelector(".ppp");
    var showHideButton = document.querySelector(".ab");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        showHideButton.innerHTML = "HIDE";
    } else {
        passwordInput.type = "password";
        showHideButton.innerHTML = "SHOW";
    }
}




