package de.tum.hack.defuse_app.networking;

import android.app.Service;
import android.util.Log;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import android.content.Intent;
import android.os.IBinder;

@Deprecated
public class UdpService extends Service {

    private static final int PORT = 5003;

    DatagramSocket socket;

    private void listen() throws Exception {
        byte[] recvBuf = new byte[15000];
        if (socket == null || socket.isClosed()) {
            socket = new DatagramSocket(PORT, NetworkHelper.getIPAddress());
            socket.setBroadcast(true);
        }
        DatagramPacket packet = new DatagramPacket(recvBuf, recvBuf.length);
        socket.receive(packet);

        String senderIP = packet.getAddress().getHostAddress();
        String message = new String(packet.getData()).trim();

        Log.i("UDP", "Got UDB broadcast from " + senderIP + ", message: " + message);
    }

    @Override
    public void onCreate() {
        Log.i("Test", "test");
    }

    @Override
    public void onDestroy() {
        socket.close();
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        new Thread(new Runnable() {
            public void run() {
                try {
                    listen();
                } catch (Exception e) {
                    Log.i("UDP", "no longer listening for UDP broadcasts cause of error " + e.getMessage());
                }
            }
        }).start();
        return 1;
    }

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}
