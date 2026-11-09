import ipaddress

def hitung_subnet(ip):
    jaringan = ipaddress.ip_interface(ip)
    subnet = jaringan.network

    hasil = {
        "IP Address": jaringan.ip,
        "Subnet Mask": subnet.netmask,
        "Network": subnet.network_address,
        "Broadcast": subnet.broadcast_address,
        "Jumlah Host": max(0, subnet.num_addresses - 2)
    }

    return hasil