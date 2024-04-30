function myFunction() {
  var x = document.getElementById("myTopNav");
  var y = document.getElementsByClassName('content-wrap');
  var z = document.getElementsByClassName('bio-data');
  var a = document.getElementsByTagName('img');
  var b = document.getElementsByTagName('button')
  if (x.className === "tabNav") {
    x.className += " responsive";
    x.style.display = 'block';
    x.style.position ='absolute';
    x.style.left = '40px';
    x.style.top = '50px';
    hide(y);
    hide(z);
    hide(a);
    hide(b);
  } else {
    x.className = "tabNav";
  }
}
function hide (elements) {
  elements = elements.length ? elements : [elements];
  for (var index = 0; index < elements.length; index++) {
    elements[index].style.display = 'none';
  }
}
