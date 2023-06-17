const switchButton = document.getElementById('switch');
const workContainer = document.getElementById('work');
 
switchButton.addEventListener('click', () => {
    document.body.classList.toggle('dark'); //cambiar el cuerpo del HTML por la clase 'dark'
    switchButton.classList.toggle('active');//cambiar el botón HTML con el id='switch' con la clase 'active'
    workContainer.classList.toggle('dark');
 
   if(document.body.classList.contains('dark')){ //cuando el cuerpo tiene la clase 'dark' actualmente
        localStorage.setItem('darkMode', 'enabled'); //almacenar estos datos si el modo oscuro está activado
    }else{
        localStorage.setItem('darkMode', 'disabled'); //almacenar estos datos si el modo oscuro está desactivado
    }
});

if(localStorage.getItem('darkMode') == 'enabled'){
    document.body.classList.toggle('dark');
    switchButton.classList.toggle('active');
    workContainer.classList.toggle('dark');
}