import socket
import common_ports
import ipaddress

def get_open_ports(target, port_range, verbose=False):
    """
    >>> get_open_ports("scanme.nmap", [22, 42], False)
    'Error: Invalid hostname'
    >>> get_open_ports("266.255.9.10", [22, 42], False)
    'Error: Invalid IP address'
    >>> get_open_ports("209.216.230.240", [440, 445], False)
    [443]
    >>> get_open_ports("www.stackoverflow.com", [79, 82], False)
    [80]
    >>> get_open_ports("scanme.nmap.org", [20, 80], False)
    [22]
    >>> get_open_ports("104.26.10.78", [440, 450], True)
    >>> get_open_ports("137.74.187.104", [440, 450], True)
    >>> get_open_ports("scanme.nmap.org", [20, 80], True)
    """

    open_ports = []

    # Is target IP address or Hostname
    target_ip = ""
    target_host = ""

    # Check if target is IP address
    arr = target.split(".")
    vald = False
    if (len(arr) == 4 ):
        vald = True
        for ii in arr:
            if ( vald and not str(ii).isdigit() ):
                vald = False

    if vald:
        # target is an IP address. Lets see if it is a valid IP.
        try:
            _ = ipaddress.ip_address(target)
            # If we are here, target is a valid IP address.
            target_ip = target
        except ValueError:
            return "Error: Invalid IP address"

        try:
            target_host = socket.gethostbyaddr(target)[0]
        except:
            target_host = ""    # Unknown Target Host. Keep it empty.
    else:
        # target is a host name.
        try:
            target_ip = socket.gethostbyname(target)
            target_host = target
        except:
            # host name is invalid
            return "Error: Invalid hostname"

    # The 'with' statement clarifies code that previously would use try...finally blocks to 
    # ensure that clean-up code is executed. Works on object that supports the context management 
    # protocol (that is, has __enter__() and __exit__() methods. 

    socket.setdefaulttimeout(.2)
    #
    for p in range(port_range[0], port_range[1] + 1):
        #print(f"Processing Port {p}")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:            
            result = s.connect_ex((target, p))
            if result == 0:
                open_ports.append(p)
    
    if verbose:
        mesg = ""
        if (target_host == ""):
            mesg = f"Open ports for {target_ip}\n"
        else:
            mesg = f"Open ports for {target_host} ({target_ip})\n"
        
        mesg += f"PORT     SERVICE\n"
        for p in open_ports:
            pt = common_ports.ports_and_services[p]
            filler = " " * (9-len(str(p)))
            mesg += f"{p}{filler}{pt}\n"
        
        #print(mesg.rstrip("\n"))
        return mesg.rstrip("\n")    # delete the trailing \n

    return(open_ports)


if __name__ == "__main__":
    import doctest  # See https://docs.python.org/3/library/doctest.html
    doctest.testmod(verbose=False)  