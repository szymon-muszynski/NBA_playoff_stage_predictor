import { SeriesSimulationRequest, SeriesSimulationResponse } from '../types';

const API_BASE_URL = 'http://localhost:8000/api/simulations';

export const simulateSeries = async (data: SeriesSimulationRequest): Promise<SeriesSimulationResponse> => {
  const response = await fetch(`${API_BASE_URL}/series`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Wystąpił błąd podczas komunikacji z serwerem');
  }

  return response.json();
};