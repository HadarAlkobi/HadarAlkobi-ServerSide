const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('div a').forEach(link => {
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
    console.log(link);
  }
})

function bigImg(x) {
    x.style.height = "350px";
    x.style.width = "350px";
  }
  
  function normalImg(x) {
    x.style.height = "300px";
    x.style.width = "300px";
  }
