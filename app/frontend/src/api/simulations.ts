import axios from 'axios';
import { SeriesSimulationRequest, SeriesSimulationResponse } from '../types';

const API_BASE_URL = 'http://localhost:8000/api/simulations';

export const simulateSeries = async (data: SeriesSimulationRequest): Promise<SeriesSimulationResponse> => {
  try {
    // Axios automatycznie parsuje JSONa (zarówno wysyłanego, jak i odbieranego)
    // Używamy axios.post<TypOdpowiedzi>(URL, dane_do_wyslania)
    const response = await axios.post<SeriesSimulationResponse>(`${API_BASE_URL}/series`, data);
    
    // Dane z serwera są zawsze schowane w obiekcie response.data
    return response.data;

  } catch (error: any) {
    // Axios automatycznie traktuje kody 400 i 500 jako błędy i wrzuca je tutaj (do catch).
    // Musimy tylko wyciągnąć naszą wiadomość błędu (detail), którą wysłało FastAPI.
    
    if (error.response && error.response.data && error.response.data.detail) {
      // Błąd złapany i zwrócony przez FastAPI (np. "Brak modelu dla sezonu")
      throw new Error(error.response.data.detail);
    }
    
    // Błąd sieci (np. wyłączony serwer backendu)
    throw new Error('Wystąpił błąd podczas komunikacji z serwerem. Czy backend jest włączony?');
  }
};