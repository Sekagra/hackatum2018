package de.tum.hack.defuse_app.activities;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import java.io.IOException;

import de.tum.hack.defuse_app.helper.AudioHelper;
import de.tum.hack.defuse_app.R;
import de.tum.hack.defuse_app.networking.UdpClient;

public class WinActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_win);

        AudioHelper.playAudio(getResources(), R.raw.bombdef, false);

        // Notify car
        UdpClient.send("[win]");
    }
}
