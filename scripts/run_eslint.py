import subprocess

def run_eslint():
    try:
        result = subprocess.run(["npx", "eslint", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("ESLint Output:")
        print(result.stdout)
    except Exception as e:
        print(f"Error running ESLint: {e}")

if __name__ == "__main__":
    run_eslint()
