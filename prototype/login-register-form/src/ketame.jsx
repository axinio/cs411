import React, { useState } from "react";
import logo from "./pill_logo.svg";

export const Main = (props) => {
    const [med, setMed] = useState('');
    const [dose, setDose] = useState('');
    const [medicines, setMedicines] = useState([]);

    const handleSubmit = (e) => {
        e.preventDefault();
        setMedicines([...medicines, { med: med, dose: dose }]);
        setMed('');
        setDose('');
    }

    const handleDelete = (medicine) => {
        setMedicines(medicines.filter(m => m !== medicine));
    }

    return (
        <div className="main-page">
            <div className="med-form-container">
                <img src={logo} className="Pill-logo" alt="logo" />
                <h2>KetaMe</h2>
                <form className="med-form" onSubmit={handleSubmit}>
                    <input value={med} onChange={(e) => setMed(e.target.value)}type="med" placeholder="Medicine" id="med" name="med" />
                    <input value={dose} onChange={(e) => setDose(e.target.value)} type="dose" placeholder="mg" id="dose" name="dose" />
                    <button type="submit">Add</button>
                </form>
                <button className="link-btn" type="log-out" onClick={() => props.onFormSwitch('login')}>Log Out</button>
            </div>
            <div className="med-list">
                {medicines.map((medicine, index) => (
                <div key={index} className="med-item">
                    <p>{medicine.med}<br /><span style={{fontSize: "12px"}}>{medicine.dose} mg</span></p>
                    <button className="delete-btn" style={{fontSize: "18px"}} onClick={() => handleDelete(medicine)}>✕</button>
                </div>
                ))}
            </div>
        </div>
    )
}