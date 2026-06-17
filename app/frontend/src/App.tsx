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