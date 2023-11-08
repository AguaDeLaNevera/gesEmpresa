import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

data = pd.read_csv("salaries.csv")

def createSalaryByJobCSV(data, salary_in_usd, job_title):
    salaryByJob = data[[job_title, salary_in_usd]].groupby(job_title).mean().round().sort_values(salary_in_usd, ascending=False)
    salaryByJob.to_csv("average_salary_by_job.csv")

def createSalaryByExperienceCSV(data, salary_in_usd, experience_level, job_title):
    salaryByExperience = data[[experience_level, job_title, salary_in_usd]].groupby([experience_level, job_title]).mean().round().sort_values(salary_in_usd, ascending=False)
    salaryByExperience.to_csv("average_salary_by_experience.csv")

def createSalaryBySizeCSV(data, salary_in_usd, company_size):
    salaryBySize = data[[company_size, salary_in_usd]].groupby(company_size).mean().round().sort_values(salary_in_usd, ascending=False)
    salaryBySize.to_csv("average_salary_by_size.csv")

def createCountBySize(data, company_size):
    countBySize = data.groupby(company_size).size()
    countBySize.to_csv("count_company_size.csv")

def generateSalaryBoxplot(data, salary_in_usd, experience_level):
    data.boxplot(column=salary_in_usd, by=experience_level)
    plt.xlabel(salary_in_usd)
    plt.ylabel(experience_level)
    plt.title(f"{salary_in_usd} Distribution by {experience_level}")
    plt.show()

def generateBarChart(data, salary_in_usd, company_size):
    plt.bar(data[company_size], data[salary_in_usd])
    plt.xlabel("Size of the company")
    plt.ylabel("Salary in usd")
    plt.title("company size by salary")
    plt.show()

def createTop5PaidCountry(data, company_location, salary_in_usd):
    salaryByCountry = data[[salary_in_usd, company_location]].groupby(company_location).mean().round().sort_values(salary_in_usd, ascending = False)
    salaryByCountry = salaryByCountry.head(5)
    salaryByCountry.to_csv("top_5_highest_paid_countries.csv") 

def createTop10JobsCountry(data, company_location):
    companyLocationSize = data.groupby(company_location).size().sort_values(ascending=False)    
    companyLocationSize = companyLocationSize.head(10)
    companyLocationSize.to_csv("top_10_countries_most_jobs.csv")

def generate3DGraphic(data, salary_in_usd, experience_level, company_size, company_location):
    np.random.seed(1)
    salaryMin = data.groupby(salary_in_usd).min().round()
    salaryMax = data.groupby(salary_in_usd).max().round()
    N = 70

    fig = go.Figure(data=[go.Mesh3d(x=(70*np.random.randn(N)),
                    y=(55*np.random.randn(N)),
                    z=(40*np.random.randn(N)),
                    opacity=0.5,
                    color='rgba(244,22,100,0.6)'
                    )])

    fig.update_layout(
        scene = dict(
            xaxis = dict(nticks=4, range=[salaryMin,salaryMax],),
                        yaxis = dict(nticks=4, range=[-50,100],),
                        zaxis = dict(nticks=4, range=[-100,100],),),
        width=700,
        margin=dict(r=20, l=10, b=10, t=10))
    fig.show()
generate3DGraphic(data, "salary_in_usd", "experience_level", "company_size", "company_location")