# Serverless Email API

A Serverless REST API built with **AWS Lambda** and **Python** that sends emails using Gmail SMTP.  
Supports input validation, proper HTTP response codes, and error handling.  


## Setup Instructions

1. Clone the repository:

```
git clone 
cd serverless-email
```

2. Install Python dependencies:

```
pip install -r requirements.txt
```

3. Create a .env file in the project root:

```
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
```


4. Start Serverless Offline:

```
sls offline
```




Example Request:

```
curl -X POST http://localhost:3000/send-email \
-H "Content-Type: application/json" \
-d '{
  "receiver_email": "receiver@example.com",
  "subject": "Test Email",
  "body_text": "Hello from Serverless!"
}'
```

Expected Response:

```
{"message": "Email sent successfully to receiver@example.com"}
```