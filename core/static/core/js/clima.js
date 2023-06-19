function obtenerClima() {
    const apiKey = '69023853454b77bb14f59764b1216bff'; // Reemplaza 'TU_CLAVE_DE_API' con tu propia clave de API
    const ciudad = 'Santiago de chile'; // Reemplaza 'NOMBRE_DE_LA_CIUDAD' con el nombre de la ciudad que deseas consultar

    // Realiza una solicitud GET a la API de OpenWeatherMap
    fetch(
      `https://api.openweathermap.org/data/2.5/weather?q=${ciudad}&appid=${apiKey}&units=metric`
    )
      .then(response => response.json())
      .then(data => {
        // Accede a los datos del clima en el objeto 'data' y actualiza los elementos HTML con la información correspondiente
        const temperatura = data.main.temp;
        const descripcion = data.weather[0].description;
        const elementoTemperatura = document.getElementById('temperatura');
        const elementoDescripcion = document.getElementById('descripcion');
        elementoTemperatura.textContent = temperatura + ' °C';
        elementoDescripcion.textContent = descripcion;
      })
      .catch(error => console.log(error));
  }