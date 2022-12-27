from cover_letter_editor import edit
from selenium import webdriver
from selenium.webdriver.common.by import By
from apply import apply
from time import sleep
from xcell_manager import contains, add_to_xcell


def find_job(driver, phone):
    # go to search page
    driver.get("https://www.linkedin.com/jobs/search")
    sleep(4)

    # filter to only see jobs that have easy apply enabled
    driver.get(driver.current_url + "&f_AL=true&f_E=1%2C2&f_I=4%2C96&sortBy=R")
    sleep(3)

    # find the jobs, get company name and job role. Maybe copy job description into my coverletter with transparent color
    elements = driver.find_elements(By.CLASS_NAME, "job-card-list__entity-lockup.artdeco-entity-lockup.artdeco-entity-lockup--size-4.ember-view")
    sleep(2)

    # get all job ids in the page
    job_ids = []
    for element in elements: 
        element.click()
        sleep(2)
        id = driver.current_url[51:61] # get the job id from url
        job_ids.append(id)
        sleep(1)
    print(job_ids)

    # go into individual job pages
    for id in job_ids:
        driver.get(f"https://www.linkedin.com/jobs/view/{id}")
        sleep(3)

        # retrieving information about the job
        company_name = driver.find_element(By.CLASS_NAME, "jobs-unified-top-card__company-name")
        location = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[1]/span[1]/span[2]")
        job_name = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/h1")
        print(company_name.text + '\n' + job_name.text + '\n' + location.text)

        
        # costumize cover letter
        edit(company_name.text, job_name.text)
        
        # check if already applied to such job using automated excell spreadsheet, if not add to excell
        if contains(id, job_name.text, company_name.text, location.text):
            continue
        else:
            # apply to job
            bool_ = apply(phone)
            
            # add to spreadsheet if successful
            if bool_:
                add_to_xcell(id, job_name.text, company_name.text, location.text)
        
        sleep(2)
        

if __name__ == '__main__':
    driver = webdriver.Firefox()
    find_job()
    driver.close()    
    