import React, { useState } from 'react';

function App() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const handleMessageChange = (event) => {
    setMessage(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const response = await fetch('http://localhost:5000/message', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    });

    const data = await response.json();

    setResponse(data.response);
  };

  return (
    <div>
      <h2>Chat z ChatGPT</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="message">Wiadomość:</label>
          <input
            type="text"
            id="message"
            value={message}
            onChange={handleMessageChange}
          />
        </div>
        <button type="submit">Wyślij</button>
      </form>
      {response && <p>Odpowiedź: {response}</p>}
    </div>
  );
}

export default App;
