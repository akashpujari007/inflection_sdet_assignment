# End-to-End Test Cases - Campaign Scheduling

| Test Case ID | Description | Steps | Expected Result |
|-------------|------------|-------|----------------|
| TC_001 | Create a campaign | 1. Send API request to create a campaign 2. Verify response 3. Check database | Campaign is created |
| TC_002 | Schedule a campaign | 1. Create a campaign 2. Set schedule time 3. Check scheduled campaigns | Campaign is scheduled correctly |
| TC_003 | Cancel a campaign | 1. Schedule a campaign 2. Cancel it 3. Verify it is removed | Campaign is canceled |
