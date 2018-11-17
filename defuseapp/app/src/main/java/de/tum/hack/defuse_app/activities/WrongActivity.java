package de.tum.hack.defuse_app.activities;

import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.io.IOException;

import de.tum.hack.defuse_app.helper.AudioHelper;
import de.tum.hack.defuse_app.helper.EmojiHelper;
import de.tum.hack.defuse_app.R;
import de.tum.hack.defuse_app.networking.UdpClient;
import de.tum.hack.defuse_app.model.Code;

public class WrongActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_wrong);

        TextView txtLose = findViewById(R.id.txtLose);
        LinearLayout layoutWrong = findViewById(R.id.layoutWrong);

        int errorCount = getIntent().getIntExtra("errorCount", 0);

        if (errorCount == Code.MAX_ERRORS) {
            txtLose.setVisibility(View.VISIBLE);
            layoutWrong.setVisibility(View.GONE);
            Thread task = new Thread(() -> {
                AudioHelper.playAudio(getResources(), R.raw.explode, false);
                try {
                    Thread.sleep(2000L);
                    AudioHelper.playAudio(getResources(), R.raw.terrorwin, false);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

                // send game over to car
                UdpClient.send("[lose]");
            });

            task.start();

        } else {
            txtLose.setVisibility(View.GONE);
            layoutWrong.setVisibility(View.VISIBLE);
            // display number of remaining lives
            LinearLayout layoutLives = findViewById(R.id.layoutLives);
            for (int i = 0; i < Code.MAX_ERRORS; i++) {
                TextView textView = new TextView(this);
                textView.setLayoutParams(new LinearLayout.LayoutParams(LinearLayout.LayoutParams.WRAP_CONTENT, LinearLayout.LayoutParams.WRAP_CONTENT));
                if(i >= Code.MAX_ERRORS - errorCount) textView.setAlpha(0.5f);
                textView.setText(EmojiHelper.getEmojiByUnicode(0x1f5a4));
                textView.setTextSize(60);
                layoutLives.addView(textView);
            }

            AudioHelper.playAudio(getResources(), R.raw.beep, false);


            // go back after some time
            Handler mHandler = new Handler();
            mHandler.postDelayed(new Runnable() {
                @Override
                public void run() {
                    finish();
                }

            }, 1500L);
        }
    }

    @Override
    public void onBackPressed() {
        // do nothing
    }
}
