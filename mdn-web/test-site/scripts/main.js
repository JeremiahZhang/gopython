var myImage = document.querySelector('img');

myImage.onclick = function() {
    var mySrc = myImage.getAttribute('src');
    
    if(mySrc == 'https://upload.wikimedia.org/wikipedia/en/thumb/1/1e/C.s.lewis3.JPG/220px-C.s.lewis3.JPG') {
        myImage.setAttribute('src', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSGZG8cGsd888PCrePP4zckA4X2hUvPv4R3-5_fuhdc2T53QXX')
    } else {
        myImage.setAttribute('src', 'https://upload.wikimedia.org/wikipedia/en/thumb/1/1e/C.s.lewis3.JPG/220px-C.s.lewis3.JPG')
    }
}