import pandas as pd


def process_inventory(path: str, filenames: str, extra_cases: str):
    
    # Must add a check for valid paths and filenames
    
    dfs = []

    for filename in filenames:
        temp_df = pd.read_csv(f'{path}/{filename}')
        # Create a column filled with an id based on the filename
        temp_df['id'] = filename.split('/')[-1].split('.')[0]
        dfs.append(temp_df)

    df = pd.concat(dfs, ignore_index=True)
    df.dropna(subset=['DisplayName'], inplace=True)
    df['InstallDate'] = pd.to_datetime(df['InstallDate'], format='%Y%m%d')

    # Reset index
    df = df.reset_index(drop=True)
    # Strip whitespace from column names
    df.columns = df.columns.str.strip()

    # Needs to check if its a dictionary with the right column names
    extra_software = pd.read_csv(f'{path}/{extra_cases}')
    df = df.append(extra_software, ignore_index=True)

    return df


def main():

    path = 'data/raw'
    filenames = ['central.csv', 'pink.csv']
    # Software used
    extra_software = 'extra.csv'

    df = process_inventory(path, filenames, extra_software)

    df.to_csv('data/processed/software-sme.csv', index=False)


main()
