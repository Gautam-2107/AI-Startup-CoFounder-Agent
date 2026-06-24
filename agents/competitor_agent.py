
from llm_client import generate_response


class CompetitorAgent:

    def analyze(self, startup_idea):

        prompt = f"""
        You are an expert startup competitor analysis consultant.

        Analyze the startup idea:

        {startup_idea}

        Provide:

        1. Potential Competitors
        2. Direct Competitors
        3. Indirect Competitors
        4. Competitor Strengths
        5. Competitor Weaknesses
        6. Market Gaps
        7. Competitive Advantage Opportunities

        Format the report professionally.
        """

        return generate_response(prompt)
