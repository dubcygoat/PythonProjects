import imaplib
from config import Gmail_password, Gmail_user
import email 
from email.header import decode_header

# account credentials
username = Gmail_user
password =  Gmail_password

# key words to identify rejected eimaps
keywords = ["invoice", "payments"]

#Gmail IMAP server
imap = imaplib.IMAP4_SSL("imap.gmail.com")

# authenticate to imap server
imap.login(username, password)

#Select Inbox for processing
inbox = imap.select("inbox")

# Search for all emails in the subject or body
status, messages = imap.search(None, "ALL")

if status == "OK":
    # Fetch the list of email IDs
    email_ids = messages[0].split()

    for num in email_ids:
        # Fetch the email by ID
        status, msg_data = imap.fetch(num, "(RFC822)")
        
        if status == "OK":
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    # Parse the email content
                    msg = email.message_from_bytes(response_part[1])

                    # Initialize an empty body string
                    body = ""
                    
                    # Check if the email has multiple parts
                    if msg.is_multipart():
                        # Iterate through the email parts
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                # Get the email body
                                if content_type == "text/plain" and "attachment" not in content_disposition:
                                    body = part.get_payload(decode=True).decode()
                                    break  # Stop at the first text/plain part
                            except Exception as e:
                                print(f"Error decoding email body: {e}")
                    else:
                        # If the email is not multipart, get the payload directly
                        body = msg.get_payload(decode=True)

                     # If body is in bytes, decode it; if already a string, skip decoding
                    if isinstance(body, bytes):
                        try:
                            body = body.decode('utf-8')
                        except UnicodeDecodeError:
                            try:
                                body = body.decode('latin-1')
                            except UnicodeDecodeError:
                                body = body.decode('ISO-8859-1')

                    # Convert body to lowercase for case-insensitive search
                    body_lower = body.lower()

                    # Check for rejection keywords in the email body
                    if any(keyword in body_lower for keyword in keywords):
                        print(f"Moving email ID {num} to 'Invoices' folder")
                        
                        # Create the "Rejections" folder if it doesn't exist
                        imap.create("Invoices")
                        
                        # Move the email to the "Rejections" folder
                        result = imap.copy(num, "Invoices")
                        if result[0] == 'OK':
                            # Mark the email as deleted from the inbox
                            imap.store(num, '+FLAGS', '\\Deleted')