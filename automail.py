import yagmail
import os
import time
import datetime

receiver = "someone@gmail.com"  # receiver email address
body = "Attendence File"  # email body
ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
filename = "Attendance"+os.sep+"Attendance_"+date+".csv"  # attach the file
# mail information
yag = yagmail.SMTP("sender@gmail.com", "password")
# sent the mail
yag.send(
    to=receiver,
    subject="Attendance Report",  # email subject
    contents=body,  # email body
    attachments=filename,  # file attached
)