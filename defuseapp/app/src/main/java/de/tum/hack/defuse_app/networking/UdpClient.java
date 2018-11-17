package de.tum.hack.defuse_app.networking;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;

public class UdpClient {
    public static void send(String data) {
        // UDP client test
        Thread task = new Thread(() -> {
            int port = 5001;
            DatagramSocket socket = null;
            try {
                socket = new DatagramSocket(port);
                InetAddress ipAddress =  InetAddress.getByName("192.168.2.1");

                DatagramPacket sendData = new DatagramPacket(data.getBytes(), data.getBytes().length, ipAddress, port);
                socket.send(sendData);
                socket.close();
            } catch (SocketException e) {
                e.printStackTrace();
            } catch (UnknownHostException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }
        });
        task.start();
    }
}
