package de.tum.hack.defuse_app.activities;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import de.tum.hack.defuse_app.R;
import de.tum.hack.defuse_app.model.Code;

public class DefuseSequenceActivity extends AppCompatActivity {
    TextView txtDefuse1;
    TextView txtDefuse2;
    TextView txtDefuse3;
    List<Code> codes;
    Random rng;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_defuse_sequence);

        this.rng = new Random();

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

    private String getEmojiByUnicode(int unicode){
        return new String(Character.toChars(unicode));
    }

    private void showRandomSelection() {
        Code c = this.codes.get(this.rng.nextInt(this.codes.size()));
        this.txtDefuse1.setText(getEmojiByUnicode(c.getCode1()));
        this.txtDefuse2.setText(getEmojiByUnicode(c.getCode2()));
        this.txtDefuse3.setText(getEmojiByUnicode(c.getCode3()));
    }

    public void onAnswerClick(View v) {
        showRandomSelection();
    }
}
