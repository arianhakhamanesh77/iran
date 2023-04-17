let slides = [...document.querySelector('.slides').children];
let l = slides.length;
let slideIndex = 1;

function setSlide(input, index) {
     slideIndex = index;
     let item = document.querySelector(`#${input}`);
     slides.forEach((element) => {
          element.classList.remove('active');
     })
     item.classList.add('active');

}


setInterval(()=>{
     slideIndex += 1;
     if(slideIndex > l){
          slideIndex = 1;
     }
     setSlide(`s${slideIndex}`, slideIndex);
}, 4000)


let remainigTime = document.querySelector('#timeeee').value;

function setTime() {
     if(remainigTime == 0) return;
     let h = Math.floor(remainigTime/3600);
     let m = Math.floor((remainigTime%3600)/60);
     let s = (remainigTime%3600)%60;
     document.querySelector('#hours').innerHTML = h;
     document.querySelector('#minutes').innerHTML = m;
     document.querySelector('#seconds').innerHTML = s;
}
setInterval(()=>{
     remainigTime -= 1;
     setTime();
}, 1000)
