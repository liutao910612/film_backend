from django.core.mail import send_mail


class CommonUtils:
    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


class EmailUtils:
    def send_email(subject, message, from_email, to_email):
        send_mail(
            subject,
            message,
            from_email,
            [to_email],
        )
