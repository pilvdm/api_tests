# Requests + PyTest API Testing Guide
## Requirements and Installations
- Python 3.8+
- Run pip install -r requirements.txt

# How to Launch
Run the following from the root directory of the project:\
- python -m pytest tests/name_of_test_file 
- or just python -m tests/ to execute all tests

# Writing Tests and Maintenance
- Tests are located in tests/ folder
- Fixtures are located in conftest
- Project variables are located in config file

# Improvements and TODOs
 - Wrap to docker img
 - Embed to be executed in CI/CD
 - Integrate reporting module to Allure
 - Colonize Mars