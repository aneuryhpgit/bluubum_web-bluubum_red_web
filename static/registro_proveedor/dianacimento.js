const selectDay = document.getElementById("day");

for (let day = 1; day <= 31; day++) {
  const option = document.createElement("option");
  option.value = day;
  option.text = day;
  selectDay.appendChild(option);
}