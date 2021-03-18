
## i don't use curl anymore --> i moved to the beautiful 'httpie'

source : "Everything curl by Daniel Stenberg""

cURL project make two products:
- curl: the command-line tool
- libcurl: the transfer library with a C API

curl support both short and long command line options
short options example :  curl -vL http://example.com
long options example : curl --verbose --location http://example.com

curl --data arbitrary http://example.com (send arguments)
curl --no-verbose http://example.com (Negative option)
curl --location http://example.com/1 --next
       --data sendthis http://example.com/2 --next
       --head http://example.com/3 (Separate options per URL)
curl -K cmdline.txt http://example.com (read options from cmdline.txt)
curl -u alice:12345 http://example.com/ (request a page requiring HTTP authentication)
curl -u alice http://example.com/  (curl will instead prompt the user for the password - for more security specially whene you work on multi-user systems)
curl http://example.com/   (outputtig data to stdout )
curl -o http://example.com/file.txt   (or --output  / download the URL then save it  using the name provided by the server)
curl -o output.html http://example.com/   (or --output  / download the URL then save it / you could choose the output path)
curl http://example.com/ > example.html (redirect stdout to a file with > filename makes the use of -o or -O superfluous)
curl http://example.com > files.html 2>errors  (The stdout stream is for the data while stderr is metadata and errors)
curl --compressed http://example.com/   (With this option enabled and if the server support it will delivers the data in a compressed way and curl will decompress it before saving it or sending it to stdout)
curl https://example.com/ --limit-rate 200K ( curl use as much bandwidth as possible but to make it not download data any faster than 200 kilobytes per second do so - you could use K, M and G -)
curl --max-filesize 100000 https://example.com/  (figure out the size before the transfer starts and abort before trying to download)

# uploding data using the HTTP protocol :
- POST : 
It usually sends a chunk of relatively small amounts of data to the receiver (using -d or --data options)
- multipart formpost :
typically used when there's a file upload involved. This type of upload is also an HTTP POST but it sends the data formatted according to some special rules (using -F or --......... options)
- PUT :
a sort of upload that was designed to send a complete resource that is meant to be put as-is on the remote site or replace an existing resource there, some web servers don't even have PUT enabled (using -T or --......... options)

# sending data to an SMTP server:
curl smtp://mail.example.com 
       --mail-from myself@example.com 
       --mail-rcpt receiver@example.com  
       --upload-file email.txt
------------------------  email.txt  ------------------------
From: John Smith <john@example.com>
To: Joe Smith <smith@example.com>
Subject: an example.com example email
Date: Mon, 7 Nov 2016 08:45:16

Dear Joe,
Welcome to this example email. What a lovely day.
------------------------------------------------------------
( suggest curl to speak SMTP securely over TLS )
curl --ssl 
       smtp://mail.example.com 
       --mail-from myself@example.com 
       --mail-rcpt receiver@example.com  
       --upload-file email.txt
( make sure the email transfer is done securely )
curl --ssl -reqd
       smtp://mail.example.com 
       --mail-from myself@example.com 
       --mail-rcpt receiver@example.com  
       --upload-file email.txt

# TLS and SSL :
( TLS defenition )
TLS stands for Transport Layer Security and is the name for the technology that was formerly called SSL.
TLS is a cryptographic security layer "on top" of TCP that makes the data tamper proof and guarantees server authenticity, based on strong public key cryptography and digital signatures.
( curl and TLS server negotiation)
When curl connections to a TLS server, it negotiates how to speak the protocol and that negotiation involves several parameters and variables that both parties need to agree to, like cryptography algorithms (cipher) and TLS version - use -v option to get thos informations.
( more info in the book ... )

( Size of an HTTP response )
An HTTP response has a certain size and curl needs to figure it out. There are several different ways to signal the end of an HTTP response but the most basic way is to use the Content-Length: header in the response and with that specify the exact number of bytes in the response body.

( HTTP response codes )
- The response code is the server's way of giving the client a hint about how the request was handled.
- curl does not consider it an error even if the response code would indicate that the requested document couldn't  be delivered (or similar), instead curl considers a successful sending and receiving of HTTP to be good.
- The first digit of the HTTP response code is a kind of 'error class':
- 1xx: transient response, more is coming
- 2xx: success
- 3xx: a redirect
- 4xx: the client asked for something the server couldn't/wouldn't deliver
- 5xx: there's problem in the server

( Chunked transfer encoding )
- An HTTP 1.1 server can decide to respond with a "chunked" encoded response, a feature that wasn't present in HTTP 1.0.
- When sending a chunked response, there's no Content-Length: for the response to indicate its size. Instead, there's a Transfer-Encoding: chunked header that tells curl there's chunked data coming and then in the response body, the data comes in a series of "chunks". Every
individual chunk starts with the size of that particular chunk (in hexadecimal), then a newline and then the contents of the chunk. This is repeated over and over until the end of the response, which is signalled with a zero sized chunk. The point of this sort of response is for
the client to be able to figure out when the responses has ended even though the server didn't know the full size before it started to send it. - This is usually the case when the response is dynamic and generated at the point when the request comes.
- Clients like curl will, of course, decode the chunks and not show the chunk sizes to users -

( Gzipped transfers )
- Responses over HTTP can be sent in compressed format. This is most commonly done by the server when it includes a Content-Encoding: gzip in the response as a hint to the client.
- Compressed responses make a lot of sense when either static resources are sent (that were compressed at a previous moment in time) or even in run-time when there's more CPU power available than bandwidth. 
- You can ask curl to both ask for compressed content and automatically and transparently uncompress gzipped data when receiving content encoded gzip (or in fact any other compression algorithm that curl understands) by using --compressed :
curl --compressed http://example.com/

( HTTP POST)
When the data is sent by a browser after data have been filled in a form, it will send it "URL
encoded", as a serialized name=value pairs separated with ampersand symbols ('&').
curl -d name=admin&shoesize=12 http://example.com/
curl -d name=admin -d shoesize=12 http://example.com/
curl -d @filename http://example.com
- POSTing with curl's -d option will make it include a default header that looks like :
'Content-Type: application/x-www-form-urlencoded'
curl -d '{json}' -H 'Content-Type: application/json' https://example.com
- As an example, you could POST a name to have it encoded by curl:
curl --data-urlencode 'name=John Doe (Junior)' http://example.com
which would send the following data in the actual request body:
name=John%20Doe%20%28Junior%29
........................... useful informations in the book

( HTTP multipart formposts )
- The default enctype used by forms, which is rarely spelled out in HTML since it is default, is application/x-www-form-urlencoded . It makes the browser "URL encode" the input as name=value pairs with the data encoded to avoid unsafe character.
- A multipart formpost is what an HTTP client sends when an HTML form is submitted with enctype set to 'multipart/form-data'.
- It is an HTTP POST request sent with the request body specially formatted as a series of "parts", separated with MIME boundaries.

curl -F person=anonymous -F secret=@file.txt http://example.com/submit.cgi ( -F or --form )
curl -F 'name=Dan' -H 'Content-Type: multipart/magic' https://example.com ( change Content-Type header )


# examples :
curl -u nabil -d '{"title":"first post", "body":"post body"}' -H 'Content-Type: application/json' localhost:8000/blog323/
curl -d '{"username":"nabil", "password":"00000000"}' -H 'Content-Type: application/json' localhost:8000/obtain-auth-token/
 {"token":"5c2847279d4c12916df77dcfa58360691590f6a2"}
curl -d '{"title":"fifth post", "body":"post body"}' -H 'Content-Type: application/json' localhost:8000/blog323/
curl -d '{"title":"first post", "body":"post body"}' -H 'Authorization: Token 5c2847279d4c12916df77dcfa58360691590f6a2; Content-Type: application/json' localhost:8000/blgo323/ 


