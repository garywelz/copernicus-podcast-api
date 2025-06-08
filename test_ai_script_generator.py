# test_ai_script_generator.py

from ai_script_generator import generate_script_and_description

if __name__ == "__main__":
    prompt = "Explain CRISPR gene editing to biology undergraduates"
    result = generate_script_and_description(prompt)

    print("\n--- SCRIPT ---\n")
    print(result["script"])

    print("\n--- DESCRIPTION ---\n")
    print(result["description"])
