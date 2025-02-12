from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class PolicyCrew():
	"""PolicyCrew crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def risk_assessment_agent(self) -> Agent:
		return Agent(
		config=self.agents_config['risk_assessment_agent'],
		verbose=True
		)
		
	@agent
	def compliance_agent(self) -> Agent:
		return Agent(
		config=self.agents_config['compliance_agent'],
		verbose=True
		)

	@agent
	def efficiency_agent(self) -> Agent:
		return Agent(
		config=self.agents_config['efficiency_agent'],
		verbose=True
		)
		
	@agent
	def human_impact_agent(self) -> Agent:
		return Agent(
		config=self.agents_config['human_impact_agent'],
		verbose=True
		)
		
	@agent
	def implementation_agent(self) -> Agent:
		return Agent(
		config=self.agents_config['implementation_agent'],
		verbose=True
		)

	@agent
	def documentation_agent(self) -> Agent:
		return Agent(
		config=self.agents_config['documentation_agent'],
		verbose=True
		)

	@agent
	def training_agent(self) -> Agent:
		return Agent(
		config=self.agents_config['training_agent'],
		verbose=True
		)

	@agent
	def integration_agent(self) -> Agent:
		return Agent(
		config=self.agents_config['integration_agent'],
		verbose=True
		)

	@task
	def risk_assessment_task(self) -> Task:
		return Task(
		config=self.tasks_config['risk_assessment_task']
		)

	@task
	def compliance_task(self) -> Task:
		return Task(
		config=self.tasks_config['compliance_task']
		)

	@task
	def efficiency_task(self) -> Task:
		return Task(
		config=self.tasks_config['efficiency_task']
		)

	@task
	def human_impact_task(self) -> Task:
		return Task(
		config=self.tasks_config['human_impact_task']
		)

	@task
	def implementation_task(self) -> Task:
		return Task(
		config=self.tasks_config['implementation_task']
		)

	@task
	def documentation_task(self) -> Task:
		return Task(
		config=self.tasks_config['documentation_task'],
		output_file='output/remote_work_policy.md'
		)

	@task
	def training_task(self) -> Task:
		return Task(
		config=self.tasks_config['training_task'],
		output_file='output/training_program.md'
		)

	@task
	def integration_task(self) -> Task:
		return Task(
		config=self.tasks_config['integration_task']
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the LatestAiDevelopment crew"""
		return Crew(
		agents=self.agents, # Automatically created by the @agent decorator
		tasks=self.tasks, # Automatically created by the @task decorator
		process=Process.sequential,
		verbose=True,
		)
