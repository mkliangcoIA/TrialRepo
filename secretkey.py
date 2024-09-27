import os

# Define the number of commits and the filename
num_commits = 5
file_name = "example_file.txt"

# Create example_file.txt with an initial message
with open(file_name, "w") as f:
    f.write("This is an example file with a secret.\n")

# Simulate multiple commits
for i in range(num_commits):
    # Open the file in append mode to add fake secrets each time
    with open(file_name, "a") as f:
        f.write(f"secret_key_{i} = 'sk_test_{i}_fake_secret'\n")
        f.write(f"api_key_{i} = 'ak_test_{i}_fake_key'\n")
        f.write(f"password_{i} = 'password_{i}'\n")
        
    # Commit the changes
    os.system(f"git add {file_name}")
    os.system(f"git commit -m 'Add fake secrets in commit {i + 1}'")

# Push to the remote repository
os.system("git push origin main")
