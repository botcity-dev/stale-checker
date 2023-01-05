# Botcity Stale Checker

The project was created with the purpose of keeping the releases always up to date, avoiding having loose commits in the
repositories without being in any release/tag.

### How to use

You can trigger the workflow directly from github or wait for it to run every day at midnight.

### How to add new repos

At the end of the **repos.txt** file it will be necessary to include the following information with PATH_GITHUB being part of the link to the repository:
```text
https://$GH_TOKEN@github.com/{PATH_GITHUB}.git
```

### Environment variables

You need to enter the following environment variables in the repository:

| Name            | Description                                                         |
|-----------------|---------------------------------------------------------------------|
| **GH_TOKEN**    | Github token with access to all repositories in the organization.   |
| **SLACK_TOKEN** | Token with the authorization to send messages in the slack channel. |
| **CHANNEL**     | Channel where error messages will be sent.                          |


## Monitored repositories
| Name                                     | Language      | Link                                                                | 
|------------------------------------------|---------------|---------------------------------------------------------------------|
| **bot-aws-s3-plugin-python**             | python        | https://github.com/botcity-dev/bot-aws-s3-plugin-python             |
| **bot-captcha-plugin-python**            | python        | https://github.com/botcity-dev/bot-captcha-plugin-python            |
| **bot-ftp-plugin-python**                | python        | https://github.com/botcity-dev/bot-ftp-plugin-python                |
| **bot-profile-finder**                   | python        | https://github.com/botcity-dev/bot-profile-finder                   |
| **bot-googledrive-plugin-python**        | python        | https://github.com/botcity-dev/bot-googledrive-plugin-python        |
| **bot-googlesheets-plugin-python**       | python        | https://github.com/botcity-dev/bot-googlesheets-plugin-python       |
| **botcity-utils-python**                 | python        | https://github.com/botcity-dev/botcity-utils-python                 |
| **bot-profile-finder**                   | python        | https://github.com/botcity-dev/bot-profile-finder                   |
| **botcity-documents-python**             | python        | https://github.com/botcity-dev/botcity-documents-python             |
| **botcity-framework-core-python**        | python        | https://github.com/botcity-dev/botcity-framework-core-python        |
| **bot-python-template**                  | python        | https://github.com/botcity-dev/bot-python-template                  |
| **botcity-studio-sdk**                   | python        | https://github.com/botcity-dev/botcity-studio-sdk                   |
| **bot-excel-plugin-python**              | python        | https://github.com/botcity-dev/bot-excel-plugin-python              |
| **bot-csv-plugin-python**                | python        | https://github.com/botcity-dev/bot-csv-plugin-python                |
| **bot-http-plugin-python**               | python        | https://github.com/botcity-dev/bot-http-plugin-python               |
| **bot-aws-secretsmanager-plugin-python** | python        | https://github.com/botcity-dev/bot-aws-secretsmanager-plugin-python |
| **bot-aws-lambda-plugin-python**         | python        | https://github.com/botcity-dev/bot-aws-lambda-plugin-python         |
| **bot-files-plugin-python**              | python        | https://github.com/botcity-dev/bot-files-plugin-python              |
| **bot-aws-sqs-plugin-python**            | python        | https://github.com/botcity-dev/bot-aws-sqs-plugin-python            |
| **bot-recorder-plugin-python**           | python        | https://github.com/botcity-dev/bot-recorder-plugin-python           |
| **bot-discord-plugin-python**            | python        | https://github.com/botcity-dev/bot-discord-plugin-python            |
| **bot-gmail-plugin-python**              | python        | https://github.com/botcity-dev/bot-gmail-plugin-python              |
| **bot-whatsapp-plugin-python**           | python        | https://github.com/botcity-dev/bot-whatsapp-plugin-python           |
| **bot-twilio-sms-plugin-python**         | python        | https://github.com/botcity-dev/bot-twilio-sms-plugin-python         |
| **bot-twilio-whatsapp-plugin-python**    | python        | https://github.com/botcity-dev/bot-twilio-whatsapp-plugin-python    |
| **bot-email-plugin-python**              | python        | https://github.com/botcity-dev/bot-email-plugin-python              |
| **bot-crawler-plugin-python**            | python        | https://github.com/botcity-dev/bot-crawler-plugin-python            |
| **bot-hashicorp-vault-plugin-python**    | python        | https://github.com/botcity-dev/bot-hashicorp-vault-plugin-python    |
| **bot-telegram-plugin-python**           | python        | https://github.com/botcity-dev/bot-telegram-plugin-python           |
| **bot-cloudvision-plugin-python**        | python        | https://github.com/botcity-dev/bot-cloudvision-plugin-python        |
| **bot-aws-textract-plugin-python**       | python        | https://github.com/botcity-dev/bot-aws-textract-plugin-python       |
| **js-template-cli**                      | typescript    | https://github.com/botcity-dev/js-template-cli                      |
| **botcity-framework-core-js**            | typescript    | https://github.com/botcity-dev/botcity-framework-core-js            |
| **botcity-maestro-sdk-js**               | typescript    | https://github.com/botcity-dev/botcity-maestro-sdk-js               |
| **botcity-framework-core**               | java          | https://github.com/botcity-dev/botcity-framework-core               |
| **botstudio**                            | java          | https://github.com/botcity-dev/botstudio                            |
