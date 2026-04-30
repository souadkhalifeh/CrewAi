# Travel Assistant Crew

A multi-agent AI travel assistant built with [CrewAI](https://www.crewai.com/), powered by **Groq (llama-3.3-70b-versatile)**. Given a departure city, destination, and travel date, the crew automatically searches for flights, recommends hotels, builds a 5-day itinerary, and provides practical travel advice.

---

## Agents

| Agent | Role | Output |
|---|---|---|
| **Flight Checker** | Searches available flights between origin and destination | `search_flights_task.md` |
| **Hotel Recommender** | Suggests hotels across budget, mid-range, and luxury tiers | `hotels_result.md` |
| **Tour Guide** | Builds a day-by-day 5-day tourism itinerary | `tour_itinerary.md` |
| **Travel Advisor** | Provides visa, safety, currency, and cultural advice | `travel_advice.md` |

Agents run **sequentially** — each one hands its output to the next.

---

## Project Structure

```
my_crew/
├── src/my_crew/
│   ├── config/
│   │   ├── agents.yaml          # Agent roles, goals, and backstories
│   │   └── tasks.yaml           # Task descriptions and expected outputs
│   ├── tools/
│   │   └── flight_tool.py       # Dummy flight search tool (random data)
│   ├── crew.py                  # Crew wiring: agents, tasks, LLM config
│   └── main.py                  # Entry point
├── .env                         # API keys and model config
└── pyproject.toml
```

---

## Setup

**1. Clone and install dependencies**

```bash
cd my_crew
pip install -e .
```

**2. Configure your `.env`**

```env
MODEL=groq/llama-3.3-70b-versatile
GROQ_API_KEY=your_groq_api_key_here
```

Get a free Groq API key at [console.groq.com](https://console.groq.com).

**3. Set your travel inputs in `main.py`**

```python
inputs = {
    'origin': 'Paris',
    'destination': 'Tokyo',
    'date': '2026-06-15',
}
```

---

## Run

```bash
python -c "from my_crew.main import run; run()"
```

Or using the CrewAI CLI:

```bash
crewai run
```

---

## Output Files

After the crew finishes, four markdown files are generated in the project root:

| File | Contents |
|---|---|
| `search_flights_task.md` | Available flights with prices, times, and a best-value recommendation |
| `hotels_result.md` | Hotel options by budget tier with amenities and top picks |
| `tour_itinerary.md` | 5-day itinerary with morning/afternoon/evening plans and restaurant tips |
| `travel_advice.md` | Visa info, weather, currency, safety tips, cultural etiquette, packing list |

---

## Tech Stack

- [CrewAI](https://www.crewai.com/) `1.14.3`
- [Groq](https://console.groq.com) — `llama-3.3-70b-versatile`
- Python `>=3.10`
