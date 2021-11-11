from uuid import getnode

# Strip off hex character from front
mac = hex(getnode())[2:].upper()

# Add semi-colons every two characters
mac = ':'.join(mac[i:i+2] for i in range(0, len(mac), 2))