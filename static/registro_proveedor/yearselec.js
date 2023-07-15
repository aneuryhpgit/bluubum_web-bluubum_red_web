const selectYear = document.getElementById("year");
const currentYear = new Date().getFullYear();

for (let year = currentYear; year >= 1900; year--) {
  const option = document.createElement("option");
  option.value = year;
  option.text = year;
  selectYear.appendChild(option);
}
