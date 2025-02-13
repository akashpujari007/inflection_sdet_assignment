# Integration Test Plan - Campaign Scheduling

## **Objective**
Ensure that the campaign scheduling service integrates properly with recipient management and email template services.

## **Test Scenarios**
1. Verify communication between the Campaign and Recipient services.
2. Verify the correctness of recipient lists when fetched.
3. Validate that the selected email template is retrieved correctly.
4. Handle errors when the email or recipient services are unavailable.

## **Test Environment**
- **Services**: Campaign, Email Template, Recipient.
- **Docker Compose**: `docker-compose-integrations.yml`
