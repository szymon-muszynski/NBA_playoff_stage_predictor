import { useState } from 'react';
import './App.css';
import { PlayoffForm } from './components/PlayoffForm';
import { PlayoffBracket } from './components/PlayoffBracket';
import { simulatePlayoffs } from './api/simulations';
import { PlayoffSimulationResponse } from './types';

function App() {
  const [result, setResult] = useState<PlayoffSimulationResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const handleSimulationSubmit = async (season: string) => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const data = await simulatePlayoffs({ season });
      setResult(data);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App" style={{ textAlign: 'center', padding: '20px' }}>
      <h1>🏀 NBA Playoff Simulator</h1>
      
      <PlayoffForm onSubmit={handleSimulationSubmit} isLoading={loading} />

      {loading && (
        <div style={{
          marginTop: '20px',
          padding: '15px',
          backgroundColor: '#2a2a2a',
          borderLeft: '4px solid #646cff',
          borderRadius: '8px',
          color: '#e0e0e0',
          maxWidth: '550px',
          margin: '20px auto',
          textAlign: 'left'
        }}>
          <p style={{ margin: '0 0 8px 0', fontWeight: '500', fontSize: '1.1em', color: '#646cff' }}>
            ⏳ Trwa symulacja, proszę czekać...
          </p>
          <p style={{ margin: 0, fontSize: '0.9em', color: '#aaa', lineHeight: '1.4' }}>
            <strong>Uwaga:</strong> Strona korzysta z darmowego serwera. Jeśli to pierwsza symulacja od dłuższego czasu, serwer musi się wybudzić, co może zająć <strong>około minuty</strong>. Każda kolejna symulacja zajmie mniej!
          </p>
        </div>
      )}

      {error && (
        <div style={{ color: 'red', margin: '20px' }}>
          <strong>Błąd:</strong> {error}
        </div>
      )}

      {/* Rysowanie drabinki */}
      <PlayoffBracket data={result} />
    </div>
  );
}

export default App;