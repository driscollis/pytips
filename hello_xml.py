import xml.etree.ElementTree as xml

def create_xml(filename):
    """
    Create an example XML file
    """
    root = xml.Element("Appointments")
    appt = xml.Element("subAppointment")
    root.append(appt)
    
    # add appointment children
    begin = xml.SubElement(appt, "begin")
    begin.text = "1181251680"
    
    tree = xml.ElementTree(root)
    with open(filename, "wb") as fh:
        tree.write(fh)

if __name__ == "__main__":
    create_xml("appt.xml")