import json

path="starter/gen_ai_fundamentals_project_starter.ipynb"

with open(path) as f:
    nb=json.load(f)

for cell in nb["cells"]:
    text="".join(cell.get("source",[]))

    # Cell 19
    text=text.replace(
        "# matches = **********",
        "matches = re.findall(pattern, response)"
    )

    # Cell 21 spelling reward
    text=text.replace(
        "# Provide a reward ",
        "# Provide a reward "
    )

    # Cell 23 counting reward
    text=text.replace(
        "# Provide reward ",
        "# Provide reward "
    )

    # Cell 25 format reward
    text=text.replace(
        "# Check if the response matches",
        "if re.fullmatch(pattern, response, flags=re.DOTALL):\n            reward = 1.0"
    )

    # Cell 27 exact answer reward
    text=text.replace(
        "# **********  # Complete the list comprehension",
        "1.0 if str(r) == str(a) else 0.0"
    )

    # Cell 31 GRPO remaining params
    text=text.replace(
        "# learning_rate=**********,",
        "learning_rate=5e-6,"
    )
    text=text.replace(
        "# beta=**********,",
        "beta=0.04,"
    )
    text=text.replace(
        "# per_device_train_batch_size=**********,",
        "per_device_train_batch_size=1,"
    )

    # Cell 36
    text=text.replace(
        "# max_steps=**********,  # ~60min",
        "max_steps=50,"
    )

    # Cell 42
    text=text.replace(
        "# **********",
        """item = ds[0]
print("Original word:", item)"""
    )

    # Cell 45
    text=text.replace(
        "# **********",
        """question = "What is the capital of France?"
print(question)"""
    )

    cell["source"]=text.splitlines(True)

with open(path,"w") as f:
    json.dump(nb,f,indent=2)

print("Finished patching notebook")
