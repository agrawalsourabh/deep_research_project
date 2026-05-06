from asyncio.tasks import as_completed
from agents import Runner, trace, gen_trace_id
from httpx import ReadTimeout
from planner_agent import WebSearchItem, WebSearchPlan, planner_agent
from search_agent import search_agent
from writer_agent import ReportData, writer_agent
from email_agnet import email_agent
import asyncio

class ResearchManager:

    
    async def run(self, query: str):
        """Run the deep research project, yielding the status update and the final report"""

        trace_id = gen_trace_id()

        with trace("Research trace", trace_id=trace_id):

            print("Starting research...")
            search_plan = await self.plan_searches(query)

            yield "Searches planned, starting to search..."
            search_results = await self.perform_searches(search_plan)

            yield "Search completed, writing reports..."
            report = await self.write_report(query, search_results)

            yield "Report written, sending email..."
            await self.send_email(report)

            yield "Report sent, research complete"
            yield report.markdown_report


    async def plan_searches(self, query:str) -> WebSearchPlan:
        """ Plan the searches to perform query """
        print("Planning searches ...")

        result = await Runner.run(
            planner_agent,
            f"Query: {query}"
        )

        print(f"will perform {len(result.final_output.searches)} searches.")

        return result.final_output_as(WebSearchPlan)


    async def perform_searches(self, search_plan:WebSearchPlan) -> list[str]:
        """ Perform searches for the query"""

        print("Searching...")
        num_completed = 0

        tasks = [asyncio.create_task(self.search(item))  for item in search_plan.searches]

        results = []

        for task in asyncio.as_completed(tasks):
            result = await task

            if result is not None:
                results.append(result)

            num_completed += 1

            print(f"Searching... {num_completed} / {len(tasks)} completed.")

        print("finished searching")
        return results


    async def search(self, item:WebSearchItem) -> str | None :
        """ Perform the search for the query """

        input = f"Search item: {item.query} \n Reason for searching: {item.reason}"

        try:
            result = await Runner.run(
                search_agent,
                input
            )

            return str(result.final_output)

        except Exception:
            return None


    
    async def write_report(self, query: str, search_results: list[str]) -> ReportData:
        """ Write the report for the query """

        print("Thinking about report")
        input = f"Original query: {query} \n Summarised search result {search_results}"

        result = await Runner.run(
            writer_agent,
            input=input
        )

        print("finished writing report.")
        return result.final_output_as(ReportData)


    async def send_email(self, report: ReportData) -> None:
        print("Writing email")
        result = await Runner.run(
            email_agent,
            report.markdown_report
        )

        print("Email sent")
        return report





