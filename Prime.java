import java.util.*;
public class Prime
{
  public static void main(String args[])
  {
    int i, j, n, flag,count = 0;
    System.out.println("Enter the Range");
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    for(i = 0; i <= n; i++)
    {
      if(i == 1 || i == 0)
      {
        continue;
      }
      flag = 1;
      for(j = 2; j <= i / 2; j++)
      {
        if(i % j == 0)
        {
          flag = 0;
        }
      }
      if(flag == 1)
      {
        System.out.println(i + " ");
        count++;
      }
    }
    System.out.println("Count Of Prime Numebers in the Given Range : " + count);
  }
}
