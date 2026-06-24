
from llm_client import generate_response


class BusinessAgent:

    def analyze(self, startup_idea):

        prompt = f"""
        You are an expert startup business strategist.

        Analyze the startup idea:

        {startup_idea}

        Provide:

        1. Business Model
        2. Revenue Streams
        3. Pricing Strategy
        4. Customer Acquisition Strategy
        5. Partnerships
        6. Scalability Potential
        7. Financial Outlook

        Format professionally.
        """

        return generate_response(prompt)
