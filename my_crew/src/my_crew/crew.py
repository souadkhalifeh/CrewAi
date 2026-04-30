import os
from dotenv import load_dotenv
from crewai import Agent, Crew, LLM, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from my_crew.tools.flight_tool import FlightSearchTool

load_dotenv()

def _llm() -> LLM:
    return LLM(
        model=os.environ["MODEL"],
        api_key=os.environ["GROQ_API_KEY"],
    )

@CrewBase
class MyCrew():
    """Travel Assistant Crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def flight_checker(self) -> Agent:
        return Agent(
            config=self.agents_config['flight_checker'],
            llm=_llm(),
            verbose=True,
            allow_delegation=False,
            tools=[FlightSearchTool()],
        )

    @agent
    def hotel_recommender(self) -> Agent:
        return Agent(
            config=self.agents_config['hotel_recommender'],
            llm=_llm(),
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def tour_guide(self) -> Agent:
        return Agent(
            config=self.agents_config['tour_guide'],
            llm=_llm(),
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def travel_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['travel_advisor'],
            llm=_llm(),
            verbose=True,
            allow_delegation=False,
        )

    @task
    def search_flights_task(self) -> Task:
        return Task(
            config=self.tasks_config['search_flights_task'],
            output_file='search_flights_task.md'
        )

    @task
    def recommend_hotels_task(self) -> Task:
        return Task(
            config=self.tasks_config['recommend_hotels_task'],
            output_file='hotels_result.md'
        )

    @task
    def plan_tour_task(self) -> Task:
        return Task(
            config=self.tasks_config['plan_tour_task'],
            output_file='tour_itinerary.md'
        )

    @task
    def travel_advice_task(self) -> Task:
        return Task(
            config=self.tasks_config['travel_advice_task'],
            output_file='travel_advice.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
