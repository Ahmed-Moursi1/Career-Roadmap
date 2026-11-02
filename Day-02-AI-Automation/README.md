# Day 2 — AI Automation: Lead Capture

A starter n8n workflow that receives a lead through a Webhook and appends the lead to Google Sheets.

## What it does
1. Receives a `POST` request at the `lead-capture` webhook.
2. Reads `name`, `email`, and `message` from the request body.
3. Appends those values and a timestamp to a Google Sheets tab named `Leads`.

## Setup
1. Create a Google Sheet and add these exact column headers in the `Leads` tab: `Name`, `Email`, `Message`, `Received At`.
2. In n8n, choose **Import from File** and import `workflow.json`.
3. Open the Google Sheets node, select your own Google Sheets OAuth2 credential, and replace `REPLACE_WITH_GOOGLE_SHEET_ID` with your spreadsheet ID.
4. Save and test the workflow. Keep it inactive until the test succeeds.
5. Copy the Test URL from the Webhook node and send a POST request with JSON such as:

```json
{
  "name": "Ahmed",
  "email": "ahmed@example.com",
  "message": "I want to know more."
}
```

## Important
- No Google credentials or spreadsheet IDs are included in this repository.
- The workflow is a starter template and requires your own n8n and Google account setup.
- Do not publish OAuth tokens, API keys, or private webhook URLs.
