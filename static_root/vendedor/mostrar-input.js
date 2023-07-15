const btnTransferencia = document.getElementById('btn-transferencia');
const btnDeposito = document.getElementById('btn-deposito');
const inputMetodoPago = document.getElementById('metodo_pago');
const divCuenta = document.getElementById('cuenta');

btnTransferencia.addEventListener('click', () => {
  inputMetodoPago.value = 'Transferencia bancaria';
  divCuenta.style.display = 'block';
});

btnDeposito.addEventListener('click', () => {
  inputMetodoPago.value = 'Depósito de efectivo';
  divCuenta.style.display = 'none';
});