<img src="../../img/logo.png" alt="Chmurowisko logo" width="200" align="right">
<br><br>
<br><br>
<br><br>

# Creating CloudFront Distribution

## LAB Overview

#### This guide introduces you to Amazon CloudFront. In this lab you will create an Amazon CloudFront distribution that will use a CloudFront domain name in the url to distribute a publicly accessible image file stored in an Amazon S3 bucket. 

## Task 1: Creating an Amazon CloudFront Web Distribution
Now you will create an Amazon CloudFront web distribution that distributes the file stored in the publicly accessible Amazon S3 bucket.

1. In the AWS Management Console homepage, click on **Services** at the top of the console and then click **CloudFront** to open the Amazon CloudFront console.
2. Click **Create Distribution**.
3. On the **Select a delivery method for your content** page, in the **Web** section, click **Get Started** to select Web as the delivery method.
4. On the next page, click in the **Origin Domain Name** box and select your Amazon S3 bucket that contains a publicly accessible image that you want to distribute ([csa03-studentX-2.s3.amazonaws.com](http://csa03-studentX-2.s3.amazonaws.com)).
5. Accept the default values for the rest of the parameters on this page, and click **Create Distribution**.

The **Status** column shows **In Progress** for your distribution on the next page. After Amazon CloudFront has created your distribution, the value of the **Status**  column for your distribution will change to **Deployed** and it will then be ready to process requests. This should take around 15-20 minutes.

The domain name that Amazon CloudFront assigns to your distribution appears in the list of distributions. It will normally look something like "dm2afjy05tegj.cloudfront.net." (It also appears on the **General** tab for a selected distribution.)

## Task 2: Using the Amazon CloudFront Web Distribution

Amazon CloudFront now knows where your Amazon S3 origin server is, and you know the domain name associated with the distribution. You can create a link to your Amazon S3 bucket content with that domain name, and have Amazon CloudFront serve it.

6. Copy the following HTML into a new text file, or use [this file](mypage.html):

```html
<html>
<head>This is my image from CloudFront</head>
<body>
<p>My text content goes here.</p>
<p><img src="http://<domain name>/<object name>" alt="my test image" /></p>
</body>
</html>
```

7. Replace <domain name> with the domain name that Amazon CloudFront assigned to your distribution.
8. Replace <object name> with the name one of images files you store in your Amazon S3 bucket.
9. Save the text in a file that has an .html filename extension (i.e. “mypage.html").
10. Open the web page you just created in a browser to ensure that you can see your content.

The browser returns your page with the embedded image file, served from the edge location that Amazon CloudFront determined was appropriate to serve the object.

## END LAB

This is the end of the CloudFront LAB. 

<br><br>

<center><p>&copy; 2019 Chmurowisko Sp. z o.o.<p></center>