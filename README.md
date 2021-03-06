# thunder-panthers

Introducing...the broken telephone version of comic strips. User will enter four phrases which will be turned into two comic strips. Firstly, the phrases will be incorporated into a 2x2 comic strip with images generated from the words entered. Most importantly, a second comic strip will be created with a “broken telephone” version of the original phrase with relevant images. Funnies can be saved to the “Best Humor” page.

<p align="center">
<img src="http://i64.tinypic.com/jl2u6c.jpg">
</p>

## Instructions
You need:
1. the requests library and a virtual environment
2. your own API keys
3. a sense of humor

Follow the code to get requests and a virtualenv.
```bash
$ virtualenv venv
$ . venv/bin/activate
$ pip install requests
```
Next, you will need to procure your own API key for TextRazor to run within the program.

visit: https://www.textrazor.com/signup

Copy the API Key as it appears in the grey box once you sign up, and then paste it within the form on our Home page. An example is shown below:

***
<p align="center">
<img src="http://i63.tinypic.com/2j35l3r.png">
</p>

***

You will also need an API key for Yandex Translate.

visit: https://translate.yandex.com/developers/keys

Sign in and click "Create a new key" and copy the API key given onto the homepage as well.

***

Finally, you will need the API key for Getty Images.

visit: https://developer.gettyimages.com/member/register

Register for an account and the key will be emailed to you. Do not use the secret key. Copy that API key into our homepage.
