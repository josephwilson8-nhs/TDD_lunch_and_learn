# Test Driven Development Lunch and Learn Repository

This is a repository full of examples of using pytest for the BI Vis Dev Team Lunch and Learn on 25th May 2022. Check out the confluence page for the Lunch and Learn [here](https://nhsd-confluence.digital.nhs.uk/pages/viewpage.action?pageId=436998498)

Feel free to clone a copy of this repository to play around with it. Please ensure you create a branch of the code to work on and keep it up to date by occasionally pulling main into your branch.

Check out the pytest documentation [here](https://docs.pytest.org/en/6.2.x/contents.html).

## Set up instructions

### Clone the repository from GitHub and create a personal branch

If you are unfamiliar with using Git and GitHub, [here is a handy tutorial](https://www.freecodecamp.org/news/git-and-github-for-beginners/).

1. Clone the repository via https

   ```git
   git clone https://github.com/josephwilson8-nhs/TDD_lunch_and_learn.git
   ```

2. Create a personal branch to work off

   ```git
   git checkout -b <name_of_your_branch>
   ```

3. Pull in changes from main (Repeat when main is updated)

   ```git
   git pull origin main
   ```

### Set up a virtual environment to use the code within

1. Create a virtual environment

   1. With pip venv

      ```bash
      python3 -m venv <env_name>
      source <env_name>/bin/activate
      pip install -r requirements.txt
      echo <env_name> >> .gitignore
      ```

   2. With conda

      ```bash
      conda create --name <env_name> --file requirements.txt
      ```

## Running tests

* To run all tests

    ```bash
    pytest
    ```

* To run all tests in a file

    ```bash
    pytest test_file_name.py
    ```

* To run all tests in a directory

    ```bash
    pytest testing/
    ```

* To run tests matching a custom marker

    ```bash
    pytest -m marker_name
    ```
