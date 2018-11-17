package de.tum.hack.defuse_app.helper;

public class EmojiHelper {
    public static String getEmojiByUnicode(int unicode){
        return new String(Character.toChars(unicode));
    }
}
