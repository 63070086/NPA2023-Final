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
                        <ip>172.30.86.1</ip>
                        <netmask>255.255.255.0</netmask>
                    </address>
                </ipv4>
            </interface>
        </interfaces>
    </config>
    """

    netconf_filter = """
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>Loopback63070086</name>
            </interface>
        </interfaces>
    </filter>
    """
    try:
        # Retrieve the interface configuration
        netconf_reply = m.get_config(source="running", filter=netconf_filter)
        xml_data = netconf_reply.xml
        print(xml_data)

        # Check if the interface already exists
        if '<ok/>' in xml_data:
            return "Interface loopback 63070086 already exists"
        else:
            # Create the interface if it does not exist
            netconf_reply_create = netconf_edit_config(netconf_config)
            xml_data_create = netconf_reply_create.xml
            print(xml_data_create)
            if '<ok/>' in xml_data_create:
                return "Interface loopback 63070086 is created successfully"
    except Exception as e:
        print("Error:", e)

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
    netconf_filter = """
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>Loopback63070086</name>
            </interface>
        </interfaces>
    </filter>
    """
    try:
        netconf_reply = m.get_config(source="running", filter=netconf_filter)
        xml_data = netconf_reply.xml
        print(xml_data)
        if '<ok/>' in xml_data:
            if '<enabled>true</enabled>' in xml_data:
                return "Interface loopback 63070086 is up"
            else:
                return "Interface loopback 63070086 is down"
        else:
            return "Interface loopback 63070086 not found"
    except Exception as e:
        print("Error:", e)

