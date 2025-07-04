# action-repo

This repository is configured to send webhook events to the webhook-repo Flask application.

## Purpose
This repository demonstrates GitHub webhook functionality by triggering events when:
- Code is pushed to any branch
- Pull requests are created
- Pull requests are merged

## Webhook Configuration

The webhook is configured to send events to: `https://your-webhook-endpoint.com/webhook`

### Events Monitored:
- **Push events** - When code is pushed to any branch
- **Pull request events** - When PRs are opened/closed
- **Merge events** - When PRs are merged

## Testing the Webhook

### 1. Test Push Events
```bash
# Make a simple change and push
echo "Test change $(date)" >> test-file.txt
git add test-file.txt
git commit -m "Test push event"
git push origin main
```

### 2. Test Pull Request Events
```bash
# Create a feature branch
git checkout -b feature/test-pr
echo "Feature change" >> feature.txt
git add feature.txt
git commit -m "Add feature"
git push origin feature/test-pr

# Create PR through GitHub UI or GitHub CLI
gh pr create --title "Test PR" --body "Testing pull request webhook"
```

### 3. Test Merge Events
```bash
# Merge the PR through GitHub UI
# This will trigger the merge webhook event
```

## Sample Files

This repository contains sample files to demonstrate different types of changes:
- `README.md` - This documentation
- `test-file.txt` - For testing push events
- `feature.txt` - For testing feature branches
- `main.py` - Sample Python code

## Webhook Payload Examples

The webhook endpoint will receive payloads for each event type and process them according to the specified format.

## Repository Settings

Make sure to configure the webhook in repository settings:
1. Go to Settings → Webhooks
2. Add webhook with your endpoint URL
3. Select individual events: Pushes, Pull requests
4. Set content type to application/json