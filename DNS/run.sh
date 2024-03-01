docker run -it --rm -v ./dnsmasq.conf:/etc/dnsmasq.conf -p 53:53/udp -p 53:53/tcp --cap-add=NET_ADMIN dockurr/dnsmasq
