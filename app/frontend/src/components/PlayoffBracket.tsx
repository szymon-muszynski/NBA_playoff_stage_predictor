import { useState } from 'react';
import { SingleSeriesResult, PlayoffSimulationResponse } from '../types';

interface Props {
  data: PlayoffSimulationResponse | null;
}

// 1. Komponent Modala (Wyskakującego okienka z historią)
const SeriesModal = ({ series, onClose }: { series: SingleSeriesResult; onClose: () => void }) => {
  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <button className="close-btn" onClick={onClose}>&times;</button>
        <h2>{series.team_a} vs {series.team_b}</h2>
        <h3 style={{ color: '#4CAF50' }}>Zwycięzca: {series.winner}</h3>
        
        <div className="series-history">
          <h4>Przebieg serii:</h4>
          <ul>
            {series.winners_history.map((winner, index) => {
              // Sprawdzamy kto przegrał dany mecz, żeby ładnie to wyświetlić
              const loser = winner === series.team_a ? series.team_b : series.team_a;
              return (
                <li key={index} className={winner === series.team_a ? 'team-a-win' : 'team-b-win'}>
                  <strong>Mecz {index + 1}:</strong> {winner} pokonuje {loser}
                </li>
              );
            })}
          </ul>
        </div>
      </div>
    </div>
  );
};

// 2. Komponent pojedynczego prostokąta (Karty Meczowej)
const MatchupCard = ({ series, onClick }: { series: SingleSeriesResult; onClick: () => void }) => {
  const teamAWins = series.winners_history.filter(w => w === series.team_a).length;
  const teamBWins = series.winners_history.filter(w => w === series.team_b).length;
  
  const isAWinner = series.winner === series.team_a;
  
  return (
    <div className="matchup-card" onClick={onClick}>
      <div className={`team-row ${isAWinner ? 'winner' : ''}`}>
        <span>{series.team_a}</span>
        <span>{teamAWins}</span>
      </div>
      <div className={`team-row ${!isAWinner ? 'winner' : ''}`}>
        <span>{series.team_b}</span>
        <span>{teamBWins}</span>
      </div>
    </div>
  );
};

// 3. Główny komponent Drabinki
export const PlayoffBracket = ({ data }: Props) => {
  // Stan przechowujący serię, którą użytkownik aktualnie "klika"
  const [selectedSeries, setSelectedSeries] = useState<SingleSeriesResult | null>(null);

  if (!data) return null;

  return (
    <>
      <div className="bracket-container">
        {/* ZACHÓD (Lewa strona) */}
        <div className="conference-side">
          <div className="round-col">
            {data.bracket.Western.round_1.map((s, i) => 
              <MatchupCard key={`w-r1-${i}`} series={s} onClick={() => setSelectedSeries(s)} />
            )}
          </div>
          <div className="round-col">
            {data.bracket.Western.round_2.map((s, i) => 
              <MatchupCard key={`w-r2-${i}`} series={s} onClick={() => setSelectedSeries(s)} />
            )}
          </div>
          <div className="round-col">
            {data.bracket.Western.conference_finals.map((s, i) => 
              <MatchupCard key={`w-cf-${i}`} series={s} onClick={() => setSelectedSeries(s)} />
            )}
          </div>
        </div>

        {/* FINAŁY (Środek) */}
        <div className="finals-col">
          <h3>NBA Finals</h3>
          <MatchupCard series={data.nba_finals} onClick={() => setSelectedSeries(data.nba_finals)} />
          <div className="champion-box">
            🏆 MISTRZ: {data.champion} 🏆
          </div>
        </div>

        {/* WSCHÓD (Prawa strona) */}
        <div className="conference-side" style={{ flexDirection: 'row-reverse' }}>
          <div className="round-col">
            {data.bracket.Eastern.round_1.map((s, i) => 
              <MatchupCard key={`e-r1-${i}`} series={s} onClick={() => setSelectedSeries(s)} />
            )}
          </div>
          <div className="round-col">
            {data.bracket.Eastern.round_2.map((s, i) => 
              <MatchupCard key={`e-r2-${i}`} series={s} onClick={() => setSelectedSeries(s)} />
            )}
          </div>
          <div className="round-col">
            {data.bracket.Eastern.conference_finals.map((s, i) => 
              <MatchupCard key={`e-cf-${i}`} series={s} onClick={() => setSelectedSeries(s)} />
            )}
          </div>
        </div>
      </div>

      {/* Wyświetlamy okienko tylko wtedy, gdy selectedSeries NIE jest nullem */}
      {selectedSeries && (
        <SeriesModal series={selectedSeries} onClose={() => setSelectedSeries(null)} />
      )}
    </>
  );
};