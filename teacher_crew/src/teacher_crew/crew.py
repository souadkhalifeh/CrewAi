from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

@CrewBase
class TeacherCrew():
    """TeacherCrew crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def lesson_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['lesson_planner'],
            verbose=True,
        )

    @agent
    def quiz_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['quiz_generator'],
            verbose=True,
        )

    @agent
    def advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['advisor'],
            verbose=True,
        )
    


    @task
    def lesson_planner_task(self) -> Task:
        return Task(
            config=self.tasks_config['lesson_plan_task'],
            output_file='lesson_plan.md'
        )

    @task
    def quiz_generator_task(self) -> Task:
        return Task(
            config=self.tasks_config['quiz_generator_task'],
            output_file='quiz.md'
        )

    @task
    def advisor_task(self) -> Task:
        return Task(
            config=self.tasks_config['advisor_task'],
            output_file='advisor_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TeacherCrew crew"""

        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )
