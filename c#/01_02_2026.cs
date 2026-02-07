/*
292- Nim Game

https://leetcode.com/problems/nim-game/

Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.
*/

public class Solution {
    public bool CanWinNim(int n) {
        if(n % 4 == 0){
          return false;
        } else {
          return true;
        }
    }
}