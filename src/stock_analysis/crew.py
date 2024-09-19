
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool
import agentops
import os


agentops.init(os.environ.get("AGENTOPS_API_KEY"))


main_llm = ChatOpenAI(model="gpt-4o", temperature=0.1, verbose=True)


search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
website_search_tool = WebsiteSearchTool()


@CrewBase
class StockAnalysisCrew():
	"""StockAnalysis crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True,
			llm=main_llm
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True,
			llm=main_llm
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the StockAnalysis crew"""
		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
		)