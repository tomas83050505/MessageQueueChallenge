import subprocess

def install_dependencies():
    """Installs dependencies from requirements.txt"""
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

def run_services():
    """Starts Service A and Service B"""
    service_a = subprocess.Popen(["uvicorn", "service_a.main:app", "--host", "127.0.0.1", "--port", "8000"])
    service_b = subprocess.Popen(["uvicorn", "service_b.main:app", "--host", "127.0.0.1", "--port", "8001"])
    return service_a, service_b

if __name__ == "__main__":
    install_dependencies()
    service_a, service_b = run_services()
    try:
        print("Services are running. Press Ctrl+C to stop.")
        service_a.wait()
        service_b.wait()
    except KeyboardInterrupt:
        print("Stopping services...")
        service_a.terminate()
        service_b.terminate()
