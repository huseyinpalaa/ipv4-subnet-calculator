# Author by Huseyin Pala

import ipaddress

print("IPv4-Subnet-Calculator".center(50,"*"))
print()

print("IP Adresini giriniz (örneğin '192.168.1.0')")
ip_adresi = input("IP ADRES: ")

print("Prefix degerini giriniz (örneğin '24' )")
alt_ag_maslasi = int(input("Prefix Değeri: "))

cidr = (f"{ip_adresi}/{alt_ag_maslasi}") # Sınıfsız

network = ipaddress.IPv4Network(cidr, strict=False)

print(f"IP Adresi: {network.network_address}")
print()
print(f"Subnet Maskesi: {network.netmask}")
print()
print(f"Broadcast(Genel Yayın) Adresi: {network.broadcast_address}")
print()
print(f"İlk Kullanılabilir Adres: {network.network_address + 1}")
print()
print(f"Son Kullanılabilir Adres: {network.broadcast_address - 1}")
print()
print(f"Toplam IP Adres Sayısı: {network.num_addresses}")


