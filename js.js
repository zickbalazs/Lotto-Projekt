var x = false;
document.getElementById('gomb').onclick = function func(){
    if (x==false){
        document.getElementById('nav').style.height="350px";
        x = !x;
    }
    else{
        document.getElementById('nav').style.height="0px";
        x = !x;
    }
}