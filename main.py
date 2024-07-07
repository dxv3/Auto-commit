import os
import random
import subprocess
from datetime import datetime, timedelta

# Configuration
REPOS = [
    r'path/to/repo',
    r'path/to/repo',
    r'path/to/repo',
    r'path/to/repo',
    r'path/to/repo',
]
START_DATE = datetime(2022, 1, 1)  # Start date for random commits
END_DATE = datetime(2024, 7, 7)    # End date for random commits
COMMITS_PER_DAY = [0, 1, 1, 2, 2, 3, 5, 7, 9]     # Possible number of commits per day

def get_random_dates(start_date, end_date, num_dates):
    dates = []
    for _ in range(num_dates):
        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        dates.append(random_date)
    return dates

def make_commit(repo_path, commit_message, commit_date):
    os.chdir(repo_path)
    # Create or modify a file
    filename = 'update.txt'
    with open(filename, 'a') as f:
      
        f.write(f"{commit_message} on {commit_date}\n")
    
    # Git commands
    subprocess.run(['git', 'add', filename])
    subprocess.run(['git', 'commit', '--date', commit_date.strftime('%Y-%m-%d %H:%M:%S'), '-m', commit_message])
    subprocess.run(['git', 'push'])

def main():
    commit_dates = get_random_dates(START_DATE, END_DATE, sum(COMMITS_PER_DAY))  # Generate all commit dates at once

    for repo in REPOS:
        for commit_date in commit_dates:
            num_commits = random.choice(COMMITS_PER_DAY)
            for _ in range(num_commits):
                commit_message = f"Update"
                make_commit(repo, commit_message, commit_date)

if __name__ == '__main__':
    main()
