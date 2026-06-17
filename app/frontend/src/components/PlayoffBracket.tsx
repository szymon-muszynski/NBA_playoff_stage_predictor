import { SingleSeriesResult, PlayoffSimulationResponse } from '../types';

interface Props {
  data: PlayoffSimulationResponse | null;
}

// Komponent pomocniczy do wyświetlania jednego meczu
const MatchupCard = ({ series }: { series: SingleSeriesResult }) => {
  // Obliczanie wyniku serii (np. 4-2) z tablicy winners_history
  const teamAWins = series.winners_history.filter(w => w === series.team_a).length;
  const teamBWins = series.winners_history.filter(w => w === series.team_b).length;
  
  const isAWinner = series.winner === series.team_a;
  
  return (
    <div className="matchup-card">
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

export const PlayoffBracket = ({ data }: Props) => {
  if (!data) return null;

  return (
    <div className="bracket-container">
      {/* ZACHÓD (Lewa strona) */}
      <div className="conference-side">
        <div className="round-col">
          {data.bracket.Western.round_1.map((s, i) => <MatchupCard key={`w-r1-${i}`} series={s} />)}
        </div>
        <div className="round-col">
          {data.bracket.Western.round_2.map((s, i) => <MatchupCard key={`w-r2-${i}`} series={s} />)}
        </div>
        <div className="round-col">
          {data.bracket.Western.conference_finals.map((s, i) => <MatchupCard key={`w-cf-${i}`} series={s} />)}
        </div>
      </div>

      {/* FINAŁY (Środek) */}
      <div className="finals-col">
        <h3>NBA Finals</h3>
        <MatchupCard series={data.nba_finals} />
        <div className="champion-box">
          🏆 MISTRZ: {data.champion} 🏆
        </div>
      </div>

      {/* WSCHÓD (Prawa strona) */}
      <div className="conference-side" style={{ flexDirection: 'row-reverse' }}>
        <div className="round-col">
          {data.bracket.Eastern.round_1.map((s, i) => <MatchupCard key={`e-r1-${i}`} series={s} />)}
        </div>
        <div className="round-col">
          {data.bracket.Eastern.round_2.map((s, i) => <MatchupCard key={`e-r2-${i}`} series={s} />)}
        </div>
        <div className="round-col">
          {data.bracket.Eastern.conference_finals.map((s, i) => <MatchupCard key={`e-cf-${i}`} series={s} />)}
        </div>
      </div>
    </div>
  );
};