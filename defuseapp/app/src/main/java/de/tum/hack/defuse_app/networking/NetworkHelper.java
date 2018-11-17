package de.tum.hack.defuse_app.networking;

import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.UnknownHostException;
import java.util.Collections;
import java.util.List;

public class NetworkHelper {
    public static InetAddress getIPAddress() {
        try {
            List<NetworkInterface> interfaces = Collections.list(NetworkInterface.getNetworkInterfaces());
            for (NetworkInterface intf : interfaces) {
                List<InetAddress> addrs = Collections.list(intf.getInetAddresses());
                for (InetAddress addr : addrs) {
                    if (!addr.isLoopbackAddress() && addr.getHostAddress().indexOf(':') < 0) {
                        return addr;
                    }
                }
            }
        } catch (Exception ignored) { } // for now eat exceptions
        return null;
    }

    public static InetAddress getBroadcastAddress() {
        try {
            return InetAddress.getByName("131.159.223.255");
        } catch (UnknownHostException e) {
            e.printStackTrace();
            return null;
        }
    }
}
