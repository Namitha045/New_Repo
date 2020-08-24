function picture(){

  var pic = "Kalam_4.jpg"
  document.getElementById("kalam_pics").src = pic.replace();
  document.getElementByTag("figure").figcaption = figcaption.replace("Price : Rs. 1300");

  var button = document.createElement("button");
  button.innerHTML = "PREVIOUS";

  var body = document.getElementById("content-wrap")[1];
  body.appendChild(button);

}

function Home(){
  var home = document.createElement('p');
  home.innerHTML = 'About home page'
  
}
