window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 400 || document.documentElement.scrollTop > 400) {
      document.querySelector(".top_Nav ").style.backgroundColor = "#6c757d";
    } else {
      document.querySelector(".top_Nav ").style.backgroundColor = "transparent";
    }
  }