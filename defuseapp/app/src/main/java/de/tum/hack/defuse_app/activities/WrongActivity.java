package de.tum.hack.defuse_app.activities;

import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.TextView;

import de.tum.hack.defuse_app.AudioHelper;
import de.tum.hack.defuse_app.EmojiHelper;
import de.tum.hack.defuse_app.R;
import de.tum.hack.defuse_app.model.Code;

import static de.tum.hack.defuse_app.model.Code.MAX_ERRORS;

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
            AudioHelper.playAudio(getResources(), R.raw.explode, false);
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
}
