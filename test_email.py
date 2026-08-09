"""Quick test to check if Gmail SMTP is working."""
import smtplib
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

MAIL_USERNAME = os.environ.get("MAIL_USERNAME", "")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", "")

print(f"Username loaded: {MAIL_USERNAME}")
print(f"Password loaded: {'YES (hidden)' if MAIL_PASSWORD and 'your_' not in MAIL_PASSWORD else 'NOT SET / placeholder'}")
print()

if not MAIL_USERNAME or "your_" in MAIL_USERNAME:
    print("[ERROR] MAIL_USERNAME is not set. Check your .env file.")
elif not MAIL_PASSWORD or "your_" in MAIL_PASSWORD:
    print("[ERROR] MAIL_PASSWORD is not set. Check your .env file.")
else:
    print("Trying to connect to Gmail SMTP...")
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as server:
            server.login(MAIL_USERNAME, MAIL_PASSWORD)
            print("[SUCCESS] Gmail SMTP login worked. Emails will be sent.")
    except smtplib.SMTPAuthenticationError:
        print("[FAILED] Authentication error! Possible reasons:")
        print("   1. Wrong App Password - make sure you copied it correctly (no spaces)")
        print("   2. You used your Gmail password instead of App Password")
        print("   3. 2-Step Verification is not enabled on your Gmail")
        print("   Go to: https://myaccount.google.com/apppasswords")
    except smtplib.SMTPConnectError:
        print("[FAILED] Could not connect to Gmail. Check your internet connection.")
    except Exception as e:
        print(f"[FAILED] Error: {e}")
