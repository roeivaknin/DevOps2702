# API Testing
# 1

import requests
import random
from selenium import webdriver


def num_of_repos():
    try:
        response = requests.get("https://api.github.com/users/avielb/repos")
    except:
        print("Could not reach the website")
    repo = response.json()
    expected = 5
    actual = len(repo)

    assert expected <= actual


# num_of_repos()

# 2

def generate_names_and_verify_ages():
    names = ['Roei', 'Eran', 'Bob', 'Matan', 'Guy', 'Shalom', 'Joy', 'Sara']
    for i in range(3):
        name = random.choice(names)
        verify_age(name)


def verify_age(name):
    try:
        response = requests.get(f"https://api.agify.io/?name={name}")
    except:
        print("Could not reach the website")
    actual = response.json()["age"]
    expected = range(0, 120)
    assert actual in expected


# generate_names_and_verify_ages()

# 3

def validate_if_il_has_at_least_5_uni():
    expected = 5
    actual = num_of_universities()
    assert actual >= expected


def num_of_universities():
    try:
        response = requests.get("http://universities.hipolabs.com/search?country=Israel")
    except:
        print("Could not reach the website")
    count = 0
    for element in response.json():
        if "University" in element["name"]:
            count += 1
    return count

# validate_if_il_has_at_least_5_uni()

# UI Testing
# 4 + 5
def validate_title_of_page(url, expected_title):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
    except:
        print("Could not reach the website")

    actual = driver.title
    assert expected_title == actual

# validate_title_of_page("https://www.ycombinator.com/", "Y Combinator")
# validate_title_of_page("https://hub.docker.com/", "Docker Hub Container Image Library | App Containerization")

