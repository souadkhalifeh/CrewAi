# CrewAI Projects

A collection of multi-agent AI crews built with [CrewAI](https://www.crewai.com/). Each crew is an independent project that solves a specific problem using a team of collaborating AI agents.

---

## Crews

### 1. Travel Assistant — `my_crew/`

Given a departure city, destination, and travel date, this crew searches for flights, recommends hotels, builds a 5-day itinerary, and provides practical travel advice.

**Agents:** Flight Checker · Hotel Recommender · Tour Guide · Travel Advisor  
**LLM:** Groq `llama-3.3-70b-versatile`  
**Outputs:** `search_flights_task.md`, `hotels_result.md`, `tour_itinerary.md`, `travel_advice.md`

```bash
cd my_crew
python -c "from my_crew.main import run; run()"
```

---

### 2. Coding Teacher Assistant — `teacher_crew/`

Given a subject and student age group, this crew generates a full lesson plan, a quiz, and actionable teaching suggestions — ready for a school coding class.

**Agents:** Lesson Planner · Quiz Designer · Teaching Advisor  
**LLM:** OpenAI (default)  
**Outputs:** `lesson_plan.md`, `quiz.md`, `advisor_report.md`

```bash
cd teacher_crew
python -c "from teacher_crew.main import run; run()"
```

---

## Setup

**Requirements:** Python 3.10–3.13

Each crew is a standalone package. From inside the crew's folder:

```bash
pip install -e .
```

Copy `.env` and fill in your API keys:

```env
# my_crew
GROQ_API_KEY=your_groq_key

# teacher_crew
OPENAI_API_KEY=your_openai_key
```

---

## Tech Stack

- [CrewAI](https://www.crewai.com/) `1.14.3`
- Python `>=3.10`
- Groq (`my_crew`) · OpenAI (`teacher_crew`)
