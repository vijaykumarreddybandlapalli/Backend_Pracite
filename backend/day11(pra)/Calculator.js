import React, { useState } from 'react';
import './Calculator.css';

function Calculator() {
  const [input, setInput] = useState("");

  const handleClick = (value) => {
    setInput(input + value);
  };

  const handleClear = () => {
    setInput("");
  };

  const handleDelete = () => {
    setInput(input.slice(0, -1));
  };

  const handleCalculate = () => {
    try {
      setInput(eval(input).toString()); // Note: eval can be dangerous, avoid in production!
    } catch {
      setInput("Error");
    }
  };

  return (
    <div className="calculator">
      <div className="display">{input || "0"}</div>
      <div className="buttons">
        <button onClick={() => handleClick("7")}>7</button>
        <button onClick={() => handleClick("8")}>8</button>
        <button onClick={() => handleClick("9")}>9</button>
        <button onClick={handleDelete}>DEL</button>
        
        <button onClick={() => handleClick("4")}>4</button>
        <button onClick={() => handleClick("5")}>5</button>
        <button onClick={() => handleClick("6")}>6</button>
        <button onClick={() => handleClick("+")}>+</button>
        
        <button onClick={() => handleClick("1")}>1</button>
        <button onClick={() => handleClick("2")}>2</button>
        <button onClick={() => handleClick("3")}>3</button>
        <button onClick={() => handleClick("-")}>-</button>
        
        <button onClick={() => handleClick(".")}>.</button>
        <button onClick={() => handleClick("0")}>0</button>
        <button onClick={() => handleClick("/")}>/</button>
        <button onClick={() => handleClick("*")}>*</button>
        
        <button className="span-two" onClick={handleClear}>RESET</button>
        <button className="span-two" onClick={handleCalculate}>=</button>
      </div>
    </div>
  );
}

export default Calculator;
