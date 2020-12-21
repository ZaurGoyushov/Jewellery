window.onscroll = function () { scrollFunction() };

function scrollFunction() {
  if (document.body.scrollTop > 400 || document.documentElement.scrollTop > 400) {
    document.querySelector(".top_Nav ").style.backgroundColor = "#6c757d";
  } else {
    document.querySelector(".top_Nav ").style.backgroundColor = "transparent";
  }
};

function search() {
  var srcBtn = document.getElementById('search_layout');
  srcBtn.style.transform = "scale(1)";
  srcBtn.style.transformOrigin = "left";

};

function close() {
  var srcBtn = document.getElementById('search_layout');
  srcBtn.style.transform = "scale(0)";
  srcBtn.style.transformOrigin = "right";

}
