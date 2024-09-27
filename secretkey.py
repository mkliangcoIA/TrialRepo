import os

# Define the number of commits and the filename
num_commits = 5
file_name = "example_secrets.py"

# Create example_secrets.py with an initial message
with open(file_name, "w") as f:
    f.write("# This file contains secrets for testing GitHub's secret scanner.\n")

# Simulate multiple commits
for i in range(num_commits):
    # Open the file in append mode to add fake secrets each time
    with open(file_name, "a") as f:
        f.write(f"\n# Fake Secret Key {i}\n")
        f.write(f"SECRET_KEY_{i} = 'sk_live_{i}_fK1wQwGnJdQ1234567890abcdef'\n") 
        f.write(f"API_KEY_{i} = 'ak_live_{i}_ABCD1234EFGH5678IJKL9012MNOP3456'\n")  
        f.write(f"DB_PASSWORD_{i} = 'P@ssw0rd{100 + i}'\n") 
        f.write(f"CREDIT_CARD_{i} = '4111 1111 1111 {4000 + i}'\n")  

    # Commit the changes
    os.system(f"git add {file_name}")
    os.system(f"git commit -m 'Add secrets in commit {i + 1}'")

# Push to the remote repository
os.system("git push origin main")
