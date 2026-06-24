
from llm_client import generate_response


class ScoringAgent:

    def analyze(self, startup_idea):

        prompt = f"""
        You are a startup investment analyst.

        Analyze this startup idea:

        {startup_idea}

        Provide:

        1. Startup Score (0-100)

        2. Founder Readiness Score (0-100)

        3. Investment Recommendation
           - INVEST
           - MAYBE
           - REJECT

        4. Top 3 Strengths

        5. Top 3 Weaknesses

        6. Reasoning

        Format professionally with clear headings.
        """

        return generate_response(prompt)
