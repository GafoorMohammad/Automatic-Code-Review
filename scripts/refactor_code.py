import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def refactor_code(code_snippet):
    response = openai.Completion.create(
        engine="code-davinci-002",
        prompt=f"Refactor this code:\n\n{code_snippet}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    code = """
    def inefficient_function():
        result = []
        for i in range(0, 1000):
            result.append(i**2)
        return result
    """
    print("Original Code:\n", code)
    suggestion = refactor_code(code)
    print("Refactored Code Suggestion:\n", suggestion)
