import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(".env")

# Ensure correct API key variable name and handle potential errors
groq_api_key = os.getenv("GROQ_API_KEY")  # Corrected variable name
if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable is missing.")
try:
    client = Groq(api_key=groq_api_key)
except Exception as e:
    print("Error creating Groq client:", str(e))
    exit(1)  # Indicate error termination

def baca_file(nama_file):
    try:
        if os.path.exists(nama_file):
            with open(nama_file, 'r') as file:
                data = file.read()
                #print("Isi file:")
                #print(data)
                return data
        else:
            print("File tidak ditemukan")
    except Exception as e:
        print("Terjadi kesalahan:", str(e))

nama_file = input("Masukkan nama file: ")
data=baca_file(nama_file)
#print(data)

def print_llm_response(prompt, data):
    """Prints the LLM model's response to a given prompt.

    Args:
        prompt (str): The prompt to query the LLM model.

    Raises:
        ValueError: If the prompt is not a string.
    """

    if not isinstance(prompt, str):
        raise ValueError("Input must be a string enclosed in quotes.")

    try:
        completion = client.chat.completions.create(
            model="llama3-groq-70b-8192-tool-use-preview",
            messages=[
                {
                    "role": "system",
                    "content": f"answer following queries based on file you read: {data}"
                },
                {"role": "user", 
                 "content": prompt},
            ],
            temperature=1.0,
        )

        response = completion.choices[0].message.content
        print("\n" * 1)
        print(response)
        print("\n" * 1)
        print("\n")
    except Exception as e:  # Catch broader exceptions for better error handling
        print("Error:", str(e))
prompt = input("Tulis Kueri Anda: ")
