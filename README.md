# GenAI Code Reviewer

GenAI Code Reviewer is an AI-powered tool designed to help developers improve their Python code by offering bug detection, suggestions for better practices, and providing fixed code snippets in real-time. The application uses the Google Gemini AI model to analyze and review Python code.

## Features

- **Instant AI Code Review**: Automatically reviews Python code for bugs and improvements.
- **Interactive Chat History**: Keep track of past code reviews and suggestions.
- **Real-time Code Analysis**: Get feedback on code as you paste it into the text area.
- **Clean & Simple User Interface**: Designed for an intuitive user experience with attractive animations.

## Screenshots

![App Screenshot](https://raw.githubusercontent.com/your-username/your-repository-name/main/path-to-your-image/image1.png)




## Requirements

To run this application locally, you need the following dependencies:

- Python 3.7 or higher
- `streamlit`
- `google-generativeai`

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/Kadirayyappan/genai-code-reviewer.git
    cd genai-code-reviewer
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:
    ```bash
    streamlit run app.py
    ```

4. Open the app in your browser (usually at `http://localhost:8501`).

## Usage

1. **Paste Python Code**: Copy and paste the Python code you want to review into the text area on the main page.
2. **Review Code**: Click the **Review Code** button to get suggestions from the AI model. The suggestions will be displayed in a clean and readable format.
3. **View Review History**: You can also view past reviews by clicking the **Show Review History** button.
4. **Connect with Me**: Access my LinkedIn and GitHub profiles via the sidebar to learn more about my work and get in touch.

This project requires a valid API key for the Google Gemini AI model. You can configure your API key in the code:
```python
genai.configure(api_key="your-api-key")
```
## Contact

For more information, feel free to contact me through the following platforms:

- [LinkedIn](https://www.linkedin.com/in/kadir-ayyappan2005/)
- [GitHub](https://github.com/Kadirayyappan)

---

