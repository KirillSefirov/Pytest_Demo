Just a little demo project to showcase the usage pytest framework to test and evaluate rest backend methods

# Local run
1) On your laptop install allure (for example `brew install allure`)
2) Install necessary libraries using `pip install --no-cache-dir -r requirements.txt`
3) Run tests `pytest --alluredir allure-results`
4) See the report by `allure serve allure-results`

To generate allure report after all tests successfully finished (make sure the folder is the same as in the step above)
allure serve allure-results

# To run tests in docker container:
1) Build a docker image using the command below, you can use any project name instead of "kirillsefirov/pytest_demo:1.0". P.S. Don't forget the dot at the end <br>
`docker build -t kirillsefirov/pytest_demo:1.0 .`
3) Run the docker container ie using docker desktop as the easiest option
