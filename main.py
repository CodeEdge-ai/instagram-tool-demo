import os
import sys
from prompts import COMPETITOR_PROMPT
from utils import save_json, save_markdown
from openai import OpenAI

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <niche>")
        sys.exit(1)
    
    niche = sys.argv[1]
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("Error: Please set your OPENAI_API_KEY environment variable.")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    print(f"🔍 Running competitor analysis for niche: {niche}...")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert Instagram growth strategist."},
                {"role": "user", "content": COMPETITOR_PROMPT.format(niche=niche)}
            ]
        )

        output_text = response.choices[0].message["content"]

        save_json({"niche": niche, "competitor_analysis": output_text}, "output.json")
        save_markdown(f"# Competitor Analysis for {niche}\n\n{output_text}", "output.md")

        print("✅ Analysis complete! Files saved as output.json and output.md.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
