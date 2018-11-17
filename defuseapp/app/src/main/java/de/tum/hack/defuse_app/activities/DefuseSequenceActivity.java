package de.tum.hack.defuse_app.activities;

import android.content.Intent;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import de.tum.hack.defuse_app.EmojiHelper;
import de.tum.hack.defuse_app.R;
import de.tum.hack.defuse_app.model.Code;

public class DefuseSequenceActivity extends AppCompatActivity {
    TextView txtDefuse1;
    TextView txtDefuse2;
    TextView txtDefuse3;
    List<Code> codes;
    Random rng;
    Code currentCode;
    int rounds;
    int errorCount;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_defuse_sequence);

        this.rng = new Random(System.currentTimeMillis());

        // get input elements for codes
        this.txtDefuse1 = findViewById(R.id.txtDefuse1);
        this.txtDefuse2 = findViewById(R.id.txtDefuse2);
        this.txtDefuse3 = findViewById(R.id.txtDefuse3);

        // load list with all possible selections
        this.codes = new ArrayList<>();
        final String[] values = getResources().getStringArray(R.array.codes);
        for(String s : values) {
            this.codes.add(Code.fromResourceString(s));
        }

        showRandomSelection();
    }

    private void showRandomSelection() {
        Code c = this.codes.get(this.rng.nextInt(this.codes.size()));
        this.txtDefuse1.setText(EmojiHelper.getEmojiByUnicode(c.getCodes().get(0)));
        this.txtDefuse2.setText(EmojiHelper.getEmojiByUnicode(c.getCodes().get(1)));
        this.txtDefuse3.setText(EmojiHelper.getEmojiByUnicode(c.getCodes().get(2)));
        this.currentCode = c;
    }

    public void onAnswerClick(View v) {
        rounds++;
        if(this.currentCode.check(((TextView)v).getText().codePoints().toArray()[0])) {
            if(this.rounds == Code.MAX_ROUNDS) {
                startActivity(new Intent(this, WinActivity.class));
                finish();
            } else {
                showRandomSelection();
            }
        } else {
            errorCount++;
            Intent intent = new Intent(this, WrongActivity.class);
            intent.putExtra("errorCount", errorCount);
            startActivity(intent);
            // go back after some time
            Handler mHandler = new Handler();
            mHandler.postDelayed(new Runnable() {
                @Override
                public void run() {
                    showRandomSelection();
                }

            }, 500L);
        }
    }
}
