window.onscroll = function () { scrollFunction() };

function scrollFunction() {
  if (document.body.scrollTop > 400 || document.documentElement.scrollTop > 400) {
    document.querySelector(".top_Nav ").style.backgroundColor = "#6c757d";
  } else {
    document.querySelector(".top_Nav ").style.backgroundColor = "transparent";
  }
}

function search() {
  var srcBtn = document.getElementById('search_layout');
  srcBtn.style.transform = "scale(1)";
  srcBtn.style.transformOrigin = "left";
  srcBtn.style.transformOrigin = "top right";

}

function cls() {
  var srcBtn = document.getElementById('search_layout');
  srcBtn.style.transform = "scale(0)";
  srcBtn.style.transformOrigin = "top right";
  srcBtn.style.transition = "all 0.7s ease";
}


var btnScrollTop=document.querySelector("#btnScrTop");
window.addEventListener("scroll",function(){
      let ms=window.scrollY;
      if(ms>350){
        btnScrollTop.style.display="flex";
      }
      else{
        btnScrollTop.style.display="none";
      }

});
btnScrollTop.addEventListener("click",function(){
  window.scrollTo({
    top:0,
    left:0,
    behavior:"smooth"
  })
})





