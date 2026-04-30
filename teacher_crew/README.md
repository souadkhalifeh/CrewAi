# Teacher Crew — Coding Teacher Assistant

A multi-agent AI crew built with [crewAI](https://crewai.com) that helps coding teachers prepare lessons for school students. Given a subject and age group, the crew automatically generates a lesson plan, a quiz, and practical teaching suggestions.

## What It Does

The crew runs three agents in sequence:

| Agent                                                                                                                               | Output file         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| **Lesson Planner** — creates a structured lesson plan with objectives, materials, and step-by-step instructions                     | `lesson_plan.md`    |
| **Quiz Designer** — generates an age-appropriate quiz with mixed question types tied to the lesson                                  | `quiz.md`           |
| **Teaching Advisor** — provides actionable teaching tips: pacing, engagement strategies, common misconceptions, and differentiation | `advisor_report.md` |

## Setup

**Requirements:** Python 3.10–3.13

1. Activate your virtual environment:

   ```bash
   # Windows
   venv\Scripts\activate
   ```

2. Install the package:

   ```bash
   pip install -e .
   ```

3. Add your OpenAI API key to `.env`:
   ```
   OPENAI_API_KEY=your_key_here
   ```

## Running the Crew

```bash
python -c "from teacher_crew.main import run; run()"
```

Or with the crewAI CLI:

```bash
crewai run
```

## Customising the Inputs

Edit `src/teacher_crew/main.py` to change the subject and age group:

```python
inputs = {
    'subject': 'Python programming',   # e.g. 'HTML & CSS', 'Scratch', 'Algorithms'
    'age_group': 'Grade 6 students',   # e.g. 'high school students', 'beginners aged 10-12'
}
```

## Project Structure

```
teacher_crew/
├── src/teacher_crew/
│   ├── config/
│   │   ├── agents.yaml       # Agent roles, goals, and backstories
│   │   └── tasks.yaml        # Task descriptions and expected outputs
│   ├── crew.py               # Crew assembly and task wiring
│   └── main.py               # Entry point — set your inputs here
├── lesson_plan.md            # Generated after running (lesson plan)
├── quiz.md                   # Generated after running (quiz)
├── advisor_report.md         # Generated after running (teaching tips)
└── pyproject.toml
```

## Support

- [crewAI Documentation](https://docs.crewai.com)
- [crewAI GitHub](https://github.com/joaomdmoura/crewai)
