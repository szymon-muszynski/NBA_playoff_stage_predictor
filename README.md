# 🏀 NBA Playoff Predictor

Aplikacja full-stack wykorzystująca Machine Learning do przewidywania wyników całych Playoffów NBA na podstawie historycznych danych i statystyk drużynowych z odpowiedniego sezonu zasadniczego.

Pierwsza wersja aplikacji jest funkcjonalna i pozwala na symulację pełnej drabinki turniejowej. Projekt łączy analitykę sportową, uczenie maszynowe oraz technologie webowe. Planowana jest dalsza rozbudowa systemu o nowe modele predykcyjne wraz z możliwością ich wyboru z poziomu interfejsu użytkownika.

<img width="1439" height="766" alt="image" src="https://github.com/user-attachments/assets/90f304d0-07e6-4084-80fc-f4e4e8e435e4" />
<img width="1439" height="766" alt="image" src="https://github.com/user-attachments/assets/01599821-df30-4f51-9ea3-9721b2dd11cc" />


## 📖 Opis projektu

Celem projektu jest stworzenie systemu, który na podstawie danych historycznych potrafi oszacować prawdopodobieństwo zwycięstwa drużyny w poszczególnych meczach i wygenerować realistyczny przebieg całego turnieju.

Aplikacja składa się z:

- backendu opartego o FastAPI,
- frontendu stworzonego w React + TypeScript,
- warstwy Machine Learning wykorzystującej modele trenowane na danych NBA z lat 2010–2024.

Obecnie użytkownik może wybrać dowolny sezon z dostępnej bazy i wygenerować kompletną drabinkę Playoff NBA (w formacie Best-of-7), od pierwszej rundy aż po finały, wraz z podglądem historii każdej serii.

## 🛠️ Stos technologiczny

### Backend
- Python
- FastAPI
- Pandas
- Scikit-learn
- Pydantic
- Joblib
- Uvicorn

### Frontend
- React
- TypeScript
- Vite
- Axios

### Machine Learning
- Regresja Logistyczna
- Skalowanie cech (Feature Scaling)
- Historyczne statystyki drużyn NBA (2010–2024)

## 🏗️ Architektura

```
Frontend (React + TypeScript)
            │
            ▼
      FastAPI REST API
            │
            ▼
      Warstwa Serwisów
            │
            ▼
      Silnik Symulacji
            │
            ▼
     Modele ML + Dane
```

Backend został zaprojektowany zgodnie z zasadą Separation of Concerns:

```
Warstwa API (Routery)
          │
          ▼
    Logika Biznesowa
          │
          ▼
 Silnik Predykcji / Symulacji
          │
          ▼
      Dane i Modele
```

Zastosowane rozwiązania:

- Dependency Injection (`Depends`)
- Walidacja zapytań i odpowiedzi przez Pydantic
- Ładowanie modeli do pamięci RAM przy starcie aplikacji (mechanizm Lifespan)
- Rozdzielenie logiki API od logiki biznesowej
- Architektura modułowa ułatwiająca dalszy rozwój projektu

## 🚀 Uruchomienie projektu lokalnie

### Backend

Przejdź do katalogu backendu:

```bash
cd backend
```

Utwórz środowisko wirtualne:

```bash
python -m venv venv
```

Aktywuj środowisko:

**Mac/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

Zainstaluj wymagane biblioteki:

```bash
pip install fastapi uvicorn pandas scikit-learn pydantic joblib
```

Upewnij się, że w katalogu `backend/data/` znajdują się pliki z danymi (m.in.):

```
models_by_season.joblib
regular_season_stats_from_2010-11_to_2023-24.csv
playoff_first_round_matchups.json
```

Uruchom serwer:

```bash
uvicorn main:app --reload
```

Backend będzie dostępny pod adresem:

```
http://localhost:8000
```

Dokumentacja API (Swagger): http://localhost:8000/docs

### Frontend

Otwórz nowe okno terminala:

```bash
cd frontend
```

Zainstaluj zależności:

```bash
npm install
```

Uruchom aplikację:

```bash
npm run dev
```

Frontend będzie dostępny pod adresem:

```
http://localhost:5173
```

## 🤖 Podejście Machine Learning

### Aktualna wersja modelu

Obecnie aplikacja wykorzystuje bazowy model Regresji Logistycznej, oparty o:

- Statystyki drużynowe z sezonu zasadniczego
- Wskaźniki przewagi własnego parkietu
- Deltę (różnicę) potencjału między rywalizującymi drużynami

Modele trenowane są osobno dla każdego sezonu, co pozwala lepiej odwzorować specyfikę danego okresu i historyczne zmiany zachodzące w lidze.

### Logika symulacji turniejowej

Silnik symulacyjny odwzorowuje zasady NBA, uwzględniając:

- format Best-of-7,
- oficjalny układ spotkań (2-2-1-1-1),
- sztywną drabinkę turniejową (bez reseeding'u),
- przyznawanie przewagi własnego parkietu na podstawie rozstawienia (seedu) lub bilansu wygranych w finałach.

## 📈 Roadmap

### Faza 1 — Wersja 1.0 (Gotowa) ✅

- Przygotowanie historycznego zbioru danych i inżynieria cech
- Trening, walidacja i serializacja bazowych modeli ML
- Solidna architektura backendu (FastAPI) i frontendu (React)
- Symulacja pełnej drabinki Playoff (od 1. rundy po Finały)
- Interaktywna wizualizacja drzewka turniejowego z wglądem w przebieg poszczególnych serii

### Faza 2 — Zaawansowane Modele ML i Analiza Formy 🚧
- [ ] Zastąpienie bazowych modeli algorytmami opartymi o drzewa decyzyjne (np. **XGBoost**, Random Forest).
- [ ] Wdrożenie podstawowych **Sieci Neuronowych (MLP - Multi-Layer Perceptron)** w celu uchwycenia złożonych, nieliniowych zależności między statystykami drużyn.
- [ ] Implementacja wskaźnika *Momentum* – uwzględnienie dodatkowych cech opisujących formę drużyny z ostatnich tygodni sezonu zasadniczego.
- [ ] Dodanie interfejsu na frontendzie umożliwiającego użytkownikowi wybór preferowanego modelu predykcyjnego (Regresja vs Drzewa vs Sieć Neuronowa) przed symulacją.

### Faza 3 — Granularność Danych (Poziom Zawodnika) 🚧
- [ ] Odejście od traktowania zespołu jako monolitu na rzecz modelu agregującego potencjał poszczególnych graczy.
- [ ] Uwzględnienie statystyk indywidualnych.
- [ ] Moduł analizy kontuzji i rotacji – dynamiczne przeliczanie siły drużyny na podstawie dostępności kluczowych zawodników w danej serii.
- [ ] Analiza bezpośrednich *matchups* – jak specyficzny styl gry i warunki fizyczne zespołu A wpływają na skuteczność zespołu B.

### Faza 4 — Rozbudowa platformy i wdrożenie 🚧
- [ ] Integracja z bazą PostgreSQL do zapisywania unikalnych symulacji generowanych przez użytkowników.
- [ ] Wdrożenie panelu historii symulacji.
- [ ] Konteneryzacja przy użyciu Dockera.
- [ ] Deployment aplikacji do chmury (AWS / Azure / Railway).

## 🎯 Cele projektu

Projekt powstał w celu rozwijania i łączenia praktycznych umiejętności z zakresu:

- Machine Learning Engineering & Data Science
- Programowania Backendowego (Python, API Design)
- Programowania Frontendowego (React, State Management)
- Architektury Oprogramowania (Clean Code)
- Analityki sportowej

## 📄 Licencja

Projekt tworzony w celach edukacyjnych oraz jako część portfolio programistycznego.
