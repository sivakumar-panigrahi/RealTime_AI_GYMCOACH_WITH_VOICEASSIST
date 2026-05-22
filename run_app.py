import subprocess
import webbrowser
import time
import os
import sys

def main():
    print("Starting AI Real-time GYM Coach...", flush=True)
    
    # Get the absolute path to the Streamlit app
    app_path = os.path.abspath("main.py")
    
    # Start the Streamlit app in the background
    streamlit_process = subprocess.Popen(
        ["uv", "run", "streamlit", "run", "main.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    print("Waiting for Streamlit server to start on port 8501...", flush=True)
    # Wait a few seconds for the Streamlit server to be up and running
    time.sleep(4)
    
    # Open the Landing Page in the default web browser
    landing_page_path = os.path.abspath(os.path.join("LandingPage", "index.html"))
    landing_url = f"file:///{landing_page_path.replace(os.sep, '/')}"
    
    print(f"Opening Landing Page: {landing_url}", flush=True)
    webbrowser.open(landing_url)
    
    print("Streamlit app is running in the background. Press Ctrl+C to stop.")
    try:
        streamlit_process.wait()
    except KeyboardInterrupt:
        print("\nStopping the application...")
        streamlit_process.terminate()
        streamlit_process.wait()
        print("Application stopped.")

if __name__ == "__main__":
    main()
