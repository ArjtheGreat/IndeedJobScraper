import csv
from jobspy import scrape_jobs

def call_job_scraper():
    """
    Scrapes Jobs using scraper
    """
    jobs = scrape_jobs(
        site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor", "google", "bayt", "naukri"],
        search_term="construction",
        google_search_term="construction jobs in the US",
        location="United States of America",
        results_wanted=100,
        hours_old=168,
        country_indeed='USA',
        
        # linkedin_fetch_description=True # gets more info such as description, direct job url (slower)
        # proxies=["208.195.175.46:65095", "208.195.175.45:65095", "localhost"],
    )
    print(f"Found {len(jobs)} jobs")
    print(jobs.shape)
    jobs.to_csv("jobs.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False) # to_excel


if __name__ == "__main__":
    call_job_scraper()
