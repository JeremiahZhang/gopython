# 第九章 Simulation and Design

- 目标:
    - Understand the potential application of simulation as a way to solve real-world problems.
    - Understand pseudo random numbers and their application in Monte Carlo simulations
    - Understand and be able to apply top-down and spiral design techniques in writing complex programs
    - Understand unit-test and be able to apply this technique in the implementation and debugging of complex programs

---

## 9.1 Simulating Racquetball

回力网球

> One particular powerful technique for solving real-world problems is simulation.

**问题:**

- Denny 与在他看来水平比它高一点的人打, 往往失败.
    - 原因: 他看来的水平差距 比 实际的差距小太多
    - 他自己心理问题
- Susan 好朋友来帮他分析, 提出一种可能
    - 这个比赛, 在本质上, 水平差距一点点, 则造成球场上巨大的比赛差距
    - 不涉及心理因素
    - 用计算机来模拟:
        - 不同水平的球员比赛
        - 不会涉及心理因素
        - 看看比赛结果如何.

**Analysis & Specification**

- basic outline of the racquetball game
    - 2 人, 与网球类似
    - 一人发球, serving
    - 球碰到墙面, 反弹
    - 一人接球, rally
        - The rally ends when one of the players faial to hit a legal shot
        - The player who misses the shot loses the rally.
        - If the loser is the player who served, then service passes to the other player
        - If the server wins the rally, a point is awarded
        - Players can only score points during their own service.
        - The first player to reach 15 points wins the game
- simulation
    - The ability-level of the players will be represented by the probability that the player wins the rally when he or she serves.
        - Players with a 0.6 probability win a point on 60% of their serves.
    - program
        - input: enter the service probability for both players
            - player 1
            - player 2
        - simulate multiple games of racquetball using those probability
        - output: the results.
- 流程

```
What is the prob. player A wins a serve?
What is the prob. player B wins a serve?
How many games to simulate?

processing

Games simulated: 500
Wins for A: 268 (53.6%)
Wins for B: 232 (46.4%)

(In each simulated game, player A serves first.)
```

## 2.Pseudo Random Numbers.

seed, and random

> A pseudo random number generator works by starting with some seed value. This value is fed to a function to produces a 'random' number. The next time a random number is needed, the current value is fed back into the function to produce a new number. With a carefully chosen function, the resuling sequence of values look essentially random. Of course, if you start the process over again with the same seed value, you end up with exactly the same sequence of numbers. It's all determined by the generating function and the value of the seed.

```
if random() < prob:
    score += 1
```

## 3.Top-Down Design  

> THE basic idea is to start with the general problem and try to express a solution in terms of smaller problem.

> Then each of the smaller problems is attacked in turn using the same technique.

> Eventually the problems get so small that they are trivial to solve. Then you just put all the pieces back together and you've got a program.

- Top-level Design

```
Print an Introduction

Get the inputs: probA, porbB, n
Simulate n games of racquetball using probA, probB
Print a report on the wins for playA and playB
```

搭建框架: 先把基本的流程写出来, 就是将上面的直接写出代码, 有些函数就当作我们是知道的.

如下: 搭建起整体骨架

```
def main():
    print_intro()
    prob_a, prob_b, n = get_inputs()
    wins_a, wins_b = sim_games(n, probA, probB)
    print_summary(wins_a, wins_b)
```

- Separation of Concerns

上面四个函数, 我们是不知道的. 我们需要完成这些函数.  

> Futher, we have specified the name, parameters and expected return values of the functions that perform these tasks. This information is called the interface or signature of a function.

- Second-level Design

设计上面的子函数啦.  

```
def print_intro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The abilities of each players is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")

def get_inputs():
    # Returns the 3 simulation parameters prob_a, prob_b, and n
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))

    return a, b, n
```

- Design sim_games

```
Initialize wins_a and wins_b to 0

loop n times
    simulate a game
    if play_a wins
        add 1 to wins_a
    else
        add 1 to wins_b
```

code:

```
def sim_n_games(n, prob_a, prob_b):
    # simulate n games and return wins_a and wins_b
    wins_a = 0
    wins_b = 0

    for i in range(n):
        score_a, score_b = sim_one_game(prob_a, prob_b)

        if score_a > score_b:
            wins_a += 1
        else:
            wins_b += 1

    return wins_a, wins_b
```

- Third-Level Design  

接下来就需要完成: sim_one_game():

```
Initialize scores to 0
set serving to "A"

Loop while game is not over:
    simulate one serve of whichever player is serving
    update the status of the game
return scores    
```
