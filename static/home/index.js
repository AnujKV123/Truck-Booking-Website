window.onload = function() {
  sessionStorage.setItem("Rdx", 1)
};

var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) { slideIndex = 1 }
  if (n < 1) { slideIndex = slides.length }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";
}




function radioData1(){
  document.getElementById('drop2').style.display = "none";
  document.getElementById('drop3').style.display = "none";
  document.getElementById('drop2').value = "";
  document.getElementById('drop3').value = "";
  sessionStorage.setItem("Rdx", 1)
}
function radioData2(){
  document.getElementById('drop2').style.display = "block";
  document.getElementById('drop3').style.display = "none";
  document.getElementById('drop3').value = "";
  sessionStorage.setItem("Rdx", 2)
}
function radioData3(){
  document.getElementById('drop2').style.display = "block";
  document.getElementById('drop3').style.display = "block";
  sessionStorage.setItem("Rdx", 3)
}

function Sheduledule_later() {
  var change_option = document.getElementById("set_time").value;
  console.log(change_option)
  if (change_option == "Schedule for later") {
    console.log("hihihihi")
    document.querySelector("#Schedule_later").style.display = "block";
  }
  else {
    document.querySelector("#Schedule_later").style.display = "none";
  }
}






