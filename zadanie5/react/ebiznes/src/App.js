import React, { useState, useEffect } from 'react';


function Produkty() {
  const [produkty, setProdukty] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8080/products')
      .then(response => response.json())
      .then(data => setProdukty(data))
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h2>Lista produktów</h2>
      <ul>
        {produkty.map(produkt => (
          <li key={produkt.id}>
            {produkt.name} - {produkt.price} zł
          </li>
        ))}
      </ul>
    </div>
  );
}

function Płatności() {
  const [nazwa, setNazwa] = useState('');
  const [numerKarty, setNumerKarty] = useState('');

  function handleSubmit(event) {
    event.preventDefault();
    fetch('/api/płatności', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nazwa, numerKarty })
    })
    .then(response => console.log(response))
    .catch(error => console.log(error));
  }

  return (
    <div>
      <h2>Formularz płatności</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Nazwa na karcie:
          <input type="text" value={nazwa} onChange={event => setNazwa(event.target.value)} />
        </label>
        <label>
          Numer karty:
          <input type="text" value={numerKarty} onChange={event => setNumerKarty(event.target.value)} />
        </label>
        <button type="submit">Wyślij</button>
      </form>
    </div>
  );
}

function App() {
  return (
    <div>
      <Produkty />
      <Płatności />
    </div>
  );
}

export default App;
