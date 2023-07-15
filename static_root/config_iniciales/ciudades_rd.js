const selectProvincias = document.getElementById("provincias");

// Lista de provincias de la República Dominicana
const provinciasRD = [
  "Santo Domingo",
  "San Cristóbal",
  "San José de Ocoa",
  "San Juan",
  "San Pedro de Macorís",
  "Sánchez Ramírez",
  "Santiago",
  "Santiago Rodríguez",
  "Samaná",
  "Azua",
  "Bahoruco",
  "Barahona",
  "Dajabón",
  "Distrito Nacional",
  "Duarte",
  "Elías Piña",
  "El Seibo",
  "Espaillat",
  "Hato Mayor",
  "Hermanas Mirabal",
  "Independencia",
  "La Altagracia",
  "La Romana",
  "La Vega",
  "María Trinidad Sánchez",
  "Monseñor Nouel",
  "Monte Cristi",
  "Monte Plata",
  "Pedernales",
  "Peravia",
  "Puerto Plata",
  "Valverde"
];

// Iterar por la lista de provincias y crear una opción para cada una
for (let i = 0; i < provinciasRD.length; i++) {
  const option = document.createElement("option");
  option.value = provinciasRD[i];
  option.text = provinciasRD[i];
  selectProvincias.appendChild(option);
}