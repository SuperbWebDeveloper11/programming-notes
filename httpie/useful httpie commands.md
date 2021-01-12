
## make post request with basic authentication:
    http -a samir -f POST localhost:8000/blog323/  title='new title' body='post body'

## obtain auth token:
    http POST localhost:8000/obtain-auth-token/ username='...' password='...'
    {
        "email": "...",
        "token": "...",
        "user_id": ...
    }

## make post request with token authentication:
    http -f POST localhost:8000/blog323/ 'Authorization: Token ...' title='...' body='...'

### response whene invalide token :
    {
        "detail": "Invalid token."
    }

### response when authentication credentials were not provided."
    {
        "detail": "Authentication credentials were not provided."
    }

