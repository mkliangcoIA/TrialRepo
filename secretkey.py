import os

# Define the number of commits and the filename
num_commits = 5
file_name = "example_file.txt"

# Create example_file.txt with fake secrets
with open(file_name, "w") as f:
    f.write("This is an example file with a secret.\n")

# Simulate multiple commits
for i in range(num_commits):
    # Append a fake secret each time
    f.write(f"secret_key_{i} = 'sk_test_{i}_4eC39HqLyjWDarjtT1zdp7dc'\n")
    f.write(f"api_key_{i} = 'ak_test_{i}_token=abc123xyz!@#'\n")
    f.write(f"password_{i} = 'P@ssw0rd123_{i}'\n")
    
    # Commit the changes
    os.system(f"git add {file_name}")
    os.system(f"git commit -m 'Add fake secrets in commit {i + 1}'")

# Push to the remote repository
os.system("git push origin main")
