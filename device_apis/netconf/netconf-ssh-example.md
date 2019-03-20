# Example NETCONF Flow over SSH

1. Open SSH Connection

    ```bash
    ssh -oHostKeyAlgorithms=+ssh-dss root@ios-xe-mgmt.cisco.com -p 10000 -s netconf
    ```

1. Send Password

    ```bash
    D_Vay!_10&
    ```

1. Receive agent `<hello>`.

1. Send manager `<hello>`

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
     <hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
     <capabilities>
       <capability>urn:ietf:params:netconf:base:1.0</capability>
     </capabilities>
       </hello>]]>]]>
    ```

    * _Note: There will be **NO** response from device._

1. End connection with `<close-session>`

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <rpc message-id="1239123" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <close-session />
    </rpc>
    ]]>]]>
    ```

1. Receive `<rpc-reply>` from agent.  Notice how the `message-id` matches your sent value. 
