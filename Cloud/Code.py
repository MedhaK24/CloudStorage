token = 'sl.BPrUvx7xE1qsWmttmZbhwy2oV9o46xrxOz8TfDRKJMVlCibR-NnnKjriqKRA8MDDPZWpgOwZnmNd-hOmBK4fVyO2yMPw3Fs16SjjftJNT3z-txesIYZQsn-9vfNWQrLPNhkLwanXUKM'
import dropbox
dbx = dropbox.Dropbox(token)
filepath = '/Users/mk24/Downloads/COUNTRY_FLAGS0500-removebg-preview.png'
f=open(filepath,'rb')
dbx.files_upload(f.read(),'/MedhaCloud/img.png')