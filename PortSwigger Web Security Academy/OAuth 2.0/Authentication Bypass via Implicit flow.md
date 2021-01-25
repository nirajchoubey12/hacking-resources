With this lab we learn about inherent security implications of using implicit grant type for an application where tokens are passed to the client which subsequently uses that for login the user to the application

Flow of the lab is like this:

1. Click on login with social media
2. This will trigger a authorize request to the authorization server: https://acd41f2a1e7fa13f8095024a02e5002e.web-security-academy.net/auth?client_id=<client_id>&redirect_uri=<redirect_uri>&response_type=token&nonce=894724906&scope=openid%20profile%20email
3. After this we are taken to social media signin page. We would enter the creds as wiener/peter and click on sign-in.
4. Wiener logged in to the authorization server and get a Authorize page. requesting the access to profile and email. If you notice the url we are still interacting with authorization server
5. Click on Authorize. This triggers a multiple back and forth request where authorization server sends the token to the client and client uses that token to log the user in
6. Request to authenticate the user using the token(**this is where vulnerability is**). 
```
POST /authenticate HTTP/1.1
Host: ac4b1f611e36a1d2807c027700f90049.web-security-academy.net
Connection: close
Content-Length: 103
Accept: application/json
Content-Type: application/json
Origin: https://ac4b1f611e36a1d2807c027700f90049.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://ac4b1f611e36a1d2807c027700f90049.web-security-academy.net/oauth-callback
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: session=0hvjvGdwD7YRSgtQ7xXqODSewMnzZ9xF

{"email":"wiener@hotdog.com","username":"wiener","token":"XKONneZF-Ecm9-f4wfn-JnPZRIXzM0DZ1S6NhJpNvc0"}
```
7. Application *does not matches the access token angainst the username and email*. So changing the email to **carlos@carlos-montoya.net** and username to carlos. logs us in as carlos
