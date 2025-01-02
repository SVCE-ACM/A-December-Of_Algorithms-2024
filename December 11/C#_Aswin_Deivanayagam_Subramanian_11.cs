using System;

class Program
{
    static bool RobotReturnToOrigin(string moves)
    {
        int x = 0, y = 0;
        foreach (char move in moves)
        {
            if (move == 'R')
            {
                x += 1;
            }
            else if (move == 'L')
            {
                x -= 1;
            }
            else if (move == 'U')
            {
                y += 1;
            }
            else if (move == 'D')
            {
                y -= 1;
            }
        }
        return x == 0 && y == 0;
    }

    static void Main()
    {
        Console.WriteLine(RobotReturnToOrigin("UDLR"));  // Example usage
    }
}
