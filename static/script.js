// Changing product colors
mainImg = document.getElementById("MainImg");
smImg = document.getElementsByClassName("small-img");

smImg[0].onclick = function() {
    mainImg.src = smImg[0].src;
}
smImg[1].onclick = function() {
    mainImg.src = smImg[1].src;
}
smImg[2].onclick = function() {
    mainImg.src = smImg[2].src;
}
smImg[3].onclick = function() {
    mainImg.src = smImg[3].src;
}

