class Solution {
    public int minimumRounds(int[] tasks) {
        Arrays.sort(tasks);
        if(tasks.length==1) return -1;
        int x=1,mr=0;
        for(int i=1;i<tasks.length;i++){
            if(tasks[i]==tasks[i-1]) x++;
            else{
                if(x==1) return -1;
                mr+=(x+2)/3;
                x=1;
            }
        }
        if(x==1) return -1;
        mr+=(x+2)/3;
        return mr;
    }
}
