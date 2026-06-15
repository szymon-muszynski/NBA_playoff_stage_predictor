import { useState } from 'react';
import { SeriesSimulationRequest } from '../types';

interface Props {
  onSubmit: (data: SeriesSimulationRequest) => void;
  isLoading: boolean;
}

export const SimulationForm = ({ onSubmit, isLoading }: Props) => {
  // Lokalne stany dla formularza
  const [season, setSeason] = useState('2014-15');
  const [homeTeam, setHomeTeam] = useState('GSW');
  const [awayTeam, setAwayTeam] = useState('LAL');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault(); // Zapobiega przeładowaniu strony po kliknięciu
    onSubmit({
      season: season,
      home_team: homeTeam.toUpperCase(),
      away_team: awayTeam.toUpperCase()
    });
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '10px', maxWidth: '300px', margin: '0 auto' }}>
      <div>
        <label>Sezon:</label>
        <input 
          value={season} 
          onChange={(e) => setSeason(e.target.value)} 
          placeholder="np. 2014-15"
          required 
        />
      </div>
      <div>
        <label>Gospodarz (Wyżej rozstawiony):</label>
        <input 
          value={homeTeam} 
          onChange={(e) => setHomeTeam(e.target.value)} 
          placeholder="np. GSW"
          required 
        />
      </div>
      <div>
        <label>Gość (Niżej rozstawiony):</label>
        <input 
          value={awayTeam} 
          onChange={(e) => setAwayTeam(e.target.value)} 
          placeholder="np. LAL"
          required 
        />
      </div>
      <button type="submit" disabled={isLoading}>
        {isLoading ? 'Symulowanie...' : 'Symuluj Serię'}
      </button>
    </form>
  );
};