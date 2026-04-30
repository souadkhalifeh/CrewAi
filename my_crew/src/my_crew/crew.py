from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

@CrewBase
class MyCrew():
    """MyCrew crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def math_teacher(self) -> Agent:
        return Agent(
            config=self.agents_config['math_teacher'], 
            verbose=True, 
            allow_delegation=False,
        )

    @agent
    def python_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['python_developer'], 
            verbose=True, 
            allow_code_execution=True, 
        )
        
    @task
    def math_task(self) -> Task:
        return Task(
            config=self.tasks_config['math_task'],
            output_file= 'math_task.md'
        )

    @task
    def python_task(self) -> Task:
        return Task(
            config=self.tasks_config['python_task'], # type: ignore[index]
            output_file='python_code.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MyCrew crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
