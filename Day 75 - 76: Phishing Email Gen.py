import random

# Fake sender emails (spoofed to look real)
SENDER_EMAILS = [
    "security@paypal.com",
    "no-reply@amazon.com",
    "support@yourbank.com",
    "helpdesk@microsoft.com"
]

# Fake subject lines
SUBJECTS = [
    "⚠️ Urgent: Your Account Has Been Compromised!",
    "🚨 Important: Unauthorized Login Attempt Detected",
    "Your Payment Has Failed – Update Your Info",
    "Action Required: Verify Your Account Now",
    "Security Notice: Unusual Activity Detected"
]

# Fake email templates
EMAIL_TEMPLATES = [
    """Dear Customer,

We detected unusual activity on your account and have temporarily locked it for security reasons. 

Please verify your identity immediately by clicking the link below:

🔗 [FAKE LINK] https://security-paypal-login.com

If you do not confirm within 24 hours, your account will be permanently locked.

Best regards,  
Security Team""",

    """Dear User,

Your recent payment on Amazon was unsuccessful due to outdated billing information.

To prevent order cancellation, please update your payment details here:

🔗 [FAKE LINK] https://amazon-billing-update.com

Thank you,  
Amazon Billing Department""",

    """Dear Valued Customer,

We noticed an unauthorized login attempt to your banking account from a new device.

If this wasn’t you, please secure your account immediately:

🔗 [FAKE LINK] https://bank-secure-login.com

Regards,  
Your Bank's Security Team"""
]

def generate_phishing_email():
    sender = random.choice(SENDER_EMAILS)
    subject = random.choice(SUBJECTS)
    body = random.choice(EMAIL_TEMPLATES)

    email = f"""
From: {sender}
Subject: {subject}

{body}
"""
    return email

if __name__ == "__main__":
    print("\n📧 Generated Phishing Email (Educational Purpose Only):\n")
    print(generate_phishing_email())
