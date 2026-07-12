import axios from 'axios';
import { SeriesSimulationRequest, SeriesSimulationResponse, PlayoffSimulationRequest, PlayoffSimulationResponse } from '../types';

const API_BASE_URL = 'https://nba-playoff-stage-predictor.onrender.com/api/simulations';

export const simulateSeries = async (data: SeriesSimulationRequest): Promise<SeriesSimulationResponse> => {
  try {
    const response = await axios.post<SeriesSimulationResponse>(`${API_BASE_URL}/series`, data);
    return response.data;
  } catch (error: any) {
    if (error.response && error.response.data && error.response.data.detail) {
      throw new Error(error.response.data.detail);
    }
    throw new Error('Wystąpił błąd podczas komunikacji z serwerem. Czy backend jest włączony?');
  }
};

export const simulatePlayoffs = async (data: PlayoffSimulationRequest): Promise<PlayoffSimulationResponse> => {
  try {
    const response = await axios.post<PlayoffSimulationResponse>(`${API_BASE_URL}/whole_playoffs`, data);
    return response.data;
  } catch (error: any) {
    if (error.response && error.response.data && error.response.data.detail) {
      throw new Error(error.response.data.detail);
    }
    throw new Error('Wystąpił błąd podczas komunikacji z serwerem.');
  }
};