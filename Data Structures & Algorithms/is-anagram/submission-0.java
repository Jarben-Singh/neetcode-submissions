class Solution {

    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        HashMap<Character, Integer> hash = new HashMap();
        HashMap<Character, Integer> hash2 = new HashMap();

        for(int n = 0; n < s.length(); n++) {

            char cs = s.charAt(n);
            char ct = t.charAt(n);

            hash.put(cs, hash.getOrDefault(cs, 0) + 1);
            hash2.put(ct, hash2.getOrDefault(ct, 0) +1);
        }

        return hash.equals(hash2);
    }

}
