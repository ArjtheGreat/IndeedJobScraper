import pandas as pd

US_STATES = {
    'AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA',
    'KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ',
    'NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT',
    'VA','WA','WV','WI','WY','DC'
}

def extract_state(location):
    """
    Extracts State from Location
    """
    if not isinstance(location, str):
        return None
    parts = [p.strip() for p in location.split(',')]
    if len(parts) >= 2:
        state_candidate = parts[1]
        if state_candidate in US_STATES:
            return state_candidate
    return None


def process_job_data():
    """
    Processes Job Data
    """
    jobs_df = pd.read_csv("app/data/jobs.csv")
    jobs_df["state"] = jobs_df["location"].apply(extract_state)

    job_counts_per_state = jobs_df["state"].value_counts().to_dict()

    return job_counts_per_state