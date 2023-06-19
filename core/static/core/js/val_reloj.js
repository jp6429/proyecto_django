function horaActual() {
    var hoy = new Date();
    var hora = hoy.getHours();
    var minutos = hoy.getMinutes();
    var segundos = hoy.getSeconds();
    ap = (hora < 12) ? "<span>AM</span>" : "<span>PM</span>";
    hora = (hora == 0) ? 12 : hora;
    hora = (hora > 12) ? hora - 12 : hora;
    //Agrega un 0 a numeros <10
    hora = checkTime(hora);
    minutos = checkTime(minutos);
    segundos = checkTime(segundos);
    document.getElementById("reloj").innerHTML = hora + ":" + minutos + ":" + segundos + " " + ap;
    
    var meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
    var dias = ['Domingo', 'Lunes', 'Martes', 'miercoles', 'Jueves', 'Viernes', 'Sabado'];
    var diaActual = dias[hoy.getDay()];
    var dia = hoy.getDate();
    var mes = meses[hoy.getMonth()];
    var annio = hoy.getFullYear();
    var date = diaActual+ " " +dia+" de "+mes+" "+annio;
    document.getElementById("fecha").innerHTML = date;
    
    var time = setTimeout(function(){ horaActual() }, 1000);
}
function checkTime(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
}