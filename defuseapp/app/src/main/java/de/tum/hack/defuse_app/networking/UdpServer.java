package de.tum.hack.defuse_app.networking;

import android.util.Log;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;

public class UdpServer extends Thread{

    private static final int PORT = 5003;
    DatagramSocket socket;
    ServerResponseHandler handler;

    boolean running;

    public UdpServer(ServerResponseHandler response) {
        super();
        this.handler = response;
    }

    public void setRunning(boolean running){
        this.running = running;
    }

    @Override
    public void run() {

        running = true;

        try {
            socket = new DatagramSocket(PORT);

            Log.e("defuse", "UDP Server is running");

            while(running){
                byte[] buf = new byte[256];

                // receive request
                DatagramPacket packet = new DatagramPacket(buf, buf.length);
                socket.receive(packet);     //this code block the program flow

                // send the response to the client at "address" and "port"
                String message = new String(packet.getData()).trim();
                this.handler.handle(message);
                Log.i("defuse", message);
            }
            Log.e("defuse", "UDP Server ended");
        } catch (SocketException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if(socket != null){
                socket.close();
                Log.e("defuse", "socket.close()");
            }
        }
    }
}
