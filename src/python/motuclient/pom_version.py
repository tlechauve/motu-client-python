from xml.etree import ElementTree

def getPOMVersion():
    version="Unknown"
    try:
        # For production tree
        version = __getPOMVersion("pom.xml")
    except:
        # For development tree
        version = __getPOMVersion("../../pom.xml")
    return version
    
def __getPOMVersion(POM_FILE):
    namespaces = {'xmlns' : 'http://maven.apache.org/POM/4.0.0'}
    tree = ElementTree.parse(POM_FILE)
    root = tree.getroot()
    version = root.find("xmlns:version", namespaces=namespaces)
    return str(version.text)