import os
from openai import OpenAI
from itertools import product
from tabulate import tabulate
from dotenv import load_dotenv
from textwrap import wrap
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key = api_key)

temperatures = [0.0, 0.7, 1.2]
max_tokens_list = [50, 150, 300]
presence_penalties = [0.0, 1.5]
frequency_penalties = [0.0, 1.5]

def interactive_prompt_playground(model="gpt-3.5-turbo", system_prompt=None, user_prompt=None):
    result = []
    combo = product(temperatures, max_tokens_list, presence_penalties, frequency_penalties)
    # print(f"{combo = }")
    for temp, max_tok, pres_pen, freq_pen in combo:
        # print(f"Testing with temperature={temp}, max_tokens={max_tok}, presence_penalty={pres_pen}, frequency_penalty={freq_pen}")
        if system_prompt is None:
            system_prompt = "You are a helpful assistant that provides information and answers questions."
        
        try:
            response = client.chat.completions.create(
                model= model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=max_tok,
                temperature=temp,
                presence_penalty=pres_pen,
                frequency_penalty=freq_pen
            )
            
            # print("Response from OpenAI:")
            # print("--------------------------------------------------")
            # print(response.choices[0].message.content)
            # print("--------------------------------------------------")
            # print("Total tokens used:", response.usage.total_tokens)
            result.append([temp, max_tok, pres_pen, freq_pen, response.choices[0].message.content])
            # return result
        except Exception as e:
            print(f"An error occurred: {e}")
            result.append([temp, max_tok, pres_pen, freq_pen, str(e)])
    return result

def reflection(model="gpt-3.5-turbo"):
    print("--------------------------------------------------")
    reflection_prompt = """
        You've just run a series of prompt tests on a language model by varying temperature, max_tokens, presence_penalty, and frequency_penalty.
        Please write a two-paragraph reflection on:
        1. What changed in the outputs and why those changes occurred.
        2. What insights can be drawn from this about prompt engineering and parameter tuning.
        Mention how different parameter combinations affected tone, detail, repetition, and creativity.
        """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a prompt engineering expert."},
                {"role": "user", "content": reflection_prompt}
            ],
            max_tokens=400,
            temperature=0.7
        )
        print("Reflection on the experiment:")
        print("--------------------------------------------------")
        print(response.choices[0].message.content)
        print("--------------------------------------------------")
    except Exception as e:
        print(f"An error occurred while generating reflection: {e}")
        print("--------------------------------------------------")
        print("Reflection could not be generated due to an error.")
        print("--------------------------------------------------")
    
    
def custom_prompt_playground(model="gpt-3.5-turbo", system_prompt=None, user_prompt=None, temperature=0.7, max_tokens=150, presence_penalty=0.0, frequency_penalty=0.0):
    if system_prompt is None:
        system_prompt = "You are a helpful assistant that provides information and answers questions."
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty
        )
        
        # print("Response from OpenAI:")
        # print("--------------------------------------------------")
        # print(response.choices[0].message.content)
        # print("--------------------------------------------------")
        # print("Total tokens used:", response.usage.total_tokens)
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Parameter playground for OpenAI API")
    print("--------------------------------------------------")
    system_prompt = input("Enter system prompt (e.g., 'You are a product copywriter.'): ").strip()
    user_prompt = input("Enter user prompt (e.g., 'Describe the iPhone'): ").strip()
    if not user_prompt:
        user_prompt = "Please enter your question or request."
    print("--------------------------------------------------")
    print("\n\n")
    print("--------------------------------------------------")
    print("Choose model \n(1) gpt-3.5-turbo, (2) gpt-4): ")
    model_choice = input("Enter your choice (1 or 2): ").strip()
    if model_choice == '1':
        model = "gpt-3.5-turbo"
    elif model_choice == '2':
        model = "gpt-4"
    else:
        print("Invalid choice. Defaulting to gpt-3.5-turbo.")
        model = "gpt-3.5-turbo"
    print("--------------------------------------------------")
    print("Would you like to test all parameter combinations or specify custom values?")
    print("(1) All combinations, (2) Custom values")
    all_combinations = input("Enter your choice (1/2): ").strip()
    result = []
    temperature = None
    max_tokens = None
    presence_penalty = None
    frequency_penalty = None
    if all_combinations == '1':
        print("Using all combinations of parameters.")
        result = interactive_prompt_playground(model=model, system_prompt=system_prompt, user_prompt=user_prompt)
    elif all_combinations == '2':
        print("--------------------------------------------------")
        temp = input("Choose temperature (1/2/3) \n(1) 0.0, (2) 0.7, (3) 1.2: ").strip()
        if temp == '1':
            temperature = 0.0
        elif temp == '2':
            temperature = 0.7
        elif temp == '3':
            temperature = 1.2
        else:
            print("Invalid choice. Defaulting to 0.7.")
            temperature = 0.7
        print("--------------------------------------------------")
        max_token = input("Choose max_token (1/2/3) \n(1) 50, (2) 150, (3) 300: ").strip()
        if max_token == '1':
            max_tokens = 50
        elif max_token == '2':
            max_tokens = 150
        elif max_token == '3':
            max_tokens = 300
        else:
            print("Invalid choice. Defaulting to 150.")
            max_tokens = 150
        print("--------------------------------------------------")
        pres_penalty = input("Choose presence_penalty (1/2) \n(1) 0.0, (2) 1.5: ").strip()
        if pres_penalty == '1':
            presence_penalty = 0.0
        elif pres_penalty == '2':
            presence_penalty = 1.5
        else:
            print("Invalid choice. Defaulting to 0.0.")
            presence_penalty = 0.0
        print("--------------------------------------------------")
        freq_penalty = input("Choose frequency_penalty (1/2) \n(1) 0.0, (2) 1.5: ").strip()
        if freq_penalty == '1':
            frequency_penalty = 0.0
        elif freq_penalty == '2':
            frequency_penalty = 1.5
        else:
            print("Invalid choice. Defaulting to 0.0.")
            frequency_penalty = 0.0
        print("--------------------------------------------------")
        custom_prompt_playground(model=model, system_prompt=system_prompt, user_prompt=user_prompt,
                                    temperature=temperature, max_tokens=max_tokens,
                                    presence_penalty=presence_penalty, frequency_penalty=frequency_penalty)
        result = [[temperature, max_tokens, presence_penalty, frequency_penalty, custom_prompt_playground(
            model=model, system_prompt=system_prompt, user_prompt=user_prompt,
            temperature=temperature, max_tokens=max_tokens,
            presence_penalty=presence_penalty, frequency_penalty=frequency_penalty)]]
    else:
        print("Invalid choice. Defaulting to all combinations.")
        all_combinations = '1'
        result = interactive_prompt_playground(model=model, system_prompt=system_prompt, user_prompt=user_prompt)
   
    
    # print(f"Using model: {model}")
    print("--------------------------------------------------")
    headers = ["Temperature", "Max Tokens", "Presence Penalty", "Frequency Penalty", "Response"]
    # Adjust table formatting to wrap text within the given space

    wrapped_result = [
        [temp, max_tok, pres_pen, freq_pen, "\n".join(wrap(response, width=50))]
        for temp, max_tok, pres_pen, freq_pen, response in result
    ]
    print("\n" + tabulate(wrapped_result, headers=headers, tablefmt="grid"))
    
    reflection(model=model)


if __name__ == "__main__":
    main()
