package de.tum.hack.defuse_app.model;

import java.util.Arrays;

public class Code {
    public static final int MAX_ROUNDS = 20;
    public static final int MAX_ERRORS = 3;
    int code1;
    int code2;
    int code3;

    public static Code fromResourceString(String resources) {
        int[] ints = Arrays.stream(resources.split(",")).mapToInt(i -> Integer.decode(i)).toArray();

        return new Code(ints[0], ints[1], ints[2]);
    }

    public Code(int code1, int code2, int code3) {
        this.code1 = code1;
        this.code2 = code2;
        this.code3 = code3;
    }

    public int getCode1() {
        return this.code1;
    }

    public int getCode2() {
        return this.code2;
    }

    public int getCode3() {
        return this.code3;
    }

    public boolean check(int selection) {
        return false;
    }
}
