from ncclient import manager
import xmltodict

m = manager.connect(
    host="10.0.15.189",
    port=830,
    username="admin",
    password="cisco",
    hostkey_verify=False
    )

def create():
    netconf_config = """
    <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>Loopback63070086</name>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
                <enabled>true</enabled>
                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                    <address>
                        <ip>172.30.086.1</ip>
                        <netmask>255.255.255.0</netmask>
                    </address>
                </ipv4>
            </interface>
        </interfaces>
    </config>
    """
    try:
        netconf_reply = netconf_edit_config(netconf_config)
        xml_data = netconf_reply.xml
        print(xml_data)
        if '<ok/>' in xml_data:
            return "Interface loopback 63070086 is created successfully"
    except:
        print("Error!")

def delete():
    netconf_config = """
    <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface operation="delete">
                <name>Loopback63070086</name>
            </interface>
        </interfaces>
    </config>
    """

    try:
        netconf_reply = netconf_edit_config(netconf_config)
        xml_data = netconf_reply.xml
        print(xml_data)
        if '<ok/>' in xml_data:
            return "Interface loopback 63070086 is deleted successfully"
    except:
        print("Error!")

def enable():
    netconf_config = """<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>Loopback63070086</name>
                <enabled>true</enabled>
            </interface>
        </interfaces>
    </config>"""

    try:
        netconf_reply = netconf_edit_config(netconf_config)
        xml_data = netconf_reply.xml
        print(xml_data)
        if '<ok/>' in xml_data:
            return "Interface loopback 63070086 is enabled successfully"
    except:
        print("Error!")

def disable():
    netconf_config = """<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>Loopback63070086</name>
                <enabled>false</enabled>
            </interface>
        </interfaces>
    </config>
    """

    try:
        netconf_reply = netconf_edit_config(netconf_config)
        xml_data = netconf_reply.xml
        print(xml_data)
        if '<ok/>' in xml_data:
            return "Interface loopback 63070086 is shutdowned successfully"
    except:
        print("Error!")

def netconf_edit_config(netconf_config):
    return  m.edit_config(target="running", config=netconf_config)

def status():
    netconf_filter = """<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>Loopback63070086</name>
            </interface>
        </interfaces>
    </filter>"""

    try:
        # Use Netconf operational operation to get interfaces-state information
        netconf_reply = m.get_config(filter=netconf_filter)
        print(netconf_reply)
        netconf_reply_dict = xmltodict.pars(netconf_reply.xml)['data']['interfaces']['interface']

        # if there data return from netconf_reply_dict is not null, the operation-state of interface loopback is returned
        if netconf_reply_dict is not None:
            # extract admin_status and oper_status from netconf_reply_dict
            admin_status = netconf_reply_dict.get('admin-status')
            oper_status = netconf_reply_dict.get('oper-status')
            if admin_status == 'up' and oper_status == 'up':
                return "Interface loopback 63070086 is enabled"
            elif admin_status == 'down' and oper_status == 'down':
                return "<!!!REPLACEME with proper message!!!>"
        else: # no operation-state data
            return "No Interface loopback 63070086"
    except:
       print("Error!")
