import { useState } from 'react';
import './App.css';
import { SimulationForm } from './components/SimulationForm';
import { SimulationResult } from './components/SimulationResult';
import { simulateSeries } from './api/simulations';
import { SeriesSimulationRequest, SeriesSimulationResponse } from './types';

function App() {
  // Stany aplikacji
  const [result, setResult] = useState<SeriesSimulationResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  // Funkcja wywoływana, gdy formularz zostanie wysłany
  const handleSimulationSubmit = async (requestData: SeriesSimulationRequest) => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      // Wołamy nasz serwis API
      const data = await simulateSeries(requestData);
      setResult(data);
    } catch (err: any) {
      // Wyłapujemy błąd (np. brak statystyk drużyny) i ustawiamy go w stanie
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App" style={{ textAlign: 'center', padding: '20px' }}>
      <h1>NBA Playoff Simulator</h1>
      <p>Podaj drużyny i sprawdź, kto wygra serię!</p>
      
      {/* Nasz komponent formularza */}
      <SimulationForm onSubmit={handleSimulationSubmit} isLoading={loading} />

      {/* Komunikat o błędzie */}
      {error && (
        <div style={{ color: 'red', marginTop: '20px' }}>
          <strong>Błąd:</strong> {error}
        </div>
      )}

      {/* Nasz komponent z wynikiem */}
      <SimulationResult result={result} />
    </div>
  );
}

export default App;