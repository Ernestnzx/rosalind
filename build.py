import os
import requests
from bs4 import BeautifulSoup

BASE_URL='http://rosalind.info/problems/list-view/?location='
sections=[
    ('Bioinformatics Stronghold','stronghold','bioinformatics-stronghold'),
    ('Algorithmic Heights','algorithmic','algorithmic-heights'),
    ('Python Village','village','python-village')
]

def get_all_problems(subdomain):
    url = f'{BASE_URL}{subdomain}'
    print(f'Parsing problem list in {subdomain}')
    rows = (
        BeautifulSoup(requests.get(url).text, 'html.parser')
            .find("table", class_="problem-list table table-striped table-bordered table-condensed")
            .find("tbody")
            .find_all("tr")
    )
    data = {}
    for row in rows:
        cols = row.find_all("td")
        if not cols: continue
        problem_id = cols[0].text.strip()
        question_name = cols[1].find("a").text.strip()
        question_link = cols[1].find("a")["href"]
        full_link = f"https://rosalind.info{question_link}"
        data[problem_id] = (question_name, full_link)
    return data

with open('README.md','w+') as new_readme:
    new_readme.write('# Rosalind\n> [Rosalind](http://rosalind.info/about) is a platform for learning bioinformatics through problem solving. This repository contains my solutions to some of the questions that I solved ✨\n\n')
    new_readme.write(' \n'.join([
        '## Why Bioinformatics? 🧬\n',
        'After learning String Data Structures (such as Suffix Arrays and Suffix Trees) and String Matching Algorithms',
        'in Competitive Programming, I found it to be one of the most satisfying yet cursed topic that I\'ve learnt so',
        'far. Coincidentally, I stumbled upon a textbook \'Algorithms in Bioinformatics: A Practical Introduction\' ' 
        'by a former Professor from the National University of Singapore and thus started a journey down this rabbit hole',
        'that I\'m thoroughly enjoying.\n\n'
    ]))
    new_readme.write('\n'.join([
        '## Current Goals in learning Bioinformatics? 🎯\n',
        '- **Exploration**: I do not have any background in Biology so I\'m using this opportunity to pick up the basics while sharpening my algorithmic skills\n'
        '- **Algorithmic Curiosity**: Solving problems is one of the main reason why I love Computer Science, so Bioinformatics is a natural progression into solving real life problems.\n\n'
    ]))
    for title,file_path,subdomain in sections:
        new_readme.write(f'## {title}\n\n')
        new_readme.write('|Problem Name|Problem ID|Solution|\n|:---|:---|:---|\n')
        solved = set([x.name.split('.')[0].strip().upper() for x in os.scandir(file_path) if x.is_file()])
        all_problems = get_all_problems(subdomain)
        rows = [(pid,*all_problems[pid]) for pid in solved if pid in all_problems]
        for pid,title,url in sorted(rows):
            new_readme.write(f'|[{title}]({url})|{pid}|[![py](./images/python.png)](./{file_path}/{pid.lower()}.py)|\n')
        new_readme.write('\n')