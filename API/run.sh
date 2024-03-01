docker run -ti --init --rm --name server -v .:/code -p 443:443 --cap-add=NET_ADMIN nike-server
