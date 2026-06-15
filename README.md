# 🏀 NBA Playoff Predictor

Aplikacja full-stack wykorzystująca Machine Learning do przewidywania wyników serii Playoff NBA na podstawie historycznych danych i statystyk drużynowych z sezonu zasadniczego.

Projekt łączy analitykę sportową, uczenie maszynowe oraz nowoczesne technologie webowe, umożliwiając symulowanie pojedynczych serii playoffowych oraz — w kolejnych etapach rozwoju — całych drabinek Playoff NBA.

---

## 📖 Opis projektu

Celem projektu jest stworzenie systemu, który na podstawie danych historycznych potrafi oszacować prawdopodobieństwo zwycięstwa drużyny w serii playoffowej.

Aplikacja składa się z:

* backendu opartego o FastAPI,
* frontendu stworzonego w React + TypeScript,
* warstwy Machine Learning wykorzystującej modele trenowane na danych NBA z lat 2010–2024.

Obecnie użytkownik może symulować pojedyncze serie Playoff NBA w formacie Best-of-7.

---

## 🛠️ Stos technologiczny

### Backend

* Python
* FastAPI
* Pandas
* Scikit-learn
* Pydantic
* Joblib
* Uvicorn

### Frontend

* React
* TypeScript
* Vite
* Axios

### Machine Learning

* Regresja Logistyczna
* Skalowanie cech (Feature Scaling)
* Historyczne statystyki drużyn NBA (2010–2024)

---

## 🏗️ Architektura

```text
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

```text
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

* Dependency Injection (`Depends`)
* Walidacja danych przez Pydantic
* Ładowanie modeli przy starcie aplikacji
* Rozdzielenie logiki API od logiki biznesowej
* Architektura modułowa ułatwiająca dalszy rozwój projektu

---

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

Upewnij się, że w katalogu `backend/data/` znajdują się:

```text
models_by_season.joblib
regular_season_stats_from_2010-11_to_2023-24.csv
```

Uruchom serwer:

```bash
uvicorn main:app --reload
```

Backend będzie dostępny pod adresem:

```text
http://localhost:8000
```

Dokumentacja API (Swagger):

```text
http://localhost:8000/docs
```

---

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

```text
http://localhost:5173
```

---

## 🤖 Podejście Machine Learning

### Aktualna wersja modelu

Obecnie aplikacja wykorzystuje:

* Regresję Logistyczną
* Statystyki drużynowe z sezonu zasadniczego
* Wskaźniki przewagi własnego parkietu
* Historyczne wyniki Playoff NBA

Modele trenowane są osobno dla każdego sezonu, co pozwala lepiej odwzorować specyfikę danego okresu i zmiany zachodzące w lidze.

### Logika symulacji

Silnik symulacyjny uwzględnia:

* format Best-of-7,
* oficjalny układ meczów NBA (2-2-1-1-1),
* przewagę własnego parkietu,
* prawdopodobieństwa generowane przez modele ML.

---

## 📈 Roadmap

### Faza 1 — Fundamenty ✅

* Przygotowanie zbioru danych
* Inżynieria cech
* Trening modeli ML
* Serializacja modeli
* Backend FastAPI
* Frontend React
* Symulacja pojedynczej serii

### Faza 2 — Symulacja całej drabinki 🚧

* [ ] Symulacja pełnych Playoffów NBA
* [ ] Automatyczne generowanie kolejnych rund
* [ ] Finały Konferencji
* [ ] Finały NBA

### Faza 3 — Zaawansowane ML 🚧

* [ ] Implementacja XGBoost
* [ ] Wskaźnik Momentum
* [ ] Analiza ostatnich meczów sezonu
* [ ] Rozszerzony zestaw cech
* [ ] Analiza ważności cech

### Faza 4 — Rozbudowa platformy 🚧

* [ ] Interaktywna wizualizacja drabinki
* [ ] Integracja z PostgreSQL
* [ ] Zapisywanie symulacji użytkowników
* [ ] Historia symulacji
* [ ] Wdrożenie do chmury

---

## 🔮 Możliwe kierunki rozwoju

* XGBoost i modele zespołowe
* Symulacje Monte Carlo
* Uwzględnianie kontuzji zawodników
* Integracja systemu ELO
* Integracja z publicznym API NBA
* Konta użytkowników
* Konteneryzacja przy użyciu Dockera
* Deployment do AWS, Azure lub Railway

---

## 🎯 Cele projektu

Projekt powstał w celu rozwijania praktycznych umiejętności z zakresu:

* Machine Learning Engineering
* Data Science
* Programowania Backendowego
* Programowania Frontendowego
* Projektowania REST API
* Architektury oprogramowania
* Analityki sportowej

---

## 📄 Licencja

Projekt tworzony w celach edukacyjnych oraz portfolio programistycznego.
