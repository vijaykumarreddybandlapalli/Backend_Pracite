let display = document.getElementById("display");
let currentInput = "";

function appendNumber(number) {
  if (currentInput === "0") currentInput = "";
  currentInput += number;
  updateDisplay();
}

function appendOperator(operator) {
  const lastChar = currentInput.slice(-1);
  if (["+","-","*","/"].includes(lastChar)) return;
  currentInput += operator;
  updateDisplay();
}

function deleteLast() {
  currentInput = currentInput.slice(0, -1);
  if (currentInput === "") currentInput = "0";
  updateDisplay();
}

function reset() {
  currentInput = "0";
  updateDisplay();
}

function calculate() {
  try {
    currentInput = eval(currentInput).toString();
    updateDisplay();
  } catch {
    display.innerText = "Error";
    currentInput = "0";
  }
}

function updateDisplay() {
  display.innerText = currentInput;
}
