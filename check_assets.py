import os


def check_assets():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r") as f:
                    lines = f.readlines()
                with open(os.path.join(root, file), "w") as f:
                    for line in lines:
                        f.write(line.replace(":/assets", "."))
