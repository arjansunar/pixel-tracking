## Email tracking with Pixel

A transparent pixel image is embedded within the body of the email payload / site.
This image's `src` attribute is prefixed with a tracking code that is created before
email is sent. This tracking code identifies that particular pixel and that email.

Later when the email/site is opened, the tracking code is used to identify the Pixel
and log user details along with `is_opened` status.

### Demo
[Screencast from 2024-08-29 10-34-43.webm](https://github.com/user-attachments/assets/5d8a74f0-1dc7-418a-9f1b-2bc4459da483)
