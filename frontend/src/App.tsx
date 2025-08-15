import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [message, setMessage] = useState<string>('')
  const [loading, setLoading] = useState<boolean>(true)

  useEffect(() => {
    fetch('http://localhost:8000/')
      .then(res => res.json())
      .then(data => {
        setMessage(data.message)
        setLoading(false)
      })
      .catch(err => {
        console.error('Error:', err)
        setLoading(false)
      })
  }, [])

  return (
    <div className="App">
      <h1>🚀 Tenax MVP</h1>
      {loading ? (
        <p>Cargando desde el backend...</p>
      ) : (
        <div>
          <p className="backend-message">{message}</p>
          <p className="frontend-status">✅ Frontend React + Vite funcionando</p>
        </div>
      )}
    </div>
  )
}

export default App