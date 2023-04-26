import React, { useState } from "react";
import './App.css';
import { Login } from "./login";
import { Register } from "./register";
import { Main } from "./ketame";

function App() {
  const [currentForm, setCurrentForm] = useState('login');
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const toggleForm = (formName) => {
    setCurrentForm(formName);
    setIsLoggedIn(formName === 'main');
  }

  return (
    <div className="App">
      {
        isLoggedIn 
        ? <Main onFormSwitch={toggleForm} /> 
        : currentForm === "login" 
          ? <Login onFormSwitch={toggleForm} onLogin={() => setIsLoggedIn(true)} /> 
          : <Register onFormSwitch={toggleForm} onLogin={() => setIsLoggedIn(true)} />
      }
    </div>
  );
}

export default App;
