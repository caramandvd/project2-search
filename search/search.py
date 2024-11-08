# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    granita = util.Stack()
    granita.push((problem.getStartState(), []))
    noduri_vizitate = []
    
    while not granita.isEmpty():
        stare, actiune = granita.pop()
        
        if problem.isGoalState(stare):
            return actiune
        
        vizitat = False
        for i in noduri_vizitate:
            if i == stare:
                vizitat = True
                break
        
        if not vizitat:
            noduri_vizitate.append(stare)
            
            for stare_ulterioara, actiune_ulterioara, cost_ulterior in problem.getSuccessors(stare):
                # Verificăm dacă starea următoare nu a fost deja vizitată
                vizitat_succesor = False
                for i in noduri_vizitate:
                    if i == stare_ulterioara:
                        vizitat_succesor = True
                        break
                
                if not vizitat_succesor:
                    granita.push((stare_ulterioara, actiune + [actiune_ulterioara]))
                
    return []
    # util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    granita = util.Queue()
    granita.push((problem.getStartState(), []))
    noduri_vizitate = []
    
    while not granita.isEmpty():
        stare, actiune = granita.pop()
        
        if problem.isGoalState(stare):
            return actiune
        
        vizitat = False
        for i in noduri_vizitate:
            if i == stare:
                vizitat = True
                break
            
        if not vizitat:
            noduri_vizitate.append(stare)
            
            for stare_ulterioara, actiune_ulterioara, cost_ulterior in problem.getSuccessors(stare):
                vizitat_succesor = False
                for i in noduri_vizitate:
                    if i == stare_ulterioara:
                        vizitat_succesor = True
                        break
                
                if not vizitat_succesor:
                    granita.push((stare_ulterioara, actiune + [actiune_ulterioara]))
                
    return []
    # util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    granita = util.PriorityQueue()
    
    granita.push((problem.getStartState(), [], 0), 0)
    
    vizitate = set()

    while not granita.isEmpty():
        stare_curenta, actiuni, cost_total = granita.pop()

        if stare_curenta not in vizitate:
            vizitate.add(stare_curenta)

            # Verificăm dacă am ajuns la țintă
            if problem.isGoalState(stare_curenta):
                return actiuni

            # Explorăm vecinii
            for urmatoarea_stare, actiune, cost in problem.getSuccessors(stare_curenta):
                if urmatoarea_stare not in vizitate:
                    noul_cost = cost_total + cost
                    noi_actiuni = actiuni + [actiune]
                    granita.push((urmatoarea_stare, noi_actiuni, noul_cost), noul_cost)

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
