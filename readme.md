# ECommerce Robot Tests

This project contains automated tests for an eCommerce website using Robot Framework, with integrated email notifications for test results.

## Overview

The automated tests are designed to perform various actions on the [shopist.io](https://shopist.io/) eCommerce website, covering scenarios such as updating profile information and scraping sofa names and prices. After each test case execution, an email notification is sent with the test result.

## Dependencies

- [Robot Framework](https://robotframework.org/)
- [Robot Framework Browser](https://marketsquare.github.io/robotframework-browser/Browser.html)
- [Robot Framework SeleniumLibrary](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html)
- [Robot Framework CSVLibrary](https://github.com/guykisel/robotframework-CSVLibrary)

## Installation

1. Clone this repository to your local machine.
2. Install dependencies using pipenv:
   ```
   pipenv install
   ```

## Configuration

Before running the tests, configure the SMTP settings and recipient email address for sending notifications:

1. Edit the `config.txt` file located in the `config` directory.
2. Specify your SMTP server, port, login, SMTP key, and recipient email address.

Example `config.txt`:
```
SMTP Server: smtp.example.com
Port: 587
Login: your_email@example.com
SMTP Key: your_smtp_password
Recipient: recipient_email@example.com
```

## Usage

To run the tests and receive email notifications upon completion, use the following command:
```
pipenv run robot --outputdir Reports .\Tests\eCommerce_tests.robot
```

## Test Cases

### Update Profile Name

This test case updates the profile name on the shopist.io website and sends an email notification with the test result.

### Scrape Shopist Sofas

This test case scrapes the names and prices of sofas from the shopist.io website, saves the results to a CSV file, and sends an email notification with the test result.

## Structure

- **Tests**: Contains the test cases written in Robot Framework.
- **Resources**: Contains resource files including settings, variables, and keywords.
- **Data**: Contains input data files such as CSV files.
- **Library**: Contains the `EmailNotificationLibrary.py` for sending email notifications.
- **config**: Contains the `config.txt` for email notification configuration.

## Author

- Osku

## License

This project is licensed under the [MIT License](LICENSE).