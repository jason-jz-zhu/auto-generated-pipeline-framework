# auto generated pipeline

## Prerquest
- Please install databathing `pip install databathing`

## Check Style
- flake configuration file `.flake`
- CMD
  - `make lint`
  
## Unit Test && Coverage Reports
- CMD 
  - `python3 setup.py pytest`
- Local Report
  - Open `reports` -> `coverage.html` -> `index.html` in your web browser.
  
## SonarQube
- Report Upload CMD
  - Main Report Update
    - `sonar-scanner -Dproject.settings=sonar-project.properties`
  - Branch Report Update
    - `sonar-scanner -Dproject.settings=sonar-project.properties -Dsonar.branch.name=$BRANCH_NAME`

## How to run
python workflowRunner.py \
--extracts_yaml="yamls/extractors.yaml" \
--transforms_yaml="yamls/transforms.yaml" \
--loaders_yaml="yamls/loaders.yaml"