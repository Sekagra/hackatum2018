package de.tum.hack.defuse_app.helper;

import android.content.res.AssetFileDescriptor;
import android.content.res.Resources;
import android.media.MediaPlayer;

import java.io.FileDescriptor;
import java.io.IOException;

public class AudioHelper {
    public static void playAudio(Resources res, int resourceId, boolean loop) {
        final AssetFileDescriptor afd = res.openRawResourceFd(resourceId);
        final FileDescriptor fileDescriptor = afd.getFileDescriptor();
        MediaPlayer player = new MediaPlayer();
        try {
            player.setDataSource(fileDescriptor, afd.getStartOffset(), afd.getLength());
            player.setLooping(loop);
            player.prepare();
            player.start();
        } catch (IOException ex) {

        }
    }
}
