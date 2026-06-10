# Email Automation - Contact Us Form

**Deployed on AWS S3 | Lambda | DynamoDB | API Gateway**  
*Note: Resources have been deleted due to AWS costs. This project is archived for educational and portfolio purposes.*

---

## 🌐 Live Website
**[http://email-automation-krsna.s3-website.ap-south-1.amazonaws.com](http://email-automation-krsna.s3-website.ap-south-1.amazonaws.com)** *(Resource Deleted)*

> ⚠️ **Disclaimer**: The live infrastructure has been removed to minimize AWS expenses as I am a student. This repository serves as a portfolio project demonstrating serverless architecture and cloud deployment experience.

---

## 📋 Project Overview

A fully serverless contact form application built with modern web technologies and AWS services. This project demonstrates end-to-end cloud application development, from frontend UI to backend email automation using AWS infrastructure.

---

## 🏗️ Architecture

### **Frontend**
- **HTML5** - Responsive contact form interface
- **CSS3** - Professional styling
- **JavaScript (ES6+)** - Asynchronous form submission

### **Backend - AWS Infrastructure** 🔗
| Service | Purpose |
|---------|---------|
| **AWS S3** | Hosts static website files |
| **AWS API Gateway** | RESTful API endpoint for form submissions |
| **AWS Lambda** | Serverless compute for backend logic |
| **AWS DynamoDB** | NoSQL database for storing contact submissions |
| **SMTP (Gmail)** | Email notification service |

---

## ⚙️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python 3.x
- **Cloud Platform**: Amazon Web Services (AWS)
- **Database**: **DynamoDB** (AWS managed NoSQL)
- **Email Service**: Gmail SMTP
- **Hosting**: AWS S3 Static Website Hosting
- **API**: AWS API Gateway
- **Compute**: AWS Lambda Functions

---

## 🚀 Features

✅ Responsive contact form UI  
✅ Real-time form validation  
✅ Asynchronous form submission via AWS API Gateway  
✅ Automated email notifications to company inbox  
✅ Customer confirmation email  
✅ **Persistent data storage in DynamoDB**  
✅ CORS-enabled API endpoints  
✅ Serverless architecture (no server maintenance required)  
✅ Secure credential management  

---

## 📁 Project Structure

```
contact-us-project/
├── index.html              # Frontend HTML form
├── script.js              # JavaScript - Form submission logic
├── style.css              # CSS styling
├── lambda_function.py     # AWS Lambda backend function
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

---

## 🔧 How It Works

### 1. **User Submission**
   - User fills out the contact form with name, email, phone, subject, and message
   - JavaScript captures the form data

### 2. **API Request**
   - JavaScript sends a POST request to AWS API Gateway endpoint
   - Endpoint: `https://x8052djvfc.execute-api.ap-south-1.amazonaws.com/contact-us`

### 3. **Lambda Processing**
   - AWS Lambda function receives the request
   - **Stores submission data in DynamoDB for persistence**
   - Validates and processes the form data

### 4. **Email Notifications**
   - Sends confirmation email to the customer
   - Sends notification email to the company inbox
   - Uses Gmail SMTP server for email delivery

### 5. **Response**
   - Returns success/error message to frontend
   - User sees status message on the form

---

## 🛠️ Setup & Deployment (Local Development)

### Prerequisites
- Python 3.8+
- AWS Account with appropriate IAM permissions
- Git

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd contact-us-project

# Install Python dependencies (if deploying Lambda locally)
pip install -r requirements.txt
```

### AWS Configuration

1. **Create S3 Bucket**
   ```bash
   aws s3 mb s3://email-automation-krsna
   aws s3 website s3://email-automation-krsna --index-document index.html
   aws s3 sync . s3://email-automation-krsna
   ```

2. **Create DynamoDB Table**
   ```bash
   aws dynamodb create-table \
     --table-name ContactSubmissions \
     --attribute-definitions AttributeName=id,AttributeType=S \
     --key-schema AttributeName=id,KeyType=HASH \
     --billing-mode PAY_PER_REQUEST \
     --region ap-south-1
   ```

3. **Deploy Lambda Function**
   - Upload `lambda_function.py` to AWS Lambda
   - Configure environment variables for email credentials
   - Assign appropriate IAM role with DynamoDB permissions

4. **Create API Gateway**
   - Create REST API with POST method
   - Configure Lambda integration
   - Enable CORS

---

## 🔐 Security Notes

- **Credentials**: Never commit sensitive data (passwords, API keys)
- **Email App Password**: Use environment variables or AWS Secrets Manager
- **DynamoDB**: Implement proper encryption and access controls
- **.gitignore**: Configured to exclude sensitive files

---

## 📦 Environment Variables

Create a `.env` file locally (not committed to git):

```
COMPANY_EMAIL=your-email@gmail.com
APP_PASSWORD=your-gmail-app-password
DYNAMODB_TABLE=ContactSubmissions
AWS_REGION=ap-south-1
```

---

## 📊 Data Persistence

All contact submissions are stored in **AWS DynamoDB** with the following schema:

```json
{
  "id": "unique-submission-id",
  "name": "Customer Name",
  "email": "customer@example.com",
  "phone": "1234567890",
  "subject": "Contact Subject",
  "message": "Contact Message",
  "timestamp": "2026-06-10T12:34:56Z"
}
```

---

## 💡 Learning Outcomes

This project demonstrates proficiency in:

- ✅ Serverless architecture design
- ✅ AWS service integration (S3, Lambda, DynamoDB, API Gateway)
- ✅ RESTful API design and consumption
- ✅ Backend automation and email services
- ✅ Full-stack web application development
- ✅ Cloud deployment and infrastructure management
- ✅ Security best practices in cloud applications

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👤 Author

**Krsna**  
Portfolio Project | AWS Certified Cloud Enthusiast | Student Developer

---

## 📞 Contact

For questions or inquiries about this project, please refer to the contact form demonstration.

---

## 🗑️ Note on AWS Resource Deletion

The AWS infrastructure for this project has been decommissioned due to:
- 📚 Student budget constraints
- 💰 AWS operational costs
- 🔄 Project lifecycle completion

This repository is maintained for:
- 📖 Educational reference
- 🎓 Portfolio demonstration
- 💾 Future reference and learning

---

**Last Updated**: June 2026  
**Status**: Archived (Resources Deleted)
