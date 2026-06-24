
from llm_client import generate_response


class SWOTAgent:

    def analyze(self, startup_idea):

        prompt = f"""
        You are an expert startup strategy consultant.

        Analyze the startup idea:

        {startup_idea}

        Provide a detailed SWOT Analysis:

        1. Strengths
        2. Weaknesses
        3. Opportunities
        4. Threats

        Format professionally with clear headings.
        """

        return generate_response(prompt)
