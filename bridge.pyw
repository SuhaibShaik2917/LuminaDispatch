from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
import os
import json
import logging
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# --- LOGGING SETUP ---
logging.basicConfig(
    filename='bridge_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)
# MAXIMUM PERMISSIVE CORS: Allows any origin, any header, any method
CORS(app, resources={r"/*": {"origins": "*"}})

# --- CONFIG LOADER ---
def load_config():
    try:
        # Get the absolute path of the folder where bridge.py is located
        base_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_path, 'config.json')
        with open(config_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Config load error: {str(e)}")
        return {}

@app.errorhandler(404)
def not_found(e):
    return jsonify({"status": "error", "message": "Endpoint not found."}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"status": "error", "message": "Internal server error."}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "online", "message": "Bridge is active"}), 200

@app.route('/send_single', methods=['POST'])
def send_single_mail():
    try:
        config = load_config()
        auth_email = request.form.get('email') or config.get('auth_email')
        auth_pass = request.form.get('password') or config.get('auth_pass')
        subject = request.form.get('subject')
        body = request.form.get('body')
        target = request.form.get('target')
        resume_file = request.files.get('resume')

        if not all([auth_email, auth_pass, subject, body, target]):
            logging.warning(f"Missing fields: email={bool(auth_email)}, pass={bool(auth_pass)}, sub={bool(subject)}, body={bool(body)}, target={bool(target)}")
            return jsonify({"status": "error", "message": "Missing required fields"}), 400

        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = auth_email
        msg['To'] = target

        if "<html" in body.lower() or "<div>" in body.lower() or "<p>" in body.lower():
            msg.attach(MIMEText(body, 'html'))
        else:
            msg.attach(MIMEText(body, 'plain'))

        if resume_file:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(resume_file.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={resume_file.filename}")
            msg.attach(part)

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(auth_email, auth_pass)
            server.send_message(msg)

        logging.info(f"Successfully sent mail to {target}")
        return jsonify({"status": "success", "target": target}), 200

    except smtplib.SMTPAuthenticationError:
        logging.error("Authentication failed: Invalid email or App Password.")
        return jsonify({"status": "error", "message": "Authentication failed"}), 401
    except Exception as e:
        logging.error(f"Error sending mail: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    print("\n" + "="*50)
    print("🚀 PROFESSIONAL BRIDGE SERVER STARTING")
    print("URL: http://127.0.0.1:5000")
    print("CORS: UNRESTRICTED MODE")
    print("="*50 + "\n")
    # Run on 0.0.0.0 to accept all local connections
    app.run(host='0.0.0.0', port=5000, debug=False)
