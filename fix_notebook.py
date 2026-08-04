import json

path = "starter/gen_ai_fundamentals_project_starter.ipynb"

with open(path, "r") as f:
    nb = json.load(f)

replacements = {
    "lora_rank = **********": "lora_rank = 16",

    'SYSTEM_PROMPT = """**********"""': '''SYSTEM_PROMPT = """
You are a careful reasoning assistant.

Solve problems step by step.

For counting letters:
1. Write each letter in order.
2. Track the running count.
3. Give the final answer clearly.

Example:

Question:
How many g are in engage?

Reasoning:
1. e - 0
2. n - 0
3. g - 1
4. a - 1
5. g - 2
6. e - 2

Final answer: 2
"""''',

    "# matches = **********": "matches = re.findall(pattern, response)",

    "# **********  # Complete the list comprehension":
    "1.0 if str(r) == str(a) else 0.0",

    "# learning_rate=**********,":
    "learning_rate=5e-6,",

    "# beta=**********,":
    "beta=0.04,",

    "# per_device_train_batch_size=**********,":
    "per_device_train_batch_size=1,",

    "# max_steps=**********,  # ~60min":
    "max_steps=50,",
}

for cell in nb["cells"]:
    if "source" in cell:
        text = "".join(cell["source"])

        for old, new in replacements.items():
            text = text.replace(old, new)

        cell["source"] = text.splitlines(True)

with open(path, "w") as f:
    json.dump(nb, f, indent=2)

print("Notebook patched successfully!")
