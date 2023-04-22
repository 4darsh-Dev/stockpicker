console.log("Hello I am working fine!");

let live = document.getElementById('live-btn');

live.addEventListener('click', function(){
    window.open("/live",'_self');
    console.log('I am clicked.')

})

let analyze = document.getElementById('analyze-btn');

analyze.addEventListener('click', function(){
    window.open("/analyze",'_self');
    console.log('I am clicked.')

})