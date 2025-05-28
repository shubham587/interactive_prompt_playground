# OpenAI Prompt Playground

This is an interactive command-line playground for testing and comparing the effects of different OpenAI GPT model parameters, such as `temperature`, `max_tokens`, `presence_penalty`, and `frequency_penalty`. It supports both GPT-3.5 and GPT-4 models and allows users to observe how these settings influence the style, tone, and content of model responses.

---

## 🚀 Features

### ✅ Parameter Control
You can experiment with the following parameters:
- **Temperature**: Controls the randomness of the output (`0.0`, `0.7`, `1.2`)
- **Max Tokens**: Limits the response length (`50`, `150`, `300`)
- **Presence Penalty**: Penalizes new topics (`0.0`, `1.5`)
- **Frequency Penalty**: Penalizes repetitive phrases (`0.0`, `1.5`)

### ✅ Model Selection
Choose between:
- `gpt-3.5-turbo`
- `gpt-4`

### ✅ Modes of Operation
- **All Combinations**: Automatically runs all combinations of the parameter values to compare outputs.
- **Custom Configuration**: Manually set the parameters and view a single result.

### ✅ Reflection Mode
Generates a short reflection based on the outputs observed. Helps in understanding how prompt engineering and parameter tuning affect responses.

---

## 🛠️ Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/shubham587/interactive_prompt_playground.git
   ```
2. **Install Dependencies**

    You’ll need:
    
    - Python 3.7+
    - `openai` (version ≥ 1.0.0)
    - `python-dotenv`
    
    Install with pip:
    
    ```bash
    pip install openai python-dotenv tabulate
    ```
    
    Run py file with python:
    ```bash
    python interactive_prompt_playground.py
    ```
