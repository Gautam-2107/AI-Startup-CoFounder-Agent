
from llm_client import generate_response


class MarketResearchAgent:

    def analyze(self, startup_idea):

        prompt = f"""
        You are an expert startup market research analyst.

        Analyze the startup idea below:

        {startup_idea}

        Provide:

        1. Market Size
        2. Target Customers
        3. Industry Trends
        4. Growth Opportunities
        5. Key Challenges

        Format the response professionally.
        """

        return generate_response(prompt)

