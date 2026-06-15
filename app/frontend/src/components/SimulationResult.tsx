import { SeriesSimulationResponse } from '../types';

interface Props {
  result: SeriesSimulationResponse | null;
}

export const SimulationResult = ({ result }: Props) => {
  if (!result) return null;

  return (
    <div style={{ marginTop: '20px', padding: '20px', border: '1px solid #ccc', borderRadius: '8px' }}>
      <h2>Wynik Symulacji</h2>
      <p><strong>Sezon:</strong> {result.season}</p>
      <p><strong>Pojedynek:</strong> {result.matchup}</p>
      <h3>Zwycięzca: <span style={{ color: '#4CAF50' }}>{result.winner}</span></h3>
    </div>
  );
};