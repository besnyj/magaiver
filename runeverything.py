import os
import threading

def ollama_run():
    os.system("ollama serve")

def fastapi_run():
    os.system("fastapi dev projeto/API/api.py")

def frontend_run():
    os.system("npm --prefix projeto/frontend run dev")

thread1 = threading.Thread(target=fastapi_run)
thread2 = threading.Thread(target=frontend_run)
thread3 = threading.Thread(target=ollama_run)

thread1.start()
thread2.start()
thread3.start()
