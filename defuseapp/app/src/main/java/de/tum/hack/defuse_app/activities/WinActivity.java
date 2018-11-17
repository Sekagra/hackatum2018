package de.tum.hack.defuse_app.activities;

import android.content.res.AssetFileDescriptor;
import android.media.MediaPlayer;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import java.io.FileDescriptor;
import java.io.IOException;

import de.tum.hack.defuse_app.AudioHelper;
import de.tum.hack.defuse_app.R;

public class WinActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_win);

        AudioHelper.playAudio(getResources(), R.raw.bombdef, false);
    }
}
