# 🚀 Lumina Dispatch

A professional, high-performance system for dispatching career outreach emails with support for HTML formatting, PDF attachments, and secure background authentication.

## 📁 Project Structure
- `bridge.pyw`: The core Python server (The Engine). Runs invisibly in the background.
- `outreach_portal.html`: The web-based control panel (The Interface).
- `config.json`: Secure storage for your Gmail credentials.
- `START_HERE.bat`: Quick-start launcher that boots the server and opens the portal.
- `bridge_log.txt`: Detailed history of every email sent (created automatically).

---

## 🛠️ Setup & Installation

### 1. Prerequisites
- **Python 3.x** must be installed on your system.
- **Required Libraries**: The bridge uses `Flask` and `Flask-CORS`. Install them via terminal:
  ```bash
  pip install flask flask-cors
  ```

### 2. Gmail Configuration (Crucial)
Gmail blocks standard passwords for security. You **MUST** use an **App Password**:
1. Enable **2-Step Verification** in your Google Account settings.
2. Search for **"App passwords"** in your account search bar.
3. Create a new app password (e.g., "Lumina Dispatch").
4. Copy the **16-character code** provided.

### 3. Configure Credentials
Open `config.json` and enter your details:
```json
{
    "auth_email": "your-email@gmail.com",
    "auth_pass": "your-16-char-app-password"
}
```
*Note: If you fill this out, you don't need to enter your email/password in the web portal every time.*

---

## 🚀 How to Use

### Step 1: Start the System
Double-click **`START_HERE.bat`**. 
- This will launch the bridge server invisibly in the background.
- It will automatically open the `outreach_portal.html` in your default browser.

### Step 2: Compose & Launch
1. **Assets**: Upload your Resume PDF.
2. **Composition**: 
   - Enter a professional subject line.
   - Write your body (Plain text or **HTML** is supported for professional formatting).
   - Enter target email addresses (one per line).
3. **Launch**: Click `🚀 Launch Campaign`.

---

## 📈 Advanced Features

### ✉️ HTML Email Support
You can use HTML tags in the body to make your emails look like professional corporate mail:
- Use `<b>Text</b>` for **Bold**.
- Use `<br>` for new lines.
- Use `<a href="link">Click Here</a>` for hyperlinks.

### ⏱️ Transmission Delay
To avoid being flagged as spam by Google, use the **Interval Delay** setting (e.g., 10 seconds) to space out your emails.

### 📜 Logs
Check `bridge_log.txt` to see the exact status of every email sent and troubleshoot any failures.

---

## 🆘 Troubleshooting
- **"Failed to fetch"**: The background server is not running. Run `START_HERE.bat` again.
- **"Authentication failed"**: Your App Password is incorrect or 2-Step Verification is disabled in Google.
- **"Endpoint not found"**: Ensure you are using the latest version of the files.
