import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def refactor_code(code):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Refactor this code:\n{code}",
        max_tokens=200,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    # Test with some sample code
    sample_code = """
    def add(a, b):
        return a + b
    """
    print("Original Code:")
    print(sample_code)
    print("\nRefactored Code:")
    print(refactor_code(sample_code))
