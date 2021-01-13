const displayedImage = document.querySelector('.displayed-img');
const thumbBar = document.querySelector('.thumb-bar');
const btn = document.querySelector('button');
const overlay = document.querySelector('.overlay');

/* Looping through images */
for(let photo = 1; photo <= 5; photo++) {
    const newPhoto = document.createElement('img');
    newPhoto.setAttribute('src', 'images/pic' + photo + '.jpg');
    thumbBar.appendChild(newPhoto);
    newPhoto.onclick = function(e) {
      displayedImage.src = e.target.src;
    }
}

/* Wiring up the Darken/Lighten button */
btn.onclick = function() {
    const btnClass = btn.getAttribute('class');
    if(btnClass === 'dark') {
      btn.setAttribute('class','light');
      btn.textContent = 'Clarear';
      overlay.style.backgroundColor = 'rgba(0,0,0,0.5)';
    }
    else {
      btn.setAttribute('class','dark');
      btn.textContent = 'Escurecer';
      overlay.style.backgroundColor = 'rgba(0,0,0,0)';
    }
}
