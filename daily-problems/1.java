/*This problem was recently asked by Google

Given a list of numbers and a number k, return whether any two numbers form list add up to k

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

BONUS: Can you do this in one pass?
*/

public bool func(int k, List<Integer> list) {
     for(int i = 0; i < list.size(); i++) {
         for(int j = 0; j < list.size(); j++) {
             if(list.get(i) + list.get(i + 1) = k) {
             return true;
             }
         }  
     }
}
