import java.util.*;
public class Series
{
  public static void main(String args[])
  {
    int t, i, j, n;

    System.out.println("Enter the number of Test Cases");
    Scanner sc = new Scanner(System.in);
    t = sc.nextInt();
    for(i = 0;i < t; i++)
    {
      System.out.println("Enter value of a");
      int a = sc.nextInt();
      System.out.println("Enter value of b");
      int b = sc.nextInt();
      System.out.println("Enter value of n");
      n = sc.nextInt();
      int sum = a + b;
      System.out.println(sum);
      for(j = 1; j <= n; j++)
      {
        int s = (int) Math.pow(2,j);
        sum+= s*b;
        System.out.println(sum);
      }
    }
  }
}
