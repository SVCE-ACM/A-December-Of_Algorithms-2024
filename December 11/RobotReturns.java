import java.util.*;

public class RobotReturns
{
    static String movesSequence(int numberOfMoves)
    {
        Scanner sc = new Scanner(System.in);
        
        String moves = new String();
        System.out.print("\nEnter moves: ");
        moves = sc.nextLine();

        return moves;
    }

    static int numberOfMoves()
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("\nEnter number of moves: ");
        int n = sc.nextInt();

        return n;
    }

    static boolean moveRobot(String moves, int numberOfMoves)
    {
        int x = 0, y = 0;
        for(int i = 0; i < numberOfMoves; i++)
        {
            switch(moves.charAt(i))
            {
                case 'R':
                {
                    x += 1;
                    break;
                }

                case 'L':
                {
                    x -= 1;
                    break;
                } 

                case 'U':
                {
                    y += 1;
                    break;
                }

                case 'D':
                {
                    y -= 1;
                }
            }
        }

        if(finalPosition(x, y))

                return true;

            else
            
                return false;
    }

    static boolean finalPosition(int x, int y)
    {
        if(x == 0 && y == 0)

            return true;

        else

            return false;
    }

    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        int n = numberOfMoves();
        String moves = movesSequence(n);
        
        if(moveRobot(moves, n))
        {
            System.out.print("\ntrue");
        }

        else

        {
            System.out.print("\nfalse");
        }
    }    
}