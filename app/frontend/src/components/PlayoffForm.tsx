import { useState } from 'react';

interface Props {
  onSubmit: (season: string) => void;
  isLoading: boolean;
}

export const PlayoffForm = ({ onSubmit, isLoading }: Props) => {
  const [season, setSeason] = useState('2023-24');

  // Generowanie listy sezonów (od 2010-11 do 2023-24)
  const seasons = [];
  for (let year = 2010; year <= 2023; year++) {
    const nextYearStr = (year + 1).toString().slice(2);
    seasons.push(`${year}-${nextYearStr}`);
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(season);
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: '20px', display: 'flex', gap: '10px', justifyContent: 'center' }}>
      <select 
        value={season} 
        onChange={(e) => setSeason(e.target.value)}
        style={{ padding: '8px', fontSize: '16px' }}
      >
        {seasons.map(s => (
          <option key={s} value={s}>{s}</option>
        ))}
      </select>
      <button type="submit" disabled={isLoading} style={{ padding: '8px 16px', cursor: 'pointer' }}>
        {isLoading ? 'Symulowanie...' : 'Symuluj Playoffy'}
      </button>
    </form>
  );
};