# Magaiver - AI-Powered Portfolio Advisor

Magaiver is a full-stack application designed to provide personalized investment portfolio recommendations. It uses a Python/FastAPI backend to process an investor's financial data from an Excel file and leverages the Gemma Large Language Model (LLM) via Ollama to generate a tailored portfolio allocation. The frontend is built with React and TypeScript, providing a user-friendly interface for file uploads and displaying results.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Backend (Python/FastAPI)](#backend-pythonfastapi)
    - [Core Logic](#core-logic)
    - [API Endpoint](#api-endpoint)
    - [Setup & Running](#setup--running)
- [Frontend (React/TypeScript)](#frontend-reacttypescript)
    - [Core Functionality](#core-functionality)
    - [Setup & Running](#setup--running-1)
- [End-to-End Workflow](#end-to-end-workflow)
- [Recommendations for Improvement](#recommendations-for-improvement)

## Project Overview

The application streamlines the process of creating an investment portfolio.

1.  **Input**: The user uploads an Excel file (`.xlsx`) containing their financial overview (net worth, expenses, risk profile).
2.  **Processing**: The backend parses the Excel file, extracts key investor data, and constructs a detailed prompt for the Gemma LLM. This prompt includes economic context, risk profile definitions, and a list of available investment products.
3.  **Generation**: The LLM processes the prompt and generates a personalized investment portfolio, allocating the investor's capital across different asset classes and specific products.
4.  **Output**: The frontend displays the generated portfolio recommendation to the user.

## Project Structure

The project is organized into two main parts: the backend and the frontend.

```
projeto/
├── API/              # FastAPI application entrypoint and models
├── backend/          # Core application logic, LLM interaction, and data files
│   ├── data/
│   │   ├── opportunities/
│   │   ├── profiles/
│   │   └── rules/
│   ├── config.py
│   ├── investidor.py
│   └── start.py
└── frontend/         # React/TypeScript client application
    ├── public/
    └── src/
        ├── components/
        ├── pages/
        ├── App.tsx
        └── main.tsx
```

## Backend (Python/FastAPI)

The backend is responsible for the core business logic of the application.

### Core Logic

Located in `projeto/backend/start.py`, the core logic is as follows:

1.  **Investor Parsing (`set_investors`)**: Reads the uploaded Excel file using `pandas` and extracts the investor's risk profile, net worth, and total expenses from specific, hardcoded cells.
2.  **Prompt Construction (`build_message`)**: Dynamically creates a comprehensive prompt for the LLM. It merges static context files (from `projeto/backend/data/`) with the parsed investor data.
3.  **LLM Interaction (`use_ollama`)**: Sends the constructed prompt to a running Ollama instance to communicate with the `gemma3:27b` model.
4.  **Response Handling**: Returns the raw text response from the LLM back to the API endpoint.

### API Endpoint

**`POST /upload_overview`**

This is the single endpoint that drives the application.

*   **Request**: `multipart/form-data`
    *   **`file`**: The user's financial overview as an `.xlsx` file.
*   **Success Response (200 OK)**:
    ```json
    {
      "message": "Perfil do Investidor: ...\n\nReserva de Emergência: ...\n\nCarteira de Investimentos: ..."
    }
    ```
*   **Error Responses**:
    *   **400 Bad Request**: If the uploaded file is not an `.xlsx` file.
    *   **500 Internal Server Error**: If any part of the backend processing fails.

### Setup & Running

**Prerequisites**:
*   Python 3.9+
*   Ollama installed and running as a separate service.
*   The Gemma model pulled: `ollama pull gemma3:27b`

**Installation**:

1.  Navigate to the `projeto/backend` directory.
2.  Create a `requirements.txt` file (a recommended version is provided in the improvements section).
3.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

**Running the Server**:

From the `ProjetoFORUM` root directory, run:
```bash
uvicorn projeto.API.api:api --reload --port 8000
```

## Frontend (React/TypeScript)

The frontend provides the user interface for interacting with the application. It is built with Vite, React, TypeScript, and uses Material-UI for components and Tailwind CSS for styling.

### Core Functionality

The main user interface is defined in `projeto/frontend/src/pages/portfolio.tsx`.

1.  **File Upload**: A styled button allows the user to select an `.xlsx` or `.xls` file from their system.
2.  **State Management**: Uses React's `useState` hook to manage the selected file, upload progress, API responses, and any potential errors.
3.  **API Communication**: On submission, it uses the `fetch` API to send the selected file to the backend endpoint (`http://localhost:8000/upload_overview`).
4.  **UI Feedback**:
    *   Displays the name of the selected file.
    *   Shows a circular progress indicator while the file is uploading and being processed.
    *   Conditionally renders either the portfolio result from the API or a detailed error message.

### Setup & Running

**Prerequisites**:
*   Node.js (LTS version recommended)
*   npm or yarn

**Installation**:

1.  Navigate to the `projeto/frontend` directory:
    ```bash
    cd projeto/frontend
    ```
2.  Install dependencies:
    ```bash
    npm install
    ```

**Running the Development Server**:

```bash
npm run dev
```
The application will be available at `http://localhost:5173` (or another port if 5173 is in use).

## End-to-End Workflow

1.  User visits the web application.
2.  User clicks "Selecione um Overview" and chooses their `.xlsx` file.
3.  The file name appears on the screen. User clicks "Enviar".
4.  A loading spinner appears. The frontend sends the file to the backend `POST /upload_overview` endpoint.
5.  The backend's `api.py` receives the request, validates the file extension, and passes the file content to `start.py`.
6.  `start.py` parses the investor data, builds a prompt with rules and opportunities, and sends it to the Ollama service.
7.  The Gemma model generates the portfolio text.
8.  The backend returns the generated text to the frontend in a JSON response.
9.  The frontend displays the text response on the screen. If any step fails, an error message is shown instead.

## Recommendations for Improvement

This project has a solid foundation, but several areas could be improved for better performance, robustness, and maintainability.

*   **Backend**:
    *   **Ollama Process Management**: Ollama should be run as a persistent, separate service, not started and stopped with every API call.
    *   **Error Handling**: Improve `try/except` blocks to return meaningful HTTP exceptions to the client instead of printing to the console.
    *   **Configuration**: Avoid hardcoding values like Excel cell positions, file paths, and model names. Use a configuration file or environment variables.
    *   **Streaming Response**: The backend sets `stream=True` for the Ollama call but doesn't handle the response as a stream. This should be fixed to correctly process the LLM's output as it's generated.
*   **Frontend**:
    *   **Dependencies**: The `react-router-dom` package is used but missing from `package.json`.
    *   **Response Rendering**: The portfolio text is rendered as a plain string. Using a Markdown renderer would preserve the formatting from the LLM.
    *   **Environment Variables**: The backend API URL is hardcoded. It should be placed in a `.env` file.
    *   **UI Consistency**: The project has two different navigation/layout approaches (`header.tsx` and `test.tsx`). A single, consistent approach should be chosen.