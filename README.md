# 🧠 OpenAI GPT Parameter Playground

This is an interactive playground for testing the effects of different OpenAI GPT parameters: `temperature`, `max_tokens`, `presence_penalty`, and `frequency_penalty`. It lets you observe how different configurations influence the output tone, creativity, repetition, and verbosity.

---

## 📋 Features

- **User-defined prompts:** Set your own `system` and `user` prompts to guide the model’s behavior and response.
- **Supports GPT-3.5 and GPT-4:** Choose between `gpt-3.5-turbo` and `gpt-4` at runtime.
- **Parameter Sweeping:** Automatically tests 36 combinations of:
  - `temperature`: `[0.0, 0.7, 1.2]`
  - `max_tokens`: `[50, 150, 300]`
  - `presence_penalty`: `[0.0, 1.5]`
  - `frequency_penalty`: `[0.0, 1.5]`
- **Formatted Output Table:** Results displayed in a readable tabular format using `tabulate`, with responses neatly word-wrapped.
- **Reflection Summary:** At the end, GPT itself generates a two-paragraph reflection on how the different parameters influenced the results.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/gpt-parameter-playground.git
cd gpt-parameter-playground
```

---

### 2. Install dependencies
```bash
pip install openai python-dotenv tabulate
```

---

### 3. Run python file
```bash
python interactive_prompt_playground.py
```
