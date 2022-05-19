# auto generated pipeline

[![Sonar Coverage](https://sonar.wal-mart.com/api/project_badges/measure?project=com.walmart.reusablecode.graph.style.pipeline.framework&metric=coverage)](https://sonar.looper.prod.walmartlabs.com/dashboard?id=com.walmart.reusablecode.graph.style.pipeline.framework) 
[![Sonar Bugs](https://sonar.wal-mart.com/api/project_badges/measure?project=com.walmart.reusablecode.graph.style.pipeline.framework&metric=bugs)](https://sonar.looper.prod.walmartlabs.com/dashboard?id=com.walmart.reusablecode.graph.style.pipeline.framework) 
[![Sonar Security](https://sonar.wal-mart.com/api/project_badges/measure?project=com.walmart.reusablecode.graph.style.pipeline.framework&metric=vulnerabilities)](https://sonar.looper.prod.walmartlabs.com/dashboard?id=com.walmart.reusablecode.graph.style.pipeline.framework) 
[![Sonar Reliability Rating](https://sonar.wal-mart.com/api/project_badges/measure?project=com.walmart.reusablecode.graph.style.pipeline.framework&metric=reliability_rating)](https://sonar.looper.prod.walmartlabs.com/dashboard?id=com.walmart.reusablecode.graph.style.pipeline.framework) 
[![Sonar Security Rating](https://sonar.wal-mart.com/api/project_badges/measure?project=com.walmart.reusablecode.graph.style.pipeline.framework&metric=security_rating)](https://sonar.looper.prod.walmartlabs.com/dashboard?id=com.walmart.reusablecode.graph.style.pipeline.framework) 
[![Sonar Tech Debt](https://sonar.wal-mart.com/api/project_badges/measure?project=com.walmart.reusablecode.graph.style.pipeline.framework&metric=sqale_index)](https://sonar.looper.prod.walmartlabs.com/dashboard?id=com.walmart.reusablecode.graph.style.pipeline.framework) 


[![Quality Gate](https://sonar.wal-mart.com/api/project_badges/quality_gate?project=com.walmart.reusablecode.graph.style.pipeline.framework)](https://sonar.looper.prod.walmartlabs.com/dashboard?id=com.walmart.reusablecode.graph.style.pipeline.framework)


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
--extracts_yaml="/Users/j0z04f2/Desktop/code/databathing_wrapper/yamls/extractors.yaml" \
--transforms_yaml="/Users/j0z04f2/Desktop/code/databathing_wrapper/yamls/transforms.yaml" \
--loaders_yaml="/Users/j0z04f2/Desktop/code/databathing_wrapper/yamls/loaders.yaml"