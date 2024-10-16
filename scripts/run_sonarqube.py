import subprocess

def run_sonarqube():
    try:
        result = subprocess.run(["sonar-scanner"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("SonarQube Output:")
        print(result.stdout)
    except Exception as e:
        print(f"Error running SonarQube: {e}")

if __name__ == "__main__":
    run_sonarqube()
