import pandas as pd


def process_software_unix(file_path: str, user: str, os: str):

    with open(file_path, 'r') as f:
        lines = f.readlines()

    headers = lines[3].split()
    headers = headers[1:]

    software = lines[5:]
    software = [line.split() for line in software]
    # Collect the first 4 elements of each line
    software_temp = [line[1:4] for line in software]
    software_temp2 = [line[4:]  for line in software]
    # Join the elements of each list into a single string
    software_temp3 = [' '.join(line) for line in software_temp2]

    df = pd.DataFrame(software_temp, columns=headers[0:3])
    df['Description'] = software_temp3

    df.to_csv(f'inventory/data/processed/{os}-software-{user}.csv', index=False)
    

process_software_unix('inventory/data/raw/ubuntu-installed-software.txt', 'mona')