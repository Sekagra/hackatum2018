package de.tum.hack.defuse_app.model;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class Code {
    public static final int MAX_ROUNDS = 15;
    public static final int MAX_ERRORS = 3;
    List<Integer> codeList;
    int correctCode;

    public static Code fromResourceString(String resources) {
        int[] ints = Arrays.stream(resources.split(",")).mapToInt(i -> Integer.decode(i)).toArray();

        return new Code(ints);
    }

    public Code(int[] codes) {
        this.correctCode = codes[0];

        // randomize for display
        this.codeList = Arrays.stream(codes).boxed().collect(Collectors.toList());
        Collections.shuffle(codeList);
    }

    public List<Integer> getCodes() {
        return this.codeList;
    }

    public boolean check(int selectedCode) {
        return this.correctCode == selectedCode;
    }
}
