
from llm_client import generate_response


class ExecutiveSummaryAgent:

    def analyze(self, startup_idea):

        prompt = f"""
        You are a startup consultant.

        Analyze this startup idea:

        {startup_idea}

        Create an executive summary including:

        1. Startup Overview
        2. Problem Being Solved
        3. Market Opportunity
        4. Key Strengths
        5. Key Risks
        6. Overall Investment Outlook

        Keep it concise and professional.
        """

        return generate_response(prompt)
