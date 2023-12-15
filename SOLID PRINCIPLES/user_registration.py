import sqlite3
import json
from smtplib import SMTP


#

"""

1. Single Responsibility Principle (SRP):
2. Open/Closed Principle (OCP):
3. Liskov Substitution Principle (LSP):
4. Interface Segregation Principle (ISP):
5. Dependency Inversion Principle (DIP):

"""

# User repository class responsible for database operations
class UserRepository:
    def __init__(self, json_file_path='users.json'):
        self.json_file_path = json_file_path
        self.load_data()

    def load_data(self):
        try:
            with open(self.json_file_path, 'r') as file:
                self.users = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            # If the file is empty or not present, initialize users to an empty list
            self.users = []

    def save_data(self):
        with open(self.json_file_path, 'w') as file:
            json.dump(self.users, file, indent=2)

    def register_user(self, user_data):
        self.users.append({'username': user_data['username'], 'email': user_data['email']})
        # Save data only if registration is successful


# Email sender class responsible for sending emails
class EmailSender:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_registration_email(self, email):
        with SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            try:
                server.login(self.sender_email, self.sender_password)
                subject = "Welcome to our platform!"
                body = "Thank you for registering with us."
                message = f"Subject: {subject}\n\n{body}"
                server.sendmail(self.sender_email, email, message)
            except Exception as e:
                # If there's an error in sending email, raise the exception
                raise e


# Registration service class coordinating user registration and email sending
class RegistrationService:
    def __init__(self, user_repository, email_sender):
        self.user_repository = user_repository
        self.email_sender = email_sender

    def register_user(self, user_data):
        try:
            # Register user in the database
            self.user_repository.register_user(user_data)
            # If registration is successful, send registration email
            self.email_sender.send_registration_email(user_data['email'])
            # Save user data to JSON file only if both registration and email sending are successful
            self.user_repository.save_data()
            print("User registration successful.")
        except Exception as e:
            print(f"User registration failed. Error: {e}")
            # If there's an error in sending email or any other exception occurs, remove the user data from the list
            self.user_repository.users.pop()
            print("User data not saved to JSON file due to registration or email sending error.")


# Example usage
if __name__ == "__main__":
    # Create instances of the classes
    user_repository = UserRepository()
    email_sender = EmailSender(smtp_server='smtp.gmail.com',
                               smtp_port=587,
                               sender_email='rockstaraks43@gmail.com',
                               sender_password='fahl jeqk kfsb jcdu')  # Use the correct password here

    registration_service = RegistrationService(user_repository, email_sender)

    # Example user data
    user_data = {'username': 'Akhilesh12', 'email': 'akkirads54321@gmail.com'}

    # Register the user and send email
    registration_service.register_user(user_data)

















"""
Save data into sqlite3

class UserRepository:
    def __init__(self, db_path=':memory:'):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                               (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                username TEXT, 
                                email TEXT)''')
        self.connection.commit()

    def register_user(self, user_data):
        self.cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)",
                            (user_data['username'], user_data['email']))
        self.connection.commit()


"""