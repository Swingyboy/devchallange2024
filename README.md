# WEB UI Automation

This project is designed for automated testing of web user interfaces using `pytest`, `pytest-bdd`, `pytest-html`, and `Playwright`. It allows for flexible testing based on different platforms (desktop or mobile) and browser configurations.

## Environment Variables

Before running the tests, ensure the following environment variables are exported or set in your `.env` file:
    
    ```bash
    export BROWSER_TYPE=chromium
    export HEADLESS=true
    export PLATFORM=desktop
    export BASE_URL=https://www.google.com
    ```
where:
- `BROWSER_TYPE` is the browser type to use (e.g., `chromium`, `firefox`)
- `HEADLESS` is a boolean value to run the browser in headless mode
- `PLATFORM` is the platform to run the tests on (e.g., `desktop`, `mobile`)
- `BASE_URL` is the base URL of the web application to test

## Dependencies
The minimum python version required is `3.9`.
Before running the tests, ensure the following dependencies are installed:
    
    ```bash
    pip install -r requirements.txt
    ```
    ```bash
    playwright install
    ```

## Running the Tests
To run the tests, execute the following command:
    
    ```bash
    pytest -s -v -m ${PLATFORM}
    ```
Depending on the platform specified, the tests will run on the specified browser and platform.
The results will be displayed in the terminal and saved in the `reports` directory as an HTML file.

