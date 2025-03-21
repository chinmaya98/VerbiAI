﻿# VerbiAI

This is a simple Streamlit application that creates a basic chatbot interface, similar to ChatGPT, using the OpenAI API.

## Features

* **Chat Interface:** Allows users to interact with an AI assistant through a clean and intuitive chat interface.
* **OpenAI Integration:** Utilizes the OpenAI API to generate responses.
* **Persistent Chat History:** Maintains a chat history within the session, providing context for the AI.
* **Clear Input Field:** Clears the input field after each submission for a seamless user experience.
* **Visual Enhancements:** Includes an icon and header for a more engaging interface.

## Prerequisites

* Python 3.8+
* Streamlit (`streamlit`)
* streamlit-chat (`streamlit-chat`)
* python-dotenv (`python-dotenv`)
* LangChain (`langchain`)
* OpenAI API Key

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS and Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install streamlit streamlit-chat python-dotenv langchain openai
    ```

4.  **Set up your OpenAI API key:**

    * Create a `.env` file in the root directory of your project.
    * Add your OpenAI API key to the `.env` file:

        ```
        OPENAI_API_KEY=your_openai_api_key
        ```

    * **Important:** Do not commit your `.env` file to version control.

## Usage

1.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    (Replace `app.py` with the name of your Python file if it's different.)

2.  **Open the application in your browser:**

    Streamlit will provide a URL (usually `http://localhost:8501`) that you can open in your web browser.

3.  **Start chatting:**

    * Enter your message in the text input field in the sidebar.
    * Press "Enter" or click the "Send" button.
    * The AI's response will appear in the chat history.

## Code Explanation

* **`init()`:** Initializes the application by loading the OpenAI API key from the `.env` file and setting up the Streamlit page configuration.
* **`main()`:**
    * Creates a `ChatOpenAI` instance.
    * Initializes the chat history in `st.session_state`.
    * Displays a header with an image.
    * Creates a sidebar with a text input field.
    * Handles user input, sends it to the OpenAI API, and updates the chat history.
    * Displays the chat history using `streamlit_chat.message`.
* **Dynamic Key:** The application uses a dynamic key for the text input to force streamlit to create a new text input widget, and therefore clear the previous text.

## Future Improvements

* **Error Handling:** Implement more robust error handling for API errors and invalid input.
* **Context Management:** Implement strategies to manage long conversations and prevent exceeding the OpenAI API's context window limit.
* **UI Enhancements:** Improve the user interface with features like message timestamps, loading indicators, and better message formatting.
* **Conversation Saving/Loading:** Add functionality to save and load conversation history.
* **More advanced System Messages:** Allow the user to change the system message.

## Contributing

Feel free to contribute to this project by submitting pull requests or opening issues.

