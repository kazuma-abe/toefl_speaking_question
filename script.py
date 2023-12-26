import smtplib
from email.mime.text import MIMEText
from openai import ChatCompletion, OpenAIAPIError

openai.api_key = 'OPENAI_API_KEY'
model = "text-davinci-003"

# generate question
def ask_question(prompt):
    try:
        response = openai.Completion.create(
          engine=model,
          prompt=prompt,
          max_tokens=100
        )
        return response.choices[0].text.strip()
    except OpenAIAPIError as e:
        print(f"Error interacting with ChatGPT: {e}")
        return "ChatGPT interaction error"

# send mail
def send_email(subject, body, to_email):
    from_email = 'EMAIL'
    password = 'EMAIL_PASSWORD'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

# main
def main():
    question = "I would like you to make a sample problem and answer of an independent task of the speaking section of the TOEFL test. The model answer should be approx. 60 sec. and 120 words. "
    answer = ask_question(question)

    subject = "Daily ChatGPT Update"
    body = f"Question: {question}\nAnswer: {answer}"

    send_email(subject, body, 'email@example.com')

if __name__ == "__main__":
    main()
