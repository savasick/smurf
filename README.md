# Smurf attack

This Python script is designed to execute a **Smurf attack**, a type of Denial-of-Service (DoS) attack that inundates a specified target IP address with numerous ICMP echo request packets. The script utilizes sIP spoofing to mask the source IP address of the packets, making it more challenging to trace the attack back to its origin. 

The Smurf attack exploits the behavior of devices on a network that respond to ICMP echo requests sent to a broadcast address. By sending these requests with a forged source IP address (the victim's IP), all devices on the network will respond to the victim, overwhelming it with traffic. 

### install

```bash
git clone https://github.com/savasick/smurf.git
cd smurf
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### usage

send to 192.168.5.110-IP
```bash
sudo python smurf.py 192.168.5.110
```