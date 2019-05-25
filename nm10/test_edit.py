
from ncclient import manager
import logging

CREATE_INTERFACE_IP = """
    <config>
        <cli-config-data>
            <cmd>interface %s</cmd>
            <cmd>ip address %s %s</cmd>
            <cmd>no shutdown</cmd>
        </cli-config-data>
    </config>
"""


def create_interface_ip(conn, interface, ip, mask):
    try:
        config_str = CREATE_INTERFACE_IP % (interface, ip, mask)
        rpc_sent = conn.edit_config(target='running', config=config_str)
    except Exception:
        print('Exception occurs while creating interface %s' % interface)


#netconf connection to router
def r_connect(host,port,user,password,):
    return manager.connect(host=host,
                           port=port,
                           username=user,
                           password=password,
                           device_params={'name': 'csr'})

# Test the code here
with r_connect('192.168.100.11.','22','simran','lab') as m:
        logging.basicConfig(level=logging.DEBUG)
        create_interface_ip(m, "Loopback99", '10.1.1.1', '255.255.255.0')
