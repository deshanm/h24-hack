
# Local Development

- makesure you use python env 3.9

if you use conda
```
 conda create -n py3.9  python=3.9  
 conda activate py3.9
```

- Now install packages - `pip install -r requirements.txt`

# Run Docker File Locally

```
docker build -t backend-api . 
docker run -p 7005:7005  backend-api 
```


# Server
Whenver, you merge something into the main branch, it will trigger the Github Action. Check details in .github/workflows

## Docs that used
- Variables and Secrets are in the github 
https://github.com/deshanm/site-audit/settings/secrets/actions

- Followed this to install the docker on ubuntu
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04

- Followed this to install nginx on ubuntu
https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-22-04

- Followed this to certbot  on ubuntu
https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-22-04

## Debug

Login to server
```
ssh [username]@[server-ip]
```


check running instances
```
docker ps
```

Check logs
```
docker logs --since=1h <container_id>
```

nginx config file path
```
vim /etc/nginx/sites-available/api.reviewmysites.com
```