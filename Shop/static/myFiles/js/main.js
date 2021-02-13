//Event:scroll  style to Nav
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
  if (document.body.scrollTop > 400 || document.documentElement.scrollTop > 400) {
    document.querySelector(".top_Nav ").style.backgroundColor = "#6c757d";
  } else {
    document.querySelector(".top_Nav ").style.backgroundColor = "transparent";
  }
}
//end of Event:scroll  style to Nav

//Event:click  search layout

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
//Event:click  search layout
//Event:click  User layout
function Update() {
  var Update = document.getElementById('Update');
  var UserUpdateTable=document.querySelector(".UpdateUser")
  UserUpdateTable.style.display = "block";

}


//Event:scroll
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
//end of Event:scroll



//change bigImage
var zoom=document.querySelector(".zoom");
var image=document.querySelector(".bigImage");
var smallImage=document.querySelectorAll(".subImage img");

smallImage.forEach(function(el){
    el.addEventListener('click',function(){
    var imageName= el.getAttribute('src').split('/')[3];
    image.style.backgroundImage= `url(/static/photo/${imageName}`;
    zoom.style.backgroundImage= `url(/static/photo/${imageName}`;  
  })
  })
  //zoom effect
  image=document.querySelector(".bigImage");
  image.addEventListener('mousemove',function(e){
  let width =image.offsetWidth;
  let height =image.offsetHeight;
  let mouseX=e.offsetX;
  let mouseY=e.offsetY;
  let bigPosX=(mouseX / width*100);
  let bigPosY=(mouseY / height*100);
  zoom.classList.add("bigImage");
  zoom.style.backgroundSize="250%";
  zoom.style.backgroundPosition=image.style.backgroundPosition=`${bigPosX}% ${bigPosY}%`;
})
 
  image.addEventListener("mouseleave",function(){
  image.style.backgroundPosition="center";
})
//end of zoom effect

  





