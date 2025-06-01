# Data-leak-prevention-system-

## 📌 Overview

The **User Data Leak Prevention System** is a security-focused web application designed to detect and prevent data leakage caused by client-side vulnerabilities, particularly **Cross-Site Scripting (XSS)**. This project emphasizes safe data handling practices and demonstrates how real-time prevention strategies can be implemented in modern web applications.

## 🛡️ Key Features

- 🚫 Detection and prevention of XSS attacks
- ✅ User input sanitization and validation
- 🧪 Real-time alerts for potential data leak vectors
- 🔐 Secure data storage mechanisms
- 📝 Logging and monitoring of suspicious activity

## 💡 Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Node.js / PHP / Python (Edit based on your tech stack)
- **Database**: MongoDB / MySQL / Firebase (Edit based on what you used)
- **Security Libraries**: DOMPurify, Helmet.js, or custom validation (specify what you used)

## 🧰 Project Structure

```bash
Data Prevention/
├── frontend/             # UI and form validation
├── backend/              # API and security logic
├── database/             # Scripts and schema for DB
├── tests/                # Test cases and vulnerability simulations
├── README.md             # Project documentation
└── LICENSE               # Licensing information
````

## ⚙️ Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Data-Prevention.git
   ```

2. Navigate into the directory:

   ```bash
   cd Data-Prevention
   ```

3. Install dependencies:

   ```bash
   npm install         # Or pip install -r requirements.txt
   ```

4. Start the server:

   ```bash
   npm start           # Or python app.py
   ```

5. Open the app in your browser at `http://localhost:3000`

## 🧪 Testing

* Use sample payloads like `<script>alert('XSS')</script>` to test input fields.
* Ensure logs are generated and alerts are triggered on malicious attempts.


## 🙋‍♀️ Author

**Poornima Thakur**
B.Tech CSE | Security Enthusiast | Passionate Developer


