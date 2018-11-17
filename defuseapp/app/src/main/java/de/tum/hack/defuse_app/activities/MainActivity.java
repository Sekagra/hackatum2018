package de.tum.hack.defuse_app.activities;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

import java.io.IOException;

import de.tum.hack.defuse_app.R;
import de.tum.hack.defuse_app.model.Code;
import de.tum.hack.defuse_app.networking.ServerResponseHandler;
import de.tum.hack.defuse_app.networking.UdpClient;
import de.tum.hack.defuse_app.networking.UdpServer;

public class MainActivity extends AppCompatActivity implements ServerResponseHandler {

    UdpServer udpServer;
    boolean serverIsLaunched;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    protected void onStart() {
        if(!serverIsLaunched) {
            udpServer = new UdpServer(this);
            udpServer.start();
            this.serverIsLaunched = true;
        }
        super.onStart();
    }

    public void onStartClick(View v) {
        UdpClient.send("{ \"cmd\": \"start\", \"speed\": 60 }");
        startActivity(new Intent(this, DefuseSequenceActivity.class));
    }

    @Override
    public void handle(String message) {
        // on 'stop' from the raspi, lose game
        if(message.contains("explode")) {
            udpServer.interrupt();
            Intent i = new Intent(this, WrongActivity.class);
            i.putExtra("errorCount", Code.MAX_ERRORS);
            startActivity(i);
        }
    }
}
