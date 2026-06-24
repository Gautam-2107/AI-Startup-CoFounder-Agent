
from llm_client import generate_response


class FinancialProjectionAgent:

    def analyze(self, startup_idea):

        prompt = f"""
        You are an expert startup financial analyst.

        Analyze the startup idea:

        {startup_idea}

        Provide:

        1. Estimated Startup Costs
        2. Revenue Model
        3. Monthly Revenue Projection
        4. Annual Revenue Projection
        5. Break-Even Analysis
        6. Funding Requirements
        7. Financial Risks
        8. Growth Potential

        Format professionally with clear headings.
        """

        return generate_response(prompt)

