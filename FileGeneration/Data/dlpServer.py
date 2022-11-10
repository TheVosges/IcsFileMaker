import ftplib
import os

FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser"
FTP_PASS = "rNrKYTX9g7z3RgJRmxWuGHbeu"


class FTPServerConnection:

    def __init__(self):
        self.ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
        self.ftp.encoding = "utf-8"
        print(self.ftp.port)

    def upload_file(self, filename):
        # Read file in binary mode
        print()
        with open(os.getcwd() + "/FileGeneration/Data/" + filename, "rb") as file:
            # Command for Uploading the file "STOR filename"
            self.ftp.storbinary(f"STOR {filename}", file)

    def list_files(self):
        # list current files & directories
        self.ftp.dir()

    def get_file(self, filename, showData=False):
        # Write file in binary mode
        filenameFixed = "Downloaded_" + filename
        with open(filenameFixed, "wb") as file:
            # Command for Downloading the file "RETR filename"
            self.ftp.retrbinary(f"RETR {filename}", file.write)
        if (showData):
            show_file_conent(filenameFixed)
        return "Downloaded_" + filename

    def show_file_conent(filename):
        # Display the content of downloaded file
        file = open(filename, "r")
        print('File Content:', file.read())

    def close_server(self):
        self.ftp.quit()


if __name__ == "__main__":
    ftpServer = FTPServerConnection()
    # ftpServer.upload_file("drugCalendar.ics")
    ftpServer.list_files()
    # filename = get_file("drugCalendar.ics", showData= True)
    ftpServer.close_server()
