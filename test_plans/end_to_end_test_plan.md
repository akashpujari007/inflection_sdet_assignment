# End-to-End Test Plan - Campaign Scheduling

## **Objective**
Ensure that the Marketing Campaign Scheduling feature works as expected by verifying all functional aspects.

## **Test Scenarios**
1. Create a new email campaign with a scheduled send time.
2. Select a recipient list and validate campaign scheduling.
3. Choose an email template for the campaign.
4. Modify a scheduled campaign.
5. Cancel a scheduled campaign.
6. Verify that campaigns are sent at the correct time.

## **Test Environment**
- **Services**: Campaign, Email Template, Recipient.
- **Docker Compose**: `docker-compose-e2e.yml`
