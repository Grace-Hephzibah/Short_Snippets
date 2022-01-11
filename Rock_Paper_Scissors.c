#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int intro(int c, int p)
{
  printf("Enter your Choice : \n\t 1. Stone \n\t 2. Paper \n\t 3. Scissors \n\n");
  printf("My Score %d \nYour Score %d \n\n", c,p);
}

int player_win(int cc, int pc)
{
  return ( (cc == 0 && pc ==1) || (cc==1 && pc ==2) || (cc==2 && pc==0) );
}

char* choice(int x)
{
  if (x==1) return "Stone";
  else if (x==2) return "Paper";
  else return "Scissors";
}

int main()
{
  char stone[] = "Stone", paper[] = "Paper", scissors[] = "Scissors";
  int cc, pc=1, cp, pp;
  char dummy = 'y';
  int c_score = 0, p_score = 0;
  // cc - computer's pl_choice
  // pc - player's choice

  // cp - computer point
  // pp - player point

  // cc     pc         winner
  // stone paper     - pc (0,1)
  // stone scissors  - cc (0,2)

  // paper stone     - cc (1,0)
  // paper scissors  - pc (1,2)

  // scissors stone  - pc (2,0)
  // scissors paper  - cc (2,1)

  while (pc < 4 && dummy != 'n')
  {
    system("cls");
    intro(c_score, p_score);

    printf("Enter your choice : ");
    scanf("%d", &pc);
    pc = pc%3;
    cc = rand()%3;

    if (pc == cc) printf("Hah! What a coincedence !\n");

    else if (player_win(cc,pc))
      {
        printf("You get a point ! \n");
        p_score += 1;
      }

    else
    {
      printf("WOW! I get a point ! \n");
      c_score += 1;
    }

    printf("\n\nUser's Choice : %s \t Computer's Choice : %s \t You(vs)Comp - %d %d \n\n ",
                choice(pc), choice(cc), p_score, c_score);

    printf("Ready for next Round ? (y/n)");
    scanf("\n%c", &dummy);
  }
}
