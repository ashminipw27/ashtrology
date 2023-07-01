import React, { useEffect, useState } from 'react';

function App() {
  const [message, setMessage] = useState('');
  const [inputValue, setInputValue] = useState('');
  const [generatedText, setGeneratedText] = useState('');

  useEffect(() => {
    fetch('/api/data')
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(error => console.log(error));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('/api/data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ value: inputValue }),
    })
      .then(response => response.text()) // Use response.text() to get the generated text as a string
      .then(data => {
        console.log('Response from server:', data);
        setGeneratedText(data); // Update the generatedText state with the received text
      })
      .catch(error => console.log(error));
  };

  return (
    <div className="App">
      <h1>{message}</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Enter a value"
        />
        <button type="submit">Submit</button>
      </form>
      {generatedText && <p>{generatedText}</p>} {/* Display the generatedText if available */}
    </div>
  );
}

export default App;


