import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, username, password, attachment_path=None):
    # Crear el objeto de mensajería
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Agregar el cuerpo del mensaje
    msg.attach(MIMEText(body, 'plain'))

    # Agregar archivo adjunto si se proporciona
    if attachment_path:
        try:
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={attachment_path.split("/")[-1]}')
                msg.attach(part)
        except Exception as e:
            print(f"Error al adjuntar el archivo: {e}")

    # Conectar con el servidor SMTP del proveedor de correo
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Usar TLS para cifrar la conexión
        server.login(username, password)  # Iniciar sesión en el servidor de correo

        # Enviar el correo
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Correo enviado con éxito.")
    except Exception as e:
        print(f"Error al enviar correo: {e}")

# Ejemplo de uso
send_email(
    subject='Asunto del correo',
    body='Cuerpo del correo',
    to_email='melphisdejesusp@gmail.com',
    from_email='ventas@melgraph.com',
    smtp_server='mail.melgraph.com',
    smtp_port=587,
    username='ventas@melgraph.com',
    password='Mel$$"852964941@grap!',
    attachment_path='C:/Users/MELGRAPH01/Downloads/Diagrama.pdf'  # Reemplaza con la ruta a tu archivo
)
